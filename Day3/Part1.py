trees = 0
#Get the number of lines in the file
num_lines = sum(1 for line in open('input.txt'))
#Make an integer to multiply the lines for to ensure enough length in the line
mult = num_lines * 3
with open(r'input.txt','r') as infile:
    #Skip first line
    next(infile)
    x = 3
    for line in infile:
        #Remove the line break at the end and repeat the line
        line = line[:-1] * mult
        if line[x]=='#':
            trees+=1
        x+=3
print("{} Trees encountered in route".format(trees))
