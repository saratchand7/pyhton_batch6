#input() --> input formatting

#print() --> output formatting(fstring)

'''a,b = 13,4.5
print(a,b)#by default sep = ' '
print(a,b,sep=',')
print(9,15,sep='-')
print('Codegnan','Python','vizag',sep='---->')
#end by default throws new line,we can modify it
print(a,b,end=' ')
print('codegnan is in vizag',end='\t')
print('PFS6 and DA6')
print()
print('----->Welcome to game<-----')

#Use print() and build a simple calculator application
#ask input from user --> add,sub,mul,div'''

'''a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f'Addition of {a} and {b} is: {a+b}')
print(f'Subtraction of {a} and {b} is: {a-b}')
print(f'Multiplication of {a} and {b} is: {a*b}')
print(f'Division of {a} and {b} is: {a/b}')'''

#Usage of %d,%f,%s ---> perfer this type only when u r working on calculations
#print("usage of %"%(args))
price = 45.356;grade = 'A';stock = 15
#print("%d"%price)
#print("%d"%grade) #TypeError: %d format: a number is required, not str
#print("price is %d"%price)
#print("price is %f"%price)
#print("price is %.1f"%price)
#print("price is %s"%grade)

#Area of circle when radius is 3.5 cm, round off the area upto 2 decimal values:
#take pi value as 3.1416

'''area_ = 3.1416 * 3.5 * 3.5
print("Area of circle is %.2f"%area_)

#New Style Formatting --> Fstring(most recommended after python 3.9 version)
name = 'Codegnan';batch = 'PFS6'
print(f'{batch} is running in {name}')
print(f'Saketh is in {name}')'''

#control Block Statements --> They control the flow of execution of the program
#conditional statements --> if,if-else,if-elif-else

#BMI converted(Body Mass Index --> weight,height) (weight in kg,height in cm)
#height --> feets --> 1 feet = 30.48 cm --> 12 inches --> 1 inch = 2.54 cm
#1 feet --> 30.48 cm --> 0.3 m
#bmi = weight / ((height)**2)

''' < 18.5 --> underweight
>= 18.5 - 24.9 --> Healthy
> = 25 - 29.9 --> Overweight
>= 30 --> Obesity

#print(bmi)
#now lets divide into categories

weight = int(input('Enter your weight in kg: '))
height = float(input('Enter your height in cm: '))
name = input('Enter your name: ')
if weight > 0 and height > 0:
    bmi = weight / ((height) ** 2)
    if bmi < 18.5:
        print(f'BMI of {name} is {bmi} and you are underweight --> eat well')
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f'BMI of {name} is {bmi} and you are Healthy --> keep it up')
    elif bmi >= 25 and bmi <= 29.9:
            print(f'BMI of {name} is {bmi} and you are Overweight --> do exercise')
    elif bmi > 30:
        print(f'BMI of {name} is {bmi} and you are Obesity --> do exercise and eat well')
else:
    print('Do enter only +ve values greater than 0')

#Task --> User can enter height in centimeters,feets  --> meters
#cal BMI
#make all users validations for height --> cms,feets
#Github links '''

'''print("------ BMI CALCULATOR ------")

name = input("Enter your name: ")

weight = float(input("Enter your weight in kgs: "))

print("\nChoose height unit:")
print("1. Centimeters")
print("2. Feet")
print("3. Meters")
print("4. Height")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    height_cm = float(input("Enter your height in centimeters: "))

    if height_cm > 0:
        height = height_cm / 100
    else:
        height = 0

elif choice == 2:
    feet = float(input("Enter your height in feet: "))

    if feet > 0:
        height = feet * 12 * 2.54 / 100
    else:
        height = 0

elif choice == 3:
    height = float(input("Enter your height in meters: "))

elif choice == 4:
    height = float(input("Enter your height in meters: "))
    height = height / 100

else:
    height = 0
    print("Invalid choice!")

if weight > 0 and height > 0:

    bmi = weight / (height ** 2)

    print(f"\nName: {name}")
    print(f"Weight: {weight} kgs")
    print(f"Height: {height:.2f} meters")
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight -> Eat well")

    elif bmi >= 18.5 and bmi <= 24.9:
        print("Category: Healthy -> Keep consistent")

    elif bmi >= 25 and bmi <= 29.9:
        print("Category: Overweight -> Start exercising")

    else:
        print("Category: Obesity")

else:
    print("Please enter only positive values greater than 0")'''

'''print("------ BMI CALCULATOR ------")
a = {'weight':[],'height':[],'name':[]}
n = int(input("How many times:"))
for i in range(n):
    weight = int(input('Enter your weight in kg: '))
    height = float(input('Enter your height in cm: '))
    name = input('Enter your name: ')
    a['weight'].append(weight)
    a['height'].append(height)
    a['name'].append(name) 
    if weight > 0 and height > 0:
        bmi = weight / ((height) ** 2)
        if bmi < 18.5:
            print(f'BMI of {name} is {bmi} and you are underweight --> eat well')
        elif bmi >= 18.5 and bmi <= 24.9:
            print(f'BMI of {name} is {bmi} and you are Healthy --> keep it up')
        elif bmi >= 25 and bmi <= 29.9:
                print(f'BMI of {name} is {bmi} and you are Overweight --> do exercise')
        elif bmi > 30:
            print(f'BMI of {name} is {bmi} and you are Obesity --> do exercise and eat well')
    else:
        print('Do enter only +ve values greater than 0')

print(a)'''

#Exception Handling -->
#Exception Handling is a mechanisam to a program which respond to run time
#error or compilations
#Exception --> It tries to make our program go in a noraml flow








        
