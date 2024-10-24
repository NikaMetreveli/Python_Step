#აღწერეთ ორი სეტი, დაბეჭდეთ სეტი, რომელიც შედგება ტაპლებისგან და ისინი შეიცავენ ორი სეტის ყველა შესატყვისს:


set1 = {1,2,3,4,5,6,7,8}
set2 = {'a', 'b', 'c', 'd', 'e'}

combinedSet = {(a,b) for a in set1 for b in set2}

print(sorted(combinedSet))

