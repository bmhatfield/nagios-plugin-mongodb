#!/usr/bin/env python
from distutils.core import setup

setup(name='nagios-plugin-mongodb',
      version='0.1.0',
      description='A script to monitor MongoDB with nagios-compatible output',
      author='Mike Zupan',
      author_email='mike@zcentric.com',
      url='https://github.com/bmhatfield/nagios-plugin-mongodb',
      py_modules=['check_mongodb'],
      license='Retribution'
     )
