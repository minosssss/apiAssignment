from .base import *

from .. import mysql

DEBUG = False
DATABASES = mysql.deploy.DATABASES
ALLOWED_HOSTS = ['*']