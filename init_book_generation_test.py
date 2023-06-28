import openai 

openai.api_key = "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"

#get chapters
chapters = {'chapters': ['The Introverted Visionary', 'The Ascent Begins', 'The Cognitive Leap', "The Spotlight's Glare", 'The Ethical Quandary', 'The Rise of the Tech Titan', 'The Invisible Enemy', 'The Global Impact', 'The Crossroads', 'The Uncharted Frontier']}

#get topics
topics = {"Liam's early life and educational background.": 1, 'The development of his interest in cognitive enhancement.': 1, 'The initial steps towards his revolutionary project.': 1, "The transformation of Liam's apartment into a lab.": 2, 'The beginning of his research and experimentation.': 2, 'The challenges and breakthroughs in his initial work.': 2, 'The process of synthesizing the cognitive enhancement substances.': 3, "Liam's personal experimentation with the substances.": 3, "The immediate and long-term effects of the substances on Liam's cognition.": 3, "The scientific community's reaction to Liam's work.": 4, "The media's portrayal of Liam and his work.": 4, "The emergence of less scrupulous individuals interested in Liam's work.": 4, 'The potential misuse of the cognitive enhancement substances.': 5, "Liam's struggle with the moral implications of his work.": 5, 'The differing viewpoints on cognitive enhancement within society.': 5, "Liam's rapid ascent to billionaire status.": 6, 'The lifestyle changes and challenges that come with wealth and fame.': 6, "The impact of Liam's success on his personal and professional relationships.": 6, "The onset of corporate espionage targeting Liam's work.": 7, 'The legal battles Liam faces due to his work.': 7, "Liam's strategic responses to these challenges.": 7, 'The societal effects of the widespread use of cognitive enhancement substances.': 8, 'The debates surrounding cognitive enhancement within various communities.': 8, 'The regulatory challenges posed by the emergence of cognitive enhancement substances.': 8, 'The critical decisions Liam must make regarding the future of his work.': 9, 'The potential implications of these decisions for the field of cognitive enhancement.': 9, "The personal and professional consequences of Liam's decisions.": 9, "The aftermath of Liam's decisions.": 10, 'The evolving landscape of cognitive enhancement technology.': 10, "Liam's reflections on his journey and his visions for the future.": 10}

