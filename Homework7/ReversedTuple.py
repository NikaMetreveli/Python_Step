# აღწერეთ ორი ტაპლის ტიპის მონაცემი, დაბეჭდეთ ტაპლი სადაც პირველ და ბოლო ელემენტს შეცვლილი ექნება ადგილები:



tuple1 = (1,2,3,4)

reversedTuple =()

reversedTuple += (tuple1[-1], )

for i in range(1,len(tuple1)-1):
    reversedTuple += (tuple1[i], )

reversedTuple += (tuple1[0], )

print(reversedTuple)

