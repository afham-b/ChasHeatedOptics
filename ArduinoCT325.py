import pyfirmata
import time

# Change to the correct COM port for your Arduino
board = pyfirmata.Arduino('COM10')  # Or '/dev/ttyUSB0' on Linux

# Start an iterator thread so pyFirmata doesn't freeze
it = pyfirmata.util.Iterator(board)
it.start()

# Set up analog pin A0
analog_input = board.get_pin('a:0:i')  # a = analog, 0 = pin A0, i = input

# Read and convert voltage to temperature
def read_temperature():
    reading = analog_input.read()
    if reading is not None:
        voltage = reading * 5.0  # Arduino uses 5V reference
        temp_c = voltage / 0.010  # 0.010 V/°C
        return temp_c
    return None

# Continuously print temperature
print("Reading temperature from CT325...")
while True:
    temp = read_temperature()
    if temp is not None:
        print(f"Temperature: {temp:.2f} °C")
    else:
        print("Waiting for signal...")
    time.sleep(1)
