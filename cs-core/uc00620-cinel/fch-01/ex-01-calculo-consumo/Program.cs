/*
 * Exercício 01 - calculo-consumo
 * Enunciado: Elabore um programa em C# que receba a quantidade de cafés consumidos.
 * Sabendo que cada café custa 0,85 €, o programa deve calcular e apresentar o valor total a pagar.
*/

using System;

namespace Ficha1_Ex01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1. Definição do preço por café (em C# usamos ponto para decimais no código)
            double precoPorCafe = 0.85;

            // 2. Entrada de dados
            Console.Write("Digite a quantidade de cafés consumidos: ");
            int quantidade = int.Parse(Console.ReadLine());

            // 3. Cálculo do valor total
            double totalAPagar = quantidade * precoPorCafe;

            // 4. Apresentação do resultado
            // O "F2" dentro do ToString serve para mostrar sempre 2 casas decimais
            Console.WriteLine("O valor total a pagar é: " + totalAPagar.ToString("F2") + " €");

            // Pausa para leitura
            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
