import openai 
import requests
from bs4 import BeautifulSoup

openai.api_key = "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"

class Book():
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "you act like a pro book author"
            }
        ]
        #self.add_message()
        #self.openai_request()
        
    def get_chapters(self):
        #read content from prompt.md and append in same format as messagess
        
        #make a request to openai and see how the content looks like
    
        
    def add_message(self):
        #self.messages.append(message)
        with open("intj.md", "r", encoding="utf-8") as file:
            content = file.read()    
            message = {
                "role": "user",
                "content": "Chapter 1: The Dutch Prodigy"
            }
            self.messages.append(message)
        
    def openai_request(self):        
        #there are not so many options left for continuing the story. i think i should input a few baasic parameters and the last content of the book
        for i in range(2):
            summary = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature=0.8, max_tokens = 6000).choices[0].message["content"]
            self.messages.append({"role": "assistant", "content": summary})
            self.messages.append({"role": "user", "content": " continue this chapter"})
        print("messages " + str(self.messages))

    def generate_folder(self):
        #generate folder with the name of the book if it does not exist
        pass
    
    def generate_chapter(self):
        #generate chapter with the name of the chapter if it does not exist
        pass

        
init = Book()
        



