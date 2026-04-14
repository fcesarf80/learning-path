/*
* ex-05-estrutura-for
* Enunciado: "Escreva um programa que leia dois vetores
* de 3 números e mostre a soma deles."
*/
using System;

class Program
{
    static void Main()
    {
        int[] a = new int[3], b = new int[3], soma = new int[3];

        Console.WriteLine("Valores do vetor A:");
        for (int i = 0; i < 3; i++) a[i] = int.Parse(Console.ReadLine());

        Console.WriteLine("Valores do vetor B:");
        for (int i = 0; i < 3; i++)
        {
            b[i] = int.Parse(Console.ReadLine());
            soma[i] = a[i] + b[i];
        }

        Console.WriteLine("Soma: " + string.Join(", ", soma));
    }
}
