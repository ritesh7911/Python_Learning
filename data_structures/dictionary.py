
### creation of dictionries

l = [(1,'the'),('the','a')]   ### first element is key and second element is value


dictionary = dict(l)

print(dictionary)


d = dict.fromkeys(['the','a','an'])

d1= dict.fromkeys(['the','a','an'],10)


print(d,d1)


## 2.Accessing data in dictionaries

a = {1:'a','list':[1,2,3],'dict':{'a':1,'b':2}}

print(a)

print(a.get(1))
print(a.get('list'))### if key is  not present it will give 'None'

print(a.get('l'),0)


### adding a key

a['tuple']=(1,2)


## update data


## hashing
'''
convert key into indexes is calles hashing. Key is made to pass through hash function. this function will create hash code and compression function



'''     



if __name__=='__main__':
    print(a.keys())  ### bydefault I can change the value
    print(a.values())

    print(a.items())
    print(a)







