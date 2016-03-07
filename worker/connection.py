'''
Created on 08-Mar-2016

@author: Rohan Shah

Contains Connection Pool's references
'''
import redis

from config import REDIS_CONFIG

# Redis internally maintains pool of connections
# By default it creates 2 ** 31 connections
redis_conn = redis.StrictRedis(**REDIS_CONFIG)
