# Hello Bink

# Explanation of application
This application is a single page flask app, that takes the paramenters given to endpoint /event. Passing the data into the  analyse_data(data) function. Conceptually analyse_data(data) can analyse certain data and return the summary of the analysis as an email.


# Steps to implement:
- Run redis server using $redis-server.
- Run $rq worker to view updates to the queue.
- Run python3 app.py in parent directory.
- Open http://127.0.0.1:5000/events
- Pass in argument like this: http://127.0.0.1:5000/event?input=parameter. Where any value can replace that of parameter.

#Testing:
- Basic unit test for functions in utils.
- run $python3 -m pytest in parent directory to start test.

# Benefit of using RQ
- Fast lookup time as it uses Redis/ Remote Dictionary server (K/V store database)- uses a system where data is read from main computer memeory.
- Reduces Load on servers as you can delay tasks based on priority. Low, Medium, High.
- Simple to implement




# Example use cases



# RQ Documentation
- https://python-rq.org/docs/