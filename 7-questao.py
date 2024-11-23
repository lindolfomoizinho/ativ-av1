import math

a = float(input("Informe o comprimento do primeiro lado: "))
b = float(input("Informe o comprimento do segundo lado: "))
c = float(input("Informe o comprimento do terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print("Os lados informados podem formar um triângulo.")
    
    angulo_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angulo_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angulo_C = 180 - (angulo_A + angulo_B)  
    print(f"Ângulos do triângulo: A = {angulo_A:.2f}°, B = {angulo_B:.2f}°, C = {angulo_C:.2f}°")

    if a == b == c:
        tipo_lado = "Equilátero"
    elif a == b or a == c or b == c:
        tipo_lado = "Isósceles"
    else:
        tipo_lado = "Escaleno"

    if angulo_A == 90 or angulo_B == 90 or angulo_C == 90:
        tipo_angulo = "Retângulo"
    elif angulo_A > 90 or angulo_B > 90 or angulo_C > 90:
        tipo_angulo = "Obtuso"
    else:
        tipo_angulo = "Agudo"

    print(f"O triângulo é {tipo_lado} e {tipo_angulo}.")
else:
    print("Os lados informados não podem formar um triângulo.")
