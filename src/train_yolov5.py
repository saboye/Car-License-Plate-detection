import os
import yaml
import subprocess

# Paths
data_dir = os.path.join('..', 'data')
train_dir = os.path.join(data_dir, 'train')
val_dir = os.path.join(data_dir, 'val')

# Create a YAML file for training
data_yaml = {
    'train': os.path.join(train_dir, 'images'),
    'val': os.path.join(val_dir, 'images'),
    'nc': 1,  # Number of classes (only license plates)
    'names': ['license']  # Class name
}

yaml_path = os.path.join(data_dir, 'data.yaml')
with open(yaml_path, 'w') as f:
    yaml.dump(data_yaml, f)

# Run the YOLOv5 training script using subprocess
subprocess.run([
    "python", "train.py",
    "--img", "640",
    "--batch", "16",
    "--epochs", "50",
    "--data", yaml_path,
    "--weights", "yolov5s.pt",
    "--cache"
], cwd=os.path.join('..', 'yolov5'))
