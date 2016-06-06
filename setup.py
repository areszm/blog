from setuptools import setup
import os

# Put here required packages
packages = ['Django<=1.9',]

# This is if you like use redis cloud w/Django...
if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 
   'REDISCLOUD_PASSWORD' in os.environ:
    packages.append('django-redis-cache')
    packages.append('hiredis')

setup(name='przedszkole32',          # <= Put your application name, in this case 'mysite'
       version='1.0',
       description='Przedszkole32 test strony', # <= Put your description if you want
       author='Your Name',          # <= Your name!!!!
       author_email='przedszkole32@gmail.com',
       url='https://pypi.python.org/pypi',
       install_requires=packages,
)
