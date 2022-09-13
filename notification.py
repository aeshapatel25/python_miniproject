import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "** Please drink more water!!",
            message = " It is IMP ",
            timeout = 10
        )
       