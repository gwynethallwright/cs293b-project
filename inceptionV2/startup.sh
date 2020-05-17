sudo apt-get update
sudo apt-get install -y python3-pip libsm6 libxrender1 libfontconfig1
python3 -m pip install --no-cache-dir -r requirements.txt
mkdir volume
sudo mount /dev/vdc volume/
