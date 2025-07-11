<h1 align="center">Flag Detection with YOLOv8</h1>

<p align="center">
  <b>YOLOv8-based object detection model to recognize South American flags.</b><br>
  <i>Trained with custom dataset, evaluated with mAP, PR-curves, and full visual metrics.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/7mgppp1903/flag-detection-YOLOv8?color=blue" />
  <img src="https://img.shields.io/github/last-commit/7mgppp1903/flag-detection-YOLOv8?color=green" />
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-red" />
</p>

---

## Demo

<details>
<summary><b>Example Predictions (click to view)</b></summary>

<table>
<tr>
<td align="center">Validation Batch</td>
<td align="center">Prediction Output</td>
</tr>
<tr>
<td><img src="training-results/val_batch0_labels.jpg" width="300"/></td>
<td><img src="training-results/val_batch0_pred.jpg" width="300"/></td>
</tr>
<tr>
<td><img src="training-results/val_batch1_labels.jpg" width="300"/></td>
<td><img src="training-results/val_batch1_pred.jpg" width="300"/></td>
</tr>
</table>

</details>

---

## 📊 Model Results

| Metric | Value |
|--------|-------|
| **mAP@0.5** | `0.888` |
| **Best Class** |  Guyana Flag (0.984) |
| **No of Classes** | 12 |

<details>
<summary><strong>📈 Precision-Recall Curve</strong></summary>

<p align="center">
  <img src="training-results/PR_curve.png" width="600"/>
</p>

</details>

<details>
<summary><strong>🧩 Confusion Matrix</strong></summary>

<p align="center">
  <img src="training-results/confusion_matrix.png" width="400"/>
  <img src="training-results/confusion_matrix_normalized.png" width="400"/>
</p>

</details>

---

## 🧠 Supported Classes

> YOLOv8 is trained on **13** flags:



