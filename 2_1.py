"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    def remove_zero(lst):
        """
        remove zeros in the list
        """
        lst1 = []
        for num in range(0, len(lst)):
            if lst[num] != 0:
                lst1.append(lst[num])
        if len(lst1) < len(lst):
            lst1.extend([0]*(len(lst)-len(lst1)))
        return lst1
    
    def combine(lst1):
        """
        combine numbers that are the same
        """
        for num in range(0,len(lst1)-1):
            if lst1[num]==lst1[num+1]:
                lst1[num] = lst1[num]*2
                lst1[num+1] = 0
        return lst1
    
    list1 = remove_zero(line)
    list2 = combine(list1)
    list3 = remove_zero(list2)
    return list3

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([8, 16, 16, 8])
