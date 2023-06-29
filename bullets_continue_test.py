"""
Chapter 1: "The Spark of Genius"
1. Liam's childhood in the Netherlands: early signs of genius.
   - Introduction of Liam's character, his family background, and upbringing in the Netherlands.
   - Narration of instances from his childhood that demonstrated his exceptional intelligence.
   - Description of his early fascination with computers, programming, and neuroscience.

2. The development of his interest in cognitive enhancement.
   - How Liam's interest in cognitive enhancement developed during his studies in computer science.
   - The influence of his professors, peers, and industry leaders on his interests.
   - The key moments that solidified his passion for cognitive enhancement.

3. The pivotal decision to pursue his passion.
   - The circumstances that led Liam to decide to dedicate his life to cognitive enhancement.
   - His preparation for this ambitious project, including further studies and research.
   - The emotional and psychological aspects of making such a life-altering decision.

Chapter 2: "The Berlin Laboratory"
1. Moving to Berlin: a new city, a new life.
   - The reasons behind choosing Berlin as his new home.
   - His initial experiences in the city, adjusting to a new culture and lifestyle.
   - The impact of this move on his personal and professional life.

2. Setting up his lab: challenges and triumphs.
   - The process of converting a room in his Berlin apartment into a lab.
   - The challenges faced in procuring equipment, setting up the lab, and starting his research.
   - The small victories and moments of joy in successfully setting up his personal lab.

3. The commencement of his ground-breaking research.
   - The initial stages of his research, including planning, experimentation, and data analysis.
   - The breakthroughs and setbacks in his research.
   - The emotional and intellectual journey of conducting such cutting-edge research.

(Continuing in this manner for the remaining chapters...)
"""

topics = """
Chapter 1: "The Spark of Genius"
1. Liam's childhood in the Netherlands: early signs of genius.
2. The development of his interest in cognitive enhancement.
3. The pivotal decision to pursue his passion.

Chapter 2: "The Berlin Laboratory"
1. Moving to Berlin: a new city, a new life.
2. Setting up his lab: challenges and triumphs.
3. The commencement of his ground-breaking research.

Chapter 3: "The Mind’s New Frontier"
1. The process of synthesizing Modafinil and LSD derivatives.
2. The first successful experiments and results.
3. The impact of these results on Liam's work and personal life.

Chapter 4: "The Cognitive Leap"
1. The decision to personally use the substances.
2. The experience of cognitive enhancement: benefits and drawbacks.
3. The initial excitement and optimism for the future.

Chapter 5: "The Unwanted Spotlight"
1. The scientific community's reaction to Liam's work.
2. Dealing with the media and public attention.
3. The first signs of trouble: unwanted attention from less scrupulous individuals.

Chapter 6: "The Ethical Quandary"
1. The ethical implications of cognitive enhancement.
2. Liam's internal struggle with the potential misuse of his work.
3. The decision to continue or halt his research.

Chapter 7: "The Billionaire's Burden"
1. The rapid success and wealth from his work.
2. The new challenges that come with being a billionaire.
3. The impact of success on Liam's personal life and relationships.

Chapter 8: "The Invisible Enemy"
1. The threat of corporate espionage.
2. The steps taken to protect his work.
3. The constant pressure and paranoia of being under threat.

Chapter 9: "The Regulatory Gauntlet"
1. The legal challenges faced due to his work.
2. The struggle to navigate complex regulations.
3. The fight to keep his work alive amidst legal pressure.

Chapter 10: "The Crossroads of Destiny"
1. The decision about the future of cognitive enhancement.
2. Coming to terms with the societal impact of his work.
3. Liam's final decision about his personal future and legacy.
"""

import re
import openai
openai.api_key = "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" 

