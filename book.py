import openai 
from bs4 import BeautifulSoup
import re

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
        self.init_book()
        self.continue_book()
        self.process_book()
        
    def chapters(self):
        print("calling chapters method")
        file_path = "prompt.md"
        with open(file_path, 'r') as file:
            content = file.read()
        self.messages.append({"role": "user", "content": content})    
        chapters = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": chapters})
        print("chapters:")
        print(chapters)
        
    def topics(self):
        print("calling topics method")
        self.messages.append({"role": "user", "content": "create three topics for each of the chapters"})
        topics = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": topics})
        print("topics:")
        print(topics)
        
    def bullet_points(self):
        print("calling bullet points method")
        self.messages.append({"role": "user", "content": "create detailed bullet points for each of the topics. don't abbreviate anything. provide the bullet points for each topics!"})
        bullet_points = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": bullet_points})
        self.outline += bullet_points
        self.parse_chapters()
        for i in range(3):
            if len(self.parsed_chapters) == 10:
                break
            else:
                self.messages.append({"role": "user", "content": "continue to have bullet points for each topic of the ten chapters."})
                bullet_points = openai.ChatCompletion.create(model="gpt-4-0613", messages=self.messages, temperature = 0.5).choices[0].message["content"]
                self.outline += "\n" + bullet_points    
                self.messages.append({"role": "assistant", "content": bullet_points})
                self.parse_chapters()
        print("bullet Points:")
        print(bullet_points)
        
    def parse_chapters(self):
        print("calling parse chapters method")
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
        print("calling parse topics method")^
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
                    break
            if line == lines[-1] and l:
                l_total.append(l)
        self.parsed_topics = l_total
        print ("parsed topics:")
        print(self.parsed_topics)
        
    def parse_bullet_points(self):   
        print("calling parse bullet points method") 
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
        
    def init_book(self):
        print("calling init book method")
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
        #todo change this name later
        with open('book_content.txt', 'w') as file:
            file.write(init_book)
            
    def continue_book(self):
        print("calling continue book method")
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
        for i in range(len(self.parsed_chapters)):
            chapter = self.parsed_chapters[i]
            start_index = 1 if i == 0 else 0
            for j in range(start_index, len(self.parsed_topics[i])):
                topic = self.parsed_topics[i][j]
                bullets = self.parsed_bullet_points[i][j]
                formatted_bullets = '\n'.join([f'{bullet.strip()}' for bullet in bullets])
                message = f"""proceed now with elaborating on chapter '{chapter}' with the topic '{topic}' and his bullet points:
                {formatted_bullets}
                
                the previous content of the book is:
                
                {previous_content}
                """
                messages.append({"role": "user", "content": message})
                continue_book = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 1.0).choices[0].message["content"]
                previous_content = continue_book
                messages.pop()
                print("continue book:")
                print(continue_book)
                self.book += '\n\n' + continue_book
                with open('book_content.txt', 'a') as file:
                    file.write('\n\n' + continue_book)
                    
                    
    def process_book():
        print("calling process book method")
        with open('book_content.txt', 'r') as file:
            lines = [line.strip() for line in file]
        previous_chapter_number = None
        cleaned_lines = []
        for line in lines:
            match = re.match(r'Chapter (\d+):', line)
            if match:
                current_chapter_number = int(match.group(1))
                if current_chapter_number == previous_chapter_number:
                    continue
                else:
                    previous_chapter_number = current_chapter_number
            elif re.match(r'(Topic \d+:|- Topic \d+:|\*\D+\*|\d+\.\D+:|- \D+:)', line):
                continue
            cleaned_lines.append(line)
        lines = cleaned_lines
        with open('new_book_content.txt', 'w') as file:
            for i in range(len(cleaned_lines)):
                if i > 0 and cleaned_lines[i] == '' and cleaned_lines[i-1] == '':
                    continue
                file.write(cleaned_lines[i] + '\n')
                    
init = Book()
    


