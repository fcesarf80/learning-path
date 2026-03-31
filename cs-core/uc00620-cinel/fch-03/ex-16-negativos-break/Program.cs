/*
* Exercício 16 - Negativo Break
* Enunciado: Cria um programa que leia vários números inteiros e os
* mostre no ecrã. O programa deve parar imediatamente se for introduzido
* um número negativo, utilizando a instrução break.
*/

using System;

namespace ex_16_break
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                int numero = int.Parse(Console.ReadLine());

                if (numero < 0)
                    break;

                Console.WriteLine(numero);
            }

            Console.ReadKey();
        }
    }
}