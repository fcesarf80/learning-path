/*
 * Exercício 09 - Cálculo de áreas (estantes) 
 * Enunciado: O Sr. Jorge pretende comprar umas estantes para o seu quarto.
 * Sabendo que o local para as estantes tem a configuração de dois retângulos
 * adjacentes (dimensões b, h e a, c), elabore um programa que calcule a área total disponível. 
*/
using System;

namespace ex_09_calculo_area
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a base (a) do primeiro retângulo: ");
            double a = double.Parse(Console.ReadLine());

            Console.Write("Digite a altura (b) do primeiro retângulo: ");
            double b = double.Parse(Console.ReadLine());

            Console.Write("Digite a base (c) do segundo retângulo: ");
            double c = double.Parse(Console.ReadLine());

            Console.Write("Digite a altura (h) do segundo retângulo: ");
            double h = double.Parse(Console.ReadLine());

            double area1 = a * b;
            double area2 = c * h;
            double areaTotal = area1 + area2;

            Console.WriteLine($"\nÁrea total disponível: {areaTotal:F2}");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}