/*
* Exercício 05 - Contagem Decrescente
* Enunciado: Cria um programa que mostre os números de 10 até 1 
* em ordem decrescente usando um for.
*/

using System;

namespace ex_05_contagem_decrescente
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int i = 10; i >= 1; i--)
            {
                Console.WriteLine(i);
            }

            Console.ReadKey();
        }
    }
}