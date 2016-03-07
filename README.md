# scale-apis-with-pub-sub
This project gives example to create scalable APIs with pub sub. Here I have used Redis for the same. This can be used to scale CPU intensive tasks across many small machines. 

### Run Web server:
- python wsgi_server

### Run worker:
- python do_sum.py

### Prerequisites:
- Install redis server on local. It can be changed fron config.py
- Install python requirements from requirements.txt

