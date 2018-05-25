import sys
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 1337
BUFFER_SIZE = 1024

outBoundData = "Cod'Munist\n"
inBoundData = ""

if len(sys.argv) > 1 :
    if sys.argv[1] == "--help" :
        print("")
        print("------------------------------------------------------")
        print("* Usage : ")
        print("    - first optional parameter = IP address (default 127.0.0.1)")
        print("    - second optional parameter = port (default 1337)")
        print("\n* example 1 : ")
        print("    java -jar clientfruit.jar")
        print("    => connects to 127.0.0.1 on port 1337")
        print("\n* example 2 : ")
        print("    java -jar clientfruit.jar 192.168.0.1 1300")
        print("    => connects to 192.168.0.1 on port 1300")
        print("------------------------------------------------------")
        quit()
    TCP_IP = sys.argv[1]
    if len(sys.argv) > 2 :
        TCP_PORT = sys.argv[2]
if len(sys.argv) == 1 :
    print("No parameters : client trying to connect locally on port 1337")
else :
    print("Parameters given : client trying to connect to IP {} on port {}".format(TCP_IP, TCP_PORT))

try :
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as err:
    print("{}.socket.{}".format(argv[0], err))
try :
    clientSocket.connect((TCP_IP, TCP_PORT))
except OSError as err:
    print("{}.connect.{}".format(argv[0], err))

clientSocket.send(outBoundData.encode())

inBoundData = clientSocket.recv(BUFFER_SIZE)

inBoundData = int(inBoundData.decode()[0])

print("Team number {}".format(inBoundData))

clientSocket.close()
