/*
* Exercício 01 - Números de 1 a 10
* Enunciado: Cria um programa que mostre no ecrã os números de 1 até 10 usando um ciclo for.
*/

using System;

namespace ex_01_numeros_1_a_10
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(i);
            }

            Console.ReadKey();
        }
    }
}