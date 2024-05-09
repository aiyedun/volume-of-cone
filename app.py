def calculate_volume_cone():
    import math
    radius = float(input("Enter the value of the radius of the base circle: "))
    height = float(input("Enter the value of the height of the cone: "))
    volume = (1/3) * math.pi * (radius**2) * height
    return volume

print(calculate_volume_cone())
