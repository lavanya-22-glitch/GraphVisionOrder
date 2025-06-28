# 🧩 Order in Chaos

> Reconstructing the correct sequence of shuffled image frames using SSIM and graph-based optimization.

---

## 📌 Overview

"Order in Chaos" is a visual reasoning project that takes a dataset of **randomized video frames** and attempts to **reconstruct the original frame order** using similarity-based techniques and graph traversal. The project includes a basic greedy model as well as a fully optimized solution that leverages **parallelism**, **graph theory**, and **DFS traversal**.

This project is ideal for demonstrating skills in:

- Data structures & algorithms (DSA)
- Computer vision (SSIM)
- Optimization techniques
- Parallel processing (multi-threading)
- Real-world graph applications

---

## 📂 Project Structure

| File/Folder          | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `main.py`            | 🚀 **Main pipeline** – Fully optimized solution using parallel SSIM, MST, and DFS.            |
| `skeleton.py`        | 🧪 **Skeleton version** – Basic SSIM + greedy nearest-neighbor approach, no DSA optimization. |
| `output1.txt`        | ✅ Output from `main.py` – Final ordered sequence of image frames.                             |
| `output.txt`         | 📝 Output from `skeleton.py` – Initial frame order using simpler logic.                       |
| `Randomized_Images/` | Input dataset of shuffled frames.                                                             |
| `Dataset.zip`        | Compressed version of the dataset.                                                            |
| `README.md`          | This file – Documentation and project insights.                                               |
| `result_checker.py`  | (Optional) Tool to validate the output accuracy.                                              |

---

## ⚙️ Tech Stack & Tools

| Area             | Tools/Libraries Used               |
| ---------------- | ---------------------------------- |
| Image Processing | OpenCV, scikit-image (SSIM)        |
| Optimization     | Kruskal's algorithm, DFS traversal |
| Performance      | ThreadPoolExecutor (parallelism)   |
| Utility          | tqdm for progress tracking         |
| Language         | Python 3.9+                        |

---

## 🧠 Algorithms Used

### 1. **Structural Similarity Index (SSIM)**

Used to compare image pairs and generate a similarity matrix.

### 2. **Maximum Spanning Tree (MST)**

Built using **Kruskal's algorithm** to connect highly similar frames without cycles.

### 3. **Depth First Search (DFS)**

Used to traverse the MST to determine the best frame order.

### 4. **Greedy Nearest Neighbor** (Skeleton version)

Finds the most similar unused frame sequentially using SSIM.

---

## 🚀 How to Run

```bash
# Clone the repo
$ git clone https://github.com/yourusername/order-in-chaos.git
$ cd order-in-chaos

# Run the optimized version
$ python main.py

# OR run the basic prototype
$ python skeleton.py
```

Make sure to place all shuffled frames inside the `Randomized_Images/` folder.

---

## 📈 Sample Output

`output1.txt` → Frame order from the optimized pipeline\
`output.txt`  → Frame order from the skeleton version

---

## 💼 Ideal For

This project is a great addition to your portfolio if you're applying to:

- **Google STEP Internship**
- **GSoC** (particularly in OpenCV or image restoration-related orgs)
- Any research or industry position requiring practical algorithm design

---

## 🧊 Future Improvements

- Use CNN feature embeddings instead of SSIM for semantic similarity
- Try hierarchical clustering + dynamic programming for better global sequence
- Visual diff/preview of before vs. after sequence

---

## 📬 Contact

Created by **Lavanya Bhadani** – feel free to connect on [LinkedIn](#) or drop a message!

---

## ⭐ Star This Project

If you find this useful or interesting, don't forget to ⭐ star the repo and share it!

