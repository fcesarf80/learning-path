/*
* Exercício 08 - Saldo bancário
* Enunciado: Cria um programa que leia o saldo de uma conta e mostre:
* "Saldo positivo" se o saldo for maior ou igual a 0
* "Saldo negativo" caso contrário
*/

using System;

namespace ex_08_saldo_bancario
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite o saldo da conta: ");
            double saldo = double.Parse(Console.ReadLine());

            if (saldo >= 0)
            {
                Console.WriteLine("Saldo positivo");
            }
            else
            {
                Console.WriteLine("Saldo negativo");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}