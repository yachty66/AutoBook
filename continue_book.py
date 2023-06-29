"""
proceed now with elaborating on [name of chapter] with the topic [name of topic] and his bullet points:

[all bullet points of the topic]

the previous content of the book is:

[previous output of the model]
"""

import openai
openai.api_key = "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"

book =""

parsed_chapters = ['The Dutch Prodigy: A Childhood in the Netherlands', 'The Berlin Experiment: A New Beginning', 'The Synthesis: Birth of a Breakthrough', 'The Ascendancy: Cognitive Enhancement Unveiled', 'The Spotlight: Attention from the World', 'The Dilemma: Power and Responsibility', "The Billionaire's Burden: A Rapid Rise to Wealth", 'The Espionage: Shadows in the Tech World', 'The Decision: Defining the Future', 'The Aftermath: A New Era of Cognitive Enhancement']

parsed_topics = [["Liam's early life and family background in the Netherlands", "The development of Liam's interest in computer science and neuroscience", 'The factors and events that led Liam to move to Berlin'], ["Liam's transition to life in Berlin and the setup of his lab", 'The initial challenges and breakthroughs in his research', "Liam's personal and professional life in Berlin"], ['The scientific process and experimentation leading to the synthesis', "Liam's initial reaction and response to the successful synthesis", 'The decision to test the substances on himself'], ["The effects of the substances on Liam's cognitive abilities", "The changes in Liam's life due to his enhanced cognition", 'The implications of these enhancements for the broader field of neuroscience'], ["The scientific community's response to Liam's work", 'The interest from less scrupulous individuals and organizations', 'The media attention and public opinion on his research'], ['The ethical implications of cognitive enhancement substances', "Liam's personal struggle with the moral dilemmas of his work", 'The potential misuse and abuse of the substances'], ["The financial success and wealth resulting from Liam's work", 'The challenges and pitfalls associated with sudden wealth', 'The impact of his newfound wealth on his personal and professional relationships'], ["The introduction of corporate espionage into Liam's life", 'The legal challenges and threats to his work', "Liam's strategies and responses to these threats"], ['The choices Liam faces regarding the future of his work', 'The potential outcomes and consequences of these decisions', 'The influence of external factors and pressures on his decision-making process'], ["The immediate aftermath of Liam's decisions", 'The long-term implications for the field of cognitive enhancement', "Liam's reflections on his journey and the future of his work"]]

