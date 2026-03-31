/* 
 * Exercício 10 – Equações
 * Enunciado: Elabore um programa em C# que resolva as seguintes equações matemáticas:
 * 1) y = 3x^2 + 5; 2) y = (x^2 + 2x) / 3; 3) y = (x^2 + 2x + 5) / (x - 1). 
 * O utilizador deve introduzir o valor de x para obter o resultado de y. 
*/

using System;

namespace ex_10_resolucao_equacao
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite o valor de x: ");
            double x = double.Parse(Console.ReadLine());

            double y1 = 3 * Math.Pow(x, 2) + 5;
            double y2 = (Math.Pow(x, 2) + 2 * x) / 3;

            if (x == 1)
            {
                Console.WriteLine("\nA equação 3 não pode ser calculada, porque o denominador seria zero.");
            }
            else
            {
                double y3 = (Math.Pow(x, 2) + 2 * x + 5) / (x - 1);
                Console.WriteLine($"\nResultado da equação 3: {y3:F2}");
            }

            Console.WriteLine($"\nResultado da equação 1: {y1:F2}");
            Console.WriteLine($"Resultado da equação 2: {y2:F2}");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}