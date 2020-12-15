import typing

def make_data(file):
    data = open(file,'r').read().splitlines()
    time = int(data[0])
    buses=[int(i) for i in data[1].split(',') if i.isnumeric()]
    return (time, buses)


def highest(minutes, bus):
    #Multiply the minute intervals by themselves up until one number higher than the bus number
    for c in range(0, bus+1):
        nextbus = minutes * c
        #If the interval is higher than the bus number and less than the bus number plus the
        #minutes then that is the next possible time for the bus
        if nextbus > bus and nextbus < bus + minutes:
            break
    return nextbus,  minutes
    

if __name__=='__main__':
    schedule = make_data('input.txt')
    buses = []
    for t in schedule[1]:
         buses.append(highest(t, schedule[0]))
    print((min(buses)[0]-schedule[0])*min(buses)[1])    

 
