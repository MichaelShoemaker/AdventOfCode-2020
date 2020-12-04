def checkPasses(x):
    #Get rid of new lines and then split on spaces
    l= [i for i in x.replace('\n',' ').split(' ')]

    #Make sure all elements have some data.
    for n, i in enumerate(l):
        if len(i.strip())==0:
            l.pop(n)

    #Change the lists to dictionaries        
    forcheck = dict(s.split(':') for s in l)

    #Check for all required fields
    if all (k in forcheck for k in ('byr','iyr','eyr','hgt','hcl','ecl','pid')):
       return 1
    else:
        return 0


#Read the file into a string
f =  open('input.txt','r').read()
#Split on double new lines(a.k.a. a blank line)
passports = f.split('\n\n')

#Set Counter
count = 0
for i in passports:
    #Sum return values
    count += checkPasses(i)
print(count)
