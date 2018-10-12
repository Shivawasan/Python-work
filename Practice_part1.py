

print("1.Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other")
def seq (numbers):
    if len(numbers)==len(set(numbers)):
        print("Numbers",numbers)
        return True
    else:
        print("Numbers",set(numbers))
        return False
print(seq(numbers=[1,2,3,4,5,6]))
print(seq(numbers=[2,3,2,4]))

print("2.Write a Python program to find the digits which are absent in a given mobile number")
def mob_num(given_num):
    n=len(given_num)
    total=(n+1)*(n+2)/2
    sum_num= sum(given_num)
    return total-sum_num
num=[1,2,3,5,6,7,8,4]
num2=mob_num(num)
print(num2)