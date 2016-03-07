'''
Created on 07-Mar-2016

@author: Rohan Shah

This module contains API entry level methods
'''
import ujson
import time
from uuid import uuid1
from threading import Timer
from bottle import request
from connection import redis_conn
from config import CHANNELS, RESULT_KEY
from validations import validate_sum_inputs

# Example method
def submit_for_sum():
    '''
    Publishes inputs to worker to sum the data
    '''
    val1 = request.forms.get('val1')
    val2 = request.forms.get('val2')
    
    # request ID pass all tasks using pub sub
    request_id = uuid1().__str__()
    
    validate_sum_inputs(val1, val2)
    
    # Publish message to redis
    redis_conn.publish(CHANNELS.get('SUM'),
                       ujson.dumps({'request_id': request_id,
                                    'val1': val1,
                                    'val2': val2}))
    # return request id to the user
    return ujson.dumps({'request_id': request_id})

def get_result_by_task_id(request_id):
    '''
    gets RESULT FROM redis for given request id if present
    '''
    data = redis_conn.hget(RESULT_KEY, request_id)
    return ujson.dumps({'result': data})

def get_sum():
    '''
    runs taks in worker to compute. Waits for task to be completed
    and returns final result. 
    This method can be used to scale the usage.
    '''
    val1 = request.forms.get('val1')
    val2 = request.forms.get('val2')
    
    # request ID pass all tasks using pub sub
    request_id = uuid1().__str__()
    
    validate_sum_inputs(val1, val2)
    
    # Publish message to redis
    redis_conn.publish(CHANNELS.get('SUM'),
                       ujson.dumps({'request_id': request_id,
                                    'val1': val1,
                                    'val2': val2}))
    
    timeout = lambda: ujson.dumps('could not retrieve sum results')
    t = Timer(0.5, timeout)
    t.start()
    while True:
        data = redis_conn.hget(RESULT_KEY, request_id)
        if data != None:
            return ujson.dumps({'result': data})
        time.sleep(0.01) # sleep for 10 ms