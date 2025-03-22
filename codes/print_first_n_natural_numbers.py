def Print1(n):
    if n==0:
        return

    print(n)
    Print1(n-1)


def Print1_de(n):
    if n==0:
        return


    Print1_de(n-1)
    print(n)

# Print1(3)
Print1_de(3)


