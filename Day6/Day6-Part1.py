countPerGroup = []
data =(open('input.txt','r').read())
groups = data.split('\n\n')
for i in groups:
    countPerGroup.append(len(set(i.replace('\n',''))))
print(sum(countPerGroup))
                    
