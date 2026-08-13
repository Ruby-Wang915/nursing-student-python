total_water=0
while total_water<2000:
    water=int(input('How much water did you drink (mL)?'))
    total_water+=water
    print(f"Total water :{total_water} mL")

print("Daily water goal achieved!")
