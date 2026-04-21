/*
 * Exercicio 03 - Do While
 * Estrutura repetitiva que testa a condição no final. O bloco é executado sempre uma vez
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex_03_estrutura_do_while
{
    internal class Program
    {
        static void Main(string[] args)
        {
           int op;

            do
                {
                  Console.WriteLine("1 - Soma");
                  Console.WriteLine("2 - Subtração");
                  Console.WriteLine("3 - Multiplicação");
                  Console.WriteLine("4 - Divisão");
                  Console.WriteLine("5 - Sair");
                  op = Convert.ToInt16(Console.ReadLine());

            } while (op != 0);
        }
    }
}
