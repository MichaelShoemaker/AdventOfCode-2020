inputs = []
with open(r'input.txt','r') as infile:
          for line in infile:
              inputs.append(line)
          

def isValid(pws):
    #Set the counter to 0 for valid passwords
    valids = 0    
    for line in pws:
        #Seperate the numbers/letter from the passwords
        pieces = line.split(':')
        #Seperate the numbers from the letter
        numLets = pieces[0].split(' ')
        #Get the first number
        bottom = int(numLets[0].split('-')[0])
        #Get the second number
        top = int(numLets[0].split('-')[1])
        #Get the search letter
        letter = numLets[1]
        #Enumerate the password string
        derp = pieces[1].strip()
        pieces[1] = derp
        try:
            for n,c in enumerate(pieces[1]):
                if pieces[1][bottom]==letter and pieces[1][top]==letter:
                    break
                elif pieces[1][bottom]==letter and pieces[1][top]!=letter:
                    valids+=1
                    break
                elif pieces[1][bottom]!=letter and pieces[1][top]==letter:
                    valids+=1
                    break
                else:
                    break
        except Exception as e:
            print("Failed with error {}".format(str(e))+'\n')
    return valids

numValids = isValid(inputs)
print(numValids)
