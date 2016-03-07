'''
Created on 08-Mar-2016

@author: Rohan Shah

This worker computes sum and stores result by request id to redis
'''
import ujson
from connection import redis_conn
from config import CHANNELS, RESULT_KEY

pubsub = redis_conn.pubsub()

# subscribe to a channel
pubsub.subscribe(CHANNELS.get('SUM'))

while True:
    for item in pubsub.listen():
        try:
            subscribed_data = item['data']
            # deserialize data
            deserialized_input = ujson.loads(subscribed_data)
            request_id = deserialized_input.get('request_id')
            val1 = float(deserialized_input.get('val1'))
            val2 = float(deserialized_input.get('val2'))
            # calculate logic: here summation
            s = val1 + val2
            # set result to redis
            redis_conn.hset(RESULT_KEY, request_id, str(s))
            print "Redis Set with Key {}: Result {}".format(request_id, s)
        except ValueError as ev:
            # in case value not JSON serializable.
            pass        
        except Exception as e:
            # Publish to Redis back to consume again in case of error
            # retry logic can be added here. But not added.
            redis_conn.publish(CHANNELS.get('SUM'),
                               subscribed_data)