prompt = """
give me 10 chapters for a book about:

**Description/Theme**: Follow the exhilarating journey of a young INTJ computer scientist from the Netherlands who creates a revolutionary cognitive enhancement algorithm and becomes a billionaire, all while grappling with ethical dilemmas and the perils of rapid success.

**Genre**: Contemporary Drama / Techno-Thriller

**Main Characters**: 
   - Name: Liam
   - Age: 28
   - Personality: INTJ - highly intelligent, analytical, driven, reserved
   - Nationality: Dutch, but moved to Berlin
   - Occupation: Computer Scientist
   - Skills: Artificial intelligence, neuroscience, programming, data analysis
   
**Setting**: Present-day, Berlin, with references to Liam's life in the Netherlands, tech hubs, corporate offices.

**Plot Points**:
   - Liam, a computer scientist with a deep interest in cognitive enhancement, decides to explore the intersection of neuroscience and biochemistry.
   - He converts a room in his Berlin apartment into a small lab.
   - Through meticulous research and experimentation, he synthesizes Modafinil and LSD derivatives aimed at cognitive enhancement.
   - His personal use of the substances results in remarkable cognitive improvements.
   - Liam's work attracts attention from both the scientific community and less scrupulous individuals.
   - He faces ethical dilemmas regarding the use and distribution of these substances.
   - His life takes a tumultuous turn as he navigates wealth, legal challenges, and moral dilemmas.
   - CliLiam involves Liam making decisions that will define his future and the implications of cognitive-enhancing substances on society.
   
**Writing Style**: Fast-paced and intellectually stimulating, focusing on Liam’s analytical and strategic mindset and the impact of technology.

**Point of View**: Third person limited, mainly focused on Liams’s perspective.
   
**Dialogue Ratio**: 40% dialogue, 60% narration/description, focusing on Liam's decision-making processes and technological developments.

**Conflict Level**: High, with ethical dilemmas, corporate espionage, and regulatory challenges.

**World-building Depth**: High; detailed descriptions of AI technology, Berlin’s tech scene, and the global impact of cognitive enhancement.

**Target Audience**: Adults, particularly those interested in technology, drama, and ethical dilemmas in AI.

**Keywords Density**: "Algorithm", "Cognitive Enhancement", "Berlin", "Tech Titan", "Ethics", "AI".

**Language/Localization**: English, with some Dutch and German phrases for authenticity.
"""


chapter = """
Chapter 1: "The Spark of Genius"
- Liam's early life, interest in cognitive enhancement, and decision to pursue it.

Chapter 2: "The Berlin Laboratory"
- Setting up the lab in his apartment, beginning of his research.

Chapter 3: "The Mind’s New Frontier"
- The process of synthesizing Modafinil and LSD derivatives, and the first successful results.

Chapter 4: "The Cognitive Leap"
- Personal use of the substances, experiencing cognitive improvements, and the initial excitement.

Chapter 5: "The Unwanted Spotlight"
- Liam's work gaining attention, dealing with the scientific community, and the first signs of trouble.

Chapter 6: "The Ethical Quandary"
- Confronting the ethical dilemmas of his work, questioning the implications of cognitive enhancement.

Chapter 7: "The Billionaire's Burden"
- Rapid success, becoming a billionaire, and the unexpected challenges that come with it.

Chapter 8: "The Invisible Enemy"
- Dealing with corporate espionage, protecting his work, and the pressure of constant threats.

Chapter 9: "The Regulatory Gauntlet"
- Facing legal challenges, navigating regulations, and the struggle to keep his work alive.

Chapter 10: "The Crossroads of Destiny"
- Making decisions about his future and the future of cognitive enhancement, coming to terms with his role in shaping society.
"""

