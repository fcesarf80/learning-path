/*
 * Exercício 02 - Maior e menor valor
 * Enunciado: Leia 8 números para um vetor e mostra:
 * → O maior valor → O menor valor → As respetivas posições no vetor
*/
using System;

namespace ex_02_maior_menor_valor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] vetor = new int[8];

            for (int posicao = 1; posicao < 9; posicao++)
            {
                Console.Write($"Digite um numero {posicao}º: ");
                int numero = int.Parse(Console.ReadLine());
                vetor[posicao] = numero;
            }

            int maior = vetor[0];
            int menor = vetor[0];
            int posMaior = 0;
            int posMenor = 0;

            for (int posicao = 0; posicao < 8; posicao++)
            {
                if (vetor[posicao] > maior)
                {
                    maior = vetor[posicao];
                    posMaior = posicao;
                }

                if (vetor[posicao] < menor)
                {
                    menor = vetor[posicao];
                    posMenor = posicao;
                }
            }

            Console.WriteLine("Maior valor: " + maior + " na posicao " + posMaior);
            Console.WriteLine("Menor valor: " + menor + " na posicao " + posMenor);

        }
    }
}