inputs = []
with open(r'input.txt','r') as infile:
    for line in infile:
        inputs.append(int(line))

def sum_is_2020(x):
    for l,n in enumerate(x):
        for m,o in enumerate(x):
            for y,z in enumerate(x):
                if l!=m and m!=y and y!=l and n + o + z == 2020:
                    return(n*o*z)
        
ans = sum_is_2020(inputs)
print(ans)
