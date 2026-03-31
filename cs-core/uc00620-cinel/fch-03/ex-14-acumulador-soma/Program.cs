/*
* Exercício 14 - Soma Acumulada
* Enunciado: Cria um programa que peça números ao utilizador e vá
* somando os valores, parando apenas quando o utilizador introduzir o número 0.
*/

using System;

namespace ex_14_soma_numeros
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int soma = 0;
            int numero;

            do
            {
                Console.Write("Digite um número: ");
                numero = int.Parse(Console.ReadLine());

                soma += numero;

            } while (numero != 0);

            Console.WriteLine($"Soma total: {soma}");
            Console.ReadKey();
        }
    }
}
