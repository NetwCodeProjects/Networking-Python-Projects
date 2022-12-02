from socket import *
import threading
import sys


FLAG = False  # this is a flag variable for checking quit

# start connection and name xchange
username =  input('Enter name: ')
HOST = 'localhost'
PORT = 1234  
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST, PORT))
print('Connecting to chat server ')
server_name = clientSocket.recv(1024)
server_name = server_name.decode()
print(server_name + ' has connected')
clientSocket.send(username.encode())

# function for sending message to server
def send_to_server(clsock):
    global FLAG
    while True:
        if FLAG == True:
            break
        # ---------if q conn close---
        send_msg = input('me> ')
        clsock.sendall(send_msg.encode())

# function for receiving message from server
def recv_from_server(clsock):
    global FLAG
    while True:
        data = clsock.recv(1024).decode()
        if data == 'q':
            print('Closing connection')
            clsock.close()
            FLAG = True
            break
        print("\n" + server_name + ': ' + data)

# this is main function
def main():
    threads = []
    
    t_send = threading.Thread(target=send_to_server, args=(clientSocket,))
    t_rcv = threading.Thread(target=recv_from_server, args=(clientSocket,))
    
    # call the function to receive message server
    #recv_from_server(clientSocket)
    threads.append(t_send)
    threads.append(t_rcv)
    
    t_send.start()
    t_rcv.start()

    t_send.join()
    t_rcv.join()

    print('EXITING')
    clientSocket.close()
    sys.exit()

# This is where the program starts
if __name__ == '__main__':
    main()