parsed_bullet_points = [['   - Born and raised in the Netherlands, in a family with a strong academic background.', '   - Parents are both professors, fostering an environment of intellectual curiosity.', "   - Early exposure to computers and science through his father's work."], ['   - Started coding at a young age, showing a natural talent for it.', '   - Developed an interest in neuroscience after reading a book on the human brain.', '   - Began to explore the intersection of computer science and neuroscience during his university years.'], ['   - Accepted a job offer from a tech startup in Berlin after graduation.', '   - The appeal of Berlin’s vibrant tech scene and the opportunity to further his research.', '   - Desire for a change of scenery and new challenges.'], ['   - Adjustment to the cultural differences between the Netherlands and Germany.', '   - Finding a suitable apartment and converting a room into a lab.', '   - Gathering necessary equipment and materials for his research.'], ['   - Initial failures and setbacks in his experiments.', '   - Breakthrough in synthesizing Modafinil and LSD derivatives.', '   - Emotional and mental response to his first successful experiment.'], ['   - Balancing work at the startup with his personal research.', '   - Building new relationships and networks in the tech industry.', '   - Personal life, hobbies, and how he spends his leisure time.'], ['   - Detailed process of synthesizing the cognitive enhancement substances.', '   - Challenges encountered during the synthesis process.', '   - The moment of success when the substances were finally synthesized.'], ['   - Initial disbelief and excitement at the successful synthesis.', '   - Decision to test the substances on himself, considering the risks and potential benefits.', '   - Preparing himself physically and mentally for the experiment.'], ['   - Internal debate about the ethics and potential dangers of self-experimentation.', '   - Taking the first dose and documenting the effects.', '   - The immediate and long-term effects of the substances on his cognition.'], ['   - Enhanced memory recall, increased focus, and improved problem-solving skills.', '   - Changes in his perception and understanding of complex concepts.', '   - The impact of these enhancements on his work and daily life.'], ['   - Rapid progress in his work and research due to enhanced abilities.', '   - Changes in his personal relationships and social interactions.', '   - The emotional and psychological impact of his enhanced cognition.'], ['   - Potential benefits of cognitive enhancement for various fields like medicine, education, and technology.', '   - Ethical considerations and potential misuse of such substances.', '   - The future of neuroscience with the introduction of cognitive enhancement.'], ['   - Recognition and accolades from the scientific community.', '   - Criticism and skepticism from some scientists and ethicists.', '   - Invitations to speak at conferences and contribute to scientific journals.'], ['   - Offers from corporations and individuals to buy his formula.', '   - Threats and coercion from people wanting to misuse his work.', '   - Measures taken to protect his work and himself.'], ['   - Coverage of his work in the media, both positive and negative.', '   - Public opinion divided between admiration, skepticism, and fear.', '   - Handling media interviews and public scrutiny.'], ['   - Debate about the fairness and ethical implications of cognitive enhancement.', '   - Potential for misuse and abuse of these substances.', '   - The responsibility of scientists in ensuring ethical use of their creations.'], ['   - Internal conflict about the right way to use and distribute the substances.', '   - The pressure of having created something with such potential for good and harm.', '   - Consultation with ethicists, lawyers, and fellow scientists about the best course of action.'], ['   - Scenarios of potential misuse, such as performance enhancement in sports or military applications.', '   - The danger of the substances falling into the wrong hands.', '   - Measures taken to prevent misuse and ensure ethical use.'], ['   - The economic value of his cognitive enhancement substances.', '   - Becoming a billionaire and the changes that brings to his life.', '   - The business aspects of his work, such as patents, licensing, and corporate partnerships.'], ['   - Dealing with financial advisors, lawyers, and the media.', '   - The impact of wealth on his personal relationships.', '   - The responsibility and pressure that comes with wealth.'], ['   - Changes in his relationships with friends, family, and colleagues.', '   - Dealing with jealousy, opportunism, and expectations from others.', '   - The challenge of maintaining authenticity and staying true to his values.'], ['   - Discovery of attempts to steal his work and sabotage his research.', '   - Dealing with corporate spies and infiltrators.', '   - The impact of this threat on his work and mental state.'], ['   - Legal battles to protect his patents and intellectual property.', '   - Dealing with lawsuits, regulatory challenges, and legal threats.', '   - The role of his legal team in navigating these challenges.'], ['   - Development of security measures to protect his work.', '   - Strategic decisions to counteract corporate espionage and legal threats.', '   - The mental and emotional toll of dealing with these threats.'], ['   - Decision about who should have access to the substances and under what conditions.', '   - Consideration of potential partnerships and collaborations.', '   - The dilemma of profit versus ethics and responsibility.'], ['   - Forecasting the potential impact of his decisions on society and the field of neuroscience.', '   - Weighing the potential benefits against the risks and ethical considerations.', '   - The pressure of making decisions that could change the world.'], ['   - The role of public opinion, legal considerations, and personal values in his decision-making.', '   - Dealing with pressure from corporations, government agencies, and the scientific community.', '   - Balancing his personal ambitions with his responsibility to society.'], ['   - Public and private reactions to his decisions.', '   - The impact of his decisions on his personal and professional life.', '   - Dealing with the consequences, both expected and unexpected.'], ['   - The potential for further research and development in cognitive enhancement.', '   - The regulatory and ethical landscape for cognitive enhancement substances.', "   - The role of Liam's work in shaping the future of neuroscience."], ['   - Reflections on his journey, his successes, and his mistakes.', '   - His plans and aspirations for the future.', '   - His hopes for the impact of his work on society and the field of neuroscience.']]

