import string
import time
#This script is approximately .006 seconds faster than Day6-Part2Improved.py
#This script uses intersection rather than iterating through string.ascii_lowercase[:]
def make_data(file):
    #Make a list where each element is all the people in the group
    data =(open(file,'r').read())
    return data.split('\n\n')

def make_groups(data):
    groups = []
    for group in data:
        #Empty list to hold each individual persons letters
        temp = []
        for person in group.strip().split('\n'):
            temp.append({char for char in person})
        groups.append(temp)
    return groups

def get_group_counts(groups):
    group_counts = []
    for group in groups:
        if len(group) == 1:
            group_counts.append(len(group[0]))
        else:
            count = len(set.intersection(*group))

            group_counts.append(count)
    return group_counts

if __name__=='__main__':
    start_time = time.time()
    print("The sum of characters every person in the group has across all groups is {}".format(sum(get_group_counts(make_groups(make_data('input.txt'))))))
    print("--- %s seconds ---" % (time.time() - start_time))
