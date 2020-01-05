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
