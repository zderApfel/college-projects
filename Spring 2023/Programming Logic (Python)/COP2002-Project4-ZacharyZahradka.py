"""
    COP2002.0M1 - Project 4
    Zachary Zahradka - 02/21/2023

    1. Program generates a random string of six digits
        - Generate a six-digit number and then convert it into a string
    2. Ask the user to input the correct number, to simulate a 2-Factor Authentication App
    3. User should get three attempts at putting it in, after the third attempt, the number should change again. 
    4. User should be able to terminate the app as well

    Testing:
    1) Incorrect Answer
    2) Correct Answer
    3) Quit
    4) Too many Incorrect Answers
"""
import random

def generateToken():
    token=random.randint(111111,999999)  #Generates a pseudo-random number for the token.
    return str(token)

def validate():
    OTP=generateToken()
    END=False
    attempts=1
    print(f"Your OTP is: {OTP}")
    i=input("Enter your OTP: ")
    while(END==False):
        if(i==OTP):
            print("Access Granted!")
            END=True
        elif(i.lower()=="quit"):
            print("Program Terminated")
            END=True
        elif(attempts>=3 and i!=OTP):
            print("Incorrect OTP entered 3 times. Generating a new OTP...")
            OTP=generateToken()
            print(f"Your OTP is: {OTP}")
            i=input("Enter your OTP: ")
        else:
            i=input("Incorrect OTP. Enter your OTP: ")
        attempts+=1
       
def main():
    validate()

main()
