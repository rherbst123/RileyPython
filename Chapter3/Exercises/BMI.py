#  Write	a	program	that	calculates	and	displays	a	person’s	body	mass	index	(BMI).	The	BMI	
# is often used to determine whether a person is overweight or underweight for his or her 
# height.	A	person’s	BMI	is	calculated	with	the	following	formula:
#  BMI 5 weight 3 703/height2
#  where weight is measured in pounds and height is measured in inches. The program should 
# ask	the	user	to	enter	his	or	her	weight	and	height,	then	display	the	user’s	BMI.	The	pro
# gram should also display a message indicating whether the person has optimal weight, is 
# underweight, or is overweight. A person’s weight is considered to be optimal if his or her 
# Programming Exercises 
# 177
#  BMI	is	between	18.5	and	25.	If	the	BMI	is	less	than	18.5,	the	person	is	considered	to	be	
# underweight.	If	the	BMI	value	is	greater	than	25,	the	person	is	considered	to	be	overweight.

weight = float(input("Enter your weight: (Pounds)"))
height = float(input("Enter your height: (inches)"))

bmi = weight * 703//height**2

print("Your Bmi is: ", bmi)

if bmi < 18.5:
    print("real skinny")
if bmi > 18.5 and bmi < 25.1:
    print("Optimal")
if bmi > 25:
    print("oh lawd he chonky")