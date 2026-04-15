/*
* Exercício 06 - Arrays multidimensionais 
* Enunciado: "Escreva um programa em C# que leia os valores
* de uma matriz 3x3 fornecidos pelo usuário e, em seguida, 
* exiba na tela cada valor com sua respectiva posição."
* */

using System;

namespace ex_06_arrays_multidimensionais
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] matriz = new int[3, 3];

            // 1. Leitura dos dados
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    Console.Write($"Valor [{i + 1},{j + 1}]: ");
                    matriz[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }

            // 2. Exibição simplificada em formato de matriz
            Console.WriteLine("\n--- Matriz Resultante ---");
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    // O "\t" alinha os números em colunas
                    Console.Write(matriz[i, j] + "\t");
                }
                Console.WriteLine(); // Pula linha após cada linha da matriz
            }

            Console.ReadKey();
        }
    }
}
