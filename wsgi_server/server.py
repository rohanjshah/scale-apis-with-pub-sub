'''
Created on 07-Mar-2016

@author: Rohan Shah

This file contains server for API response.
This uses light weight framework like bottle and connects
with workers through redis and gets response.
It is written with example API to calculate sum.
This server is the gevented system, which executes requests
in concurrent manner.
'''

from gevent import monkey
monkey.patch_all()

import ujson

from bottle import Bottle, response, run
from apis import submit_for_sum, get_result_by_task_id,\
                 get_sum

# Bottle wsgi app instance
app = Bottle()

@app.error(400)
def error400(error):
    '''
    Manages 400 Error and returns JSON
    '''
    response.content_type = 'application/json'
    return ujson.dumps({"error": True, "message": error.body})

@app.error(404)
def error404(error):
    '''
    Manages 404 Error and returns JSON
    '''
    response.content_type = 'application/json'
    return ujson.dumps({"error": True, "message": error.body})

@app.error(405)
def error405(error):
    '''
    Manages 405 Error and returns JSON
    '''
    response.content_type = 'application/json'
    return ujson.dumps({"error": True, "message": error.body})

@app.error(500)
def error500(error):
    '''
    Manages 500 Error and returns JSON
    '''
    response.content_type = 'application/json'
    return ujson.dumps({"error": True, "message": '%s:\n%s'%(error.body, error.traceback)})

# Add routes to the app. This will create different routes, allowed methods with function
app.route('/v1/submit-for-sum', ['POST'], submit_for_sum) # Submit for worker process
app.route('/v1/get-result-by-task-id/<request_id>', ['GET'], get_result_by_task_id) # get sum by job status
app.route('/v1/get-sum', ['POST'], get_sum)

if __name__ == '__main__':
    # Runs API WSGI SERVER
    # Use app variable as application when being used with uwsgi.
    run(app, host='localhost', port=8000, server='gevent')