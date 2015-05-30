#!/usr/bin/env bash

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
apt-get update

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
pip install Flask

#Install MongoDB
apt-get install -y mongodb-org