outline = """
Chapter 1: "The Dutch Prodigy: A Childhood in the Netherlands"
- Topic 1: Liam's early life and family background in the Netherlands.
   - Born and raised in the Netherlands, in a family with a strong academic background.
   - Parents are both professors, fostering an environment of intellectual curiosity.
   - Early exposure to computers and science through his father's work.
- Topic 2: The development of Liam's interest in computer science and neuroscience.
   - Started coding at a young age, showing a natural talent for it.
   - Developed an interest in neuroscience after reading a book on the human brain.
   - Began to explore the intersection of computer science and neuroscience during his university years.
- Topic 3: The factors and events that led Liam to move to Berlin.
   - Accepted a job offer from a tech startup in Berlin after graduation.
   - The appeal of Berlin’s vibrant tech scene and the opportunity to further his research.
   - Desire for a change of scenery and new challenges.

Chapter 2: "The Berlin Experiment: A New Beginning"
- Topic 1: Liam's transition to life in Berlin and the setup of his lab.
   - Adjustment to the cultural differences between the Netherlands and Germany.
   - Finding a suitable apartment and converting a room into a lab.
   - Gathering necessary equipment and materials for his research.
- Topic 2: The initial challenges and breakthroughs in his research.
   - Initial failures and setbacks in his experiments.
   - Breakthrough in synthesizing Modafinil and LSD derivatives.
   - Emotional and mental response to his first successful experiment.
- Topic 3: Liam's personal and professional life in Berlin.
   - Balancing work at the startup with his personal research.
   - Building new relationships and networks in the tech industry.
   - Personal life, hobbies, and how he spends his leisure time.

Chapter 3: "The Synthesis: Birth of a Breakthrough"
- Topic 1: The scientific process and experimentation leading to the synthesis.
   - Detailed process of synthesizing the cognitive enhancement substances.
   - Challenges encountered during the synthesis process.
   - The moment of success when the substances were finally synthesized.
- Topic 2: Liam's initial reaction and response to the successful synthesis.
   - Initial disbelief and excitement at the successful synthesis.
   - Decision to test the substances on himself, considering the risks and potential benefits.
   - Preparing himself physically and mentally for the experiment.
- Topic 3: The decision to test the substances on himself.
   - Internal debate about the ethics and potential dangers of self-experimentation.
   - Taking the first dose and documenting the effects.
   - The immediate and long-term effects of the substances on his cognition.

Chapter 4: "The Ascendancy: Cognitive Enhancement Unveiled"
- Topic 1: The effects of the substances on Liam's cognitive abilities.
   - Enhanced memory recall, increased focus, and improved problem-solving skills.
   - Changes in his perception and understanding of complex concepts.
   - The impact of these enhancements on his work and daily life.
- Topic 2: The changes in Liam's life due to his enhanced cognition.
   - Rapid progress in his work and research due to enhanced abilities.
   - Changes in his personal relationships and social interactions.
   - The emotional and psychological impact of his enhanced cognition.
- Topic 3: The implications of these enhancements for the broader field of neuroscience.
   - Potential benefits of cognitive enhancement for various fields like medicine, education, and technology.
   - Ethical considerations and potential misuse of such substances.
   - The future of neuroscience with the introduction of cognitive enhancement.

Chapter 5: "The Spotlight: Attention from the World"
- Topic 1: The scientific community's response to Liam's work.
   - Recognition and accolades from the scientific community.
   - Criticism and skepticism from some scientists and ethicists.
   - Invitations to speak at conferences and contribute to scientific journals.
- Topic 2: The interest from less scrupulous individuals and organizations.
   - Offers from corporations and individuals to buy his formula.
   - Threats and coercion from people wanting to misuse his work.
   - Measures taken to protect his work and himself.
- Topic 3: The media attention and public opinion on his research.
   - Coverage of his work in the media, both positive and negative.
   - Public opinion divided between admiration, skepticism, and fear.
   - Handling media interviews and public scrutiny.

Chapter 6: "The Dilemma: Power and Responsibility"
- Topic 1: The ethical implications of cognitive enhancement substances.
   - Debate about the fairness and ethical implications of cognitive enhancement.
   - Potential for misuse and abuse of these substances.
   - The responsibility of scientists in ensuring ethical use of their creations.
- Topic 2: Liam's personal struggle with the moral dilemmas of his work.
   - Internal conflict about the right way to use and distribute the substances.
   - The pressure of having created something with such potential for good and harm.
   - Consultation with ethicists, lawyers, and fellow scientists about the best course of action.
- Topic 3: The potential misuse and abuse of the substances.
   - Scenarios of potential misuse, such as performance enhancement in sports or military applications.
   - The danger of the substances falling into the wrong hands.
   - Measures taken to prevent misuse and ensure ethical use.

Chapter 7: "The Billionaire's Burden: A Rapid Rise to Wealth"
- Topic 1: The financial success and wealth resulting from Liam's work.
   - The economic value of his cognitive enhancement substances.
   - Becoming a billionaire and the changes that brings to his life.
   - The business aspects of his work, such as patents, licensing, and corporate partnerships.
- Topic 2: The challenges and pitfalls associated with sudden wealth.
   - Dealing with financial advisors, lawyers, and the media.
   - The impact of wealth on his personal relationships.
   - The responsibility and pressure that comes with wealth.
- Topic 3: The impact of his newfound wealth on his personal and professional relationships.
   - Changes in his relationships with friends, family, and colleagues.
   - Dealing with jealousy, opportunism, and expectations from others.
   - The challenge of maintaining authenticity and staying true to his values.

Chapter 8: "The Espionage: Shadows in the Tech World"
- Topic 1: The introduction of corporate espionage into Liam's life.
   - Discovery of attempts to steal his work and sabotage his research.
   - Dealing with corporate spies and infiltrators.
   - The impact of this threat on his work and mental state.
- Topic 2: The legal challenges and threats to his work.
   - Legal battles to protect his patents and intellectual property.
   - Dealing with lawsuits, regulatory challenges, and legal threats.
   - The role of his legal team in navigating these challenges.
- Topic 3: Liam's strategies and responses to these threats.
   - Development of security measures to protect his work.
   - Strategic decisions to counteract corporate espionage and legal threats.
   - The mental and emotional toll of dealing with these threats.

Chapter 9: "The Decision: Defining the Future"
- Topic 1: The choices Liam faces regarding the future of his work.
   - Decision about who should have access to the substances and under what conditions.
   - Consideration of potential partnerships and collaborations.
   - The dilemma of profit versus ethics and responsibility.
- Topic 2: The potential outcomes and consequences of these decisions.
   - Forecasting the potential impact of his decisions on society and the field of neuroscience.
   - Weighing the potential benefits against the risks and ethical considerations.
   - The pressure of making decisions that could change the world.
- Topic 3: The influence of external factors and pressures on his decision-making process.
   - The role of public opinion, legal considerations, and personal values in his decision-making.
   - Dealing with pressure from corporations, government agencies, and the scientific community.
   - Balancing his personal ambitions with his responsibility to society.

Chapter 10: "The Aftermath: A New Era of Cognitive Enhancement"
- Topic 1: The immediate aftermath of Liam's decisions.
   - Public and private reactions to his decisions.
   - The impact of his decisions on his personal and professional life.
   - Dealing with the consequences, both expected and unexpected.
- Topic 2: The long-term implications for the field of cognitive enhancement.
   - The potential for further research and development in cognitive enhancement.
   - The regulatory and ethical landscape for cognitive enhancement substances.
   - The role of Liam's work in shaping the future of neuroscience.
- Topic 3: Liam's reflections on his journey and the future of his work.
   - Reflections on his journey, his successes, and his mistakes.
   - His plans and aspirations for the future.
   - His hopes for the impact of his work on society and the field of neuroscience.
"""
import re

