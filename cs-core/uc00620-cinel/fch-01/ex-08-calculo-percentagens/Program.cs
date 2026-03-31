/* 
* Exercício 08 - Percentagem de raparigas e rapazes numa turma 
* Enunciado: Elabore um programa em C# que peça o número de raparigas
* e o número de rapazes de uma turma. O programa deve calcular e apresentar:
* a percentagem de raparigas e a percentagem de rapazes na turma. 
*/

using System;

namespace ex_08_calculo_percentagens
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite o número de alunas: ");
            double alunas = double.Parse(Console.ReadLine());

            Console.Write("Digite o número de alunos: ");
            double alunos = double.Parse(Console.ReadLine());

            double total = alunas + alunos;

            double percAlunas = (alunas / total) * 100;
            double percAlunos = (alunos / total) * 100;

            Console.WriteLine($"\nPercentagem de alunas: {percAlunas:F2}%");
            Console.WriteLine($"Percentagem de alunos: {percAlunos:F2}%");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}