#! /bin/bash
sudo apt update -y
sudo apt install python-pip -y
sudo apt install git -y
mkdir /app
cd /app
git clone https://github.com/stashconsulting/pythondemo.git
cd ./pythondemo/
pip install -r requirements.txt
python app.py &
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy