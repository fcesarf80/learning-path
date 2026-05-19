using System;

namespace FilmesApp
{
    internal class Categoria
    {
        public int IdCategoria { get; set; }
        public string Descricao { get; set; }

        public Categoria(int idCategoria, string descricao)
        {
            this.IdCategoria = idCategoria;
            this.Descricao = descricao;
        }

        public override int GetHashCode()
        {
            return -964325053 + IdCategoria.GetHashCode();
        }

        public override string ToString()
        {
            return Descricao;
        }
    }
}
