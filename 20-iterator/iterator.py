# Python Iterators

#Iterable vs Iterator

list = [0,1,2]
# print(list.__iter__())
# print(iter(list))
itr1 = list.__iter__()
print(itr1.__next__())
print(itr1.__next__())
print(itr1.__next__())
# print(itr1.__next__())


# itr1 = list1.__iter__()



#Looping Through an Iterator
list2 = [1,4,5]
# for x in list2:
#     print(x)



#Create an Iterator

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

c = Counter(5,10)
for i in c:
    print(i, end=' ')
#StopIteration
