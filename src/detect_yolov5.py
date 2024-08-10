import os
from yolov5 import detect  # Assuming yolov5 is in PYTHONPATH

# Paths
weights_path = os.path.join('runs', 'train', 'exp', 'weights', 'best.pt')
images_path = os.path.join('..', 'data', 'images')

# Run inference
detect.run(
    source=images_path,
    weights=weights_path,
    imgsz=640,
    conf_thres=0.25
)
