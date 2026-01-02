import socket

def port_scanner(target):
    open_ports = []

    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.4)

            if sock.connect_ex((target, port)) == 0:
                open_ports.append(port)

            sock.close()
        except:
            pass

    return open_ports