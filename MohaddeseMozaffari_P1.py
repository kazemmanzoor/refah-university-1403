def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return f"Equation has two real solutions:\nx1 = {x1:.2f}\nx2 = {x2:.2f}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Equation has one real solution:\nx = {x:.2f}"
    else:
        real_part = -b / (2 * a)
        imag_part = ((-delta) ** 0.5) / (2 * a)
        return f"Equation has two complex solutions:\nx1 = {real_part:.2f} + {imag_part:.2f}i\nx2 = {real_part:.2f} - {imag_part:.2f}i"


print("Please enter the coefficients of the quadratic equation ax² + bx + c:")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("This is not a quadratic equation (a cannot be zero)")
else:
    result = solve_quadratic(a, b, c)
    print(result)
