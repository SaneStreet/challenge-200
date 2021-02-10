#c1 = 108
#c2 = 111
#chars = [72, 101, 108, 108, 111]
#newChars = []
#print(max(c1 - c2, c2 - c1))

#for index, item in enumerate(chars):
#    print('numbers', index, '=', item)

#for element in chars:
    #number = ord(element)
    #print(number)

    #newChars.append(number)
    #print(newChars)
#print(newChars)
# initialising _list 
#chars = ["H", "e", "l", "l", "o"] 
chars = [72, 101, 108, 108, 111]
# printing iniial_list 
print("Character Codes:", chars) 
  
# Calculating difference list 
newChars = []
if chars[0]:
        number = chars[0]
        newChars.append(number)
for x, y in zip(chars[0::], chars[1::]): 
    #numbers = chr(y)
    newChars.append(y-x) 
      
# printing difference list 
print ("Differences: ", newChars) 