# import struct
# import math
# import pyaudio
# from itertools import count

# pa = pyaudio.PyAudio()

# FORMAT = pyaudio.paFloat32
# CHANNELS = 1
# RATE = 44100

# OUTPUT_BLOCK_TIME = 0.05
# OUTPUT_FRAMES_PER_BLOCK = int(RATE*OUTPUT_BLOCK_TIME)


# def sine_gen():
#     time = 0
#     format = "%df" % OUTPUT_FRAMES_PER_BLOCK
#     voices = []
#     voices.append(lambda sampletime: math.sin(
#         sampletime * math.pi * 2 * 440.0))

#     for frame in count():
#         block = []
#         for i in range(OUTPUT_FRAMES_PER_BLOCK):
#             sampletime = time + \
#                 (float(i) / OUTPUT_FRAMES_PER_BLOCK) * OUTPUT_BLOCK_TIME
#             sample = sum(voice(sampletime)
#                          for voice in voices) / len(voices)
#             block.append(sample)
#         yield struct.pack(format, *block)
#         time += OUTPUT_BLOCK_TIME
#         if frame == 20:
#             voices.append(
#                 lambda sampletime: math.sin(
#                     sampletime * math.pi * 2 * 880.0)
#             )


# stream = pa.open(format=FORMAT,
#                  channels=CHANNELS, rate=RATE, output=1)

# for i, block in enumerate(sine_gen()):
#     stream.write(block)
