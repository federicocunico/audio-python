
# # """
# # PyAudio Example: Make a wire between input and output (i.e., record a
# # few samples and play them back immediately).
# # """

# import pyaudio

# CHUNK = 1024
# WIDTH = 2
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5

# p = pyaudio.PyAudio()

# stream = p.open(format=p.get_format_from_width(WIDTH),
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 output=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# # wf1 = wave.open("YYY.wav", 'rb')
# # wf1 = wave.open("XXX.wav", 'rb')

# # def callback(in_data, frame_count, time_info, status):
# #     data1 = wf.readframes(frame_count)
# #     data2 = wf1.readframes(frame_count)
# #     decodeddata1 = numpy.fromstring(data1, numpy.int16)
# #     decodeddata2 = numpy.fromstring(data2, numpy.int16)
# #     newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5).astype(numpy.int16)
# #     return (result.tostring(), pyaudio.paContinue)


# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     stream.write(data, CHUNK)

# print("* done")

# stream.stop_stream()
# stream.close()

# p.terminate()


# """
# # Raspberry 
# # import myPyLib   # get control-C handler

# import time
# import math
# import pyaudio
# from numpy import linspace,sin,pi,int16

# pa = None;
# s  = None;

# def init_audio(rate=8000):
#     global pa,s
#     print("init_audio: Create PyAudio object")
#     pa = pyaudio.PyAudio()
#     print("init_audio: Open stream")
#     s = pa.open(output=True,
#                 channels=1,
#                 rate=rate,
#                 format=pyaudio.paInt16,
#                 output_device_index=0)
#     print ("init_audio: audio stream initialized")

# def close_audio():
#     global pa,s
#     print ("close_audio: Closing stream")
#     s.close()
#     print( "close_audio: Terminating PyAudio Object")
#     pa.terminate()


# def note(freq, len, amp=5000, rate=8000):
#     t = linspace(0,len,len*rate)
#     data = sin(2*pi*freq*t)*amp
#     return data.astype(int16) # two byte integers

# def tone(freq=440.0, tonelen=0.5, amplitude=5000, rate=8000):
#     global s
#     # generate sound
#     tone = note(freq, tonelen, amplitude, rate)

#     # play it    
#     #print "tone.main(): start playing tone"
#     s.write(tone)


# # ##### MAIN ######
# def main():
#     # myPyLib.set_cntl_c_handler(close_audio)  # Set CNTL-C handler 

#     # open audio channel
#     init_audio()

#     # play tones forever    
#     print ("tone.main(): start playing tones")
#     while True:
#         print ("tone.main: tone() 440")
#         tone()
#         time.sleep(3)
#         print("tone.main: tone(261)")
#         tone(261,1)
#         time.sleep(3)
#         print("tone.main: tone(880)")
#         tone(880)
#         time.sleep(3)


# if __name__ == "__main__":
#     main()


# """