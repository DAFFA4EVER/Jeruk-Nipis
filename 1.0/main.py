import speech_recognition as sr

import data_user as ds

from scan_context import context_scan

def recognize_speech_mic(recognizer, mic):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError(recognizer, sr.Recognizer)
    if not isinstance(mic, sr.Microphone):
        raise TypeError(mic, sr.Microphone)

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response['transcription'] = recognizer.recognize_sphinx(audio)
    except sr.RequestError:
        response['success'] = False
        response['error'] = "API unavailable"
    except sr.UnknownValueError:
        response['error'] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    print(
        "Jeruk Nipis (Alpha)"
    )
    data = ds.create()
    continue_ = True
    mic = sr.Microphone(device_index=1)
    recognizer = sr.Recognizer()

    while continue_:
        print("Say Something Dude")

        audio_data = recognize_speech_mic(recognizer, mic)

        if audio_data['error']:
            print(audio_data['error'])
        else:
            context_scan(audio_data, data[0])

        sel = input("Continue?(y/n) ")
        if sel == "n":
            continue_ = False
