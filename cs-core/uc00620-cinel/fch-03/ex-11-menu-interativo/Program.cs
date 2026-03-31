/*
* Exercício 11 - Menu de Opções
* Enunciado: Cria um programa que mostre um menu com as opções
* (1- Somar, 2- Subtrair, 0- Sair) e repita a exibição até que o utilizador escolha a opção 0.
*/

using System;

namespace ex_11_menu_opcoes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int opcao;

            do
            {
                Console.WriteLine("1 - Somar");
                Console.WriteLine("2 - Subtrair");
                Console.WriteLine("0 - Sair");

                opcao = int.Parse(Console.ReadLine());

            } while (opcao != 0);

            Console.ReadKey();
        }
    }
}