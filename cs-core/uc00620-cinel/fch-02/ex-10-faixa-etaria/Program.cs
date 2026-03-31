/*
* Exercício 10 – Faixa Etaria
* Enunciado: Cria um programa que leia a idade de uma pessoa e mostre:
* "Criança" se idade < 13  -  "Adolescente" se idade entre 13 e 17  - "Adulto" se idade ≥ 18
*/

using System;

namespace ex_10_classificacao_idade
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a idade: ");
            int idade = int.Parse(Console.ReadLine());

            if (idade < 13)
            {
                Console.WriteLine("Criança");
            }
            else if (idade <= 17)
            {
                Console.WriteLine("Adolescente");
            }
            else
            {
                Console.WriteLine("Adulto");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}