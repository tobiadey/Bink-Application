'''
Bink Application - Building a small project using Flask & RQ
'''
from flask import Flask, request
from rq import Queue
from redis import Redis
from app.utils.utils import analyse_data
import time


app = Flask(__name__)

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)


@app.route("/event")
def event_handler():

    if request.args.get("data"):
        data = request.args.get("data")
        job = q.enqueue(analyse_data, data)
        nl = '\n'
        q_length= len(q)
        return (
            f'Result:{job.result}'
            f'enqueued at {job.enqueued_at}'
            f'input value {data}'
            f'queue length {q_length}'
                )

    return "Nothing inputed in endpoint header"

if __name__ == "__main__":
    app.run(debug=True)