#Name:Tawonga Taibu
#Task Number:11
#Task Name:Natural Language Processing
# ------------------------- spaCy -------------------------------------
# spaCy is a Python natural language processing library specifically designed with
# the goal of being a useful library for implementing production-ready systems.
# It is particularly fast and intuitive, making it a top contender for NLP tasks.

# ------------------------- IMPORTANT -------------------------------------
#	Please make sure you have read and understand the instructions for this task.
#	We will be working with spaCy which is an EXTERNAL Python module. SpaCy, as
#	well as its English language model, should have been installed at the start of 
#   your bootcamp. If you have any problems, contact a mentor for support. 
#   SpaCy MUST BE INSTALLED BEFORE YOU CAN COMPLETE THIS TASK. 

# ************************** INSTALLATION **************************************
# Below are the commands that are needed to install spaCy, FYI. You should not
# need to do this as it should have been done for you by a script HyperionDev
# runs at the start of your bootcamp, but has been retained here FOR YOUR INTEREST.
 
# Type the following commands in command line
# pip3 install spacy
# python3 -m spacy download en_core_web_sm  
# ----------------OR----------------------
# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

#Load the small English model
nlp = spacy.load("en_core_web_sm")

#Define the garden path sentences
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Missisippi.",
    "The old man the boats.",  
    "The horse raced past the barn fell." 
]

# Process each sentence with spaCy
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nSentence: {sentence}")
    
    #Tokenization
    #Tokenization is a foundational step in many NLP tasks. Tokenising text
    #is the process of splitting a text into two words,symbols,punctuation,
    #spaces and other elements, thereby creating 'tokens'.
    print("Tokens:", [token.text for token in doc])

    #Named Entity Recognition
    #This is a process of classifying named entities found in a text into
    #predefined categories, such as persons,places, organisations and dates
    #etc.
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])

    # Print explanation for unknown entity labels
    for ent in doc.ents:
        print(f"{ent.text}: {spacy.explain(ent.label_)}")

# Example comments about entities
# Comment 1:
# Entity: Mississippi was labelled as GPE (Countries, cities, states)
# Explanation: This makes sense since Mississippi is a state in the USA.

# Comment 2:
# Entity: Mary was labelled as PERSON (People, including fictional)
# Explanation: This is should be correct because Mary is usually a female name for a person worldwide.

#References
#https://www.apartmenttherapy.com/garden-sentences-262915

#Acknowledgements
#http://www.inf.ed.ac.uk/teaching/courses/inf2a/