from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info


def RunCommand():
    # Touch a file in the current directory
    with open('xploit.txt', 'w') as f:
        f.write('xploit')
    

class RunInstallCommand(install):
    RunCommand()
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "xploit",
    version = "0.0.1",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
    },
)
