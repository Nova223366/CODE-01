import math 
angle_deg = float(input("Enter angle in degrees: "))

angle_rad = math.radians(angle_deg)

sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad) 

print(f"Sine of {angle_deg} degrees is: {sin_value}")
print(f"Cosine of {angle_deg} degrees is: {cos_value}")
print(f"Tangent of {angle_deg} degrees is: {tan_value}")