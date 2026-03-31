/*
 * ex - 02 - interpolacao - strings /*
 * Enunciado: Elabore um programa em C# que peça ao utilizador
 * o nome e o sobrenome.
* O programa deve apresentar uma mensagem de boas-vindas.
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex_02_intercalacoes_strings
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite seu nome: ");
            string nome = Console.ReadLine();

            Console.Write("Digite seu sobrenome: ");
            string sobrenome = Console.ReadLine();

            Console.WriteLine($"Bem-vindo, {nome} {sobrenome}!");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();

        }
    }
}
