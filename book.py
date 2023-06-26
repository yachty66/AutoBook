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
        self.outline = ""
        self.chapters()
        self.topics()
        self.bullet_points()
        #todo skip for now because consistency was always given
        #self.inconsistencies()
        
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
        chapters = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        #append chapters to self.message
        self.messages.append({"role": "assistant", "content": chapters})        

        
    def topics(self):
        #add "create topics for each of the chapters" to self.messages
        self.messages.append({"role": "user", "content": "create three topics for each of the chapters"})
        #make new request to openai and see how the content looks like
        topics = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        #append topics to self.message
        self.messages.append({"role": "assistant", "content": topics})
        
    def bullet_points(self):
        self.messages.append({"role": "user", "content": "create detailed bullet points for each of the topics. don't abbreviate anything. provide the bullet points for each topic"})
        bullet_points = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        #can repeat as long as their is no chapter ten 
        self.messages.append({"role": "assistant", "content": bullet_points})
        #add "continue this chapter" to self.messages
        self.messages.append({"role": "user", "content": "create detailed bullet points for each of the remaining chapters"})
        continuation = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": continuation})
        #add bullet_points and continuation to outline
        self.outline += bullet_points
        self.outline += continuation
        
    def inconsistencies(self):
        self.messages.append({"role": "user", "content": f"are you seeing any inconsistencies with the outline of the following book?:\n\n{self.outline}"})
        inconsistencies = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        print("inconsistencies:")
        print(inconsistencies)
        self.messages.append({"role": "assistant", "content": inconsistencies})
        #please make corrections to the outline
        self.messages.append({"role": "user", "content": "please make corrections to the chapters, topics and bullet points in the case of inconsistencies and respond with the corrected outline. include every chapter also if its consistent already"})
        corrections = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages).choices[0].message["content"]
        print("corrections:")
        print(corrections)
        
    def generate_book(self):
        """
        7. start now with elaborating on [name of chapter] with the topic [name of topic] and his bullet points:

        [all bullet points of the topic]
        """
        #need to have a dictionary which contains chapter, topic and bullet points and sukksessive generated outputs
        #iter over it and add generated content in a file where i save my book content
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
        



