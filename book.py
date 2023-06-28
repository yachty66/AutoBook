import openai 
import requests
from bs4 import BeautifulSoup
import re
import json

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
        self.parse_chapters()
        self.parse_topics()
        self.parse_bullet_points()
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
        chapters = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        #append chapters to self.message
        self.messages.append({"role": "assistant", "content": chapters})
        print("Chapters:")
        print(chapters)
        
    def topics(self):
        #add "create topics for each of the chapters" to self.messages
        self.messages.append({"role": "user", "content": "create three topics for each of the chapters"})
        #make new request to openai and see how the content looks like
        topics = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        #append topics to self.message
        self.messages.append({"role": "assistant", "content": topics})
        print("Topics:")
        print(topics)
        
    def bullet_points(self):
        self.messages.append({"role": "user", "content": "create detailed bullet points for each of the topics. don't abbreviate anything. provide the bullet points for each topics!"})
        bullet_points = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": bullet_points})
        self.outline += bullet_points
        print("Bullet Points:")
        print(bullet_points)
        
    def parse_chapters(self):
        #Chapter 1: "The Reluctant Genius", **Chapter 1: The Whispers of Genius**
        chapter_pattern = r'Chapter \d+: "(.*?)"'
        chapters = re.findall(chapter_pattern, self.outline)
        chapters_json = {'chapters': chapters}
        print ("parsed chapters:")
        print(chapters_json)
        
    def parse_topics(self):
        # Add the topics and the number of the chapter where the topic is mentioned
        topics = re.findall(r'(?<=Chapter )(\d+)|- Topic \d+: (.+)|^\d\. (.+):|^- (.+):|^\d\. (.+)$', self.outline, re.MULTILINE)
        cleaned_topics = {}
        current_chapter = 0
        for topic in topics:
            if topic[0]:
                current_chapter = int(topic[0])
            else:
                topic_text = topic[1] if topic[1] else (topic[2] if topic[2] else (topic[3] if topic[3] else topic[4]))
                cleaned_topics[f"{topic_text}"] = current_chapter
        print ("parsed topics:")
        print(cleaned_topics)
        
    def parse_bullet_points(self):    
        chapter_patterns = [
            re.compile(r'^\*\*Chapter (\d+): "(.*?)"\*\*$'),  # Format one
            re.compile(r'^Chapter (\d+): "(.*?)"$'),  # Format two
            re.compile(r"^\*\*Chapter (\d+): (.*?)\*\*$"),  # Format three
            re.compile(r"^Chapter (\d+): (.*?)$"),  # Format four
        ]
        topic_pattern1 = re.compile(r'^\s*\d+\.\s*(.*?)\.?$')
        topic_pattern2 = re.compile(r"^\s*-?\s*\d*\.*\s*(.*:)\s*$")
        topic_pattern3 = re.compile(r"^\s*-\s*Topic\s*\d+:\s*(.*?)\.?$")
        topic_patterns = [topic_pattern1, topic_pattern2, topic_pattern3]
        is_inside_topic = False
        is_topic = False
        l_total = []
        l = []
        lines = self.outline.split("\n")
        lines = [line for line in lines if line.strip() != '']
        for line in lines:
            is_topic = False
            for chapter_pattern in chapter_patterns:
                chapter_match = chapter_pattern.match(line)
                if chapter_match:
                    is_inside_topic = False
            for topic_pattern in topic_patterns:
                topic_match = topic_pattern.match(line)
                if topic_match:
                    is_topic = True
                    is_inside_topic = True 
                    if l:
                        l_total.append(l)
                        l = []
                    break
            if not is_topic and is_inside_topic:
                l.append(line)
                if lines.index(line) == len(lines) - 2:
                    l_total.append(l)
        print("parsed bullet points:")
        print(l_total)
        
    def init_book_generation(self):
        pass
        
    """def inconsistencies(self):
        self.messages.append({"role": "user", "content": f"are you seeing any inconsistencies with the outline of the following book?:\n\n{self.outline}"})
        inconsistencies = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        print("inconsistencies:")
        print(inconsistencies)
        self.messages.append({"role": "assistant", "content": inconsistencies})
        #please make corrections to the outline
        self.messages.append({"role": "user", "content": "please make corrections to the chapters, topics and bullet points in the case of inconsistencies and respond with the corrected outline. include every chapter also if its consistent already"})
        corrections = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        print("corrections:")
        print(corrections)"""
        

init = Book()
        
#Chapters:
#Chapter 1: "An Unconventional Mind"
#- Introduction to Liam, his background, personality, and his life in the Netherlands. His move to Berlin and his fascination with cognitive enhancement.


