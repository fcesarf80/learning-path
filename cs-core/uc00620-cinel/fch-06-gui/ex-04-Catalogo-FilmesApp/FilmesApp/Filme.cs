using System;
using System.ComponentModel;

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

        [DisplayName("Duração")]
        public int Duracao { get; set; }

        [DisplayName("Ano")]
        public int Ano { get; set; }

        [DisplayName("Resumo")]
        public string Resumo { get; set; }

        [DisplayName("Foto")]
        public byte[] Foto { get; set; }

        [DisplayName("Categoria")]
        public string Tipo { get; set; }
    }
}
