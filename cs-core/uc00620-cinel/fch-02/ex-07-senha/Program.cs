/*
* ex-07-senha
* Exercício 01 - Cria um programa que Leia uma senha (número inteiro) e mostre: 
* "Acesso permitido" se a senha for igual a 1234. "Acesso negado" caso contrário
*/


using System;

namespace Ficha2_Ex07_Senha
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1. Entrada de dados
            Console.Write("Digite a senha de acesso: ");
            string senhaDigitada = Console.ReadLine();

            // 2. Verificação (A senha correta é "1234")
            if (senhaDigitada == "1234")
            {
                Console.WriteLine("Acesso Permitido!");
            }
            else
            {
                Console.WriteLine("Acesso Negado.");
            }

            // 3. Pausa
            Console.WriteLine("\nPressione qualquer tecla para encerrar...");
            Console.ReadKey();
        }
    }
}
