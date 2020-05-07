## Edible Campus Human Recognition Project

We use TensorFlow to classify videos from [UCSB's Edible Campus program](https://sustainability.ucsb.edu/ediblecampus/) with the aim of determining whether humans are present at the garden or not. We envision that our solution might be implemented to guard against theft or vandalism.

### Scripts Usage

#### Mass Copy Drive files to a directory
Requirements : <br/>
1>pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib <br/>
2>Generate OAuth2 credentials for your google account at [Google Developer Console](https://console.developers.google.com/apis/credentials) and save the generated file as credentials.json <br/>
3>Obtain the directory_id of the output directory from your drive specified in the url <br/>

Usage : python3 drive_mover.py <output_directory_id>

#### Machine Learning Script
- For Eucalyptus: `sudo apt-get install libsm6 libxrender1 libfontconfig1`
- `python3 -m pip install --no-cache-dir requirements.txt`
- `python3 -W ignore train.py --path [PATH]`, where PATH is the path to a directory that contains directories named `contains_human` and `human_less`.

### Team Members
Gwyneth Allwright, Swaroop Rao and Sabrina Tsui. This is our project for CS293B Cloud Computing (Spring 2020) at UCSB.
