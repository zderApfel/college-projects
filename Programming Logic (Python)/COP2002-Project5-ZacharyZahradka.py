"""
    COP2002.0M1 - Project 5
    Zachary Zahradka - 03/16/2023
"""

# 1. Identify the class (given the IP address, user answers with "A", "B", or "C")

# 2. Provide the default subnet mask: Given an IP address, the user answers with the appropriate default subnet mask

# 3. Exit: The program ends

import random

def generateRandomIP():
    #Interpolated string that makes an IP address of random numbers
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

def whatClass(address):
    end=False #Tells the while loop to stop
    compareTo=address.split(".") #Gave IP its own variable that splits it into an array to make it easier to compare values
    correct="" #The correct answer, for comparison purposes
    choice=input(f"What class (A, B, C, or D) is {address} (q=quit)? ")
    while(end==False):
        if(choice.lower()=="q"):
            end=True
            main()
        elif(int(compareTo[0])>=1 and int(compareTo[0])<=127):
            correct="a"
            if(choice.lower()==correct):
                print("Correct!\n\n")
                #Generates a new IP address after the first one is guessed correctly
                end=True
                compareTo=whatClass(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatClass(generateRandomIP())
        
        elif(int(compareTo[0])>=128 and int(compareTo[0])<=191):
            correct="b"
            if(choice.lower()==correct):
                print("Correct!\n\n")
                end=True
                compareTo=whatClass(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatClass(generateRandomIP())
        
        elif(int(compareTo[0])>=192 and int(compareTo[0])<=223):
            correct="c"
            if(compareTo.lower()==correct):
                print("Correct!\n\n")
                end=True
                compareTo=whatClass(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatClass(generateRandomIP())
        
        #I added class D because I think that was a mistake in the assignment, I'd be left with a range of numbers with no home :(
        elif(int(compareTo[0])>=224 and int(compareTo[0])<=255):
            correct="d"
            if(choice.lower()==correct):
                print("Correct!\n\n")
                end=True
                compareTo=whatClass(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatClass(generateRandomIP())
            
def whatSM(address):
    end=False
    compareTo=address.split(".")
    correct=""
    choice=input(f"What is the default subnet mask for {address} (q=quit)? If it does not have a subnet mask, type 'None'. ")
    while(end==False):
        if(choice.lower()=="q"):
            end=True
            main()
        elif(int(compareTo[0])>=1 and int(compareTo[0])<=127):
            correct="255.0.0.0"
            if(choice==correct):
                print("Correct!\n\n")
                end=True
                compareTo=whatSM(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatSM(generateRandomIP())

        elif(int(compareTo[0])>=128 and int(compareTo[0])<=191):
            correct="255.255.0.0"
            if(choice==correct):
                print("Correct!\n\n")
                end=True
                compareTo=whatSM(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatSM(generateRandomIP())

        elif(int(compareTo[0])>=192 and int(compareTo[0])<=223):
            correct="255.255.255.0"
            if(choice==correct):
                print("Correct!\n\n")
                end=True
                compareTo=whatSM(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatSM(generateRandomIP())

        #Although I did learn while writing this that class D IP addresses do not have subnet masks so I added this as a little trick question >:)
        elif(int(compareTo[0])>=128 and int(compareTo[0])<=191):
            correct="none"
            if(choice.lower(correct)):
                print("Correct!\n\n")
                end=True
                compareTo=whatSM(generateRandomIP())
            else:
                print(f"Incorrect. The correct answer is: {correct}")
                end=True
                compareTo=whatSM(generateRandomIP())


# Starts program and also generates an initial IP address
def main():
    print ("Welcome to the IPv4 Address Practice Program!\n\n")

    print("Main Menu: \n")
    print("1. Identify whether an IP Address is Class A, B, C, or D\n")
    print("2. Identify what the subnet mask is for a given IP address\n")
    print("3. Exit\n\n")

    choice=input("Choice: ")
    address=generateRandomIP()

    if(choice=="1"):
        whatClass(address)
    
    elif(choice=="2"):
        whatSM(address)
    
    elif(choice=="3"):
        print("Thanks for using the program. I hope you feel more comfortable with IP addressing.")
    
    else:
        print("Choice not recognized, quitting program.")

main()