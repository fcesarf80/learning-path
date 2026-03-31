/*
* Exercício 09 - Maior Número
* Enunciado: Cria um programa que leia vários números inteiros e 
* determine o maior valor introduzido, terminando quando o utilizador inserir 0.
*/

using System;

namespace ex_09_maior_numero
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int maior = int.MinValue;
            int numero;

            do
            {
                Console.Write("Digite um número: ");
                numero = int.Parse(Console.ReadLine());

                if (numero != 0 && numero > maior)
                    maior = numero;

            } while (numero != 0);

            Console.WriteLine($"Maior número: {maior}");
            Console.ReadKey();
        }
    }
}