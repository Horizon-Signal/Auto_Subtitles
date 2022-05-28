import speech_recognition as sr
from googletrans import Translator

class Subtitle:
    def __init__(self, file_path, source_lang_code='ja-JP', dest_lang_code='zh-CN'):
        self.source_lang = source_lang_code
        self.dest_lang = dest_lang_code
        self.file_path = file_path
        self.source_list = []
        self.dest_list = []
        self.time = []

        # generate the subtitle in source language based on the audio, add results into self.source_list
    def generate_source_sub_titles(self):
        invalid_counter = 0
        r = sr.Recognizer()
        audio_file = sr.AudioFile(self.file_path)
        size = 0

        with audio_file as source:
            total_duration = source.DURATION
            r.adjust_for_ambient_noise(source)
            while True:
                try:
                    # audio = r.record(source, duration=60)
                    audio = r.listen(source)
                    value = (r.recognize_google(audio, language=self.source_lang))

                    size += (int)(len(audio.get_aiff_data()) / 1000)
                    self.time.append(size)
                    #print(size)
                    #print(value)
                    self.source_list.append(value)

                except sr.UnknownValueError as e:
                    print("[?]")
                    # r.adjust_for_ambient_noise(source)
                    if invalid_counter > 5:
                        break
                    else:
                        invalid_counter += 1


        # Calculating the duration of each individual subtitle based on its size in byte
        # duration in secs = (size of an subtitle segment in byte / total size in byte) * total duration in secs
        index = 0
        while index < len(self.time):
            self.time[index] = (self.time[index] / size) * total_duration
            index += 1


    # Translate the source subtitle in self.source_list and fill the result into self.dest_list
    def translate(self):
        translator = Translator()
        for s in self.source_list:
            self.dest_list.append(translator.translate(s, dest=self.dest_lang).text)

    def print_dest_titles(self):
        print(len(self.time))
        print(len(self.dest_list))
        index = 0
        for s in self.dest_list:
            print(self.time[index])
            print(s)
            index += 1