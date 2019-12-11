
def compute_diff(l):
    result = []
    for each in l:
        result.append(each[0] - each[1])
    return result

l = [(6,3),(7,4),(2,3),(1,3),(5,8),(9,0)]
diff_l = compute_diff(l)
print("l:", l)
print("diff_l:", diff_l)



def compute_diff_v2(l):
    return [x[0] - x[1] for x in l]

def compute_sum(l):
    return [x[0] + x[1] for x in l]

l = [(6,3),(7,4),(2,3),(1,3),(5,8),(9,0)]
diff_l = compute_diff_v2(l)
sum_l = compute_sum(l)
print(l)
print(diff_l)
print(sum_l)
    