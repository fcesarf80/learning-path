/* 
* Exercício 11 - Áreas diversas (Jardim)
* Enunciado: Considere uma quinta composta por quatro zonas distintas:
1) Jardim (retângulo central)
   - Comprimento: A
   - Altura: X

2) Casa (quadrado)
   - Lado: B

3) Piscina (meio círculo)
   - O diâmetro da piscina corresponde à altura X
   - Logo, o raio é X / 2

4) Pomar (triângulo retângulo)
   - Base: T
   - Altura: X

O programa deve solicitar ao utilizador os valores de:
A, B, T e X

E calcular:

- Perímetro do pomar
  (soma dos lados do triângulo)

- Área do pomar
  Fórmula: (T × X) / 2

- Área da casa
  Fórmula: B²

- Área do jardim
  Fórmula: A × X

- Área da piscina
  (meio círculo)
  Fórmula: (π × (X/2)²) / 2

Apresentar todos os resultados com duas casas decimais.
*/


using System;

namespace ex_11_perimetro_planta
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite o valor de A: ");
            double A = double.Parse(Console.ReadLine());

            Console.Write("Digite o valor de B: ");
            double B = double.Parse(Console.ReadLine());

            Console.Write("Digite o valor de R: ");
            double R = double.Parse(Console.ReadLine());

            Console.Write("Digite o valor de Y: ");
            double Y = double.Parse(Console.ReadLine());

            double perimetroPomar = 2 * (A + B);
            double areaPomar = A * B;
            double areaCasa = R * R;
            double areaPiscina = Math.PI * Math.Pow(Y, 2);
            double areaJardim = areaPomar - areaCasa - areaPiscina;

            Console.WriteLine($"\nPerímetro do pomar: {perimetroPomar:F2}");
            Console.WriteLine($"Área do pomar: {areaPomar:F2}");
            Console.WriteLine($"Área da casa: {areaCasa:F2}");
            Console.WriteLine($"Área do jardim: {areaJardim:F2}");
            Console.WriteLine($"Área da piscina: {areaPiscina:F2}");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}