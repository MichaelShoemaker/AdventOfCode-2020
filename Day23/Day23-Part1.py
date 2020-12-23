import time
import typing

def make_cups(file):
    cups = open(file,'r').read()
    return [int(c) for c in cups if c != '\n']


def play(cups: list, turns: int) -> list:
    counter = 0
    for x in range(0,turns):
##        print(f"-- move {x+1} --")
##        print(f"cups: {cups}")
        
        #current cup
        if counter == 0:
            current_cup = cups[0]
        elif (cups.index(current_cup) + 1) >= len(cups):
            current_cup = cups[(cups.index(last_cup)+1)%len(cups)]
        else:
            current_cup = cups[cups.index(last_cup)+1]
                
##        print(f"current cup: {current_cup}")
        
        #pick up next three into a list
        if cups.index(current_cup) == len(cups)-1:
            pick_up = cups[0:3]
        elif cups.index(current_cup) == len(cups)-2:
            pick_up = [cups[-1]] + cups[0:2]
        elif cups.index(current_cup) == len(cups)-3:
            pick_up = cups[-2:] + [cups[0]]
        else:
            first = cups.index(current_cup)+1
            last = first+3
            pick_up = cups[first:last]
        
##        print(f"pick up: {pick_up}")
        #Remove the picked up cups from the list
        for i in pick_up:
            cups.remove(i)

        next_cup = current_cup -1

        if next_cup == 0:
            next_cup = max(cups)
        
        #Make sure it isn't a picked up cup
        while next_cup in pick_up:
            lowest = min(cups)
            highest = max(cups)
            next_cup -= 1
            if next_cup < lowest:
                next_cup = highest
                break
            
##        print(f"destination: {next_cup}")
        #Get the index of the next cup
        index = cups.index(next_cup)
        for i in range(1,4):
            if index +1 > len(cups):
                cups.insert(index+i % len(cups)-1, pick_up[i-1])
            else:
                
                cups.insert(index+i,pick_up[i-1])
                
##        print(cups)
        #time.sleep(1)
        last_cup = current_cup
        counter += 1
    return cups

if __name__=='__main__':
    print(play(make_cups('input.txt'), 100))
    
