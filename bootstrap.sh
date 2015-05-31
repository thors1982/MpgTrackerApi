#!/usr/bin/env bash

#Install MongoDB
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
apt-get update

apt-get install -y mongodb-org

#Install Apache
apt-get install -y apache2
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi

#Install python/flask
apt-get install -y python-virtualenv
mkdir mpgTrackerApi
cd mpgTrackerApi
virtualenv venv
. venv/bin/activate
sudo pip install flask-restful
sudo pip install pymongo
sudo pip install flask-pymongo

#Run api
python /vagrant/api.py

