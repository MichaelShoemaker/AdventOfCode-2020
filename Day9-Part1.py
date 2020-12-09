from itertools import combinations
def make_int_list(file):
    raw = open(file,'r').read().split('\n')
    clean_data = filter(lambda i: len(i)>0,raw)
    return [int(i) for i in clean_data]
    

def check_for_val(file, preammble, start, end):
    preammble = preammble
    start = start
    end = end
    
    data = make_int_list(file)
    for check in data[preammble:]:
        pos = [sum(i) for i in combinations(data[start:end],2)]
        if int(check) not in pos:
            #print(f"{check} is not a possible value based on the previous {preammble} numbers")
            return int(check)
            break
        start+=1
        end+=1


if __name__=='__main__':
    assert check_for_val('test.txt',5,0,5) == 127
    print(check_for_val('input.txt',25,0,25))
