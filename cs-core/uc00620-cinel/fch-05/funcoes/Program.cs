/*
 * Exercício  - Funções
 * Enunciado: ---
*/
namespace funcoes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // O Main serve apenas para chamar os outros métodos
            MostrarMenu("Antônio");

            Console.WriteLine("Introduza o primeiro valor:");
            int a = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Introduza o segundo valor:");
            int b = Convert.ToInt32(Console.ReadLine());

            int resultadoSoma = Soma(a, b);
            Console.WriteLine($"O resultado da soma é: {resultadoSoma}");
        } // <--- O Main termina aqui!

        // Métodos criados FORA do Main, mas dentro da classe Program
        private static void MostrarMenu(string nome)
        {
            Console.WriteLine($"Olá {nome}, bem-vindo!");
            Console.WriteLine("-----MENU-------");
            Console.WriteLine("1 - Soma");
            Console.WriteLine("2 - Subtração");
            Console.WriteLine("3 - Multiplicação");
            Console.WriteLine("4 - Divisão");
            Console.WriteLine("Escolha uma opção:");
        }

        private static int Soma(int x, int y)
        {
            int resultado = x + y;
            return resultado;
        }
    }
}
