# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:30:35 2016

@author: Lily
"""

List1 = []
tuple1 = (1, 0, 3, 4, 10)
tuple2 = (2, 0, 3, 4, 12)

for ii in range(5):
    List1.append(tuple1)
    List1.append(tuple2)

def test(some_tuple_list, f, Value):
    new_list = []
    for ii in range(len(some_tuple_list)):
        if (f(some_tuple_list[ii], Value)):
            new_list.append(some_tuple_list[ii])
    return new_list
    
def include(some_tuple, val):
    if (some_tuple[0]==val):
        print("true")
        return True
    else:
        print("false")
        return False
        
print(test(List1, include, 2))
    
#print(test(List1, lambda s: str(s[4])[1] == "2"))
#print(test(List1, lambda s: (s[1]==1))
    
#print(filter(lambda s: s[0] == 1, List1))
    
test(List1, (lambda s,v: str(s[4])[1]), "2")