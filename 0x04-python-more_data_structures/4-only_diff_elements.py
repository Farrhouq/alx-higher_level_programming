#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a_only = {ele for ele in set_1 if not ele in set_2}
    b_only = {ele for ele in set_2 if not ele in set_1}
    for i in b_only:
        a_only.add(i)
    return a_only
