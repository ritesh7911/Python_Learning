l = [3,2,4]

def find_element_in_an_array(l,x):
    lenght = len(l)
    print(lenght)
    if lenght==0:

        return


    if l[0]==x:
        return True

    smaller_list = l[1:]

    xx = find_element_in_an_array(smaller_list, x)

    if xx:
        return True

    else:
        return False








print(find_element_in_an_array(l,456))