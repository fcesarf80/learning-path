/* 
 * Exercício 06 - Cálculo da velocidade média 
 * Enunciado: Elabore um programa em C# que calcule a velocidade média de um veículo,
 * pedindo ao utilizador: distância percorrida (em quilómetros) e tempo gasto (em minutos).
 * A velocidade média deve ser apresentada em metros por segundo (m/s). 
* Utilize a fórmula: v = d / t. Deve realizar as conversões necessárias de unidades. 
*/

using System;

namespace ex_06_velocidade_media
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a distância (em km): ");
            double distanciaKm = double.Parse(Console.ReadLine());

            Console.Write("Digite o tempo (em minutos): ");
            double tempoMin = double.Parse(Console.ReadLine());

            // Conversões
            double distanciaMetros = distanciaKm * 1000;
            double tempoSegundos = tempoMin * 60;

            // Cálculo da velocidade
            double velocidade = distanciaMetros / tempoSegundos;

            Console.WriteLine($"\nVelocidade média: {velocidade:F2} m/s");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}