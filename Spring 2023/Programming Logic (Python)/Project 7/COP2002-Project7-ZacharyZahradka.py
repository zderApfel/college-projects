'''
    Zachary Zahradka
    COP2002.0M1
    04/28/2023
    Project 7: Files and Classes
'''
class JSONObject:
    def __init__(self,keys,values,file):
        self.keys = keys
        self.values = values
        self.objects = []
        self.file = file

    def writeToJSON(self):
        for value in self.values:
            i = 0
            newObj = {}
            while i < len(self.keys):
                newObj[self.keys[i]] = value[i]
                i+=1
            self.objects.append(newObj)
        self.makeParsable()

        with open(self.file, 'w') as file_object:
            file_object.write('{\n\t')
            i = 0
            while i < len(self.objects):
                o = self.objects[i]
                file_object.write('"'+str(i+1)+'": {\n')
                i+=1
                if i == len(self.objects):
                    file_object.write('\t\t'+o+'\n\t}'+'\n')
                    file_object.write('}')
                else:
                    file_object.write('\t\t'+o+'\n\t},'+'\n\t')
                

    def makeParsable(self):
        new = []
        for o in self.objects:
            o = str(o)
            o = o.replace('{','')
            o = o.replace('}','')
            o = o.replace("'",'"')
            o = o.replace(", ",',\n\t\t')
            print(o)
            new.append(o)
        self.objects = new


                    



class TakeCSV:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keys = []
        self.values = []
        self.getData()

    def getData(self):
        with open(self.filepath, 'r') as file_object:     
            for line in file_object:
                line = line.replace('\n',"")
                x = line.split(',')
                self.values.append(x)
        self.keys = self.values[0]
        self.values.pop(0)


    

def main():
    x = TakeCSV('files/input.csv')
    JSONObject(x.keys,x.values,'files/output.json').writeToJSON()

main()