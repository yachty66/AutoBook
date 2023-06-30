# mbti_books

- [x] remove unappropriate headlines
- [x] remove "--"
- [x] remove the **content** below an 
- [x] check what else is wrong / missing
- [x] write automation script which is automating this
    - write book parameters for intj -
    - write get chapters method where i read the book parameters and make a request - 
    - see / compare the quality of the output with my chatgpt output - 
    - create topics for each of the chapters (method for that) - 
    - compare with chatgpt - 
    - try if 32k model available for agi house - 
    - create method which is generating the content - 
    - add logs to script - 
    - run every request with 0.0 temp - 
    - make ten runs and save the result of each of the ten runs to see how all the possible outcomes look like - 
    - save all chapters in a dictionary --> create method dictionary -
    - save all topics in the dictionary - 
    - integrate bullet point parser and test it in application - 
    - generate method for initial book generation --> start now with elaborating on [name of chapter] with the topic [name of topic] and his bullet points: [all bullet points of the topic]
        -  add same prompts to message like prompt one in chatgpt 
    - write content directly to an file -
    - add generate init book method to book.py -
    - fix current error from init book -
        - find out why chapters are empty -
    - fix also why topics are empty - 
    - make sure that accessing for prompt in book generation everything is alrigh still -
    - create method for continuation of book generation --> write continuation to next file
- [ ] new block
    - find out why so many chapters are printed and fix that - 
    - fix the error which occured -
    - find out why i am still getting the mad error of multiple chapters -
    - fix problem that i sometimes dont get all chapters - 
    - make test file where i make continuaton working, i.e. write a whole book via continuation - 
    - implement continue book function -
    - start with cleanup book function -
        - remove all duplicate chapters and write result back to file - 
        - remove all lines which introduce a topic and write result back to file - 
    - clean code and add print statements everywhere to understand every step which is happening - 
    - fix error of parsing topics -
    - create my first book -
    - read book to get impression of quality of book - 
    - cleanup my files a bit - 
    - add functionality that chapter gets added at the beginning of the lines only if the current chapter was not already added -
    - check if my process function also works with continuation function -
    - add new line if new chapter thing gets added -
    - create title of book method - 
    - create folder with name == title -  
    - generate midjourney image and put it inside folder --> not so important actually, can i add later... - add support for matching the pattern of a topic like "*Exploration of Liam's fascination with cognitive enhancement*" -
    - find out why there is no space after the chapter name... and correct - 
    - find out why there is an error - 
    - generate an book cover for the intj book -
    - try to upload the book to amazon -
    - create metadata file -
    - create book for elona musk - 
    - create beef bezos ...  -
    - create a book for all the mbti types which are left -
    - deal with **Topic 3: The Humorous and Heartwarming Conclusion to Elona's Journey** and **Chapter: The Sweet Smell of Success** and **Topic: The transformation in Elona's approach towards her business** and *Topic: The unexpected claim of copyrights on scents by aliens*
    - fix errror that topics were not parsed correctly 




- [ ] create book title
- [ ] create book cover
- [ ] ask chatgpt what else is missing for a book (like author and chapter part)
- [ ] upload to amazon
- [ ] share with daan 
- [ ] automating the process with algo




--> adding consistence images and remove 

## parameters for creating a book 

1. **Number of Pages**: As you mentioned, this parameter specifies the desired length of the book.

2. **Description/Theme**: A brief description or theme for guiding the content of the book.

3. **Genre**: Specify the genre (e.g., science fiction, fantasy, romance, mystery) to guide the tone and style.

4. **Main Characters**: Allow the user to specify the main characters, their traits, and relationships.

5. **Setting**: Parameters for the setting of the story, such as time period, location, culture, etc.

6. **Plot Points**: Optionally allow the user to provide key plot points or events they want to be included.

7. **Writing Style**: Parameters for controlling the writing style - e.g., formal, casual, poetic, etc.

8. **Point of View**: Allow specification of the point of view (e.g., first person, third person).

9. **Chapter Titles or Themes**: Optionally allow the user to specify titles or themes for each chapter.

10. **Dialogue Ratio**: Control the ratio of dialogue to narration/description in the book.

11. **Conflict Level**: A parameter to control the intensity and frequency of conflicts in the story.

12. **World-building Depth**: For genres like fantasy or sci-fi, a parameter to control the level of world-building details.

13. **Target Audience**: Specify the target audience (e.g., young adults, adults) to tailor the language and content accordingly.

14. **Keywords Density**: Allow the user to specify certain keywords that should be frequently used or themes that should be emphasized throughout the book.

15. **Image Placement Guidelines**: If the book includes images, allow the user to specify guidelines on where and how images should be placed.

16. **Language/Localization**: Specify the language in which the book should be written.

17. **Max Tokens per Request**: Since language models often have a limit on the number of tokens per request, this parameter can be used to chunk the content appropriately.

18. **Feedback Loop**: Option for user feedback integration; user can provide feedback after each chapter, which gets incorporated in the subsequent chapters.






how can i automate the process of creating the book?

best case i directly prompt gpt 4 in a way so that it is making some kind of placeholder at the places where a image should be 

250 pages is solid. 

combination of midjourney and gpt4. 

INTJ
INTP
ENTJ
ENTP


- [ ] structure
    - generate story line
    - generate chapers
    - 

- [ ] outreach
    - generate a beef bezos book where a guy called beff bezos is selling beef and is becoming billionaire with that
    - make one for elona musk which was selling high tech parfum
    - reddit 
    - goodreads
    - youtube video on ai hacker

