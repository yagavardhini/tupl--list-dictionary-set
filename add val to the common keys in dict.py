from collections import Counter
dict1={'a':10,'b':3}
dict2={'c':34,'a':18}
dict3=Counter(dict1)+Counter(dict2)
print(dict3)
