/*
* Exercício 06 - Número dentro do Intervalo
* Enunciado: Cria um programa que leia um número inteiro e 
* continue a pedi-lo enquanto o valor inserido não estiver entre 1 e 100.
*/

using System;

namespace ex_06_numero_intervalo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int numero;

            do
            {
                Console.Write("Digite um número entre 1 e 100: ");
                numero = int.Parse(Console.ReadLine());

            } while (numero < 1 || numero > 100);

            Console.ReadKey();
        }
    }
}