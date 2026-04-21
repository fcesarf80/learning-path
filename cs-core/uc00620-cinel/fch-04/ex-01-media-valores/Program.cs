using System;

namespace ex_01_media_valores
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] numeros = new int[10];
            int soma = 0;

            for (int posicao = 0; posicao < 10; posicao++)
            {
                Console.WriteLine($"Digite o número {posicao + 1}: ");
                int numero = int.Parse(Console.ReadLine());

                numeros[posicao] = numero;
                soma += numero;
            }

            double media = soma / 10.0;
            Console.WriteLine("A média é: " + media);
        }
    }
}

