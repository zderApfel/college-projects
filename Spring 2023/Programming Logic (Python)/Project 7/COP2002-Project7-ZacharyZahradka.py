'''
    Zachary Zahradka
    COP2002.0M1
    04/25/2023
    Project 7: Files and Classes
'''
class JSONObject:
    def __init__(self,keys,value):
        self.keys = keys
        self.value = value
        self.item = self.makeItem()

    def makeItem(self):
        i = 0
        newObj = {}
        while i < len(self.keys):
            newObj[self.keys[i]] = self.value[i]
            i+=1
        return newObj


class TakeCSV:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keys = []
        self.values = []
        self.objs = []

    def getData(self):
        with open(self.filepath, 'r') as file_object:     
            for line in file_object:
                line = line.replace('\n',"")
                x = line.split(',')
                self.values.append(x)
        self.keys = self.values[0]
        self.values.pop(0)
        
        for value in self.values:
            x = JSONObject(self.keys,value).item
            self.objs.append(x)
            print(x)

                

    def showObjects(self):
        self.getData()

TakeCSV('files/input.csv').showObjects()