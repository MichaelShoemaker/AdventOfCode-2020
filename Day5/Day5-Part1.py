allseats = []
with open('input.txt','r') as infile:
    for line in infile:
        index = 0
        seats = [i for i in range(0,128)]
        cols = [i for i in range(0,8)]
        seatMark = 0
        colMark = 0
        #Find the row
        while index < 7:
            mark = int(len(seats)/2)
            if line[index] == 'F':
                seats = seats[:mark]
            elif line[index] == 'B':
                seats = seats[mark:]
            index+=1
        seatMark = seats[0]
        while index < 10:
            mark = int(len(cols)/2)
            if line[index]=="R":
                cols = cols[mark:]
                #print(cols)
            elif line[index] == "L":
                cols = cols[:mark]
                #print(cols)
            index+=1
        colMark = cols[0]
        allseats.append(seatMark * 8 + colMark)
print(max(allseats))
             
        
