/*
 * Exercicio 01 Estruturas de repeticao
 * Estrutura repetitiva com inicio e fim certo
 * for (inicio do ciclo, fim do ciclo; incremento (algo que permite o ciclo avançar))
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;

namespace ex_01_estruturas_repeticao
{
    internal class Program
    {
        static void Main(string[] args)
        {
            

            int i, num, soma, n;
            double media;
            soma = 0;
            Console.WriteLine("Quantos números quer ler? ");
            n = Convert.ToInt16(Console.ReadLine());

            for (i = 1; i <= n; i++) {

                Console.Write($"Introduza o {i}º valor: ");
                num = Convert.ToInt16(Console.ReadLine());
                soma = soma + num;

            }

            Console.WriteLine(i);

            media = soma / n;

            

            {

            }
        }
    }
}
