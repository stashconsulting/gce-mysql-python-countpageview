#! /bin/bash
sudo apt update -y
sudo apt install python-pip -y
sudo apt install git -y
mkdir /app
cd /app
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances="stone-door-258502:us-west1:instance"=tcp:3306
git clone https://github.com/stashconsulting/pythondemo.git
cd ./pythondemo/
pip install -r requirements.txt
python app.py &
