/*
* ex - 04 - Extrutura de dados
* Enunciado:  "Crie um programa que use um laço de repetição
* para ler 5 idades, armazene-as em um array e, ao final, exiba
* a média aritmética, a maior e a menor idade informadas."
*/
using System;

namespace ex_04_estruturas_dados
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] idade = new int[5];
            double soma = 0; // Usamos double para que a divisão da média seja precisa

            for (int i = 0; i < 5; i++)
            {
                Console.Write("Introduza a " + (i + 1) + "ª idade: ");
                idade[i] = Convert.ToInt32(Console.ReadLine());

                // Somamos a idade digitada à variável soma
                soma += idade[i];
            }

            // Calculamos a média dividindo o total por 5
            double media = soma / 5;

            Console.WriteLine("\nIdades armazenadas com sucesso!");
            Console.WriteLine("A média das idades é: " + media.ToString("F2")); // "F2" limita a 2 casas decimais

            Console.WriteLine("\nPressione qualquer tecla para limpar e sair...");
            Console.ReadKey();
            Console.Clear();
        }
    }
}
