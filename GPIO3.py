import serial
import serial.tools.list_ports
import threading
import logging

# Basic logging setup
logging.basicConfig(level=logging.INFO)

# Configuration parameters (could be externalized to a config file or command-line arguments)
PORT_NAME = "COM5"
BAUD_RATE = 115200
TARGET_PID = 60000  # Update this to match your device's PID if necessary

def find_device(target_pid):
    """Find and return the port of the device with the specified PID."""
    dev_list = serial.tools.list_ports.comports()
    for dev in dev_list:
        logging.info(f"Found device: {dev.device}, PID: {dev.pid}")
        if dev.pid == target_pid:
            logging.info("Target device found.")
            return dev.device
    logging.error("Target device not found.")
    return None

def send(data: str, wait=False):
    """Send data to the serial device. Wait for a response if wait is True."""
    device_port = find_device(TARGET_PID)
    if device_port is None:
        logging.error("No suitable device found.")
        return
    
    try:
        with serial.Serial(port=device_port, baudrate=BAUD_RATE) as ser:
            if wait:
                ser.write(data.encode())
                response = ser.readline()[:-2].decode()  # Adjust as necessary for your protocol
                logging.info(f"Response: {response}")
                return response
            else:
                threading.Thread(target=lambda: thread_send(ser, data)).start()
    except serial.SerialException as e:
        logging.error(f"Serial exception: {e}")

def thread_send(ser, data):
    """Function to send data in a thread."""
    try:
        ser.open()
        ser.write(data.encode())
        response = ser.readline()[:-2].decode()  # Adjust as necessary for your protocol
        logging.info(f"Thread response: {response}")
    except serial.SerialException as e:
        logging.error(f"Thread serial exception: {e}")
    finally:
        ser.close()

def receive_data(timeout=1):
    """Receive data from the serial device."""
    device_port = find_device(TARGET_PID)
    if device_port is None:
        logging.error("No suitable device found for receiving data.")
        return None

    try:
        with serial.Serial(port=device_port, baudrate=BAUD_RATE, timeout=timeout) as ser:
            data = ser.readline().decode().strip()  # Read a line and decode it
            logging.info(f"Received data: {data}")
            return data
    except serial.SerialException as e:
        logging.error(f"Error receiving data: {e}")
        return None

if __name__ == "__main__":
    # Example usage for sending data
    send("FDR", wait=False)
    # Example usage for receiving data
    received_data = receive_data()
    logging.info(f"Data received: {received_data}")

