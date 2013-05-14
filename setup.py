#!/usr/bin/env python
from distutils.core import setup

nagios_path = '/usr/lib/nagios/plugins'

setup(name='nagios-plugin-mongodb',
      version='0.1.0',
      description='A script to monitor MongoDB with nagios-compatible output',
      author='Mike Zupan',
      author_email='mike@zcentric.com',
      url='https://github.com/bmhatfield/nagios-plugin-mongodb',
      data_files=[(nagios_path, 'check_mongodb.py')],
      license='Retribution'
     )
