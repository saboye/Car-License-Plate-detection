import os
import xml.etree.ElementTree as ET
from PIL import Image

# Define directories
annotations_dir = os.path.join('..', 'data', 'annotations')
images_dir = os.path.join('..', 'data', 'images')
yolo_labels_dir = os.path.join('..', 'data', 'labels')  # Create this directory

if not os.path.exists(yolo_labels_dir):
    os.makedirs(yolo_labels_dir)

def convert_to_yolo_format(xml_file, img_shape):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    yolo_format = []

    img_width = img_shape[0]
    img_height = img_shape[1]

    for member in root.findall('object'):
        bndbox = member.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        # Convert to YOLO format
        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_format.append(f"0 {x_center} {y_center} {width} {height}\n")

    return yolo_format

# Convert all annotations
for xml_file in os.listdir(annotations_dir):
    xml_path = os.path.join(annotations_dir, xml_file)
    img_path = os.path.join(images_dir, xml_file.replace('.xml', '.png'))  # or .jpg

    img_shape = Image.open(img_path).size
    yolo_format = convert_to_yolo_format(xml_path, img_shape)

    # Save YOLO format file
    with open(os.path.join(yolo_labels_dir, xml_file.replace('.xml', '.txt')), 'w') as f:
        f.writelines(yolo_format)
