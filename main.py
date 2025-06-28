import os
import cv2
from tqdm import tqdm
from skimage.metrics import structural_similarity as ssim
from collections import defaultdict
import heapq
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== Configuration =====
folder_name = "Randomized_Images"
output_file = "output1.txt"
imsize = (64, 64)
start_frame = "4096000.jpg"

# ===== SSIM Similarity Function =====
def ssim_score(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, imsize)
    img2 = cv2.resize(img2, imsize)
    score, _ = ssim(img1, img2, full=True)
    return score

# ===== Parallel SSIM Matrix Builder =====
def ssim_task(pair):
    f1, f2 = pair
    p1 = os.path.join(folder_name, f1)
    p2 = os.path.join(folder_name, f2)
    return (f1, f2, ssim_score(p1, p2))

def build_ssim_matrix_parallel(filenames):
    matrix = {f: {} for f in filenames}
    pairs = [(filenames[i], filenames[j]) for i in range(len(filenames)) for j in range(i+1, len(filenames))]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(ssim_task, pair) for pair in pairs]
        for future in tqdm(as_completed(futures), total=len(pairs), desc="⚡ Building SSIM Matrix", dynamic_ncols=True, leave=True):
            f1, f2, score = future.result()
            matrix[f1][f2] = score
            matrix[f2][f1] = score
    return matrix

# ===== Build Maximum Spanning Tree (Kruskal's Algorithm) =====
def build_mst(filenames, matrix):
    parent = {f: f for f in filenames}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root, v_root = find(u), find(v)
        if u_root != v_root:
            parent[u_root] = v_root
            return True
        return False

    edges = []
    for i in range(len(filenames)):
        for j in range(i + 1, len(filenames)):
            u, v = filenames[i], filenames[j]
            score = matrix[u][v]
            heapq.heappush(edges, (-score, u, v))  # Max heap

    mst = defaultdict(list)
    with tqdm(total=len(edges), desc="🌳 Building MST", dynamic_ncols=True, leave=True) as pbar:
        while edges:
            neg_score, u, v = heapq.heappop(edges)
            if union(u, v):
                mst[u].append(v)
                mst[v].append(u)
            pbar.update(1)
    return mst

# ===== DFS Traversal to Order Frames =====
def dfs_traversal(graph, start):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        result.append(node)
        for neighbor in sorted(graph[node], key=lambda x: -len(graph[x])):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result

# ===== Save Ordered Filenames to File =====
def save_output(filenames, output_path):
    with open(output_path, "w") as f:
        for name in filenames:
            f.write(name + "\n")
    print(f"\n✅ Saved ordered list to '{output_path}'")

# ===== Main Driver =====
if __name__ == "__main__":
    filenames = [f for f in os.listdir(folder_name) if f.lower().endswith(".jpg")]

    print("📊 Precomputing SSIM similarity matrix (Parallel)...")
    ssim_matrix = build_ssim_matrix_parallel(filenames)

    print("🌳 Constructing Maximum Spanning Tree...")
    mst = build_mst(filenames, ssim_matrix)

    print("🧭 Traversing MST with DFS to determine order...")
    ordered_filenames = dfs_traversal(mst, start_frame)

    save_output(ordered_filenames, output_file)
