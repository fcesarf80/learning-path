/*
 * Exercício 04 - Nota positiva
 * Enunciado: Cria um programa que leia uma nota (0 a 20) e mostre
 * "Aprovado" se a nota for maior ou igual a 10.
*/

using System;

namespace ex_04_nota_positiva
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a nota (0 a 20): ");
            double nota = double.Parse(Console.ReadLine());

            if (nota >= 10)
            {
                Console.WriteLine("Aprovado");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}