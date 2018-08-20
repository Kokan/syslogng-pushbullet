#!/usr/bin/env python2

from setuptools import setup, find_packages

setup(name="syslogng-pushbullet",
      version="0.1",
      description="Pushbullet destination for syslog-ng.",
      long_description="",
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "requests"
          ],
      keywords=[
          "Development Status :: 3 - Alpha",
          "Operating System :: POSIX :: Linux",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: System Administrators",
          "Programming Language :: Python :: 2.7",
      ]
)
