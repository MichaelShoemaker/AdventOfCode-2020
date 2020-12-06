inputs = []
with open(r'input.txt','r') as infile:
          for line in infile:
              inputs.append(line)
          

def is_valid(pws):
    valids = 0
    
    for line in pws:
        char_count = 0
        pieces = line.split(':')
        numLets = pieces[0].split(' ')
        bottom = int(numLets[0].split('-')[0])
        top = int(numLets[0].split('-')[1])
        letter = numLets[1]
        for i in pieces[1]:
            if i == letter:
                char_count+=1
        if char_count >= bottom and char_count <= top:
            valids+=1

    return valids

num_valids = is_valid(inputs)
print(num_valids)
