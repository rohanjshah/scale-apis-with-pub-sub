'''
Created on 08-Mar-2016

@author: Rohan Shah
'''

from server import app, run

# Runs API WSGI SERVER
# Use app variable as application when being used with uwsgi.
run(app, host='localhost', port=8000, server='gevent')