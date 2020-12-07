import re

class Node:
    def __init__(self, parent = None, state=None, number = None):
        self.parent = parent
        self.state = state
        self.number = number
        self.nextval = None

def rollup(x):
    my_counts = 1
    while x.parent:
        my_counts = my_counts * x.number + x.number
        x = x.parent
    return my_counts   

def node_trace(x):
    line = 0
    while x.parent:
        print(f"Node {line} has name {x.state} and value {x.number}.")
        line+=1
        x = x.parent
        
# Make the stack frontier to keep track of nodes to explore
front = []

#Initialize the first Node with the source (bag) as the state
start = Node(parent = None, state = 'shiny gold bags', number = 1)

# Add the first Node to the frontier
front.append(start)

#Keep list of terminal nodes
tally = []

check = 0
while True:
    # If the frontier is empty that means there is nothing left to search
    if len(front)==0:
        print("Fontier is now empty")
        break
    
    node = front.pop(0)
    data = open('test.txt','r').read().split('\n')
    
    for line in data:
        #If there are no more bags in this line brach rollup the count

        line = line.split('contain')
        if node.state == line[0].strip():
            if 'no other bags' in line[1]:
                child = Node(state = re.findall('[a-z ]+',val)[1].strip(), number = 1, parent = node)
                tally.append(child)
            else:
                for val in line[1].split(','):
                    child = Node(state = re.findall('[a-z ]+',val)[1].strip(), number = int(re.findall('\d+',val)[0]), parent = node)
                    #print(f"Adding child {child.state} to frontier")
                    front.append(child)


all_count = 0
for i in tally:
    all_count += rollup(i)

for i in tally:
    node_trace(i)
            
