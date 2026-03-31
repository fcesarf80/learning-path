/*
* Exercício 17 - Ignorar Números Pares 
* Enunciado: Cria um programa que mostre os números de 1 a 20, 
*mas ignore (não imprima) os números pares, utilizando a instrução 
*/

using System;

namespace ex_17_continue
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 20; i++)
            {
                if (i % 2 == 0)
                    continue;

                Console.WriteLine(i);
            }

            Console.ReadKey();
        }
    }
}