/* 
* Exercício 11 - Áreas diversas (Jardim) 
* Enunciado: O Sr. Frederico tem uma quinta com várias divisões (pomar, casa, jardim, piscina).
 * Elabore um programa que receba as medidas de A, B, R e Y, e determine: 
* Perímetro do pomar, Área do pomar, Área da casa, Área do jardim e Área da piscina.
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