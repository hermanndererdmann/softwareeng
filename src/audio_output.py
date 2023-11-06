from gtts import gTTS
from playsound import playsound  

class audio_out:
    def __init__(self):
        pass

    def text_to_speech(self, imgdata):


        # Initialize gTTS with the text to convert
        text_output = self.__data_to_text(imgdata)  
        
        tts = gTTS(text=text_output, lang= 'en', slow=False)  
        
        #Here we are saving the transformed audio in a mp3 file named  
        # exam.mp3  
        tts.save("output.mp3")  
        
        # Play the exam.mp3 file  
        playsound("output.mp3")
    
    def __data_to_text(self, imgdata):
        # pattern & color have same length
        text_list = []
        for i in range(len(imgdata.pattern)):
            text_list.append(imgdata.color[i])
            text_list.append(imgdata.pattern[i])
            text_list.append(".")

        s = " "
        return s.join(text_list)