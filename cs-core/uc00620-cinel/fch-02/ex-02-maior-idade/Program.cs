/*
 * Exercício 02 - Maior de idade
 * Enunciado: Cria um programa que Leia a idade de uma pessoa
 * e mostre "Maior de idade" se a idade for maior ou igual a 18.
*/

using System;

namespace ex_02_maior_de_idade
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a idade: ");
            int idade = int.Parse(Console.ReadLine());

            if (idade >= 18)
            {
                Console.WriteLine("Maior de idade");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}