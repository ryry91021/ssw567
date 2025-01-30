def classify_triangle(a,b,c):
    if any(side <= 0 for side in [a, b, c]):
        raise ValueError("Lengths must be positive")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("This is not a working triangle")
    else:
        if a==b==c:
            return "equilateral"
        elif a==b!=c or a!=b==c or a==c!=b:
            return "isosceles"
        elif ((a**2)+(b**2)==(c**2)) or ((b**2)+(c**2)==(a**2)) or ((a**2)+(c**2)==(c**2)):
            return "right"
        elif a!=b!=c:
            return "scalene"
        
        return