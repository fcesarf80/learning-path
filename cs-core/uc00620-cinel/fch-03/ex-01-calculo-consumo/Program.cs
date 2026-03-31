/*
 * ex - 01 - Calculo consumo
 * Enunciado: Elabore um programa em C# que receba a quantidade
 * de cafés consumidos. Sabendo que cada café custa 0,85 €, o 
 * programa deve calcular e apresentar o valor total a pagar.
 */
using System;

namespace ex_01_calculo_consumo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const double precoCafe = 0.85;

            Console.Write("Digite a quantidade de cafés consumidos: ");
            int quantidade = int.Parse(Console.ReadLine());

            double totalPagar = quantidade * precoCafe;

            Console.WriteLine("Valor total a pagar: " + totalPagar.ToString("F2") + " €");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
