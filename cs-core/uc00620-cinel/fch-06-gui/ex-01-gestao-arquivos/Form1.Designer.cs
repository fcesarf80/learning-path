namespace ex_01_windows_forms_app01
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.lblPriAplicacao = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.btnConcatenar = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(56, 68);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(177, 28);
            this.label1.TabIndex = 0;
            this.label1.Text = "Nome Completo: ";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(67, 126);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(96, 28);
            this.label2.TabIndex = 1;
            this.label2.Text = "Apelido: ";
            // 
            // lblPriAplicacao
            // 
            this.lblPriAplicacao.AutoSize = true;
            this.lblPriAplicacao.BackColor = System.Drawing.Color.DarkOrange;
            this.lblPriAplicacao.Font = new System.Drawing.Font("Segoe UI", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblPriAplicacao.Location = new System.Drawing.Point(168, 18);
            this.lblPriAplicacao.Name = "lblPriAplicacao";
            this.lblPriAplicacao.Size = new System.Drawing.Size(262, 38);
            this.lblPriAplicacao.TabIndex = 2;
            this.lblPriAplicacao.Text = "Primeira Aplicação";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(270, 75);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(291, 22);
            this.textBox1.TabIndex = 3;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(286, 126);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(291, 22);
            this.textBox2.TabIndex = 4;
            // 
            // btnConcatenar
            // 
            this.btnConcatenar.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnConcatenar.ForeColor = System.Drawing.Color.Blue;
            this.btnConcatenar.Location = new System.Drawing.Point(270, 178);
            this.btnConcatenar.Name = "btnConcatenar";
            this.btnConcatenar.Size = new System.Drawing.Size(235, 55);
            this.btnConcatenar.TabIndex = 5;
            this.btnConcatenar.Text = "➕  Concatenar";
            this.btnConcatenar.UseVisualStyleBackColor = true;
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(160, 293);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(345, 153);
            this.panel1.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(687, 584);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.btnConcatenar);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.lblPriAplicacao);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label lblPriAplicacao;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button btnConcatenar;
        private System.Windows.Forms.Panel panel1;
    }
}

