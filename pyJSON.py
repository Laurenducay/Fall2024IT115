#Import syntax for storing and exchaning data. JSON is ritten with javascript object notation
import json

#Data name up of key value pairs where left is key right is value 
data1 = {

    'name': 'Lauren Ducay',
    'age':21,
    'city': 'Seattle, WA',
    'interests': ['Art', 'music','traveling','pokemon','games'],
    'is_student': True

}


#Creating a Json and writing the python obeject contents to the JSON
with open('data1.json', 'w') as json_file:
    #dumping the data into the JSON file created
    json.dump(data1, json_file,indent=4)
#Confirmss that the data has been written
print("You have successfully written to data1.json")

#Creating a Json and reading the python object contents to the JSON
with open ('data1.json','r') as json_file:
    #accessing the class library and loading the JSON file
    loaded_data = json.load(json_file)
#Confirms that the jsson file is able to be read
print("Successfully able to read data1.json")
print(loaded_data)

    #Add/remove/change items in key value pairs
loaded_data['age'] = 20
loaded_data['interests'].append('Food')
loaded_data['interests'].append('Matcha')

#Creates and rewrites the python object contents to the JSON
with open('data1.json', 'w') as json_file:
    #dumping the data into the JSON file created
    json.dump(loaded_data, json_file,indent=4)
#print line to confirm data has been re-written
print("Your data has been re-written to data.json")