## Edible Campus Human Recognition Project

We use TensorFlow to classify videos from [UCSB's Edible Campus program](https://sustainability.ucsb.edu/ediblecampus/) with the aim of determining whether humans are present at the garden or not. We envision that our solution might be implemented to guard against theft or vandalism.

### Scripts Usage

#### Mass Copy Drive files to a directory
Requirements : <br/>
1>pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib <br/>
2>Generate OAuth2 credentials for your google account at [Google Developer Console](https://console.developers.google.com/apis/credentials) and save the generated file as credentials.json <br/>
3>Obtain the directory_id of the output directory from your drive specified in the url <br/>

Usage : python3 drive_mover.py <output_directory_id>

#### Startup Script
  To be run after booting up a new instance(installs docker, mounts a drive at /dev/vdc, and runs a docker container with jupyter, tensorflow and keras.
  - chmod +x startup.sh
  - ./startup.sh

#### Connect to Jupyter Notebook  
  To connect to the remote Jupyter notebook server. Port forwarding to the remote server
  - nohup ssh -N -f -L localhost:8888:localhost:8888 -i farm_4.pem ubuntu@(IP of remote server)
  Open localhost:8888 on your browser
 
#### Machine Learning Script
- Requirements: `python3 -m pip install --no-cache-dir -r requirements.txt`
- `python3 -W ignore train.py [--path PATH] [--extract EXTRACT] [--frames FRAMES] [--videos VIDEOS] [--xdim XDIM] [--ydim YDIM]`.
	- PATH is the path to a directory that contains directories named `contains_human` and `human_less`. Default: current working directory.
	- EXTRACT is an integer (0 or 1) that stipulates whether or not video frame extraction should be performed (it might already have been performed). Default: 1 (perform extraction).
	- FRAMES is an integer that represents the number of frames per video to extract. Default: extract 15 frames.
	- VIDEOS is an integer that can be used to restrict the number of videos to use from each of `contains_human` and `human_less`. Default: use all videos.
	- XDIM and YDIM are integers that represent the dimensions of the resized video frames. Default: 50 x 50.

#### Running InceptionV2 Trained model
- Startup Script(Install pip3, tensorflow, opencv, and mounts the volume)
	chmod +x startup.sh
	./startup.sh
- Download the pre-trained model
	wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
	tar -xvzf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
- Modify variables
	threshold - percent of human within a frame
	humanCountThreshold - number of frames in the video that should contain humans
	videos_path - directory path which contains the videos
	model_path - verify model_path points to the downloaded and extracted model from above step
- Running script
	python3 detect_human.py
- Output
	A text file with filename of the video and 1/0 representing whether human was detected or not.

### Team Members
Gwyneth Allwright, Swaroop Rao and Sabrina Tsui. This is our project for CS293B Cloud Computing (Spring 2020) at UCSB.
