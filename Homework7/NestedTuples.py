# აღწერეთ ერთმანეთში ჩადგმული ტაპლის მონაცემები, დაბეჭდეთ ერთი სრული ტაპლი, სადაც მოცემული იქნება ყველა ელემენტი.


tuple1 = (1, (2, 3), (4, (5, 6)))

simplifiedTuple = ()

for i in tuple1:
    if type(i) == tuple:
        for j in range(len(i)):
            simplifiedTuple += (i[j], )
    else:
        simplifiedTuple += (i, )

print(simplifiedTuple)

#აქ სამწუხაროდ ვერ ვხვდები როგორ დავწერო ისე, რომ სადაც 2 ტაპლია ერთმანეთში, ეგ გაყოს (აი (4, (5,6) სადაცაა), ისე რო უაზროდ კიდევ ერთი if არ დავამატო