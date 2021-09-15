from plyer import notification
import time


def notif(title,message):
    notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=True)

if __name__ =='__main__':
    while True:
        notif('Hello Amazing people!', 'Thankyou for reading! Take care!')
        time.sleep(5) 
