#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import heartbeat

# Flask
DEBUG = False
SECRET_KEY = os.urandom(32)
APPLICATION_ROOT = '/api/downstream/v1'
SERVER_NAME = 'dsnode'

# SQLAlchemy (DB)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/downstream'  # NOQA

FILES_PATH = 'tmp/'
TAGS_PATH = 'tags/'
MMDB_PATH = 'data/GeoLite2-City.mmdb'


HEARTBEAT = heartbeat.Swizzle.Swizzle

MONGO_LOGGING = False
MONGO_URI = 'mongodb://localhost/downstream_log'

MAX_CHUNK_SIZE = 32000000
DEFAULT_CHUNK_SIZE = 100
MAX_TOKENS_PER_IP = 5
MIN_SJCX_BALANCE = 10000
MAX_SIG_MESSAGE_SIZE = 1024
REQUIRE_SIGNATURE = False
