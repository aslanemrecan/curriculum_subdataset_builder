import torch
import os
import numpy as np
import glob
from torch.utils.data import Dataset, DataLoader


#settings
data_path = "/data/Koutsoubn8/ijcnn_v7data"

large_dir = 'data/large_boxes'
medium_dir = 'data/medium_boxes'
small_dir = 'data/small_boxes'

os.makedirs(large_dir, exist_ok=True) #creates the output directories
os.makedirs(medium_dir, exist_ok=True)
os.makedirs(small_dir, exist_ok=True)

#data loader

#stats data
def xywh2xyxy(xywh):
    xyxy = torch.zeros_like(xywh)
    xyxy[:, 0] = xywh[:, 0] - xywh[:, 2] / 2
    xyxy[:, 1] = xywh[:, 1] - xywh[:, 3] / 2
    xyxy[:, 2] = xywh[:, 0] + xywh[:, 2] / 2
    xyxy[:, 3] = xywh[:, 1] + xywh[:, 3] / 2
    return xyxy

#cycle through data
for inputs, labels, files in os.walk(data_path):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join())
            annotation_file = os.path.join ###????





#split&saves
large_boxes = bounding_boxes[areas > large_thresh]
medium_boxes = bounding_boxes[(areas <= large_thresh) & (areas > small_thresh)]
small_boxes = bounding_boxes[areas <= small_thresh]


# Copy the image to the appropriate output directory
output_filepath = os.path.join(output_dir, filename)
os.system(f"cp {filepath} {output_filepath}")