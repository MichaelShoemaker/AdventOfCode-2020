#import time
import typing
from itertools import combinations_with_replacement

#Create ordered list of ints, add zero to the beginning
#and a value three larger than the highest value
def make_data(file) -> list:
    data = open(file,'r').read().splitlines()
    intdata = [int(i) for i in data if len(i) > 0]
    intdata.sort()
    intdata.insert(0,0)
    adapter = max(intdata)+3
    intdata.append(adapter)
    return intdata


def find_jumps(file) -> int:
    jumps = make_data(file)
    ones = 0
    threes = 0
    for r, i in enumerate(jumps):
        if r+1 > len(jumps)-1:
            break
        elif jumps[r+1] -1 == i:
            #print(f"Jump from {i} to {jumps[r+1]} is 1")
            #time.sleep(.5)
            ones+=1
        elif jumps[r+1] - 3 == i:
            #print(f"Jump from {i} to {jumps[r+1]} is 3")
            #time.sleep(.5)
            threes +=1
        else:
            2
    return ones * threes
 
def make_viable_combos(data: list) -> int:
    parts = []
    winners = []
    end = len(data) -1
    for num1, e1 in enumerate(data):
        for num2, e2 in enumerate(data):
            temp= data[num1:num2]
            if len(temp)==0:
                pass
            else:# (max(temp)-min(temp))/3>=len(temp):
                if temp[0]!=0 and max(data)-3 in temp:
                    parts.append([0]+temp+[22])
                elif max(data)-3 in temp and temp not in parts:
                    parts.append(temp+[22])
                else:
                    pass
                
    for t, l in enumerate(parts):
        for n, r in enumerate(l):
            if n == len(data) -1:
                winners.append(l)
            elif l[n+1]-r > 3:
                print(temp)
                break
            
    for i in parts:
        print(i)

            
            
        

if __name__=='__main__':
    assert find_jumps('test.txt') == 220
    assert find_jumps('small.txt') == 35
    print(make_viable_combos(make_data('small.txt')))
    #print(f"The answer to Part1 is {find_jumps('input.txt')}")

