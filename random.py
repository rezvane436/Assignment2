>>> import random
>>> list=[]
>>> for i in range(10):
          r=random.randint(1,100)
          if r not in list: list.append(r)

>>> list
[13, 53, 25, 95, 64, 87, 27, 93, 74, 60]