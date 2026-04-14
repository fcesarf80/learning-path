using System;

namespace ex_06_arrays_multidimensionais
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1. Declaração da matriz 3x3
            int[,] matriz = new int[3, 3];

            // 2. Loop para preencher a matriz
            for (int i = 0; i <= 2; i++)
            {
                for (int j = 0; j <= 2; j++)
                {
                    Console.Write($"Introduza o valor para a posição {i + 1}, {j + 1}: ");
                    string entrada = Console.ReadLine();
                    matriz[i, j] = Convert.ToInt32(entrada);
                }
            }

            Console.WriteLine("\n--- Valores Guardados ---");

            // 3. Loop para exibir os valores
            for (int i = 0; i <= 2; i++)
            {
                for (int j = 0; j <= 2; j++)
                {
                    Console.WriteLine($"O valor da posição {i + 1}, {j + 1} é: {matriz[i, j]}");
                }
            }

            // Mantém a consola aberta até premires uma tecla
            Console.ReadKey();
        }
    }
}
