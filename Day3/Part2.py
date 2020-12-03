import math

#Get the number of lines in the file
num_lines = sum(1 for line in open('input.txt'))

#Make an integer to multiply the lines for to ensure enough length in the line
mult = num_lines * 7

slopes = [1,3,5,7,1]
treeCounts = []
skip = 0
for n,i in enumerate(slopes):
    trees = 0
    with open(r'input.txt','r') as infile:
        x = i
        #All but the last element move down one at a time
        if n < 4:
            #Skip first line
            next(infile)            
            for line in infile:
                #Remove the line break at the end and repeat the line
                line = line[:-1] * mult
                if line[x]=='#':
                    trees+=1
                x+=i
            treeCounts.append(trees)
        #If it is the last element, move down two lines at a time
        else:
            next(infile)
            next(infile)
            #To know when to skip lines
            tracker = 0
            for line in infile:
                line = line[:-1] * mult
                if tracker % 2 == 0:
                    if line[x] == '#':
                        trees += 1
                        tracker += 1
                    else:
                        tracker += 1
                        pass
                    x+=i
                elif tracker % 2 != 0:
                    tracker +=1
                    pass
            treeCounts.append(trees)
        
print(treeCounts)        
print("{} Trees encountered in all routes".format(math.prod(treeCounts)))
