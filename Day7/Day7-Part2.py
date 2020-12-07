import re

class Node:
    def __init__(self, parent = None, state=None, number = None):
        self.parent = parent
        self.state = state
        self.number = number
        self.nextval = None

        
# Make the stack frontier to keep track of nodes to explore
front = []

#Initialize the first Node with the source (bag) as the state
start = Node(parent = None, state = 'shiny gold bags', number = 1)

# Add the first Node to the frontier
front.append(start)

# Initialize an empty set to keep track of explored
explored = []

check = 0
while True:
    # If the frontier is empty that means there is nothing to explore
    if len(front)==0:
        #print(check)
        raise Exception("Uh oh. Frontier is empty")

    node = front.pop(0)
    print(node.state)
    data = open('test.txt','r').read().split('\n')
    
    for line in data:
        line = line.split('contain')
        if node.state == line[0].strip():
            for val in line[1:]:
                print(val)
                child = Node(state = re.findall('[a-z ]+',val), number = int(re.findall('\d+',val)[0]), parent = node)
                print("Adding child to frontier")
                front.append(child)
                print(len(front))
            print("Adding Node to Explored")
    explored.append(node)
    check+=1
