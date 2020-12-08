import time

def get_jmps_nops(file):
    tracker = set()
    data = open(file,'r').read().split('\n')
    q = 0
    jmps_and_nops = []
    while True:
        if q in tracker:
                print("Breaking...")
                break
            
        if data[q][0:3] == 'acc':
            if data[q][4]=='+':
                tracker.add(q)
                q+=1
            elif data[q][4]=='-':
                tracker.add(q)
                q+=1
        elif data[q][0:3] == 'nop':
            tracker.add(q)
            jmps_and_nops.append(['nop',q])
            q+=1
            
        elif data[q][0:3]=='jmp':
            if data[q][4:6]=='+0':
                jmps_and_nops.append(['nop +0',q])
                tracker.add(q)
                q+=1
                
            elif data[q][4]=='+':
                tracker.add(q)
                jmps_and_nops.append(['jmp',q])
                q+=int(data[q][5:8])
                
            elif data[q][4]=='-':
                tracker.add(q)
                jmps_and_nops.append(['jmp',q])
                q-=int(data[q][5:8])
    return jmps_and_nops           
            
            
            
def find_switch(file, x):
    tracker = set()
    accumulator = 0
    data = open('input.txt','r').read().split('\n')
    q=0
    if x[0]=='jmp':
        data[x[1]]='nop'+data[x[1]][3:]
    elif x[0]=='nop':
        data[x[1]]='jmp'+data[x[1]][3:]
    while True:
        if q == len(data)-1:
            print(f"Solution found using {x} accumulator is {accumulator}")
            return accumulator
        if q in tracker:
                return f"No solution found for {x}"                       
        if data[q][0:3] == 'acc':
            if data[q][4]=='+':
                tracker.add(q)
                accumulator += int(data[q][5:8])
                q+=1
            elif data[q][4]=='-':
                tracker.add(q)
                accumulator -= int(data[q][5:8])
                q+=1
        elif data[q][0:3] == 'nop':
            tracker.add(q)
            q+=1                        
        elif data[q][0:3]=='jmp':
            if data[q][4:6]=='+0':
                tracker.add(q)
                q+=1                
            elif data[q][4]=='+':
                if q + int(data[q][5:8]) > len(data):
                    print(f"Solution found using {x} accumulator is {accumulator}")
                    return accumulator
                tracker.add(q)
                q+=int(data[q][5:8])                
            elif data[q][4]=='-':
                tracker.add(q)
                q-=int(data[q][5:8])
    print(accumulator)

if __name__=='__main__':
    switches =get_jmps_nops('input.txt')

    for x in switches:
        c  = 0
        #print(f"Attempting try {c} out of {len(switches)} with inputs {x}")
        find_switch('input.txt',x)
        c+=1
        

