import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "No Problem",
            message = "I Have A Message For You!",
            timeout = 10  #seconds
        )
        time.sleep(15) #seconds
