/*
* Exercício 13 - Número Válido
* Enunciado: Cria um programa que peça um número ao utilizador
* e repita o pedido enquanto o número for menor que 1 ou maior que 10.
*/

using System;

namespace ex_13_numero_valido
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int numero;

            do
            {
                Console.Write("Digite um número entre 1 e 10: ");
                numero = int.Parse(Console.ReadLine());

            } while (numero < 1 || numero > 10);

            Console.ReadKey();
        }
    }
}
