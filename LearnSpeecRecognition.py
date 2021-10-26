import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()
mic = sr.Microphone()

test = sr.AudioFile(r'Audio Testing\audio_files_harvard.wav')

with test as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print(type(audio))

to_text = r.recognize_sphinx(audio)

file_save = open(r'Audio Testing\To Text.txt', 'w')
file_save.writelines(to_text)

file_save.close()

print("Say Something !")
sr.Microphone(device_index=1)

with mic as mic_source:
    r.adjust_for_ambient_noise(mic_source)
    mic_audio = r.listen(mic_source)

mic_to_text = r.recognize_sphinx(mic_audio)

file_save2 = open(r'Audio Testing\Mic To Text.txt', 'w')
file_save2.writelines(mic_to_text)
file_save2.close()
