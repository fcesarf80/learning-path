/*
 * Exercício 02 -Soma de Números (1 a N)
 * Enunciado: Cria um programa que leia um número inteiro N e calcule
 * a soma de todos os números de 1*até N usando um for.
*/

using System;

namespace ex_02_soma_de_numeros
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número: ");
            int n = int.Parse(Console.ReadLine());

            int soma = 0;

            for (int i = 1; i <= n; i++)
            {
                soma += i;
            }

            Console.WriteLine($"Soma: {soma}");
            Console.ReadKey();
        }
    }
}