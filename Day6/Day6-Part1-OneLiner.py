print(sum([len(set(i.replace('\n',''))) for i in open('input.txt','r').read().split('\n\n')]))
