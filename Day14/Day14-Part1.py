import re
import typing

def make_data(file):
    data = open(file,'r').read().splitlines()
    return data

def make_binary(bin_string: str)->str:
    converted = bin(int(bin_string))[2:]
    while len(converted) < 36:
        converted = '0' + converted
    return converted

def get_mask_value(mask: str, binary: str) -> str:
    ret_str =''
    for i in range(len(mask)):
        if mask[i] == 'X':
            ret_str = ret_str + binary[i]
        elif mask[i] == '1':
            ret_str = ret_str + '1'
        elif mask[i] == '0':
            ret_str =ret_str+'0'
        
    return ret_str

def make_array(data):
    current_high = 0
    x = 0
    for i in data:
        
        if i[:4]=='mask':
            pass
        else:
            x = int(re.findall(r'\d+', i)[0])
            
        if x > current_high:
            current_high = x
        else:
            pass       
    return [None for i in range(current_high+1)]

if __name__=='__main__':
    data = make_data('test.txt')
    mem = make_array(data)
    mask = ''
    bin_str = ''
    masked_val = ''
    index = ''
    for line in data:
        if line[0:4]=='mask':
            mask = line.split('=')[1].strip()
        else:
            bin_str = make_binary(line.split('=')[1].strip())
            masked_val = get_mask_value(mask, bin_str)
            index = re.findall('\d+',line)[0]
            mem[int(index)] = int(masked_val,2)
    total = 0
    for i in mem:
        if i:
            total += i
        else:
            pass
    print(total)
