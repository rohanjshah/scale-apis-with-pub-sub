'''
Created on 07-Mar-2016

@author: Rohan Shah
'''

REDIS_CONFIG = {
                'host': 'localhost',
                'port': 6379,
                'db': 11,
                }

CHANNELS = {# identifier: channel_name
            'SUM': 'sum'
            }

RESULT_KEY = 'results_map'