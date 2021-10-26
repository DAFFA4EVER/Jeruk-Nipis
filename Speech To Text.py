import speech_recognition as sr

data = [].__str__()

def printWords(s):
    global data
    s = s.split()
    for word in s:
        print(word)


mic_input = sr.Microphone(device_index=1)
recognizer = sr.Recognizer()

print("Say something !")

# Mic input
with mic_input as source:
    recognizer.adjust_for_ambient_noise(source)
    mic_input = recognizer.listen(source)

# Save mic input data and recognize it
speech_to_text = recognizer.recognize_google(mic_input)

print(f'You say : {speech_to_text}')


test = False

print(test)