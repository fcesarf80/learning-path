/*
* Exercício 08 - Contar Números
* Enunciado: Cria um programa que leia números inteiros e conte quantos
* foram introduzidos. O ciclo termina quando o utilizador inserir o número 0.
*/

using System;

namespace ex_08_contar_numeros
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int contador = 0;
            int numero;

            do
            {
                Console.Write("Digite um número: ");
                numero = int.Parse(Console.ReadLine());

                if (numero != 0)
                    contador++;

            } while (numero != 0);

            Console.WriteLine($"Quantidade: {contador}");
            Console.ReadKey();
        }
    }
}