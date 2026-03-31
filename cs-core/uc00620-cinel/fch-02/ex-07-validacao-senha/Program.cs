/*
 * Exercício 07 - Senha
 * Enunciado: Cria um programa que Leia uma senha (número inteiro) e mostre:
 * "Acesso permitido" se a senha for igual a 1234 - "Acesso negado" caso contrário 2 de 2
*/

using System;

namespace ex_07_senha
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a senha: ");
            int senha = int.Parse(Console.ReadLine());

            if (senha == 1234)
            {
                Console.WriteLine("Acesso permitido");
            }
            else
            {
                Console.WriteLine("Acesso negado");
            }

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}