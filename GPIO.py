import serial
import serial.tools.list_ports
import threading
 
devList = serial.tools.list_ports.comports()

if devList == []:
    print("No device Found")

for dev in devList:
    print(dev.device)
    if dev.pid == 60000:
        print("ok")
        break
    else:
        print("No device Found")
        quit()

ser = serial.Serial()
ser.baudrate = 115200
ser.port = dev.device

def send(data:str, Wait=False):
    if Wait:
        ser.open()
        ser.write(data.encode())
        rsp = ser.readline()[:-2].decode()
        ser.close()
        return rsp
    else:
        th = threading.Thread(target=lambda: thread(data)).start()

def thread(data):
    ser.open()
    ser.write(data.encode())
    print(ser.readline()[:-2].decode())
    ser.close()

if __name__ == "__main__":
    send("FDR")