# This script should be run if switching devices
# It will setup all the prerequisites for this project.

import subprocess

apt_packages = ['git', 'python-pip', 'mongodb']
pip_packages = ['flask', 'Flask-PyMongo']


def run_proc(cmd):
    p = subprocess.Popen(cmd)
    p.communicate()


def install_apt():
    cmd = ['sudo', 'apt-get', 'install', '-y']
    cmd.extend(apt_packages)
    run_proc(cmd)


def install_pip():
    for pack in pip_packages:
        cmd = ['sudo', 'pip', 'install', pack]
        run_proc(cmd)

run_proc(['sudo', 'apt-get', 'update'])
install_apt()
install_pip()


