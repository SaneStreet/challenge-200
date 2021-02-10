"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge201.py'
"""
# function that takes a string
def Maskify(string):
    # get the unmasked string
    unmasked = string
    # get the length of the string without the last 4
    # then  replace them with #, and add the last 4 back on
    masked = len(unmasked[:-4]) * "#" + unmasked[-4:]
    # prrint the masked string
    print(masked)

# function calls with string as argument
Maskify("4512987512105562")
Maskify("64607935616")
Maskify("1")
Maskify("")