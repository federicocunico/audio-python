
import pyaudio
import threading
from tabulate import tabulate
from PyAudioMixer import Clock, MicInput, Mixer, Output, Sound


def stream1():
    mix = Mixer(clock)
    song = Sound(mix, "test/the_only_file_example_i_need.wav", loop=5)
    song.play()
    mic = MicInput(mix)
    mic.unmute()
    speakers = Output(mix)
    speakers.start()

# To get device index please run audiodevicename.py


if __name__ == "__main__":
    test = pyaudio.PyAudio()

    audioindevice = []
    audiooutdevice = []

    for i in range(test.get_device_count()):
        if (test.get_device_info_by_index(i)['maxInputChannels'] > 0):
            audioindevice.append([str(i), test.get_device_info_by_index(i)['name']])
        else:
            pass

    for i in range(test.get_device_count()):
        if (test.get_device_info_by_index(i)['maxOutputChannels'] > 0):
            audiooutdevice.append([str(i), test.get_device_info_by_index(i)['name']])
        else:
            pass

    # print("Audio input devices: " + str(audioindevice) + "\n")
    print("Audio input devices: ")
    print(tabulate(audioindevice))

    # print("Audio output devices: " + str(audiooutdevice) + "\n")
    print("Audio output devices: ")
    print(tabulate(audiooutdevice))

    # Clock runs in a seperate thread
    clock = Clock()
    t1 = threading.Thread(target=stream1)
    t1.start()
