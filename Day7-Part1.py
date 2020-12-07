possibilities = set()
last_iter = 0
this_iter = 1
data = open('input.txt','r').read().split('\n')
while last_iter < this_iter:
    #Go through the data
    for line in data:
        line = line.replace('bags','')
        #If shiny gold is in line and
        if "shiny gold" in line:
            #Make line a list
            line = line.split(' ')
            #If the bag is not already in the list and is not 'shiny gold' add it
            if line[0]+' '+line[1] not in possibilities and line[0]+' '+line[1] != 'shiny gold':
                #Get just the type of the bag and add it
                bag = line[0]+' '+line[1]
                print(f"Adding {bag} to list")
                possibilities.add(bag)
                #Update the counter for the while loop
                last_iter = this_iter
                this_iter = len(possibilities)
                print(f"If Last Iter {last_iter}, This Iter {this_iter}")
        elif len(possibilities) > 0:
            temp = set()
            data2 = open('input.txt','r').read().split('\n')
            for line in data2:
                line = line.replace('bags','')
                for i in possibilities:
                    if i in line and  str(line[0:10]) != 'shiny gold':
                        line = line.split(' ')
                        if line[0]+' '+line[1] not in possibilities:
                            bag = line[0]+' '+line[1]
                            print(f"Adding {bag} to temp")
                            temp.add(bag)
                            last_iter = this_iter
                            this_iter = len(possibilities)
                            print(f"Elif Last Iter {last_iter}, This Iter {this_iter}")
                    else:
                        last_iter = this_iter
                        this_iter = len(possibilities)
                for n in temp:
                    if n not in possibilities:
                        possibilities.add(n)

print(len(possibilities))                
