

from .base import *
from .. import mysql

DEBUG = True
DATABASES = mysql.local.DATABASES
ALLOWED_HOSTS = ['*']