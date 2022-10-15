
import geo

print("----Geometric object area calculator----".upper())
main = True
while main:
    print("Which shape would you like to calculate ?")
    print(
        """1 - Rectangle\n"""
        """2 - Square\n"""
        """3 - Triangle\n"""
        """4 - Circle\n"""
        """5 - Regular Hexagon\n"""
        """6 - Exit"""
    )

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                first_side = float(input("Enter first side of rectangle: "))
                second_side = float(input("Enter second side of rectangle: "))
                rectangle = geo.Rectangle(first_side, second_side)
                print(rectangle.__str__())
            elif choice == 2:
                side = float(input("Enter side of square: "))
                square = geo.Square(side)
                print(side.__str__())
            elif choice == 3:
                base = float(input("Enter base of triangle: "))
                height = float(input("Enter height of triangle: "))
                triangle = geo.Triangle(base, height)
                print(triangle.__str__())
            elif choice == 4:
                radius = float(input("Enter radius of triangle: "))
                circle = geo.Circle(radius)
                print(circle.__str__())
            elif choice == 5:
                side = float(input("Enter side of hexagon: "))
                hexagon = geo.Hexagon(side)
                print(hexagon.__str__())
            elif choice == 6:
                main = False
                break
            break
        except ValueError:
            print("Please enter integer number.")
