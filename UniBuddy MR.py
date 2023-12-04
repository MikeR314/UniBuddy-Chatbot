# UniBuddy task brief:

'''
[Case Study Story] --> Imagine the first day of university for a freshman named Alex. 
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
'''

# Initialise Conversation
print("Hi, my name is UniBuddy, your personalised chatbot! Let's get started...")

# Ask for name and return a personalised greeting, use capitalize to put an upper case letter, even if the user doesn't
name = input("\nPlease enter your name : ").capitalize()
print(f"\nHi {name}, welcome to university! I'm going to ask a few questions to get to know you better and give you some tips on university life")

# Ask for age, cast to integer and give an output based on this
# Use try-except to produce an error message if not a number, and a while loop to keep looping until a number is added
while True :
    try :
        age = int(input("\nPlease enter your age : "))

        if age < 18 :
            print("\nWow, you're young! You should probably stay away from the bars for now!")
        elif age < 22 :
            print("\nThere are loads of freshman events going on where you can meet likeminded new students like yourself, mostly aged 18-21")
        else :
            print("\nAh, a mature student! If you need any help juggling study with personal life, please speak to our support team")
        break
    except ValueError :
        print("\nThat is not a valid age, please try again")

# Ask favourite colour and change to lower case
colour = input("\nPlease enter your favourite colour : ").lower()

# First output if colour is green
if colour == "green" :
    print("\nExcellent! Me too! Green is our main university colour, seen on all our logos and sports kits - you'll fit right in here!")
# Output for all other colours
else :
    print(f"\nOh that's cool, I'm biased but I prefer green to {colour}, as you'll see on all our university logos and sports kits")
    # Output specifically just for blue
    if colour == "blue" :
        print("Although as you like blue, you might like the university's Blue Art Club, who meet on Tuesday nights")
        
# Ask about study
course = input(f"\nSo {name}, tell me what course you're studying : ").lower()
# Print answer for science subjects
if course in ["maths", "physics", "chemistry", "biology"] :
    print("\nScience subjects are hard, but there is help available in the science working group if you need")
# Print answer for arts subjects
elif course in ["art", "literature", "music", "drama"] :
    print("\nThe arts are great. Have you checked out our university museum and arts centre yet? You'd love it!")
# Print answer for computing
elif course == "computing" :
    print("\nGreat! I love computing, probably because I'm a computer myself...")
# Print answer for humanities
elif course in ["history", "geography", "law", "english", "economics", "psychology"] :
    print(f"\nThere's lots of writing in {course}. If you need any more pens or paper, we have a stationery shop on campus")
# Print answer if not included in any of the above
else :
    print(f"\nI don't have any specific resources for that, but good luck with {course}")

# Closing statement
print(f"\nThanks for telling me about yourself {name}. I really hope you'll love it here, studying {course}.")

# Ask for questions (use lower.() to keep everything lower case)
question = input("\nBefore I go, do you have any other questions for me? If not, type 'goodbye' and I'll let you get on with your day : ").lower()

# Define some expected question key words to use when answering questions
key_words = ["accommodation", "clubs", "library", "fees", "course", "mentor", "lecture"]

# Provide information on these key topics, definied above
answers = [
    "The university provides a wide range of accommodation on or off campus, speak to the accommodation team for all the info and availabilty",
    "There are loads of clubs and societies that you can get involved with. Pop along to the freshers fair in the first week to sign up",
    "The library can be found at the bottom of the hill, and is open from 8am to 10pm every day. There is more info on the noticeboard outside the building",
    "For info about fees, please speak to the fees office, which can be found on campus next to the library",
    "For specific information about your course, talk to your course supervisor",
    "We have a mentoring scheme at this university. If you want to be involved as either a mentor or mentee, please see the mentoring page on our website",
    "For any specific questions about lectures, please talk to the lecturer on that subject"
    ]

# Find how many iterations we will need to check through as a for loop
number_of_questions = len(key_words)

# Firstly use while loop for whether we need to answer a question, or say goodbye
while question != "goodbye" :
    
    # Start a counter so we can tell when we have cycled through all the possible questions
    count = 0
    for i in range(0,number_of_questions) :
        
        # If the key word is included somewhere in the question, print the output for that key word
        if key_words[i] in question :
            print(answers[i])
        # If not, increase the counter and retry with the next key word
        else :
            count += 1
        
    # Once all words are checked, if nothing has been answered, count will be equal to number_of_questions
    if count == number_of_questions :
        print("\nI'm sorry, I don't understand that question")
            
    # Re-ask the question before looping back in the while loop
    question = input("\nDo you have any further questions? If not please type 'goodbye' : ").lower()
    
else :
    # They've said goodbye, so end the chat
    print(f"\nOk, nice to chat with you {name}. See you again soon!")