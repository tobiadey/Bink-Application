import time

def analyse_data(data):
    '''
    Function that will be enqueued.
    
    This function can do something like anyalyse data 
    when it is not an immediate priority to send the analysed data back to the customer.
    
    Can even send the data as an email after the process is done 
    '''
    print("Task is running")
    print(f"Input value was {data}")
    time.sleep(2) #need to give worker enough time to give result
    print("Task Completed")
    return data
