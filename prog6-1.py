# Assignment 6
# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

print("NUMBER SORTER GENERATOR")
print("Welcome! Insert four numbers that you want to sort in a sequence")

first_num = (input("Enter First Number: "))
second_num = (input("Enter Second Number: "))
third_num = (input("Enter Third Number: "))
fourth_num = (input("Enter Fourth Number: "))

if first_num <= second_num:
    first_num, second_num = second_num, first_num
    if second_num < third_num:
         second_num,third_num = third_num, second_num
elif third_num <= fourth_num:
        third_num, fourth_num = fourth_num, third_num

if first_num <= second_num:
        first_num, second_num = second_num,first_num
        if second_num < third_num:
              second_num, third_num = third_num, second_num
if third_num <= fourth_num:
    third_num, fourth_num = fourth_num, third_num

if first_num <= second_num:
        first_num, second_num= second_num, first_num
        
elif second_num <= third_num:
        second_num, third_num = third_num, second_num
        if third_num <= fourth_num:
               third_num, fourth_num = fourth_num, third_num

sort = first_num, second_num, third_num, fourth_num

print("The following numbers are arranged from highest to lowest accordingly:")
print(sort)