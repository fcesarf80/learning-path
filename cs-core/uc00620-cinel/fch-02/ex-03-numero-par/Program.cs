/*
 * Exercício 03 - Número par
 * Enunciado: Cria um programa que Leia um número inteiro
 * e Mostre "Número par" se o número for divisível por 2.
*/

using System;

namespace ex_03_numero_par
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número inteiro: ");
            int numero = int.Parse(Console.ReadLine());

            if (numero % 2 == 0)
            {
                Console.WriteLine("Número par");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}