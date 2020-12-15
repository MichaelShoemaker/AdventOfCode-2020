import typing

def get_index_diff(check: list) -> int:
    second_to = 0
    last = 0
    for i in range(len(check)):
        if check[i] == check[-1]:
            second_to = last
            last = i
    return last - second_to

def get_index_diff_rev(inlist: list) -> int:
    check = inlist.copy()
    check.reverse()
    places = 0
    for i in range(1,len(check)):
        places+=1
        if check[i] == check[0]:
            break
    return places

def count_out(seed: list, end: int) -> int:
    #Test is [0,3,6]
    #Length is 3, last index is 2
    end-=1
    initial_list = seed.copy()
    current_index = len(seed)
    while len(initial_list) <= end:
        if len(initial_list)%1000000==0:
            print(f"Checking with length {len(initial_list)}")
        #print(f"Looking at {initial_list[current_index-1]}")
        if initial_list[current_index-1] not in initial_list[:current_index-1]:
            initial_list.append(0)
            current_index+=1
        elif initial_list[-1] in initial_list[:-1]:
            diff = get_index_diff_rev(initial_list)
            initial_list.append(diff)
            current_index+=1
##            print(initial_list)
            
    return initial_list[end]



if __name__=='__main__':
    #print(f"Part1's answer is {count_out([2,1,3], 2020)}")
    #print(f"Part1's answer is {count_out([0,20,7,16,1,18,15], 2020)}")
    print(f"Part1's answer is {count_out([0,3,6], 30000000)}")
