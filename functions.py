def circleArea(radius):
    area = 3.1415 * radius ** 2
    return area

def temperature(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def totalDue(money, tax):
    total = money + money * tax / 100
    return total

area = float(input("Enter radius of circle: "))
print("Area of cirlce: ", circleArea(area))


money = float(input("Enter money: "))
tax = float(input("Enter tax: "))
print("Total due: ", totalDue(money, tax))


fahrenheit = float(input("Enter fahrenheit temperature: "))
print("Celsius temperature is: ", temperature(fahrenheit))