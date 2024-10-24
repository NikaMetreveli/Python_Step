# აღწერეთ ორი tuple ტიპის მონაცემი, გააერთიანეთ ეს ორი tuple და დაბეჭდეთ ერთი მთლიანი დუბლიკატების გარეშე,
# შექმენით ლისტი duplicated_values და მასში დაამატეთ ის ინფორმაცია მხოლოდ ერთხელ, რომელიც დუბლირებული სახით გვხვდება tuple-ში, დაბეჭდეთ მოცემული სია
#






tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

combinedTuple =()
duplicatedValues = []

for i in range(len(tuple1)):
    if tuple1[i] in tuple2:
        if tuple1[i] not in combinedTuple:
            combinedTuple += (tuple1[i],)
            duplicatedValues.append(tuple1[i])
    elif tuple1[i] not in combinedTuple:
        combinedTuple += (tuple1[i],)


for i in range(len(tuple2)):
    if tuple2[i] not in combinedTuple:
        combinedTuple += (tuple2[i],)

print(combinedTuple)
print(duplicatedValues)