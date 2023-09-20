import socket, struct, pickle, os

class command:
    cmd:str
    arg:int

    msg = {
        "fdr0" : "checking feeder status"
    }

    rsp = {
        "fdr0" : "currently not dispensing",
        "fdr1" : "currently dispensing"
    }

    def __init__(self, cmd:str, arg:int) -> None:
        self.cmd = cmd
        self.arg = arg
    
    def pr_msg(self) -> str:
        return self.msg[self.cmd+str(self.arg)]
    def pr_rsp(self, r:int) ->str:
        return self.rsp[self.cmd.replace(" ","") + str(r)]
        

class server:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clients = []

    def __init__(self, port:int) -> None:
        """Binds to 0.0.0.0 at designated port"""
        self.serverSocket.bind(("0.0.0.0", port))
    
    def send(self, cmd:command, clientID:int, tab = None) -> int:
        """Sends a command object to the client specified in the parameters with the client index"""

        if tab != None:
            tab.Output.append(cmd.cmd + " " + str(cmd.arg))

        for i in range(5 - len(cmd.cmd)): cmd.cmd += " "
        client:socket.socket = self.clients[clientID][0]
        data = struct.pack("!4si", cmd.cmd.encode("utf-8"), cmd.arg)
        try:
            client.sendall(data)
        except:
            return -1
        return self.receive(clientID)

    def receive(self, clientID) -> command:
        """Waits till there is something to receive then returns the command object received"""
        client:socket.socket = self.clients[clientID][0]
        try:
            data = client.recv(13)
        except:
            return -1
        rsp = struct.unpack("!i", data)

        return rsp[0]

    def connect(self) -> int:
        """Waits for and accepts connections from clients nConnections times"""
        try :
            self.serverSocket.listen()
            client, ip = self.serverSocket.accept()
            clientID = int.from_bytes(client.recv(1), 'big')
            while len(self.clients) <= clientID:
                self.clients.append(None)
            self.clients[clientID] = (client, ip)
            return clientID
        except:
            return -1
    
    def receive_dict(self,clientID) ->dict:
        client:socket.socket = self.clients[clientID][0]
        try :
            data = client.recv(99999)
        except:
            return -1
        return pickle.loads(data)
    
    def send_file(self, file:os.path.pardir, clientID):
        client:socket.socket = self.clients[clientID][0]
        filesize = os.path.getsize(file)
        print(filesize)
        client.sendall(f"{file}<SEPARATOR>{filesize}".encode())
        with open(file, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read()
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                client.sendall(bytes_read)
        
class client:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self, ip, port) -> None:
        """Connects to the server at designated ip and port"""
        self.clientSocket.connect((ip, port))

    def send(self, rsp:int) -> None:
        """Sends a command object to the server"""
        data = struct.pack("!i", rsp)
        self.clientSocket.sendall(data)

    def receive(self) -> command:
        """Waits till there is something to receive then returns the command object received"""
        data = self.clientSocket.recv(13)
        cmd, arg = struct.unpack("!4si", data)
        cmd = cmd.decode("utf-8")
        cmd = cmd.replace(" ","")

        return command(cmd, arg)
    
    def setID(self, clientID:int) -> None:
        """Sends the clientID to the server"""
        self.clientSocket.sendall(clientID.to_bytes(1, 'big'))

    def send_dict(self, dict:dict):
        self.clientSocket.sendall(pickle.dumps(dict))

    def receive_file(self):
        received = self.clientSocket.recv(4096).decode()
        filename, filesize = received.split("<SEPARATOR>")
        # remove absolute path if there is
        filename = os.path.basename(filename)
        open(filename,"a").write(received)
        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = self.clientSocket.recv(4096)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)




Server = False
# Run this script to have a test client that will print all the commands it receves.

# if __name__ == "__main__" and Server:
#     serv = server(5555)
#     serv.connect()

#     while True:
#         cmd = input("cmd : ")
#         arg = input("arg : ")

#         msg = command(cmd,int(arg))
#         print(msg.pr_msg())

#         serv.send(msg,1)
#         print(msg.pr_rsp(serv.receive(1)))


# if __name__ == "__main__" and not Server:
#     ID = int(input("ID : "))
#     connection = False
#     print("attempting to connect",end='',flush=True)
#     while not connection:
#         try:
#             print(".",end='',flush=True)
#             cl = client("localhost",5555)
#         except:
#             continue
#         connection = True
#         print("\nconnected")
#     cl.setID(ID)
#     while True:
#         try:
#             data = cl.receive()
#         except:
#             print("disconnected")
#             break
#         print(data.cmd,data.arg)
#         cl.send(1)

# if __name__ == "__main__" and Server:
#     serv = server(5555)
#     serv.connect()

#     while True:
#         print(serv.receive_dict(1))


# if __name__ == "__main__" and not Server:
#     ID = 1
#     connection = False
#     print("attempting to connect",end='',flush=True)
#     while not connection:
#         try:
#             print(".",end='',flush=True)
#             cl = client("localhost",5555)
#         except:
#             continue
#         connection = True
#         print("\nconnected")
#     cl.setID(ID)

#     data = {
#         "1" : 1,
#         "2" : 2
#     }

#     while True:
#         cl.send_dict(data)

if __name__ == "__main__" and Server == False:
    cl = client("localhost",5555)
    cl.setID(1)
    data = cl.receive()
    print(data.cmd,data.arg)
    cl.send(1)
    print(cl.receive_file())
if __name__ == "__main__" and Server == True:
    serv = server(5555)
    serv.connect()
    serv.send(command("a",1),1)
    serv.send_file(__file__, 1)