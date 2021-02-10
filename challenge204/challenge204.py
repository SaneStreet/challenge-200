"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge201.py'
"""
# function that takes a string
def Potatoes(text):
    # assigns the number of potatoes in a string
    potatoes = text.count('potato')
    # print the amount
    print(potatoes)

# function calls with string argument
Potatoes("potato")
Potatoes("potatopotato")
Potatoes("potatoapple")
Potatoes("potatoapplepotatobananapotato")