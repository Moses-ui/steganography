from scipy.io.wavfile import read, write
import numpy as np

filename = "song/" + input("Enter file name (.wav): ")
rate, data = read(filename)

secret = input("Enter secret message: ") + "###"
bits = list(map(int, ''.join([bin(ord(c)).lstrip('0b').rjust(8,'0') for c in secret])))

shape = data.shape
data = np.reshape(data, data.size)
for i, bit in enumerate(bits):
    data[i] = (data[i] & 254) | bit

data = np.reshape(data, shape)

output = input("Enter output name (.wav): ")
write(f"output/{output}", rate, data)