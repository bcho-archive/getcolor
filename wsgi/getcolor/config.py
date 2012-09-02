#oding: utf-8

import os
parent = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(parent, 'data', 'getcolor.sqlite')

SITE_TITLE = 'Get Some Color See See'

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % database

#: for development
DEBUG = True
