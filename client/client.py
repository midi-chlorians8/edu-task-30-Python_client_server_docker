# https://www.youtube.com/watch?v=unwP2UjWRq8
# 30.01.2022 По мотивам видео с канала SweetCoder
# Код отправляет раз в 2 секунды учебные сообщения

#!/usr/bin/python3
from encodings import utf_8
from math import fabs
from urllib import response
import requests

import time #Для даты + задержки в цикле

# ========== Блок проверки ввода пользователем параметра (url) ========== 
import sys #Для приёма аргументов
print(__name__)

debug = False

if debug == False:
    if __name__ == "__main__": 
        if len (sys.argv) > 1:
            print ("URL= , {}!".format (sys.argv[1] ) +'\n' )
        else:
            print ("Введи один параметр вида http://localhost:2000 !" +'\n' + 'Подставь свой IP и port')
            sys.exit() #Завершить программу
# ========== Блок проверки ввода пользователем параметра (url) ========== 
    from sys import argv #Чтоб передать параметром урл в код
    script, url = argv

else:
    url = 'http://localhost:2000'



i=0 #counter


while True:
    local_time = time.ctime(time.time()) #Замеряем текущее время
    
    response = requests.post(url,data='Messadge:' + str(i) +
                                      " |" + " " + "Date:" + str(local_time) ,stream=True)

    status_code = response.status_code,'status_code'

    print('I am client_1 '+ "|" + ' My_messadge:' + str(i) + 
                                      " |" + " " +  "Date:"  + str(local_time) + " " + str(status_code) )
    sys.stderr.write('I am client_1 '+ "|" + ' My_messadge:' + str(i) + 
                                      " |" + " " +  "Date:"  + str(local_time) + " " + str(status_code) )
    time.sleep(1)
    i +=1


















#print(response.status_code,'status_code')                                   
#response = requests.post(url,data='Asaka')  #requests.get(url) 
#print(response.status_code,'status_code')
#response = requests.post(url,data='Asaka')
#response = requests.get(url,stream=True)
#response = requests.post(url,data='Asaka')