from functools import reduce
li = [4,5,6,7,8,9]
new= reduce(lambda x,y:x+y,li) 
print(new)