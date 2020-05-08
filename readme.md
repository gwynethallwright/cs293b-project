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
  For Eucalyptus: `sudo apt-get install libsm6 libxrender1 libfontconfig1`
- `python3 -m pip install --no-cache-dir -r requirements.txt`
- `python3 -W ignore train.py --path [PATH] --extract [EXTRACT]`.
	- PATH is the path to a directory that contains directories named `contains_human` and `human_less`. Default: current working directory.
	- EXTRACT is an integer (0 or 1) that stipulates whether or not video frame extraction should be performed (it might already have been performed). Default: 1 (perform extraction).

### Team Members
Gwyneth Allwright, Swaroop Rao and Sabrina Tsui. This is our project for CS293B Cloud Computing (Spring 2020) at UCSB.
