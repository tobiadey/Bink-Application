'''
Bink Application - Building a small project using Flask & RQ

Flask - 
Redis-
RQ- 
'''
from flask import Flask, request
from rq import Queue
from redis import Redis
import time



def hello():
    '''
    Function that will be enqueued
    '''
    return "hello world"


app = Flask(__name__)

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

if __name__ == "__main__":
    app.run(debug=True)