#get bullet points 
bullet_points = [['   - Born and raised in the Netherlands, showing early signs of high intelligence and introversion.', '   - His pursuit of a degree in Computer Science, showcasing his analytical and problem-solving skills.', "   - His move to Berlin to further his research and immerse himself in the city's thriving tech scene."], ['   - His fascination with the human brain and its untapped potential.', '   - His exploration of the intersection of neuroscience, biochemistry, and artificial intelligence.', '   - The formulation of his vision for cognitive enhancement technology.'], ['   - His decision to dedicate his life to the development of cognitive enhancement substances.', '   - The transformation of his Berlin apartment into a makeshift lab.', '   - The beginning of his intensive research and experimentation.'], ['   - The setup of his lab, complete with necessary equipment and substances.', '   - His adoption of rigorous safety measures and protocols.', '   - The establishment of a disciplined work schedule, reflecting his driven personality.'], ['   - His deep dive into the intricacies of neuroscience and biochemistry.', '   - The initial trials and errors in his quest to create a cognitive enhancement substance.', '   - His persistence in the face of setbacks, driven by his unwavering belief in his vision.'], ['   - The technical difficulties and complexities he encounters.', '   - His breakthrough in synthesizing Modafinil and LSD derivatives.', '   - His excitement and anticipation at the prospect of testing the substances.'], ['   - The meticulous process of combining Modafinil and LSD derivatives.', '   - The careful monitoring and documentation of the synthesis process.', '   - The successful creation of a potentially revolutionary cognitive enhancement substance.'], ['   - His decision to test the substances on himself, reflecting his fearless and committed nature.', '   - The immediate effects of the substances on his cognitive abilities.', '   - The long-term improvements in his cognition, including enhanced focus, memory, and creativity.'], ['   - The remarkable increase in his cognitive abilities, exceeding his expectations.', '   - The potential implications of these results for the field of cognitive enhancement.', '   - His decision to share his findings with the scientific community.'], ['   - The initial skepticism followed by growing interest from scientists.', '   - The validation of his work through peer reviews and publications.', '   - The increased attention from research institutions and tech companies.'], ["   - The media's fascination with Liam's story, leading to widespread coverage.", '   - The portrayal of Liam as a revolutionary figure in the tech world.', "   - The public's mixed reactions to Liam and his work, ranging from admiration to suspicion."], ["   - The interest from individuals seeking to exploit Liam's work for personal gain.", "   - The attempts to steal Liam's research and substances.", "   - Liam's efforts to protect his work and maintain his integrity."], ['   - The risk of the substances being used for unethical purposes, such as performance enhancement.', '   - The potential for societal inequality resulting from unequal access to the substances.', '   - The debates about the ethical implications of cognitive enhancement.'], ['   - His realization of the potential negative consequences of his work.', '   - His internal conflict between his vision and the potential misuse of his substances.', '   - His decision to take responsibility for the ethical implications of his work.'], ["   - The public's fascination and fear of cognitive enhancement technology.", '   - The debates about the ethical, social, and legal implications of cognitive enhancement.', '   - The polarization of society into supporters and detractors of cognitive enhancement.'], ['   - The commercialization of his cognitive enhancement substances, leading to immense wealth.', '   - His transition from a scientist to a tech titan, complete with the trappings of wealth and fame.', '   - The changes in his lifestyle and relationships due to his newfound status.'], ['   - The luxuries and privileges that come with his wealth.', '   - The challenges of maintaining privacy and dealing with public scrutiny.', '   - The strain on his relationships due to his fame and wealth.'], ['   - The changes in his relationships with friends and family.', '   - The emergence of new relationships, both genuine and opportunistic.', '   - His struggle to maintain his authenticity and integrity amidst his success.'], ['   - The attempts by competitors to steal his research and substances.', '   - The infiltration of his company and lab by corporate spies.', '   - His efforts to protect his work and company from these threats.'], ['   - The lawsuits and regulatory challenges he faces.', '   - His struggle to navigate the complex legal landscape of cognitive enhancement.', '   - His determination to defend his work and vision in the face of these challenges.'], ['   - His use of his analytical and strategic skills to tackle these challenges.', '   - His efforts to strengthen the security and legal protection of his work.', '   - His resilience in the face of adversity, demonstrating his commitment to his vision.'], ['   - The impact on productivity and creativity in various sectors.', '   - The debates about the societal implications of cognitive enhancement.', '   - The regulatory challenges posed by the widespread use of these substances.'], ['   - The differing views among scientists, ethicists, and the public.', '   - The discussions about the ethical, social, and legal implications of cognitive enhancement.', '   - The polarization of society into proponents and critics of cognitive enhancement.'], ['   - The lack of existing regulations for cognitive enhancement substances.', '   - The efforts by governments and regulatory bodies to establish regulations.', "   - Liam's involvement in these discussions, reflecting his commitment to ethical cognitive enhancement."], ['   - The choice between commercial success and ethical responsibility.', '   - The decision about the future direction of his company.', '   - The personal and professional implications of these decisions.'], ['   - The impact on the development and use of cognitive enhancement substances.', '   - The potential for setting precedents in the field of cognitive enhancement.', '   - The anticipation and uncertainty about the future of cognitive enhancement.'], ['   - The impact on his reputation and status in the tech world.', '   - The changes in his relationships and lifestyle due to his decisions.', '   - His reflections on his journey and the lessons he has learned.'], ['   - The consequences of his decisions for his company and the field of cognitive enhancement.', "   - The public's reactions to his decisions.", '   - His efforts to navigate the new landscape of cognitive enhancement.'], ['   - The ongoing research and development in the field of cognitive enhancement.', '   - The emergence of new players and technologies in the field.', '   - The anticipation and uncertainty about the future of cognitive enhancement.'], ['   - His reflections on his successes, failures, and lessons learned.', '   - His visions for the future of cognitive enhancement.', '   - His determination to continue contributing to the field of cognitive enhancement.']]
def generate():
    """
    - system prompt
    - user: write the outline of an book
    - assitant: outline 
    - user: elaboration prompt
    """
    messages = [
            {
                "role": "system",
                "content": "you are a pro book author with the task of writing a book."
            },
            {
                "role":"user",
                "content": "write the outline of an book."
            },
            #todo add self.outline here (but the bullet point format)
            {
                "role":"assistant",
                "content": """Chapter 1: "The Introverted Visionary"
                            1. Liam's early life and educational background.
                            - Born and raised in the Netherlands, showing early signs of high intelligence and introversion.
                            - His pursuit of a degree in Computer Science, showcasing his analytical and problem-solving skills.
                            - His move to Berlin to further his research and immerse himself in the city's thriving tech scene.

                            2. The development of his interest in cognitive enhancement.
                            - His fascination with the human brain and its untapped potential.
                            - His exploration of the intersection of neuroscience, biochemistry, and artificial intelligence.
                            - The formulation of his vision for cognitive enhancement technology.

                            3. The initial steps towards his revolutionary project.
                            - His decision to dedicate his life to the development of cognitive enhancement substances.
                            - The transformation of his Berlin apartment into a makeshift lab.
                            - The beginning of his intensive research and experimentation.

                            Chapter 2: "The Ascent Begins"
                            1. The transformation of Liam's apartment into a lab.
                            - The setup of his lab, complete with necessary equipment and substances.
                            - His adoption of rigorous safety measures and protocols.
                            - The establishment of a disciplined work schedule, reflecting his driven personality.

                            2. The beginning of his research and experimentation.
                            - His deep dive into the intricacies of neuroscience and biochemistry.
                            - The initial trials and errors in his quest to create a cognitive enhancement substance.
                            - His persistence in the face of setbacks, driven by his unwavering belief in his vision.

                            3. The challenges and breakthroughs in his initial work.
                            - The technical difficulties and complexities he encounters.
                            - His breakthrough in synthesizing Modafinil and LSD derivatives.
                            - His excitement and anticipation at the prospect of testing the substances.

                            Chapter 3: "The Cognitive Leap"
                            1. The process of synthesizing the cognitive enhancement substances.
                            - The meticulous process of combining Modafinil and LSD derivatives.
                            - The careful monitoring and documentation of the synthesis process.
                            - The successful creation of a potentially revolutionary cognitive enhancement substance.

                            2. Liam's personal experimentation with the substances.
                            - His decision to test the substances on himself, reflecting his fearless and committed nature.
                            - The immediate effects of the substances on his cognitive abilities.
                            - The long-term improvements in his cognition, including enhanced focus, memory, and creativity.

                            3. The immediate and long-term effects of the substances on Liam's cognition.
                            - The remarkable increase in his cognitive abilities, exceeding his expectations.
                            - The potential implications of these results for the field of cognitive enhancement.
                            - His decision to share his findings with the scientific community.

                            Chapter 4: "The Spotlight's Glare"
                            1. The scientific community's reaction to Liam's work.
                            - The initial skepticism followed by growing interest from scientists.
                            - The validation of his work through peer reviews and publications.
                            - The increased attention from research institutions and tech companies.

                            2. The media's portrayal of Liam and his work.
                            - The media's fascination with Liam's story, leading to widespread coverage.
                            - The portrayal of Liam as a revolutionary figure in the tech world.
                            - The public's mixed reactions to Liam and his work, ranging from admiration to suspicion.

                            3. The emergence of less scrupulous individuals interested in Liam's work.
                            - The interest from individuals seeking to exploit Liam's work for personal gain.
                            - The attempts to steal Liam's research and substances.
                            - Liam's efforts to protect his work and maintain his integrity.

                            Chapter 5: "The Ethical Quandary"
                            1. The potential misuse of the cognitive enhancement substances.
                            - The risk of the substances being used for unethical purposes, such as performance enhancement.
                            - The potential for societal inequality resulting from unequal access to the substances.
                            - The debates about the ethical implications of cognitive enhancement.

                            2. Liam's struggle with the moral implications of his work.
                            - His realization of the potential negative consequences of his work.
                            - His internal conflict between his vision and the potential misuse of his substances.
                            - His decision to take responsibility for the ethical implications of his work.

                            3. The differing viewpoints on cognitive enhancement within society.
                            - The public's fascination and fear of cognitive enhancement technology.
                            - The debates about the ethical, social, and legal implications of cognitive enhancement.
                            - The polarization of society into supporters and detractors of cognitive enhancement.

                            Chapter 6: "The Rise of the Tech Titan"
                            1. Liam's rapid ascent to billionaire status.
                            - The commercialization of his cognitive enhancement substances, leading to immense wealth.
                            - His transition from a scientist to a tech titan, complete with the trappings of wealth and fame.
                            - The changes in his lifestyle and relationships due to his newfound status.

                            2. The lifestyle changes and challenges that come with wealth and fame.
                            - The luxuries and privileges that come with his wealth.
                            - The challenges of maintaining privacy and dealing with public scrutiny.
                            - The strain on his relationships due to his fame and wealth.

                            3. The impact of Liam's success on his personal and professional relationships.
                            - The changes in his relationships with friends and family.
                            - The emergence of new relationships, both genuine and opportunistic.
                            - His struggle to maintain his authenticity and integrity amidst his success.

                            Chapter 7: "The Invisible Enemy"
                            1. The onset of corporate espionage targeting Liam's work.
                            - The attempts by competitors to steal his research and substances.
                            - The infiltration of his company and lab by corporate spies.
                            - His efforts to protect his work and company from these threats.

                            2. The legal battles Liam faces due to his work.
                            - The lawsuits and regulatory challenges he faces.
                            - His struggle to navigate the complex legal landscape of cognitive enhancement.
                            - His determination to defend his work and vision in the face of these challenges.

                            3. Liam's strategic responses to these challenges.
                            - His use of his analytical and strategic skills to tackle these challenges.
                            - His efforts to strengthen the security and legal protection of his work.
                            - His resilience in the face of adversity, demonstrating his commitment to his vision.

                            Chapter 8: "The Global Impact"
                            1. The societal effects of the widespread use of cognitive enhancement substances.
                            - The impact on productivity and creativity in various sectors.
                            - The debates about the societal implications of cognitive enhancement.
                            - The regulatory challenges posed by the widespread use of these substances.

                            2. The debates surrounding cognitive enhancement within various communities.
                            - The differing views among scientists, ethicists, and the public.
                            - The discussions about the ethical, social, and legal implications of cognitive enhancement.
                            - The polarization of society into proponents and critics of cognitive enhancement.

                            3. The regulatory challenges posed by the emergence of cognitive enhancement substances.
                            - The lack of existing regulations for cognitive enhancement substances.
                            - The efforts by governments and regulatory bodies to establish regulations.
                            - Liam's involvement in these discussions, reflecting his commitment to ethical cognitive enhancement.

                            Chapter 9: "The Crossroads"
                            1. The critical decisions Liam must make regarding the future of his work.
                            - The choice between commercial success and ethical responsibility.
                            - The decision about the future direction of his company.
                            - The personal and professional implications of these decisions.

                            2. The potential implications of these decisions for the field of cognitive enhancement.
                            - The impact on the development and use of cognitive enhancement substances.
                            - The potential for setting precedents in the field of cognitive enhancement.
                            - The anticipation and uncertainty about the future of cognitive enhancement.

                            3. The personal and professional consequences of Liam's decisions.
                            - The impact on his reputation and status in the tech world.
                            - The changes in his relationships and lifestyle due to his decisions.
                            - His reflections on his journey and the lessons he has learned.

                            Chapter 10: "The Uncharted Frontier"
                            1. The aftermath of Liam's decisions.
                            - The consequences of his decisions for his company and the field of cognitive enhancement.
                            - The public's reactions to his decisions.
                            - His efforts to navigate the new landscape of cognitive enhancement.

                            2. The evolving landscape of cognitive enhancement technology.
                            - The ongoing research and development in the field of cognitive enhancement.
                            - The emergence of new players and technologies in the field.
                            - The anticipation and uncertainty about the future of cognitive enhancement.

                            3. Liam's reflections on his journey and his visions for the future.
                            - His reflections on his successes, failures, and lessons learned.
                            - His visions for the future of cognitive enhancement.
                            - His determination to continue contributing to the field of cognitive enhancement.
                            """
            }
        ]
    chapter = chapters['chapters'][0]
    topic = list(topics.keys())[0]
    bullets = bullet_points[0]
    """
    7. start now with elaborating on [name of chapter] with the topic [name of topic] and his bullet points:

    [all bullet points of the topic]
    """
    formatted_bullets = '\n'.join([f'{bullet.strip()}' for bullet in bullets])
    message = f"""Start now with elaborating on chapter '{chapter}' with the topic '{topic}' and his bullet points:
    {formatted_bullets}
    """
    #add message to messages
    messages.append({"role": "user", "content": message})
    init_book = openai.ChatCompletion.create(model="gpt-4-0613", messages=messages, temperature = 1.0).choices[0].message["content"]
    #write init_book content to an file
    with open('book_content.txt', 'w') as file:
        file.write(init_book)

    #self.messages.append({"role": "user", "content": "create detailed bullet points for each of the topics. don't abbreviate anything. provide the bullet points for each topics!"})

generate()