topics = """
Chapter 1: "The Spark of Genius"
1. Liam's childhood in the Netherlands: early signs of genius.
2. The development of his interest in cognitive enhancement.
3. The pivotal decision to pursue his passion.

Chapter 2: "The Berlin Laboratory"
1. Moving to Berlin: a new city, a new life.
2. Setting up his lab: challenges and triumphs.
3. The commencement of his ground-breaking research.

Chapter 3: "The Mind’s New Frontier"
1. The process of synthesizing Modafinil and LSD derivatives.
2. The first successful experiments and results.
3. The impact of these results on Liam's work and personal life.

Chapter 4: "The Cognitive Leap"
1. The decision to personally use the substances.
2. The experience of cognitive enhancement: benefits and drawbacks.
3. The initial excitement and optimism for the future.

Chapter 5: "The Unwanted Spotlight"
1. The scientific community's reaction to Liam's work.
2. Dealing with the media and public attention.
3. The first signs of trouble: unwanted attention from less scrupulous individuals.

Chapter 6: "The Ethical Quandary"
1. The ethical implications of cognitive enhancement.
2. Liam's internal struggle with the potential misuse of his work.
3. The decision to continue or halt his research.

Chapter 7: "The Billionaire's Burden"
1. The rapid success and wealth from his work.
2. The new challenges that come with being a billionaire.
3. The impact of success on Liam's personal life and relationships.

Chapter 8: "The Invisible Enemy"
1. The threat of corporate espionage.
2. The steps taken to protect his work.
3. The constant pressure and paranoia of being under threat.

Chapter 9: "The Regulatory Gauntlet"
1. The legal challenges faced due to his work.
2. The struggle to navigate complex regulations.
3. The fight to keep his work alive amidst legal pressure.

Chapter 10: "The Crossroads of Destiny"
1. The decision about the future of cognitive enhancement.
2. Coming to terms with the societal impact of his work.
3. Liam's final decision about his personal future and legacy.
"""


messages = [
            {
                "role": "system",
                "content": "you act like a pro book author"
            },
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": chapter
            },
            {
                "role": "user",
                "content": "create three topics for each of the chapters"
            },
            {
                "role": "assistant",
                "content": topics
            }
        ]

parsed_chapters = ""
outline = ""


def parse_chapters():
    global parsed_chapters
    global outline
    chapter_patterns = [
        re.compile(r'^\*\*Chapter (\d+): "(.*?)"\*\*$'),  # Format one
        re.compile(r'^Chapter (\d+): "(.*?)"$'),  # Format two
        re.compile(r"^\*\*Chapter (\d+): (.*?)\*\*$"),  # Format three
        re.compile(r"^Chapter (\d+): (.*?)$"),  # Format four
    ]
    chapters = []
    print("outline in parse chapter:")
    print(outline)
    lines = outline.split("\n")
    lines = [line for line in lines if line.strip() != '']
    print("lines:")
    print(lines)
    for line in lines:
        for chapter_pattern in chapter_patterns:
            chapter_match = chapter_pattern.match(line)
            if chapter_match:
                chapter = chapter_match.group(2)
                chapters.append(chapter)
                break
    parsed_chapters = chapters
    #print ("parsed chapters:")
    #print(self.parsed_chapters)

def bullet_points():
    global outline
    global parsed_chapters
    #messages.append({"role": "user", "content": "create detailed bullet points of each of the topics. don't abbreviate anything. provide the bullet points for each topics!"})
    messages.append({"role": "user", "content": "create detailed bullet points of each of the topics."})
    bullet_points = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 0.5).choices[0].message["content"]
    print("bullet points number one:")
    print(bullet_points)
    messages.append({"role": "assistant", "content": bullet_points})
    outline = bullet_points
    parse_chapters()
    print("parsed chapters:")
    print(parsed_chapters)
    print("len chapters:")
    print(len(parsed_chapters))
    # try at a maximum of three times to have a full outline
    for i in range(3):
        print("outline number " + str(i) + ":" + outline)
        if len(parsed_chapters) == 10:
            break
        else:
            print("not enough chapter")
            messages.append({"role": "user", "content": "continue to have bullet points for each topic of the ten chapters."})
            bullet_points = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 0.5).choices[0].message["content"]
            outline += "\n" + bullet_points    
            messages.append({"role": "assistant", "content": bullet_points})
            parse_chapters()
            
    print("outline in the end:")
    print(outline)
    




    
bullet_points()
        
