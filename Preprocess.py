import cv2
from keras.preprocessing import image
import os
import numpy as np

def set_working_dir(path):
  if os.getcwd() != path:
    os.chdir(path)

def check_create_dirs(outer_dir, inner_dir):
    if not os.path.exists(outer_dir):
        os.makedirs(outer_dir)
    if not os.path.exists(outer_dir + "/" + inner_dir):
        os.makedirs(outer_dir + "/" + inner_dir)

def generate_filepath(writefile_prefix, directory, frame_number):
    return directory + "/" + writefile_prefix[:-4] + "/" + writefile_prefix[:-4] + "_%d.png" % frame_number

def extract_frames(readfile, writefile_prefix, directory, resize=True, x_dim=224, y_dim=224):
    video = cv2.VideoCapture(readfile)
    success, image = video.read()
    frame_number = 0
    check_create_dirs(directory, writefile_prefix[:-4])
    while success:
        if resize:
            image = cv2.resize(image, (x_dim, y_dim))
        cv2.imwrite(generate_filepath(writefile_prefix, directory, frame_number), image)
        success, image = video.read()
        frame_number += 1
    return frame_number + 1

def extract_frames_all(read_directory_name, write_directory_name):
  for filename in os.listdir(read_directory_name):
    extract_frames(read_directory_name + "/" + filename, filename, write_directory_name)

def read_training_data(base_directory_name, training_set):
  for directory in os.listdir(base_directory_name):
    for filename in os.listdir(base_directory_name + "/" + directory):
      train_image = image.load_img(base_directory_name + "/" + directory + "/" + filename, target_size=(224,224,3))
      train_image = image.img_to_array(train_image)
      train_image = train_image/255
      training_set.append(train_image)

## if __name__ == '__main__':
##    set_working_dir("/content/drive/Shared drives/farmcam_human_detection")
##    extract_frames_all("contains_human", "contains_human_extracted")
##    extract_frames_all("human_less", "human_less_extracted")
##    training_set = []
##    read_training_data("contains_human_extracted", training_set)
##    x_training_data = np.array(training_set)
