#Question 1
def hello_name(user_name):
    print("Hello "+user_name)
user_name = input('Enter USERNAME: ')
hello_name(user_name)

#Question 2
def first_odds():
    for n in range(1,101):
        if n % 2 != 0:
            print(n)
first_odds()

#Question 3
def max_num_in_list( a_list ):
    max = a_list[ 0 ]
    for n in a_list:
        if n > max:
            max = n
    return max
a_list = [19, 72, 45, 66, 9]
print(max_num_in_list(a_list))

#Question 4
def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return True
    elif(a_year % 100 == 0):
        return False
    elif(a_year % 4 == 0):
        return True
    else:
        return False
a_year = int(input('Enter year: '))
print(is_leap_year(a_year))

#Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

a_list = [11,12,13,14,15]
print(is_consecutive(a_list))
a_list = [20,22,23,24,25]
print(is_consecutive(a_list))