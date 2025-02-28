import nltk
from nltk.chat.util import Chat,reflections
words=[
    [r"hi|hello|hey",["Hello, how can i help you?","Hi,how is all going?","hello back,how are you?"]]
    [r"how are you?",["I am doing good, how can i assist you today?"]]
    [r"my name is (.*)",["hello %1,your name sounds great."]]
    [r"what is your name?",["I am chatbot, there to assist you anytime."]]
    [r"(.*)",["Sorry,i didn't get you properly!"]]
    [r"Can you assist me in my work?",["Yes,there to help you always","yes please tell me"]]
    [r"bye|quit|out|see you",["Take care,byebye"]]
]
def chatbot():
    print("Hello for now!")
    a=Chat(words,reflections)
    a.converse()
chatbot()