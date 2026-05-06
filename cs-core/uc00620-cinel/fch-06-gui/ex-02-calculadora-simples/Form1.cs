using System;
using System.Windows.Forms;

namespace ex_02_calculadora_simples
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label6_Click(object sender, EventArgs e)
        {
            int num1, num2, resultadoS, resultadoM;

            num1 = int.Parse(txtNum1.Text);

            num2 = int.Parse(txtNum2.Text);

            resultadoS = num1 + num2;
            resultadoM = num1 + num2;

            lblResultado.Text = resultadoS.ToString() + " " + resultadoM.ToString();

            MessageBox.Show("O resultado da soma é" + resultadoS.ToString(), "Resultado");

        }
        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            MessageBox.Show("foi");
        }

        private void btnInfo_Click(object sender, EventArgs e)
        {
            string genero, infoExtra;

            if (rdMasv.Checked)
            {
                genero = "Masculino";
            }
  }
}

    MensageBox