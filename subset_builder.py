import os
import shutil
import pandas as pd
import numpy as np

source_images_path = "/data/Koutsoubn8/Real_world_training/images"
source_labels_path = "/data/Koutsoubn8/Real_world_training/labels"
destination_images_path = "dataset_builder/validation_mainset/images"
destination_labels_path = "dataset_builder/validation_mainset/labels"

# Get the list of image names
image_names = os.listdir(source_images_path)

# Read the labels from individual text files
labels = []
for image_name in image_names:
    label_file = os.path.splitext(image_name)[0] + '.txt'
    with open(os.path.join(source_labels_path, label_file), 'r') as f:
        label = f.read().strip()
        labels.append(label)

# Create a DataFrame with image names and labels
labels_df = pd.DataFrame({'image_name': image_names, 'label': labels})

# Create the new folders for the selected images and labels if they don't exist
os.makedirs(destination_images_path, exist_ok=True)
os.makedirs(destination_labels_path, exist_ok=True)

# Select 5k random images and their labels
selected_images_df = labels_df.sample(n=17000, random_state=42)

# Copy the selected images and labels to the new folders
for index, row in selected_images_df.iterrows():
    image_name = row['image_name']
    label_file = os.path.splitext(image_name)[0] + '.txt'
    
    shutil.copy(os.path.join(source_images_path, image_name), os.path.join(destination_images_path, image_name))
    shutil.copy(os.path.join(source_labels_path, label_file), os.path.join(destination_labels_path, label_file))