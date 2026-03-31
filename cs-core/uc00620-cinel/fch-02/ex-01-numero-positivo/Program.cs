/*
* Exercício 1 – Número Positivo
* Enunciado: Cria um programa que leia um número inteiro e
* mostre a mensagem "Número positivo" se o número  for maior que 0.
*/

using System;

namespace ex_01_numero_positivo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número inteiro: ");
            int numero = int.Parse(Console.ReadLine());

            if (numero > 0)
            {
                Console.WriteLine("Número positivo");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}