# Import socket module
import sys  # In order to terminate the program
import threading
from socket import *

FLAG = False  # this is a flag variable for checking quit

# start connection and xchange name
username =  input('Enter name: ')
HOST = 'localhost'
serverPort = 1234  

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, serverPort))
serverSocket.listen(1)
print('The chat server is ready to connect to a chat client')
connectionSocket, addr = serverSocket.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

connectionSocket.send(username.encode())
client_name = connectionSocket.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected')


# function for receiving message from client
def recv_from_client(conn):
    global FLAG
    try:
        # Receives the request message from the client
        while True:
            if FLAG == True:
                break
            message = conn.recv(1024).decode()
            # if 'q' is received from the client the server quits
            if message == 'q':
                conn.send('q'.encode())
                print('Closing connection')
                conn.close()
                FLAG = True
                break
            print("\n" + client_name + ': ' + message)
    except:
        conn.close()


# function for sending to client
def send_to_client(conn):
    global FLAG
    try:
        while True:
            if FLAG == True:
                break
            send_msg = input('me> ')
            # the server can provide 'q' as an input if it wish to quit
            if send_msg == 'q':
                conn.send('q'.encode())
                print('Closing connection')
                conn.close()
                FLAG = True
                break
            conn.send(send_msg.encode())
    except:
        conn.close()


# this is main function
def main():
    threads = []
    global FLAG
    t_rcv = threading.Thread(target=recv_from_client, args=(connectionSocket,))
    t_send = threading.Thread(target=send_to_client, args=(connectionSocket,))
    
    # call the function to receive message server
    #recv_from_server(connectionSocket)
    threads.append(t_rcv)
    threads.append(t_send)

    t_rcv.start()
    t_send.start()
    
    t_rcv.join()
    t_send.join()

    # closing serverScoket before exiting
    print('EXITING')
    serverSocket.close()

    #Terminate the program after sending the corresponding data
    sys.exit()

# This is where the program starts
if __name__ == '__main__':
    main()

