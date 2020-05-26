# Code adapted from Tensorflow Object Detection Framework
# https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb
# Tensorflow Object Detection Detector

import logging
import os
import sys
import numpy as np
import tensorflow.compat.v1 as tf
import cv2
import argparse
import smtplib

logging.getLogger('tensorflow').disabled = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.disable_v2_behavior()

def parse_command_line():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--path', type=str, default=None, required=True)
    args = parser.parse_args()
    return args.path

def alert_user(filename):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    myEmail = "farmCamAlert293@gmail.com"
    myEmailPass = "richisawesome"
    destEmail = "gwynethallwright@gmail.com"
    # Log in to the server using user provided credentials
    server.login(myEmail, myEmailPass)
    # Send the mail
    subject = "Human detected"
    body = "The device has detected human activity in video " + filename + "."
    message = ("From: %s\r\n" % myEmail
             + "To: %s\r\n" % destEmail
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)
    server.sendmail(myEmail, destEmail, message)
    server.close()

class DetectorAPI:
    def __init__(self, path_to_ckpt):
        self.path_to_ckpt = path_to_ckpt
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.path_to_ckpt, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        self.default_graph = self.detection_graph.as_default()
        self.sess = tf.Session(graph=self.detection_graph)
        # Definite input and output Tensors for detection_graph
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def processFrame(self, image):
        # Expand dimensions since the trained_model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image, axis=0)
        # Actual detection.
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        im_height, im_width,_ = image.shape
        boxes_list = [None for i in range(boxes.shape[1])]
        for i in range(boxes.shape[1]):
            boxes_list[i] = (int(boxes[0,i,0] * im_height),
                        int(boxes[0,i,1]*im_width),
                        int(boxes[0,i,2] * im_height),
                        int(boxes[0,i,3]*im_width))
        return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])

    def close(self):
        self.sess.close()
        self.default_graph.close()

if __name__ == "__main__":
    filename = parse_command_line()
    model_path = '/home/ubuntu/ssd_mobilenet_v1_coco_2018_01_28/frozen_inference_graph.pb'
    odapi = DetectorAPI(path_to_ckpt=model_path)
    threshold = 0.4
    humanCountThreshold = 2
    x_dim = 1280
    y_dim = 720
    skip_frames = 1
    videos_path = "./"
    print("Started processing for " + filename)
    cap = cv2.VideoCapture(videos_path + filename)
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if num_frames <= 0 :
        print("Video could not be read.")
        sys.exit()
    humanCount = 0
    frame_num = 0
    while True:

        r, img = cap.read()

        if r==False:
            print("Human not found in "+filename)
            break

        img = cv2.resize(img, (x_dim, y_dim))
        boxes, scores, classes, num = odapi.processFrame(img)

        for i in range(len(boxes)):
            # Class 1 represents human
            if classes[i] == 1 and scores[i] > threshold:
                humanCount = humanCount+1

            if humanCount > humanCountThreshold:
                print("Human found in "+filename)
                alert_user(filename)
                sys.exit()
