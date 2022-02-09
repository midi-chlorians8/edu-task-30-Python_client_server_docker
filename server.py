
# Код принимает сообщение с локальной Grafana через hook. Парсит. Решает повторяется ли прошлое сообщение или нет.
# По мотивам видео: https://www.youtube.com/watch?v=f5ic6D30_mQ
# Autor: Mister I
# 03.08.2021

# ===================================== SERVER =====================================
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём обьект сервер который пользует сокет.
server.bind(('127.0.0.1', 2000))  # Привязываем сервер к ip и порту
#server.bind(('0.0.0.0', 2000))  # Привязываем сервер к ip и порту
server.listen(4)  # Слушаем 4 входящих соединения
print('Working...')

# Test answer. Work as Received HTTP/0.9 when not allowed
client_socket, address = server.accept()
data = client_socket.recv(1624).decode('utf-8')

HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
answer = 'Well done, buddy...'.encode('utf-8')


client_socket.send(HDRS.encode('utf-8') + answer)
# Test answer. Work as Received HTTP/0.9 when not allowed

# Logical variables ============
count = 0  # Cтартовое значение
old_data = 'first'
new_data = 'second'
# Logical variables ============

    # Обработка повторяемости.
def add():
       
    if count % 2 == 0:
        new_data = message_string

    else:
        old_data = message_string

    if new_data == old_data:
        return print("Povtor!")
    else:
        return print("Net Povtora")
        #print(old_data)
        #print(new_data)
    # Обработка повторяемости

# ===================================== SERVER =====================================




while True:  # В цикле бесконечном слушаем и печатаем входящие данные
    client_socket, address = server.accept()  # Тут задержка программы пока не придут данные на сокет. Сокет - програмный интерфейс приаттаченный к порту
    data = client_socket.recv(1024).decode('utf-8')  # Принимаем 1024 байта и декодируем их как строку в utf-8 кодировке

    # ============= Инкримент вход сообщений. Нужен для обработки повторов
#    count = count + 1
#    print("count:", + count)

    # ============= Инкримент вход сообщений. Нужен для обработки повторов

    print('\n=========================\n')
    print(data) #//Распечатать сырые данные вход

    split_data = data.split("\n")  # Нарезаем в массив строк по символу переноса строки

    # print("split_data:")
    # print(split_data)

    # print("split_data[0]:")
    # print(split_data[0])

    # print("split_data[7]:")
    # print(split_data[7],'\n')

    # messadge_string = split_data[7].split(",")  #Нарезаем в массив строк по символу ЗАПЯТАЯ
    message_string = split_data[len(split_data) - 1].split(
        ",")  # Нарезаем в массив строк по символу ЗАПЯТАЯ ; [len(split_data)-1] = Последний элемент массива. Счёт с нуля поэтому -1
    #print("Message_strings [all] :")
    #print(message_string[0])
    
    # print(len(messadge_string) )    #len() тут кол во элементов в массиве
    
    #for x in message_string:  # Перебирает все элементы массива и распечатывает
    #    print(x)  # Перебирает все элементы массива и распечатывает

    #add()

    #content = load_page_from_get_request(data) #'dadada...'.encode('utf-8')
    client_socket.send(HDRS.encode('utf-8') + answer)

print('shutdown this shit...')



