import re

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
        if 2020 >= int(forcheck['byr']) >= 1920 \
           and len(forcheck['byr']) == 4 \
           and 2020 >= int(forcheck['iyr']) >= 2010 \
           and len(forcheck['iyr']) == 4 \
           and 2030 >= int(forcheck['eyr']) >= 2020 \
           and len(forcheck['eyr']) == 4\
           and forcheck['hgt'][-2:] in ['cm','in'] \
           and forcheck['hcl'][0]=='#' and re.match("^[a-z0-9]+$", forcheck['hcl'][1:]) and len(forcheck['hcl'][1:]) == 6\
           and forcheck['ecl'] in ('amb','blu','brn','gry','grn','hzl','oth') \
           and forcheck['pid'].isnumeric() and len(forcheck['pid']) == 9:
               if forcheck['hgt'][-2:] =='cm' and 150 <= int(forcheck['hgt'][:-2]) <= 193:
                   return 1
               elif forcheck['hgt'][-2:] =='in' and 59 <= int(forcheck['hgt'][:-2]) <= 76:
                   return 1
               else:
                   print(forcheck)
                   print("WTF")
                   return 0
        else:
            return 0
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
    checkPasses(i)
print(count)
#168 is incorrect
