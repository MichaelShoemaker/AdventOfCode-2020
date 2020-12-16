import re
import typing

def make_rules(file) -> set:
    badseats = set()
    data = open(file,'r').read().split('\n\n')
    ranges = re.findall('\d+',data[0])
    
    start = 0
    while start + 1 <= len(ranges)-1:
        for i in range(int(ranges[start]),int(ranges[start+1])+1):
            badseats.add(i)
        start+=2
    return badseats

def make_tickets(file, rules) -> set:
    tickets = []
    bad = []
    raw = open(file,'r').read().splitlines()
    data = [row for row in raw if len(row)>1]
    
    for line in data:
        if line[0].isnumeric():
            tickets.append([int(x) for x in line.split(',')])
    for i in tickets:
        for s in i:
            if s not in rules:
                bad.append(s)
    return sum(bad)

if __name__=='__main__':
    rules = make_rules('input.txt')
    
    print(make_tickets('input.txt', rules))
