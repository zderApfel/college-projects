# 1. Get input from user asking what they need help with


# 2. After that, loop through a list of technicians


# 3. Assign it to one of the technicians


# 4. If no keyword detected, route to next available technician

FALLBACK="next available technician"
KEYWORDS=["urgent","linux","windows","mac","office","zoom","password","locked out"]
TECHNICIANS=["Pry Ority","Pebble Penguin","Kurt Ains","Don Alds","Dusty Places","Don Alds","Pebble Penguin", "Pebble Penguin"]

query=input("Enter the text for the ticket: ")

def findKeyWord(input):
    for word in KEYWORDS:
        if word in input.lower(): 
            i = KEYWORDS.index(word) #Iteration through parallel tuples
            print(f"Keyword detected: {KEYWORDS[i]}")
            
            return TECHNICIANS[i]
    
    print(f"Keyword detected: None")
    
    return FALLBACK

print(f"Route to: {findKeyWord(query)}")
