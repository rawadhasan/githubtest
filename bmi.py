# collect height, weight, and units
weight = input('enter weight: ')
weightunit = str(input('enter unit of weight: '))
height = input('enter height: ')
heightunit = str(input("enter height: "))

# convert to imperial units
if heightunit == 'inches' or 'in' or 'inch':
    height = float(height)*0.0254
else:
    height = height
if weightunit == 'lbs' or 'lb' or 'pounds' or 'pound':
    weight = float(weight)*0.4536
else:
    weight = weight

# calcualte bmi
bmi = 703*(weight/(height)^2)
print(bmi)