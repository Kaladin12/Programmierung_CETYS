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
