
<div align="center">
  <h1>Car License Plate Detection</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/github/contributors/saboye/car_license_plate_detection?color=blue&logo=github&style=for-the-badge" alt="GitHub contributors" />
    <img src="https://img.shields.io/github/forks/saboye/car_license_plate_detection?logo=github&style=for-the-badge" alt="GitHub forks" />
    <img src="https://img.shields.io/github/issues-raw/saboye/car_license_plate_detection?style=for-the-badge" alt="GitHub issues" />
    <img src="https://img.shields.io/github/license/saboye/car_license_plate_detection?style=for-the-badge" alt="GitHub license" />
    <img src="https://img.shields.io/github/last-commit/saboye/car_license_plate_detection?style=for-the-badge" alt="GitHub last commit" />
    <img src="https://img.shields.io/badge/yolo-5.0-blue?style=for-the-badge&logo=yolo" alt="YOLO" />
    <img src="https://img.shields.io/badge/pytorch-1.10.0-blue?style=for-the-badge&logo=pytorch" alt="PyTorch" />
    <img src="https://img.shields.io/badge/opencv-4.5.3-blue?style=for-the-badge&logo=opencv" alt="OpenCV" />
</p>

![License Plate Detection](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/val_batch1_pred.jpg)

This repository contains a project on car license plate detection using advanced computer vision techniques. The project leverages the YOLO (You Only Look Once) object detection framework to detect car license plates in various environmental conditions.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Challenges and Considerations](#challenges-and-considerations)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to develop a robust system for detecting car license plates from images and videos. The project includes the following key components:
- Exploratory Data Analysis (EDA)
- Image Preprocessing
- Data Augmentation
- Model Training using the YOLO framework
- Hyperparameter Tuning
- Deployment for real-time detection

## Dataset

The primary dataset used in this project is sourced from the [Car License Plate Detection dataset](https://www.kaggle.com/datasets). Additional data is integrated from public datasets, traffic surveillance footage, and synthetic datasets to improve the model's performance.

## Installation

To run the project locally, please follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/saboye/car_license_plate_detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car_license_plate_detection
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the license plate detection model, follow these steps:

1. Ensure your dataset is prepared and placed in the `data/` directory.
2. Run the training script to train the model:
   ```bash
   python train.py
   ```
3. Use the `detect.py` script to perform detection on new images or videos:
   ```bash
   python detect.py --input path_to_input_file --output path_to_output_file
   ```

## Model Architecture

The model architecture is based on the YOLO object detection framework, which is known for its speed and accuracy in detecting objects in images. The architecture includes:
- Convolutional layers for feature extraction (as part of YOLO)
- Bounding box regression layers for license plate localization
- Object classification layers to identify license plates within the detected bounding boxes

## Results

The model's performance was evaluated using several metrics, including Precision, Recall, and F1-Score. The following key results were obtained:

- **F1-Confidence Curve:** The F1-Score peaks at 0.97 when the confidence threshold is set at 0.511. This curve illustrates the trade-off between confidence and F1-Score, demonstrating that the model maintains a high F1-Score across a wide range of confidence levels.

  ![F1-Confidence Curve](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/F1_curve.png)

- **Precision-Recall Curve:** The model achieves a mean Average Precision (mAP) of 0.985 at an IoU threshold of 0.5. The Precision-Recall curve is nearly perfect, indicating that the model is highly precise and recalls most instances of license plates.

  ![Precision-Recall Curve](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/PR_curve.png)

- **Precision-Confidence Curve:** The model achieves a Precision of 1.00 at a confidence level of 0.919. This curve demonstrates the model's reliability in making predictions at high confidence levels.

  ![Precision-Confidence Curve](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/PR_curve.png)

- **Recall-Confidence Curve:** The Recall remains high across various confidence levels, with a perfect score of 1.00 achieved at lower confidence thresholds.

  ![Recall-Confidence Curve](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/R_curve.png)

- **Exploratory Data Analysis (EDA):** The EDA visualizes the distribution of bounding box parameters (x, y, width, height) for license plates, providing insights into their spatial characteristics in the dataset.

  ![EDA](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/labels_correlogram.jpg)

- **Training and Validation Loss Curves:** The loss curves for both training and validation show a consistent decrease, indicating effective learning during the training process. The metrics also indicate that the model generalizes well to unseen data.

  ![Loss Curves](https://github.com/saboye/car_license_plate_detection/blob/main/runs/train/exp3/results.png)

These results indicate that the model is highly effective in detecting license plates with high precision and recall. The model's performance metrics confirm its suitability for deployment in real-time applications.

## Challenges and Considerations

This project faced several challenges, including:
- Handling incomplete or low-quality images
- Integrating data from multiple sources
- Addressing biases in the dataset
- Ensuring model scalability

## Future Work

Potential future improvements include:
- Enhancing detection accuracy in various lighting and weather conditions
- Expanding the dataset with more diverse license plates
- Deploying the model in a mobile or edge computing environment

## Contributing

Contributions are welcome! 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
