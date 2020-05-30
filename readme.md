## Edible Campus Human Recognition Project

We use TensorFlow to classify videos from [UCSB's Edible Campus program](https://sustainability.ucsb.edu/ediblecampus/) with the aim of determining whether humans are present at the garden or not. We envision that our solution might be implemented to guard against theft or vandalism.

### Scripts Usage

#### Monitoring Script
- Overview and usage:
  - Bash script for use on IoT device.
  - Extra requirements: `sudo apt-get inotify-tools`.
  - Usage: `monitor.sh [DIR]` to monitor a directory.
  - Executes Python classification script when a file with a .mkv extension is placed in DIR.
  - When a human is detected, an email is sent to the account specified in `detect_human_monitor.py`.
- Download the pre-trained model:
	- wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
	- tar -xvzf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
- Modify variables in `detect_human_monitor.py`:
	- `threshold` - percent of human within a frame.
	- `humanCountThreshold` - number of frames in the video that should contain humans.
	- `videos_path` - directory path which contains the videos.
	- `model_path` - should point to the downloaded and extracted model from above step.

#### Video Transfer Script
- Overview and usage:
  - Simulates the arrival of videos on the IoT device.
  - A new video arrives every five seconds.
  - Usage: `add_videos.sh [DIR]` to add videos to DIR.
  - DIR should be the same directory specified in the monitoring script's command line argument.
- Modify variables in `add_videos.sh`:
  - `contains_humans_dir` - directory path for videos manually classified as containing humans.
  - `human_less_dir` - directory path for videos manually classified as not containing humans.

### Team Members
Gwyneth Allwright, Swaroop Rao and Sabrina Tsui. This is our project for CS293B Cloud Computing (Spring 2020) at UCSB.
