#Need string to iterate a-z easily
import string

#List to hold the counts of each group
countPerGroup = []

#List to hold lists of each groups answers
newGroup = []

#Read in the data
data =(open('input.txt','r').read())

#Make a list for each group
groups = data.split('\n\n')

for i in groups:
    temp = []
    #Remove trailing spaces and make a list for each person
    for line in i.strip().split('\n'):
        temp.append([char for char in line])
    newGroup.append(temp)

for i in newGroup:
    #If there is only one list in the list then all characters are counted 
    if len(i) == 1:
        countPerGroup.append(len(i[0]))
    else:
        count = 0
        #Go through every lowercase letter
        for c in string.ascii_lowercase[:]:
            #If a letter is in all lists addto the count for the group
            if all(c in ls for ls in i):
                count += 1
        countPerGroup.append(count)
        
print(sum(countPerGroup))
