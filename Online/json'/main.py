import json
'''
mijson='{ "nombre":"Elian", "edad":18 }'
file=json.loads(mijson)
print(file)
mijson={ "nombre":"Elian", "edad":18 }

js=json.dumps(mijson)'''

try:
    file=open('ex.json','r')
    data=json.load(file)
finally:
    file.close()

print(data)