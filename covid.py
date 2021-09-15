from plyer import notification
import time
import requests
from bs4 import BeautifulSoup

try:
    result = requests.get("https://www.mohfw.gov.in/").text
    soup = BeautifulSoup(result,"html.parser")
    soup.encode("utf-8")
    total_cases = soup.find("li",{"class":"bg-blue"}).get_text().strip()
    print(total_cases)

    def notif(title,cases):
        notification.notify(title= title,
                            message= cases,
                            app_icon ="C:\\Users\\hp\\Downloads\\virus.ico",
                            timeout = 10,
                            toast=False)


    while True:
        notif('Total Cases of COVID! \n Take care!\nThankyou for reading.',total_cases)
        time.sleep(1200) 
except:
    print("Please! Check your internet connection")
