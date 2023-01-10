from socket import *
from plyer import notification
import os

def notify(mess):
    notification.notify(
    title = 'control',
    message = mess,
    app_icon = None,
    timeout = 10,
)
    
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

notify(f"server on listening in port {serverPort}")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence =  str.lower(connectionSocket.recv(1024).decode())
    print('recieved ',sentence)
    
    if ( 'shutdown' in sentence):
        notify('remotely shutting down')
        connectionSocket.send('shutting down'.encode())
        os.system("shutdown /s /t 10")
        
    elif ( 'hibernate' in sentence):
        notify("Remotely hibernating")
        connectionSocket.send('hibernating'.encode())
        os.system("shutdown /h")
        
    elif('test' in sentence):
        notify("testing")
        connectionSocket.send('ok'.encode())