def merge(d1,d2):
    return (d2.update(d1))
d1={'a':10,'b':2}
d2={'c':4,'f':8}
print(merge(d1,d2))
print(d2)
