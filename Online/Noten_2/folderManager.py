import json
import os


class folderManager:
    #The actual path of the file we want to manage
    def __init__(self, filePath=''):
        self.filePath = filePath
    
    def getAll(self):
        self.students = []
        try:
            with open(self.filePath, 'r') as file:
                self.students = json.load(file)
            return self.students
        except: return None

    def getAllNotes(self, folderName):
        myStd = self.getAll()
        for folder in myStd:
            if folder["name"]==folderName:
                return folder["notes"]
    
    def addFolder(self, student):
        #Gets the info of the Student  as a dict (we can change the name if it's confusing because it's a dict actually)
        self.data = student
        newData = []
        #dumps the data into JSON file
        try:
            if os.stat(self.filePath).st_size > 0:
                with open(self.filePath, 'r') as f:  #reads actual students on json file
                    newData=json.load(f)
                    newData.append(self.data) #appends new student
            else: newData = [self.data]
            with open(self.filePath, 'w', newline='\n') as f: #overwrites json file with new student, this keeps the json format
                json.dump(newData, f, indent=4)
        except: return 'ERROR' #If nothing gets returned, the process was a success, otherwise return something
    
    