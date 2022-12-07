import socket
# import sys

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    # sys.stdout.flush()
    flush_input()
    msg=input('Client: ')
    client.sendto(str.encode(msg),('127.0.0.1',8000))
    if(msg=='exit'):
        print('Connection is terminated ')
        break
    data,add=client.recvfrom(1024)
    print('server:',data.decode())
