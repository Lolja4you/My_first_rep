import json


class JSON_SOURCE:
    def __init__(self, nameTableModel):
        data = {}
        self.data = data
        self.nameTableModel = nameTableModel
        data['table_model'] = []
        data['table_model'].append({
            'name': self.nameTableModel,
        })
        
        def writeJson(self):
            with open('data.json', 'w') as outfile:
                json.dump(self.data, outfile)
            
            return print("write success!\n")
        
        return writeJson(self)
