using System;
using System.IO;
using System.Windows.Forms;

namespace ex_01_windows_forms_app01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            lstvResultados.View = View.List;
            lstvResultados.FullRowSelect = true;
        }

        private void btnIconlocalizarPastaRaiz_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog folder = new FolderBrowserDialog())
            {
                if (folder.ShowDialog() == DialogResult.OK)
                {
                    txtCaminhoRaiz.Text = folder.SelectedPath;
                }
            }
        }

        private void btnIconlocalizarPastaDestino_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog folder = new FolderBrowserDialog())
            {
                if (folder.ShowDialog() == DialogResult.OK)
                {
                    txtCaminhoDestino.Text = folder.SelectedPath;
                }
            }
        }

        private void btnIconListarArq_Click(object sender, EventArgs e)
        {
            string caminhoRaiz = txtCaminhoRaiz.Text;

            if (string.IsNullOrWhiteSpace(caminhoRaiz))
            {
                MessageBox.Show("Informe o diretório raiz.");
                return;
            }

            if (!Directory.Exists(caminhoRaiz))
            {
                MessageBox.Show("O diretório raiz não existe.");
                return;
            }

            lstvResultados.Items.Clear();

            string[] arquivos = Directory.GetFiles(caminhoRaiz);

            foreach (string arquivo in arquivos)
            {
                FileInfo info = new FileInfo(arquivo);
                lstvResultados.Items.Add(info.Name);
            }

            MessageBox.Show("Arquivos listados com sucesso.");
        }
    }
}