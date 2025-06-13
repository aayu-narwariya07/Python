# function to calculate area of a cricle
import math 
def area_circle(radius):
    if radius < 0:
        raise ValueError ("Radius cannot be negative")
    return math.pi * radius ** 2

def area_rectangle(length, widht):
    if length < 0 or widht < 0:
        raise ValueError ("length and widht cannot be negative")
    return length * widht

def area_triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError ("base and height cannot be negative")
    return(base * height) / 2

r = input("Enter you redius.: ")
