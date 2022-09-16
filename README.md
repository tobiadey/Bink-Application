# Hello Bink
This is a single page flask app, that takes the paramenters given to endpoint **/event**. Using format **http://127.0.0.1:5000/event?data=parameter**. It passes the data into the analyse_data(data) function which returns the original input. Conceptually analyse_data(data) can analyse certain data, return a validation response to the customer then when the task is completed by the redis worker, return the summary of the analysis as an email.

# Demo Video
https://youtu.be/xc2y0eX7bgg
# Notes:
- On push unit testing is done using git actions

# Steps to implement:
- Run redis server using $redis-server.
- Run $rq worker to view updates to the queue.
- Run python3 app.py in parent directory.
- Open http://127.0.0.1:5000/events
- Pass in argument like this: http://127.0.0.1:5000/event?data=parameter. Where any value can replace "parameter".

# Testing:
- Basic unit test for functions in utils.
- run $python3 -m pytest in parent directory to start test.

# Benefit of using RQ
- Fast lookup time as it uses Redis/ Remote Dictionary server (K/V store database)- uses a system where data is read from main computer memory.
- Reduces load on servers as Redis worker executes the tasks outside of the application's HTTP server and they can be delayed based on priority. Low, Medium, High.
- Simple to implement
- Prevents timeouts from long HTTP requests.



# RQ Documentation
- https://python-rq.org/docs/