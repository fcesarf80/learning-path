/*
* Exercício 09 - Classificação de temperatura
* Enunciado: Cria um programa que leia uma temperatura (em °C) e mostre:
* "Frio" se for menor que 10 - "Agradável" se estiver entre 10 e 25
* "Quente" se for maior que 25
*/

using System;

namespace ex_09_classificacao_temperatura
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a temperatura em °C: ");
            double temperatura = double.Parse(Console.ReadLine());

            if (temperatura < 10)
            {
                Console.WriteLine("Frio");
            }
            else if (temperatura <= 25)
            {
                Console.WriteLine("Agradável");
            }
            else
            {
                Console.WriteLine("Quente");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}