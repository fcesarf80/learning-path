/*
* Exercício 01 - Temperatura
* Enunciado: Cria um programa que leia uma temperatura (em °C) e mostre:
* "Está frio" se for menor que 15 - "Está quente" caso contrário
*/

using System;

namespace Ficha2_Ex06
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1. Entrada de dados
            Console.Write("Digite a temperatura atual em °C: ");
            double temperatura = double.Parse(Console.ReadLine());

            // 2. Lógica de decisão (IF / ELSE)
            if (temperatura < 15)
            {
                Console.WriteLine("Está frio");
            }
            else
            {
                Console.WriteLine("Está quente");
            }

            // 3. Pausa para ver o resultado
            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
