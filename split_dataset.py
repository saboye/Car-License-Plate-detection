import os
import shutil
import random

# Paths
images_dir = os.path.join('data', 'images')
labels_dir = os.path.join('data', 'labels')
train_images_dir = os.path.join('data', 'train', 'images')
train_labels_dir = os.path.join('data', 'train', 'labels')
val_images_dir = os.path.join('data', 'val', 'images')
val_labels_dir = os.path.join('data', 'val', 'labels')

# Ensure directories exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# List all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith('.png') or f.endswith('.jpg')]

# Shuffle and split
random.shuffle(image_files)
split_idx = int(0.8 * len(image_files))  # 80% for training

train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Move training files
for file in train_files:
    # Move image
    shutil.move(os.path.join(images_dir, file), os.path.join(train_images_dir, file))
    # Move corresponding label
    label_file = file.replace('.png', '.txt').replace('.jpg', '.txt')
    shutil.move(os.path.join(labels_dir, label_file), os.path.join(train_labels_dir, label_file))

# Move validation files
for file in val_files:
    # Move image
    shutil.move(os.path.join(images_dir, file), os.path.join(val_images_dir, file))
    # Move corresponding label
    label_file = file.replace('.png', '.txt').replace('.jpg', '.txt')
    shutil.move(os.path.join(labels_dir, label_file), os.path.join(val_labels_dir, label_file))
