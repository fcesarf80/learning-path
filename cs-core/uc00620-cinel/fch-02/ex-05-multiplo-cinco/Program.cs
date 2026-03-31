/*
 * Exercício 05 - Múltiplo de 5
 * Enunciado: Cria um programa que leia um número inteiro e mostre
 * "Múltiplo de 5" se o número for divisível por 5.
*/

using System;

namespace ex_05_multiplo_de_5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número inteiro: ");
            int numero = int.Parse(Console.ReadLine());

            if (numero % 5 == 0)
            {
                Console.WriteLine("Múltiplo de 5");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}