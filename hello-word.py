#!/usr/bin/python3
import time #Для задержки
import sys #Для вывода в поток ошибок



while True:
    print('Hello-Word')
    time.sleep(1)
    sys.stderr.write('Hello-Word stderr All Good\n')

