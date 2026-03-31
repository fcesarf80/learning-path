/*
* Exercício 12 - Senha Correta
* Enunciado: Cria um programa que peça ao utilizador uma senha e repit
* a o pedido até que a senha correta (ex: 1234) seja inserida.
*/

using System;

namespace ex_12_senha_correta
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int senha;

            do
            {
                Console.Write("Digite a senha: ");
                senha = int.Parse(Console.ReadLine());

            } while (senha != 1234);

            Console.WriteLine("Senha correta");
            Console.ReadKey();
        }
    }
}