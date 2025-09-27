# # import process
# from process import balance as bal
# from process import add_num

# balance = 40000
# # print(process.my_name)
# # print(process.age)
# # print(process.sentence)
# print(balance)
# print(bal)



import random as ran

cars = ["teddy", "5naira", "1naira", "iphone"]
bias = [1, 2, 5, 0]

our_choices = ran.choices(cars, weights=bias, k = 1)
print(our_choices)
# sample = ran.sample(cars, k = 2)
# print(sample)
# our_choice = ran.choice(cars)
# print(our_choice)
# ran.shuffle(cars)
# print(cars)
# guess_int = ran.randint(1, 6)
# guess_float = ran.uniform(1, 6)
# any_float = ran.random()

# print(any_float)
