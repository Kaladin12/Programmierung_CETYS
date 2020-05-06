class Folder:
    #Birth format:  '01/01/1994' and we can work with it just by splitting the /
    def __init__(self, name=''):
        self.name = name
        #self.rootFolder = rootFolder
        #self.date = date
        #self.description = description
    
    def getJSONforFolder(self):

        data = {
            "name": self.name,
            "notes": []
        }
        return data


class Note(Folder):
    def __init__(self, folderName, noteName, date, description):
        super().__init__(folderName)
        self.name=noteName
        self.date=date
        self.description= description


    def getJSONforNote(self):
        #Converts all class instance properties into a dict and returns it
        data = {
            "name": self.name,
            "date": self.date,
            "description": self.description
        }
        
        return data