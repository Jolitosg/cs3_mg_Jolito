earth_weight = int(input("Enter your weight: "))

def calculate_space_weight(earth_weight, destination):
    if destination == "mars":
        return earth_weight * 0.38
    elif destination == "Jupiter":
        return earth_weight * 2.34
    elif destination == "The Moon":
        return earth_weight * 0.16
    else:
        print("error we don't know that destination")
        return 0

print(calculate_space_weight(earth_weight ,"mars"))
print(calculate_space_weight(earth_weight,"Jupiter"))
print(calculate_space_weight(earth_weight,"The Moon"))
