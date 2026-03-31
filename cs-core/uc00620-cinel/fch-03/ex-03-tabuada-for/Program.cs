/*
* Exercício 03 - Tabuada
* Enunciado: Crie um programa que leia um número inteiro e
*  mostre a tabuada desse número (de 1 a 10) usando um for.
*/

using System;

namespace ex_03_tabuada
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número: ");
            int numero = int.Parse(Console.ReadLine());

            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine($"{numero} x {i} = {numero * i}");
            }

            Console.ReadKey();
        }
    }
}