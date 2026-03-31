/*
* Exercício 10 - Divisões Sucessivas
* Enunciado: Cria um programa que leia um número inteiro e o divida
* por 2 repetidamente até que o resultado seja menor que 1, utilizando um ciclo while.
*/

using System;

namespace ex_10_divisoes_sucessivas
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double numero = double.Parse(Console.ReadLine());

            while (numero >= 1)
            {
                Console.WriteLine(numero);
                numero /= 2;
            }

            Console.ReadKey();
        }
    }
}
