/*
 * ex - 07 - Cálculo do preço com IVA
 * Enunciado: Sabendo que a taxa de IVA é de 23%, elabore
 * um programa em C# que receba o preço de um produto sem
 * IVA e calcule o preço final com IVA incluído.
 */

using System;

namespace ex_07_calculo_imposto
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite o preço do produto (sem IVA): ");
            double preco = double.Parse(Console.ReadLine());

            double precoFinal = preco * 1.23;

            Console.WriteLine($"\nPreço com IVA (23%): {precoFinal:F2} €");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}