/*
 * Exercício 04 - Cálculo da área de um trapézio
 * Enunciado: Elabore um programa em C# que calcule a área de um trapézio, 
* pedindo ao utilizador a base maior (m), a base menor (n) e a altura (h). 
* Utilize a fórmula: Área = ((m + n) * h) / 2. * O resultado deve ser apresentado arredondado a uma casa decimal. 
*/

using System;

namespace ex_04_area_trapezio
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a base maior (m): ");
            double m = double.Parse(Console.ReadLine());

            Console.Write("Digite a base menor (n): ");
            double n = double.Parse(Console.ReadLine());

            Console.Write("Digite a altura (h): ");
            double h = double.Parse(Console.ReadLine());

            double area = ((m + n) * h) / 2;

            Console.WriteLine($"\nÁrea do trapézio é: {area:F1}");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
