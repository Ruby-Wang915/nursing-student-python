temperatures = [36.7, 38.1, 37.2, 39.0, 36.5, 37.8]
fever_count=0
for temperatures in temperatures:
    if temperatures>=37.5:
        fever_count+=1
        print(f'Fever:{temperatures}')
print(f'Patient with fever : {fever_count}')
