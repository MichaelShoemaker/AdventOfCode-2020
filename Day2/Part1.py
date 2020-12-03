inputs = []
with open(r'input.txt','r') as infile:
          for line in infile:
              inputs.append(line)
          

def isValid(pws):
    valids = 0
    
    for line in pws:
        charCount = 0
        pieces = line.split(':')
        numLets = pieces[0].split(' ')
        bottom = int(numLets[0].split('-')[0])
        top = int(numLets[0].split('-')[1])
        letter = numLets[1]
        for i in pieces[1]:
            if i == letter:
                charCount+=1
        if charCount >= bottom and charCount <= top:
            valids+=1

    return valids

numValids = isValid(inputs)
print(numValids)
