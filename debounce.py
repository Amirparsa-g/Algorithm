import datetime
import time
def debounce(f):
    last_call = 0
    def wrapper(*args , **kwargs):
        nonlocal last_call
        current_time = time.time()
        if (current_time-last_call) < 2:
            print("you have to wait for at least 2 secconds to have access to this function")
            return
        last_call = current_time
        return f(*args , **kwargs)
    return wrapper

@debounce
def send_massage(massage):
    print(massage)

send_massage("hi")
time.sleep(1)
send_massage("hi again")
time.sleep(2)
send_massage("hi again and again")
time.sleep(2.5)
send_massage("hi again and again and again")