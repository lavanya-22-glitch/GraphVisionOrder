import os
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

FRAME_FOLDER = "Randomized_Images"
OUTPUT_FILE = "output.txt"
RESIZE_SHAPE = (64, 64)

def get_feature_vector(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, RESIZE_SHAPE)
    return img.flatten()

def load_all_features(frame_folder):
    features = {}
    for filename in tqdm(os.listdir(frame_folder), desc="Extracting features"):
        path = os.path.join(frame_folder, filename)
        features[filename] = get_feature_vector(path)
    return features

def find_next_frame(current_frame, features, used):
    current_vec = features[current_frame]
    best_score = -1
    best_frame = None
    for fname, vec in features.items():
        if fname in used:
            continue
        score = cosine_similarity([current_vec], [vec])[0][0]
        if score > best_score:
            best_score = score
            best_frame = fname
    return best_frame

def main():
    features = load_all_features(FRAME_FOLDER)
    all_frames = list(features.keys())

    ordered = ["4096000.jpg"]
    used = set(ordered)

    print("Ordering frames...")
    while len(ordered) < len(all_frames):
        next_frame = find_next_frame(ordered[-1], features, used)
        if not next_frame:
            print("Error: Could not find next frame!")
            break
        ordered.append(next_frame)
        used.add(next_frame)

    print(f"Frames ordered: {len(ordered)}")

    with open(OUTPUT_FILE, "w") as f:
        for name in ordered:
            f.write(name + "\n")
    print(f"✅ Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
