
import pyaudio
import threading
from tabulate import tabulate
from PyAudioMixer import Clock, MicInput, Mixer, Output, Sound


class device_definition:
    def __init__(self, name):
        self.id = -1
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"


devices = {
    "console_aux": device_definition("Line In (High Definition Audio"),
    "chat_aux": device_definition("Headset Microphone (Microsoft L"),
    "chat_mic": device_definition("Headset Earphone (Microsoft Lif"),
    "headset_phone": device_definition("Speakers (HyperX Cloud Revolver"),
    "headset_mic": device_definition("Microphone (HyperX Cloud Revolv"),
}


def stream1():
    red = Mixer(clock, stereo=False)
    chat_aux = MicInput(red, devices["chat_aux"].id)
    console_aux = MicInput(red, devices["console_aux"].id)
    headset_phone = Output(red, devices["headset_phone"].id)
    console_aux.unmute()
    chat_aux.unmute()
    headset_phone.start()


def stream2():
    blue = Mixer(clock2, stereo=False)
    headset_mic = MicInput(blue, devices["headset_mic"].id)
    chat_mic = Output(blue, devices["chat_mic"].id)
    headset_mic.unmute()
    chat_mic.start()


# To get device index please run audiodevicename.py
if __name__ == "__main__":
    test = pyaudio.PyAudio()

    audioindevice = []
    audiooutdevice = []

    for i in range(test.get_device_count()):
        device_name = test.get_device_info_by_index(i)['name']
        for dk in devices.keys():
            d = devices[dk]
            if (d.name in device_name and d.id == -1):
                d.id = i

    for i in range(test.get_device_count()):
        if (test.get_device_info_by_index(i)['maxInputChannels'] > 0):
            audioindevice.append(
                [str(i), test.get_device_info_by_index(i)['name'] + f" - {test.get_device_info_by_index(i)['maxInputChannels']} - {test.get_device_info_by_index(i)['maxOutputChannels']}"])
        else:
            pass

    for i in range(test.get_device_count()):
        if (test.get_device_info_by_index(i)['maxOutputChannels'] > 0):
            audiooutdevice.append(
                [str(i), test.get_device_info_by_index(i)['name'] + f" - {test.get_device_info_by_index(i)['maxInputChannels']} - {test.get_device_info_by_index(i)['maxOutputChannels']}"])
        else:
            pass

    # print("Audio input devices: " + str(audioindevice) + "\n")
    print("Audio input devices: ")
    print(tabulate(audioindevice))

    # print("Audio output devices: " + str(audiooutdevice) + "\n")
    print("Audio output devices: ")
    print(tabulate(audiooutdevice))

    # print devices
    for dk in devices.keys():
        d = devices[dk]
        print(d)

    # Clock runs in a seperate thread
    clock = Clock()
    t1 = threading.Thread(target=stream1)
    t1.start()

    # Clock runs in a seperate thread
    clock2 = Clock()
    t1 = threading.Thread(target=stream2)
    t1.start()
