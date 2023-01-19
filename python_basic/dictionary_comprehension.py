students = ["태연", "진우", "정현", "하눌", "성진"]
for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number, name))

students_dict = {
    "{}번".format(number + 1): name for number, name in enumerate(students)
}
print(students_dict)

scores = [85, 92, 78, 90, 100]
for x, y in zip(students, scores):
    print(x, y)

score_dic = {
    student: score for student, score in zip(students, scores)
}
print(score_dic)

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]

product_dict = {
    product: price for product, price in zip(product_list, price_list)
}

print(product_dict)
