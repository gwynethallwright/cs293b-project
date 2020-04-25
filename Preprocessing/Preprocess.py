import cv2
import os

def generate_filepath(writefile_prefix, frame_number):
    return writefile_prefix + "/" + writefile_prefix + "_%d.png" % frame_number

def extract_frames(readfile, writefile_prefix):
    video = cv2.VideoCapture(readfile)
    success, image = video.read()
    frame_number = 0
    if not os.path.exists(writefile_prefix):
        os.makedirs(writefile_prefix)
    while success:
      cv2.imwrite(generate_filepath(writefile_prefix, frame_number), image)
      success, image = video.read()
      frame_number += 1
    return frame_number + 1

if __name__ == '__main__':
    num_frames = extract_frames("FARM1-42655-2020_04_03__10_05_38.mkv", "FARM1")
