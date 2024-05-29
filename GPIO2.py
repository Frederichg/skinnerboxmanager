import serial
import serial.tools.list_ports
import threading

# List all connected serial devices
devList = serial.tools.list_ports.comports()

# Initialize serial connection
ser = serial.Serial()
ser.baudrate = 115200

# Variable to check if device is found
device_found = False

# Try to find the Arduino Nano Every by checking connected devices
for dev in devList:
    print(f"Found device: {dev.device}")
    # Assuming the PID check is necessary, adjust or verify the correct PID
    # If you're not sure about the PID, you can comment out this check
    # and directly attempt to connect to the known COM port (COM5 in this case)
    if dev.device == "COM5":
        ser.port = dev.device
        device_found = True
        print("Arduino Nano Every found on COM5")
        break

if not device_found:
    print("Arduino Nano Every not found. Please check the connection and try again.")
else:
    # Function to send data
    def send(data:str, Wait=False):
        if Wait:
            ser.open()
            ser.write(data.encode())
            rsp = ser.readline()[:-2].decode()
            ser.close()
            return rsp
        else:
            th = threading.Thread(target=lambda: thread(data)).start()

    # Function to handle threaded sending
    def thread(data):
        ser.open()
        ser.write(data.encode())
        print(ser.readline()[:-2].decode())
        ser.close()

    if __name__ == "__main__":
        send("FDR")

