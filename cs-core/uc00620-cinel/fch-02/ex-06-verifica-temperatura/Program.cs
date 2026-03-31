/*
 * Exercício 06 – Verifica Temperatura
 * Enunciado: Cria um programa que leia uma temperatura (em °C) e mostre:
 * "Está frio" se for menor que 15 -  "Está quente" caso contrário
*/

using System;

namespace ex_06_temperatura
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a temperatura em °C: ");
            double temperatura = double.Parse(Console.ReadLine());

            if (temperatura < 15)
            {
                Console.WriteLine("Está frio");
            }
            else
            {
                Console.WriteLine("Está quente");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}