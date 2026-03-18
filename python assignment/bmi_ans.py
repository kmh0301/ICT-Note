print("Please input your weight(kg):")
weight = float(input())
print("Please input your height(m):")
height = float(input())
BMI = weight / (height ** 2)

# Display BMI with 3 significant figures (Bonus requirement)
print(f"Your BMI is: {BMI:.3g}")

if BMI >= 24:
    print("FAT")
elif BMI <= 20:
    print("THIN")
else:
    print("FIT")
