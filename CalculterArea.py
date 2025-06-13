from ast import main
import AreaCalculation as ac
def Exception():
    try:
        print("select the shape to caculate the area: ")
        print("1.Circle")
        print("2. Rectangle")
        print("3. Triangle")
        choice = int(input("Enter your choice (1/2/3): "))
        if choice == 1:
            radius = float(input("Enter the radius of circle: "))
            area = ac.area_circle(radius)
            print(f"The area of the circle is: {area: 2f}")
        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width "))
            area = ac.area_rectangle(length, width)
            print(f"The aera of the rectangle is: {area:.2f}")
        elif choice == 3:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = ac.area_triangle(base, height)
            print(f"The area of the triangle is: {area:.2f}")
        else:
            print("Invalid choice! please select a valid oprion. ")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred : {e}")

if __name__ == "__main__":
    Exception()
