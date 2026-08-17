def calculate_average(temperatures):
    total=0
    for t in temperatures:
        total+=t
    average=total/len(temperatures)
    return average

temperatures=[]
for i in range(5):
    temperature=float(input(f'Enter temperature {i+1}:'))
    temperatures.append(temperature)

result=calculate_average(temperatures)
print('Average temperature is : ',result)
