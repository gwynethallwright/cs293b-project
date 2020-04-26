## Edible Campus Human Recognition Project

We use TensorFlow to classify videos from [UCSB's Edible Campus program](https://sustainability.ucsb.edu/ediblecampus/) with the aim of determining whether humans are present at the garden or not. We envision that our solution might be implemented to guard against theft or vandalism.

###Scripts Usage

####Mass Copy Drive files to a directory
Requirements : pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
               Generate OAuth2 credentials for your gmail account at (https://console.developers.google.com/apis/credentials) and save the generated file as credentials.json
	       Obtain the directory_id of the output directory from your drive specified in the url
Usage : python3 drive_mover.py <output_directory_id>

### Team Members
Gwyneth Allwright, Swaroop Rao and Sabrina Tsui. This is our project for CS293B Cloud Computing (Spring 2020) at UCSB.
