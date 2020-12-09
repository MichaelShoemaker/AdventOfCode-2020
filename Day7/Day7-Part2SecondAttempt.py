import re
import time

total = 0

class Node:
    def __init__(self, color, number, explored=False, parent = None):
        self.parent = parent
        self.color = color
        self.number = number
        self.explored = explored

    def __repr__(self):
        return f"Node Parent:{self.parent} Color:{self.color} Number:{self.number} Explored:{self.explored}"
    

def make_data(file):
    data = open(file,'r').read().replace('bags','bag').splitlines()
    return data


def make_node(data, search_item):
    frontier = []
    for line in data:
        line = line.split('contain')
        if line[0].strip()==search_item:
            node = Node(color=search_item, number = 1, explored = False)
            frontier.append(node)
            return frontier

def crawl_nodes(frontier):
    total_from_nodes = 0
    queue = frontier
    nodecount = 0
    for node in queue:
        while node.parent:
            if node.parent.explored == False:
                total_from_nodes = total_from_nodes + (node.number * node.parent.number)
                node.parent.explored = True
                node = node.parent
                print(node.color, node.number)
                nodecount+=1
            else:
                total_from_nodes += node.number
                node = node.parent
                print(node.color, node.number)
                nodecount+=1
    return total_from_nodes, nodecount
        
    

def crawl_file():
    frontier = make_node(make_data('test.txt'), 'shiny gold bag')
    data = make_data('test.txt')
    queue = []
    while len(frontier) > 0:
        node = frontier.pop(0)
        #print(f"Searching for {node.color}")
        time.sleep(1)
        for line in data:
            line = line.split('contain')
            if line[0].strip()==node.color:
                #print(f"Found {node.color} in {line[0].strip()}")
                #time.sleep(.5)
                line = line[1].split(',')
                
                for bag in line:
                    if line[0].strip()=='no other bag.':
                        #print(f"Adding {child.color} with value {child.number} to queue")
                        #time.sleep(.5)
                        queue.append(node)
                    elif bag[1].isnumeric():
                        child = Node(color = re.findall('[a-z ]+',bag)[1].strip(), number = int(re.findall('\d+',bag)[0]), parent = node, explored = False)
                        #print(f"Adding {child.color} with value {child.number} to frontier")
                        #time.sleep(.5)
                        frontier.append(child)
    return crawl_nodes(queue)
    

print(crawl_file())

