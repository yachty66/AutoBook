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
        self.chapters()
        #self.add_message()
        #self.openai_request()
        
    def chapters(self):
        #read content from prompt.md and append in same format as messagess
        file_path = "prompt.md"
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
        #add to self.messages
        self.messages.append({"role": "user", "content": content})    
        #make a request to openai and see how the content looks like
        openai_request = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        print(openai_request)
        
    def topics(self):
        
        pass
    
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
        



