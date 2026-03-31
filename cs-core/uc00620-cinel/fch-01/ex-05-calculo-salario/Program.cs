/* 
* Exercício 05 - Cálculo do salário de um funcionário
 * Enunciado: Elabore um programa em C# que peça: nome do funcionário,
 * número de horas trabalhadas, valor recebido por hora e número de filhos. 
 * O programa deve calcular o salário bruto (horas * valor por hora),
 * acrescentar 3% ao salário bruto por cada filho e apresentar o salário final.
*/

using System;

namespace ex_05_calculo_salario
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.Write("Digite o nome do funcionário: ");
            string nome = Console.ReadLine();

            Console.Write("Digite o número de horas trabalhadas: ");
            double horasTrabalhadas = double.Parse(Console.ReadLine());

            Console.Write("Digite o valor recebido por hora: ");
            double valorHora = double.Parse(Console.ReadLine());

            Console.Write("Digite o número de filhos: ");
            int numeroFilhos = int.Parse(Console.ReadLine());

            double salarioBruto = horasTrabalhadas * valorHora;
            double acrescimo = salarioBruto * 0.03 * numeroFilhos;
            double salarioFinal = salarioBruto + acrescimo;

            Console.WriteLine($"\nFuncionário: {nome}");
            Console.WriteLine($"Salário bruto: {salarioBruto:F2} €");
            Console.WriteLine($"Acréscimo por filhos: {acrescimo:F2} €");
            Console.WriteLine($"Salário final: {salarioFinal:F2} €");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}

