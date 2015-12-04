# This script should be run if switching devices
# It will setup all the prerequisites for this project.

import subprocess

apt_packages = ['git', 'python-pip']
pip_packages = ['flask', 'Flask-PyMongo']


def install_apt():
    p = subprocess.Popen(['sudo', 'apt-get', 'install','-y'].extend(apt_packages))
    p.communicate()


def install_pip():
    p = subprocess.Popen(['sudo', 'pip', 'install','-y'].extend(pip_packages))
    p.communicate()

install_apt()
install_pip()

