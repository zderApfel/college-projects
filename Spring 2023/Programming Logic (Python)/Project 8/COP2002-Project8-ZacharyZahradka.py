'''
    Zachary Zahradka
    COP2002.0M1
    04/29/2023
    Project 8: Testing your Code

    Scenario: Another programmer is writing a class to convert binary values to decimal values and your 
    supervisor has tasked you with automating the testing for this project.

    Specifications:
    1) Create four test cases, where you test four different
    first-position octets of IP addresses.
    2) You will be creating four test cases in a .csv,
    one that fails, and three that pass.

    A reminder of octet classes: 
        A: 0-126
        B: 128-191 
        C: 192-223
'''

import unittest



class TestCases: #Creates test cases and returns their classes that will be tested
    def __init__(self, filepath): 
        self.filepath = filepath

        self.octetClass = '' #This value is NOT used for testing verification and only for printing to the console
        self.value = 0
        self.cases = []

        with open(self.filepath,'r') as file_object:
            for line in file_object:
                self.value = int(line)

                if self.value >= 0 and self.value <=126:
                    self.octetClass = 'Class A'

                elif self.value >= 128 and self.value <=191:
                    self.octetClass = 'Class B'

                elif self.value >= 192 and self.value <=223:
                    self.octetClass = 'Class C'
                
                else:
                    self.octetClass = 'Failure'
                self.cases.append([self.octetClass, self.value])
        
        for x in self.cases:
            print('This is the setup method for creating an object for before each test case.')
            print(f'{x[0]}: {x[1]}')
            if x[0] == 'Failure':
                print('F')
            else:
                print('.')

class Test(unittest.TestCase):
    def __init__(self):
        self.testCases = TestCases('files/test.csv').cases
        self.valid = []

        i = 0
        while i <= 223:
            self.valid.append(i)
            i+=1

    def runTest(self):
        i = 0
        for case in self.testCases:
            self.assertIn(case[1] ,self.valid)
    def showStuff(self):
        print(self.testCases)



def main():
    x = Test()
    x.runTest()
main()

