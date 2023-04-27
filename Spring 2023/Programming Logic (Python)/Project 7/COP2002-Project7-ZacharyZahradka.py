'''
    Zachary Zahradka
    COP2002.0M1
    04/25/2023
    Project 7: Files and Classes
'''
class JSONObject:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class TakeCSV:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keys = []
        self.values = []
        self.objects = []

    def getData(self):
        with open(self.filepath, 'r') as file_object:     
            for line in file_object:
                line = line.replace('\n',"")
                x = line.split(',')
                self.values.append(x)
        self.keys = self.values[0]
        self.values.pop(0)

    def makeItems(self):
        self.getData()
        i = 0
        while i < len(self.keys):
            item = JSONObject(self.keys[i],self.values[i])
            self.objects.append(item)
            i+=1

    def showObjects(self):
        self.getData()
        self.makeItems()
        print(self.objects)

TakeCSV('files/input.csv').showObjects()