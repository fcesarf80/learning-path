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
        static void Main()
        {
            int[,] matriz = new int[3, 3];

            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                {
                    Console.Write($"[{i},{j}]: ");
                    matriz[i, j] = int.Parse(Console.ReadLine());
                }

            Console.WriteLine("\nMatriz:");
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                    Console.Write(matriz[i, j] + "\t");
                Console.WriteLine();
            }
        }
    }
}

