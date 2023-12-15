import math

def solve_quadratic(a: float, b: float, c:float) -> tuple:
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        raise ValueError("negative discriminant")
    
    sqrt_d = math.sqrt(discriminant)

    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)

    return (x1, x2)
