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
        self.book = ""
        self.parsed_chapters = ""
        self.parsed_topics = ""
        self.parsed_bullet_points = ""
        self.chapters()
        self.topics()
        self.bullet_points()
        self.parse_chapters()
        self.parse_topics()
        self.parse_bullet_points()
        self.init_book_generation()
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
        #self.str_chapters = chapters
        print("Chapters:")
        print(chapters)
        
    def topics(self):
        #add "create topics for each of the chapters" to self.messages
        self.messages.append({"role": "user", "content": "create three topics for each of the chapters"})
        #make new request to openai and see how the content looks like
        topics = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        #append topics to self.message
        self.messages.append({"role": "assistant", "content": topics})
        #self.str_topics = topics 
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
        chapter_patterns = [
            re.compile(r'^\*\*Chapter (\d+): "(.*?)"\*\*$'),  # Format one
            re.compile(r'^Chapter (\d+): "(.*?)"$'),  # Format two
            re.compile(r"^\*\*Chapter (\d+): (.*?)\*\*$"),  # Format three
            re.compile(r"^Chapter (\d+): (.*?)$"),  # Format four
        ]
        chapters = []
        lines = self.outline.split("\n")
        lines = [line for line in lines if line.strip() != '']
        for line in lines:
            for chapter_pattern in chapter_patterns:
                chapter_match = chapter_pattern.match(line)
                if chapter_match:
                    chapter = chapter_match.group(2)
                    chapters.append(chapter)
                    break
        self.parsed_chapters = chapters
        print ("parsed chapters:")
        print(self.parsed_chapters)
        
    def parse_topics(self):
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
        lines = self.outline.split("\n")
        lines = [line for line in lines if line.strip() != '']
        l = []
        l_total = []
        for line in lines:
            for chapter_pattern in chapter_patterns:
                    chapter_match = chapter_pattern.match(line)
                    if chapter_match:
                        if l:
                            l_total.append(l)
                            l = []
                        break
            for topic_pattern in topic_patterns:
                topic_match = topic_pattern.match(line)
                if topic_match:
                    l.append(topic_match.group(1))
                    print(l)
                    break
            if line == lines[-1] and l:
                l_total.append(l)
        self.parsed_topics = l_total
        print ("parsed topics:")
        print(self.parsed_topics)
        
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
        self.parsed_bullet_points = l_total
        print("parsed bullet points:")
        print(self.parsed_bullet_points)
        
    def init_book_generation(self):
        messages = [
            {
                "role": "system",
                "content": "you are a pro book author with the task of writing a book."
            },
            {
                "role":"user",
                "content": "write the outline of an book."
            },
            {
                "role":"assistant",
                "content": self.outline
            }
        ]
        chapter = self.parsed_chapters[0]
        topic = self.parsed_topics[0][0]
        bullets = self.parsed_bullet_points[0]
        formatted_bullets = '\n'.join([f'{bullet.strip()}' for bullet in bullets])
        message = f"""Start now with elaborating on chapter '{chapter}' with the topic '{topic}' and his bullet points:
        {formatted_bullets}
        """
        messages.append({"role": "user", "content": message})
        init_book = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 1.0).choices[0].message["content"]
        print("init book:")
        print(init_book)
        self.book += init_book
        with open('book_content.txt', 'w') as file:
            file.write(init_book)
                    
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


