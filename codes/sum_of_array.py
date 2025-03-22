l = [1,2]

def sum_of_array(l):
    length =len(l)
    if len(l)==0:
        return 'list is empty'
    if length==1 :
        return l[0]
    smaller_array = l[1:]
    smaller_sum = sum_of_array(smaller_array)
    return l[0]+smaller_sum




print(sum_of_array(l))