previous_content = ""

def init_book():
    global previous_content
    global parsed_chapters
    global parsed_topics
    global parsed_bullet_points
    global book
    
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
            "content": outline
        }
    ]
    chapter = parsed_chapters[0]
    topic = parsed_topics[0][0]
    bullets = parsed_bullet_points[0]
    formatted_bullets = '\n'.join([f'{bullet.strip()}' for bullet in bullets])
    message = f"""Start now with elaborating on chapter '{chapter}' with the topic '{topic}' and his bullet points:
    {formatted_bullets}
    """
    messages.append({"role": "user", "content": message})
    init_book = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 1.0).choices[0].message["content"]
    previous_content = init_book
    print("----------------init book:----------------")
    print(init_book)
    book += init_book
    with open('book_content2.txt', 'w') as file:
        file.write(init_book)
        
def continue_book():
    global previous_content
    global parsed_chapters
    global parsed_topics
    global parsed_bullet_points
    global book
    
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
            "content": outline
        }
    ]
    for i in range(len(parsed_chapters)):
        chapter = parsed_chapters[i]
        start_index = 1 if i == 0 else 0
        for j in range(start_index, len(parsed_topics[i])):
            topic = parsed_topics[i][j]
            bullets = parsed_bullet_points[i][j]
            formatted_bullets = '\n'.join([f'{bullet.strip()}' for bullet in bullets])
            #make request 
            message = f"""proceed now with elaborating on chapter '{chapter}' with the topic '{topic}' and his bullet points:
            {formatted_bullets}
            
            the previous content of the book is:
            
            {previous_content}
            """
            messages.append({"role": "user", "content": message})
            continue_book = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 1.0).choices[0].message["content"]
            previous_content = continue_book
            #remove last message again
            messages.pop()
            print("----------------continue book:----------------")
            print(continue_book)
            book += '\n\n' + continue_book
            with open('book_content2.txt', 'a') as file:
                file.write('\n\n' + continue_book)
                
                

def process_book():
    #here i do anything for making the cleanup of the book
    #i need of cource always the chapter but only once
    #can start with removing all chapter duplicates. i think it also would make it easier if i just going to remove all topics. so i can try to match chapter patterns and 
    
    with open('test.txt', 'r') as file:
        lines = [line.strip() for line in file]
    print(lines)
    
    #iter over lines and check if a line matches the pattern of a chapter 
    #if so get the number of the chapter and store it in a variable. compare number with previous chapter number if its the same remove current line from lines
    previous_chapter_number = None
    cleaned_lines = []
    for line in lines:
        # Check if the line matches the pattern of a chapter
        match = re.match(r'Chapter (\d+):', line)
        if match:
            current_chapter_number = int(match.group(1))
            # If the chapter number is the same as the previous one, skip this line
            if current_chapter_number == previous_chapter_number:
                continue
            else:
                previous_chapter_number = current_chapter_number
        cleaned_lines.append(line)

    lines = cleaned_lines
    with open('test2.txt', 'w') as file:
        for line in cleaned_lines:
            file.write(line + '\n')
    
    
         
process_book()
#init_book()
#continue_book()