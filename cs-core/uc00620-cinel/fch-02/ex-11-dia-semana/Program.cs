/*
 * Exercício 11 - Dia da Semana
 * Enunciado: Cria um programa que leia um número de 1 a 7 e mostre
 * o dia da semana correspondente: 1 – Segunda, 2 – Terça, … 7 – Domingo.
 * Se o número for inválido, mostrar "Número inválido".
*/

using System;

namespace ex_11_dia_da_semana
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número de 1 a 7: ");
            int dia = int.Parse(Console.ReadLine());

            switch (dia)
            {
                case 1:
                    Console.WriteLine("Segunda");
                    break;
                case 2:
                    Console.WriteLine("Terça");
                    break;
                case 3:
                    Console.WriteLine("Quarta");
                    break;
                case 4:
                    Console.WriteLine("Quinta");
                    break;
                case 5:
                    Console.WriteLine("Sexta");
                    break;
                case 6:
                    Console.WriteLine("Sábado");
                    break;
                case 7:
                    Console.WriteLine("Domingo");
                    break;
                default:
                    Console.WriteLine("Número inválido");
                    break;
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}