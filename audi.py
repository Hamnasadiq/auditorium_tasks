#----1----
# add the two digit input
two_digit_number = (input())
n0_1=int(two_digit_number[0])
no_2=int(two_digit_number[1])
print(n0_1+no_2)

#----2----
#life in weeks left when we live until 90 years
age = int(input())
cal2=int(age*52)
cal=int(90*52)
cal3=cal-cal2
print(f"You have {cal3} weeks left.")

#----3----
# BMI_calculator
height = float(input())
weight = int(input())
BMI=float(weight/(height**2))
if BMI<18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI>=18.5 and BMI <25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI>=25 and BMI<30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI>=30 and BMI<35:
  print(f"Your BMI is {BMI}, you are obese.")
elif BMI>=35:
  print(f"Your BMI is {BMI}, you are clinically obese.")

#-----4-----
# EVEN or ODD
# Which number do you want to check?
number = int(input())
if number%2==0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#-----5-----
# LEAP year or not
# Which year do you want to check?
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")

#----6-----
#Pizza order calculator
print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input() 
extra_cheese = input() 
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size selected.")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3 
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

#-----7-----
#  FizzBUZZ
for number in range(1,101):
  if number%3==0 and number%5==0:
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)

#----8-----
#calculates the sum of all the even numbers from 1 to X(any number).
target = int(input()) 
count=0
for x in range(1,target+1):
  if x%2==0:
    count+=x
print(f"{count}")