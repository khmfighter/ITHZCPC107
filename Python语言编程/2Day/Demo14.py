import socket

def socket_server():
    try:
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        bindAddr=('',8088)

        ss.bind(("localhost",8088))

    except Exception as e:
        raise e

def send_data():
    pass


if __name__=="__main__":
    socket_server()