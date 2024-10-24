# დაწერეთ lambda ფუნქცია, რომელიც პასუხად დააბრუნებს სტრინგი არის თუ არა პალინდრომი,
# სტრინგები უნდა იყოს შენახული ლისტში. დაწერეთ filter ფუნქციის გამოყენები


list1 = ['kayak', 'chair', 'wow', 'ball', 'computer', 'rotator']

def filter_palindromes(given_list):

    palindrome_filter = filter(lambda a : a==a[::-1], given_list)
    return list(palindrome_filter)

print(filter_palindromes(list1))