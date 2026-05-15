using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FilmesApp
{
    internal class Filme
    {

        namespace FilmesApp
    {
        internal class Filme
        {
            [DisplayName("Número Filme")] 
            public int NumeroFilme { get; set; }
            [DisplayName("Nome Filme")]
            public string Nome { get; set; }
            [DisplayName("Nome Realizador")] 
            public string NomeRealizador { get; set; }
            public int Duracao { get; set; }
            public int Ano { get; set; }
            [DisplayName("Resumo")] 
            public string Resumo { get; set; }
            [DisplayName("Foto")] 
            public byte[] Foto { get; set; }
            // Se der erro em 'Categoria', mude para 'string' ou crie a enumeração Categoria
            public string Tipo { get; set; }
        }
    }



}
}
