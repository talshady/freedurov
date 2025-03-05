import socket
import threading
import protocol
import time
import pyaudio
import numpy as np


#create a server

addr = (socket.gethostbyname(socket.gethostname()), 4444)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)
protocol.checkPingAndSmthinElseSER(server, addr)

#wait for a response, if after amn of time passes and he doesnt connect fk him

#connect to called one server, if doesnt connect then failed to connect

addr = (socket.gethostbyname(socket.gethostname()), 3333)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
protocol.checkPingAndSmthinElseCLI(client, addr)

p = pyaudio.PyAudio()
def recordAudio(sample_rate=44100):
    duration = 1#replace w smthin related to ping
    #add quality
    chunk_size = int(sample_rate * duration)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    raw_audio = stream.read(chunk_size)
    stream.stop_stream()
    stream.close()
    
recordAudio()

#now extract voice