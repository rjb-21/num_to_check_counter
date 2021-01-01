#!/usr/bin/env python
# coding: utf-8


n1 = 372**2
n2 = 809**2
numbers = 0
for i in range(n1,n2):
    i_str = str(i)
    if i_str[0] <= i_str[1] and i_str[1] <= i_str[2] and i_str[2] <= i_str[3] and i_str[3] <= i_str[4] and i_str[4] <= i_str[5]:
        pairs = []
        counter = 0
        for j in range(0,5):
            if i_str[j] == i_str[j+1]:
                counter += 1
                pairs.append(i_str[j]+i_str[j+1])
                if counter > 1:
                    pairs_set = set(pairs)
                    if len(pairs_set) > 1:
                        print(i)
                        numbers += 1
print(f'There is {numbers} numbers to check.')                




