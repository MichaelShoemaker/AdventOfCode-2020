import time
tracker = set()
line = 0
data = open('input.txt','r').read().split('\n')
#print(data[0][4:6])
accumulator = 0
q = 0
while True:
    #print(q)
    if q in tracker:
            print("Breaking...")
            #time.sleep(1)
            break       
    if data[q][0:3] == 'acc':
        if data[q][4]=='+':
            tracker.add(q)
            accumulator += int(data[q][5:8])
            #print(f"Incrimenting by {int(data[q][5:8])}")
            #time.sleep(1)
            q+=1
        elif data[q][4]=='-':
            tracker.add(q)
            accumulator -= int(data[q][5:8])
            #print(f"Decreasing q by {int(data[q][5:8])}")
            #time.sleep(1)
            q+=1
    elif data[q][0:3] == 'nop':
        tracker.add(q)
        #print(f"NOP Operation on line {q}")
        #time.sleep(1)
        q+=1        
        
    
    elif data[q][0:3]=='jmp':
        if data[q][4:6]=='+0':
            #print(f"jmp 0 on line {q}")
            #time.sleep(1)
            tracker.add(q)
            q+=1
            
        elif data[q][4]=='+':
            tracker.add(q)
            #print(f"jmp +by {int(data[q][5:8])}")
            #time.sleep(1)
            q+=int(data[q][5:8])
            
        elif data[q][4]=='-':
            tracker.add(q)
            #print(f"jmp -by {int(data[q][5:8])}")
            q-=int(data[q][5:8])
            
            #time.sleep(1)
            
            
print(accumulator)
