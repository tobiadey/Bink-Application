'''
Bink Application - Building a small project using Flask & RQ

Flask - 
Redis-
RQ- 
'''
from flask import Flask, request
from rq import Queue
from redis import Redis
from utils import hello
import time


app = Flask(__name__)

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)


@app.route("/event")
def event_handler():

    if request.args.get("input"):
        input_value = request.args.get("input")
        job = q.enqueue(hello, input_value)
        return f"Job {job.id} has been enqued. Value added as input was {input_value}"

    return "Nothing inputed in endpoint header"

if __name__ == "__main__":
    app.run(debug=True)