def calculaAreaCircunferencia(raio):
    pi = 3.14
    return pi*raio**2

def calculaAreaTriangulo(base, altura):
    return base * altura / 2
    

if __name__ == "__main__":
    base = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    area = calculaAreaTriangulo(base, altura)
    print("A area do triangulo é {}".format(area))
    # print(calculaAreaCircunferencia(float(input("Digite o raio: "))))