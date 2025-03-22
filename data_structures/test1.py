

def Compare(t1,t2):
    if ((t1 is None) and (t2 is None)) or (t1.key==t2.key) or (Compare(t1.left,t2.left) and Compare(t1.right,t2.right) ):
        return True
    else:
        return False















