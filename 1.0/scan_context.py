from datetime import datetime
import os
import subprocess


def time(audio_data):
    scan_voice = audio_data['transcription']
    for word in scan_voice.split():
        word.lower()
        if word == "is":  # Show current time
            waktu = datetime.now()
            current_time = waktu.strftime("%H:%M")
            print(f"Now is {current_time}")


def favorite(audio_data, data):
    scan_voice = audio_data['transcription']
    for word in scan_voice.split():
        word.lower()
        if word == "food":
            for word2 in scan_voice.split():
                word2.lower()
                if word2 == "your" or word2 == "yours":
                    print("My favorite food is Lotek")
                    break
                if word2 == "my":
                    print(f"Your favorite food is {data.name}")
                    break
        if word == "film" or word == "movie":
            for word2 in scan_voice.split():
                word2.lower()
                if word2 == "my":
                    print(f"Your favorite film is {data.film}")
                    break
                elif word2 == "your" or word2 == "yours":
                    print("My favorite film is Sword Art Online")
                    break


def name(audio_data, data):
    scan_voice = audio_data['transcription']
    for word in scan_voice.split():
        word.lower()
        if word == "my":
            if data.name == "":
                user_name = input(
                    "I don't know your name. What is your name? ")
            else:
                print(f"Your name is {data.name}")
        elif word == "your":
            print(f"My name is Jeruk Nipis")


def open_something(audio_data):
    scan_voice = audio_data['transcription']
    for word in scan_voice.split():
        word.lower()
        if word == "edge":
            os.open(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        if word == "excel":
            os.open(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        if word == "word":
            subprocess.call(
                r"%ProgramFiles%\Windows NT\Accessories\wordpad.exe")


def context_scan(audio_data, data):
    print(f"You say : {audio_data['transcription']}")
    scan_voice = audio_data['transcription']
    for word in scan_voice.split():
        word.lower()
        if word == "time":
            time(audio_data)
            break
        if word == "favorite":
            favorite(audio_data, data)
            break
        if word == "name":
            name(audio_data, data)
            break
        if word == "open":
            open_something(audio_data)
