def make_data(file):
    data = open(file,'r').read().splitlines()
    splitdata = [[i[0],i[1:]] for i in data]
    return splitdata


class Boat:
    
    
    def __init__(self, direction):
        directions = ['north','east','south','west']
        self.direction = direction
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0

    def next_direction(instructions):
        direction = instructions[1]
        if instructions[0]=='R':
            directions = ['north','east','south','west']
        elif instructions[0]=='L':
            directions = ['west','south','east','north']

        moves = int(instructions[1])/90

        if moves <= len(directions[directions.index(direction):])-1:
            changes = int(moves) + directions.index(direction)
        else:
            changes = int((moves + directions.index(direction)) % 4)

        return direction[changes]


    def move(self, instructions: list):
        if instructions[0] == 'F':
            if self.direction == 'north':
                self.north += int(instructions[1])
            elif self.direction == 'east':
                self.east += int(instructions[1])
            elif self.direction == 'south':
                self.south += int(instructions[1])
            elif self.direction == 'west':
                self.west += int(instructions[1])

        elif instructions[0] in ['R','L']:
            direction = instructions[0]
            
            if instructions[0]=='R':
                directions = ['north','east','south','west']
            elif instructions[0]=='L':
                directions = ['west','south','east','north']

            moves = int(instructions[1])/90

            if moves <= len(directions[directions.index(self.direction):])-1:
                changes = int(moves) + directions.index(self.direction)
            else:
                changes = int((moves + directions.index(self.direction)) % 4)

            self.direction = directions[changes]

        elif instructions[0] in ['N','E','S','W']:
            if instructions[0]=='N':
                self.north += int(instructions[1])
            elif instructions[0]=='E':
                self.east += int(instructions[1])
            elif instructions[0]=='S':
                self.south += int(instructions[1])
            elif instructions[0]=='W':
                self.west += int(instructions[1])
        #print(instructions, self.north, self.east, self.south, self.west, self.direction)

                
    def location(self):
        return (abs(abs(self.north) - abs(self.south))) +  abs((abs(self.east) - abs(self.west)))



if __name__=='__main__':
    data = make_data('input.txt')
    boat = Boat('east')
    
    for move in data:
        #print(move[0], move[1])
        boat.move(move)
    print(boat.location())
