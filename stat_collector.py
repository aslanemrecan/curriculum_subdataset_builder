
# Imports
import pandas as pd
import os
from PIL import Image

# settings
#data_path = "/data/Koutsoubn8/ijcnn_v7data/high_density_100k/train"
#data_path = "/data/Koutsoubn8/ijcnn_v7data/single_label_set/train"
#data_path = "/data/Koutsoubn8/Real_world_test"
data_path = "/home/aslane84/dataset_builder/dataset_builder/validation_mainset"
# create an empty list to store the label data
label_data = []

# walk the directory tree and process each YOLO label file
for dirpath, dirnames, filenames in os.walk(data_path):
    for filename in filenames:
        if filename.endswith(".txt"):
            # open the YOLO label file and read its contents
            with open(os.path.join(dirpath, filename), "r") as f:
                contents = f.readlines()

            # iterate over each line in the file and extract the width and height of each object
            for line in contents:
                parts = line.strip().split()
                width = float(parts[3])
                height = float(parts[4])
                
                # append the label data to the list
                label_data.append({"path": os.path.join(dirpath, filename), "area": width * height})

# create a pandas DataFrame from the label data
df = pd.DataFrame(label_data)

# Save 
df.to_csv("STATS_FOR_" + data_path.replace("/","_") + ".csv", index = False)
