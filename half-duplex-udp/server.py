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

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8000))
print('Waiting for the connection')
while True:
    data,addr=s.recvfrom(1024)
    print('Client:',data.decode())
    # sys.stdout.flush()
    flush_input()
    msg=input('server: ')
    s.sendto(str.encode(msg),addr)
    if(msg=='exit'):
        print('Connection is terminated')
        break
