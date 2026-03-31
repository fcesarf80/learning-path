/*
* Exercício 04 - Números Pares
* Enunciado: Cria um programa que mostre todos os números ~
* pares entre 1 e 20 usando um ciclo for.
*/

using System;

namespace ex_04_numeros_pares
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 20; i++)
            {
                if (i % 2 == 0)
                    Console.WriteLine(i);
            }

            Console.ReadKey();
        }
    }
}