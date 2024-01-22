# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers 
# print only those numbers which are divisible by 5

num_list = [5, 23, 35, 53, 75, 95, 18, 100]
print ("Given lists", num_list)
print("Divisible by 5: ")
for num in num_list:
    if num % 5 == 0:
        print(num)

