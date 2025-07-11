<h1 align="center">Flag Detection using YOLOv8</h1>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/7mgppp1903/flag-detection-YOLOv8?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/7mgppp1903/flag-detection-YOLOv8?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/7mgppp1903/flag-detection-YOLOv8?style=for-the-badge" />
</p>

<p align="center">
  <b>Real-time flag detection using YOLOv8 and a large-scale public dataset.</b><br>
  Accurate, fast, and trained on flags from across the world
</p>

---

## What's New?

- Migrated from a small custom-made dataset of South American Flags to the **Open Images Dataset V6** for higher class diversity and image quality
- Expanded scope from regional (South American) flags to **global flag detection**

---

## Demo

<p align="center">
  <img src="results/val_batch1_pred.jpg" alt="demo" width="70%">
</p>

---

## Features

- YOLOv8m-based detection
- Trained on a large, real-world global flag dataset
- Supports image, video, and webcam input
- Visual evaluation with PR curves, confusion matrices, and F1 scores

---

## Tech Stack

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- Python 3.10+
- PyTorch
- OpenCV
- Matplotlib, Seaborn

---

</details>

---

## 📂 Dataset Source

The project originally used a small custom-labeled dataset focused on South American flags. To scale the project and improve detection accuracy, I switched to a much larger and publicly available dataset:

- **[Open Images Dataset V6](http://storage.googleapis.com/openimages/web/index.html)** 
- contains 2,785,498 instance segmentations from various countries and regions with verified bounding boxes

**Reference Paper**  
Kuznetsova et al., *The Open Images Dataset V6: A Large-Scale Benchmark for Object Detection*, 2018  
📖 [Read the paper](https://arxiv.org/abs/1811.00982)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/7mgppp1903/flag-detection-YOLOv8.git
cd flag-detection-YOLOv8

# Install dependencies
pip install -r requirements.txt
pip install ultralytics



