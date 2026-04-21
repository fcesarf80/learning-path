/*
 * Exercício 02 - Estrutura While 
 * Estrutura utilizada quando não sabemos o fim do ciclo.
 * */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex_02_estrutura_while
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num, soma = 0;
            double media;

            Console.Write("Introduza um valor: ");
            num = Convert.ToInt32(Console.ReadLine());

            soma = num;

            while (num != 0)
            {
                Console.Write("Introduza um valor: ");
                num = Convert.ToInt32(Console.ReadLine());
                soma = soma + num;
                i = i + 1;
            }

            media = soma / i;

            Console.WriteLine(i);
            Console.WriteLine(soma);
            Console.WriteLine(media);
