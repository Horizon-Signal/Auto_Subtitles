from core.subtitle import Subtitle

subt = Subtitle('?', 'ja-JP', 'zh-CN')
subt.generate_source_sub_titles()
subt.translate()
subt.print_dest_titles()




    # mic = sr.Microphone()
    # with mic as source:
    #      r.adjust_for_ambient_noise(source)
    #      audio = r.listen(source)
    #      value = r.recognize_google(audio, language="zh-CN")
    #      print(value)