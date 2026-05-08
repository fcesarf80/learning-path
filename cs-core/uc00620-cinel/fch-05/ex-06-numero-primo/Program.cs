/*
 * Exercício 06 - Método para verificar número primo
 * Enunciado: Implemente um método que receba um número e retorne true se for primo e false caso contrário.
*/
using System;

namespace ex_06_numero_primo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número: ");
            int numero = int.Parse(Console.ReadLine());

            bool primo = true;
            int limite = 0;

            if (numero < 2 || (numero > 2 && numero % 2 == 0))
            {
                primo = false;
            }
            else
            {
                limite = (int)Math.Sqrt(numero);

                // O "range(3, limite + 1, 2)" do Python vira este "for"
                for (int divisor = 3; divisor <= limite; divisor += 2)
                {
                    if (numero % divisor == 0)
                    {
                        primo = false;
                        break;p
                    }
                }
            }

            // Exibição do resultado com a frase personalizada
            string status = primo ? "é primo" : "não é primo";
            Console.WriteLine($"{numero} {status}");
        }
    }
}
