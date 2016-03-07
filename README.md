# scale-apis-with-pub-sub
This project gives example to create scalable APIs with pub sub. Here I have used Redis for the same. This can be used to scale CPU intensive tasks across many small machines. 

### Run Web server:
- python wsgi_server

### Run worker:
- cd worker
- python do_sum.py

### Prerequisites:
- Install redis server on local. It can be changed fron config.py
- Install python requirements from requirements.txt

### e.g.

1.  URI: /v1/get-sum  #Get Final sum by distributed execution in back
    - method: POST,
    - payload: 
          - val1: 12.234
          - val2: 23

2.  URI: /v1/get-result-by-task-id/27558760-e4a7-11e5-abec-645a0429f291    #Gets result by request ID
    - method: GET

3.  URI: /v1/submit-for-sum    # Submits task and returns request ID
    - method: POST
    - payload: 
          - val1: 12.234
          - val2: 23
