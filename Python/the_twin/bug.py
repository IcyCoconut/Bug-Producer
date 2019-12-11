
def compute_diff(l):
    for each in l:
        each = each[0] - each[1]
    return l

l = [(6,3),(7,4),(2,3),(1,3),(5,8),(9,0)]
diff_l = compute_diff(l)
print("l:", l)
print("diff_l:", diff_l)



def compute_diff_v2(l):
    for i in range(len(l)):
        l[i] = l[i][0] - l[i][1]
    return l

def compute_sum(l):
    for i in range(len(l)):
        l[i] = l[i][0] + l[i][1]
    return l

l = [(6,3),(7,4),(2,3),(1,3),(5,8),(9,0)]
diff_l = compute_diff_v2(l)
sum_l = compute_sum(l)
print(l)
print(diff_l)
print(sum_l)
    