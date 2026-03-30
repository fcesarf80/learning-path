/* ex - 03 - media - aritmetica /*
 * Enunciado: Elabore um programa em C# que receba três notas
 * da *disciplina de Matemática * e calcule a média * aritmética
 * das três notas, apresentando o resultado ao utilizador. 
*/

using System;

namespace ex_03_media_aritmetica
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a primeira nota: ");
            double nota1 = double.Parse(Console.ReadLine());

            Console.Write("Digite a segunda nota: ");
            double nota2 = double.Parse(Console.ReadLine());

            Console.Write("Digite a terceira nota: ");
            double nota3 = double.Parse(Console.ReadLine());

            double media = (nota1 + nota2 + nota3) / 3;

            Console.WriteLine($"A média aritmética é: {media:F2}");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}