'''
    COP2002.0M1 - Files and Functions
    Zachary Zahradka
    04/18/2023

    Specifications:
    
    1) Get all the class codes from input.csv
    2) Collect the program codes from each of the students in studentRosterExample.csv
    3) Match these program codes to their matching courses
    4) Load these matching courses into a new file
'''

def getDefaultValues(file):
    courses = [] #Each line of the file will be added to this list

    with open(file, 'r') as file_object:
        
        for line in file_object:
            courses.append(line)

    return courses


def getStudentValues(file):
    codes = [] #Each line of the file will be added to this list

    with open(file, 'r') as file_object:
        print("Processing student input file...\n")        
        for line in file_object:
            x = line.split(',')
            codes.append(x[5])

    codes.pop(0)
    for y in codes:
        print(f'*{y}*')

    return codes


def makeOutput(file): #Will write to output.csv
    courses = getDefaultValues('files/courses.csv')
    codes = getStudentValues('files/studentRosterExample.csv')
    courseNames = []
    '''
        Take the code from the file
        Search through list of courses for matching code (index 0)
        Return name of class (index 1)
    '''
    print("\nWriting to file...\n")
    for code in codes:
        for course in courses:
            course = course.split(',')
            if(code == course[0]):
                course[1].replace('\n','')
                courseNames.append(course[1])
                print(f'    {course[1]}')

    with open(file, 'w') as file_object:
        for x in courseNames:
            file_object.write(f'{x}')

    print('\nProgram finished.')


def main():
    makeOutput('files/output.csv')

main()