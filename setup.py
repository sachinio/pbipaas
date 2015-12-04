# This script should be run if switching devices
# It will setup all the prerequisites for this project.

import subprocess

apt_packages = ['git', 'python-pip']
pip_packages = ['flask', 'Flask-PyMongo']


def install_apt(pack):
    p = subprocess.Popen(['sudo', 'apt-get', 'install', pack])
    p.communicate()


def install_pip(pack):
    p = subprocess.Popen(['sudo', 'pip', 'install', pack])
    p.communicate()


# install packages

for x in apt_packages:
    install_apt(x)

for x in pip_packages:
    install_pip(x)

