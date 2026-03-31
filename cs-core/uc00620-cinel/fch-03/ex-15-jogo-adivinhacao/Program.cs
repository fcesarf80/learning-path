/*
* Exercício 15 - Adivinhar o Número
* Enunciado: Cria um programa onde o utilizador tem de adivinhar
* um número pré-definido (ex: 7), repetindo as tentativas até acertar.
*/

using System;

namespace ex_15_adivinhar_numero
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int numero;

            do
            {
                Console.Write("Adivinhe o número: ");
                numero = int.Parse(Console.ReadLine());

            } while (numero != 7);

            Console.WriteLine("Acertou!");
            Console.ReadKey();
        }
    }
}