def make_int_list(file):
    raw = open(file,'r').read().split('\n')
    clean_data = filter(lambda i: len(i)>0,raw)
    return [int(i) for i in clean_data]
    

def check_for_val(file, preammble, start, end, target):
    preammble = preammble
    start = start
    end = end
        
    data = make_int_list(file)

    limit = len(data)
    while True:
        num = data[start:end]
        if sum(num)==target:
            return min(data[start:end])+max(data[start:end])
        elif end == limit:
            end = start+1
            start+=1
        else:
            end +=1
        


if __name__=='__main__':
    assert check_for_val('test.txt',0,1,5,127) == 62
    print(check_for_val('input.txt',0,1,25,1212510616))


