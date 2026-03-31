/*
* Exercício 07 - Soma de Positivos
* Enunciado: Cria um programa que leia números inteiros e 
* some apenas os valores positivos. O programa termina 
* quando for introduzido um número negativo.
*/

using System;

namespace ex_07_soma_positivos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int soma = 0;
            int numero;

            do
            {
                Console.Write("Digite um número: ");
                numero = int.Parse(Console.ReadLine());

                if (numero >= 0)
                    soma += numero;

            } while (numero >= 0);

            Console.WriteLine($"Soma: {soma}");
            Console.ReadKey();
        }
    }
}
