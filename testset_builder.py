import os
import shutil
import pandas as pd

def create_directories(dir_names, dir_paths):
    for dir_path in dir_paths:
        for dir_name in dir_names:
            full_dir_path = os.path.join(dir_path, dir_name)
            if not os.path.exists(full_dir_path):
                os.makedirs(full_dir_path)

def copy_files(paths_dict, size_path):
    for idx, file_path in paths_dict.items():
        filename = os.path.splitext(os.path.basename(file_path))[0]
        shutil.copy(file_path, os.path.join(size_path, "labels", filename + ".txt"))
        shutil.copy(file_path.replace("labels", "images").replace("txt", "jpg"), os.path.join(size_path, "images", filename + ".jpg"))

def copy_all_files(small_paths, medium_paths, large_paths, small_path, medium_path, large_path):
    copy_files(small_paths, small_path)
    copy_files(medium_paths, medium_path)
    copy_files(large_paths, large_path)

# Settings
#stat_path = "STATS_FOR__data_Koutsoubn8_ijcnn_v7data_high_density_100k_train.csv"
stat_path = "STATS_FOR__data_Koutsoubn8_Real_world_test.csv"
save_path = "test_data/"

# Read the CSV file into a pandas dataframe
df = pd.read_csv(stat_path)

# Split the data into three quantile bins
bin_idx, bin_thresholds = pd.qcut(df.iloc[:, 1], q=3, labels=False, retbins=True)

# Extract values paths of df that are small, med, lg
small_paths = df[bin_idx == 0].iloc[:, 0]
medium_paths = df[bin_idx == 1].iloc[:,0]
large_paths = df[bin_idx == 2].iloc[:,0]
# Make new folder to save in
small_path = os.path.join(save_path, "small")
medium_path = os.path.join(save_path, "medium")
large_path = os.path.join(save_path, "large")

dir_names = ["labels", "images"]
dir_paths = [small_path, medium_path, large_path]

create_directories(dir_names, dir_paths)
copy_all_files(small_paths, medium_paths, large_paths, small_path, medium_path, large_path)
