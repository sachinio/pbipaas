# This script should be run if switching devices
# It will setup all the prerequisites for this project.

import subprocess

apt_packages = ['git', 'python-pip']
pip_packages = ['flask', 'Flask-PyMongo']


def install_apt():
    cmd = ['sudo', 'apt-get', 'install','-y']
    cmd.extend(apt_packages)
    p = subprocess.Popen(cmd)
    p.communicate()


def install_pip():
    for pack in pip_packages:
        cmd = ['sudo', 'pip', 'install', pack]
        cmd.extend(pip_packages)
        p = subprocess.Popen(cmd)
        p.communicate()

install_apt()
install_pip()

