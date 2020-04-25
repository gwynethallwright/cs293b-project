import cv2

def extract_frames(filename):
    video = cv2.VideoCapture(filename)
    success, image = video.read()
    frame_number = 0
    while success:
      cv2.imwrite("frame%d.png" % frame_number, image)
      success, image = video.read()
      frame_number += 1

if __name__ == '__main__':
    extract_frames('FARM1-42655-2020_04_03__10_05_38.mkv')
