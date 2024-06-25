from scipy.io.wavfile import read, write
import numpy as np

filename = "output/" + input("Enter file name (.wav): ")
rate, data = read(filename)

shape = data.shape
data = np.reshape(data, data.size)

byte_extract = [bytes & 1 for bytes in data]
string_extract = "".join(chr(int("".join(map(str,byte_extract[i:i+8])),2)) for i in range(0,len(byte_extract),8))
secret = string_extract.split("###")[0]

print("Secret message: " + secret)