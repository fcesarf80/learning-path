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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.pnlBtn = new System.Windows.Forms.Panel();
            this.grpBtns = new System.Windows.Forms.GroupBox();
            this.pnlLytBtns = new System.Windows.Forms.TableLayoutPanel();
            this.btnIconListarArq = new FontAwesome.Sharp.IconButton();
            this.btnIconCopiar = new FontAwesome.Sharp.IconButton();
            this.btnIconMover = new FontAwesome.Sharp.IconButton();
            this.btnIconExcluir = new FontAwesome.Sharp.IconButton();
            this.pnlInformacoes = new System.Windows.Forms.Panel();
            this.gbxInformacoes = new System.Windows.Forms.GroupBox();
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.txtCaminhoRaiz = new System.Windows.Forms.TextBox();
            this.btnIconlocalizarPastaRaiz = new FontAwesome.Sharp.IconButton();
            this.btnIconlocalizarPastaDestino = new FontAwesome.Sharp.IconButton();
            this.lblRaiz = new System.Windows.Forms.Label();
            this.txtCaminhoDestino = new System.Windows.Forms.TextBox();
            this.lblDestino = new System.Windows.Forms.Label();
            this.pnlGreey = new System.Windows.Forms.Panel();
            this.grpBxResultados = new System.Windows.Forms.GroupBox();
            this.tlpFinalTela = new System.Windows.Forms.TableLayoutPanel();
            this.btnIconIniciar = new FontAwesome.Sharp.IconButton();
            this.lstvResultados = new System.Windows.Forms.ListView();
            this.pnlBtn.SuspendLayout();
            this.grpBtns.SuspendLayout();
            this.pnlLytBtns.SuspendLayout();
            this.pnlInformacoes.SuspendLayout();
            this.gbxInformacoes.SuspendLayout();
            this.tableLayoutPanel1.SuspendLayout();
            this.pnlGreey.SuspendLayout();
            this.grpBxResultados.SuspendLayout();
            this.tlpFinalTela.SuspendLayout();
            this.SuspendLayout();
            // 
            // pnlBtn
            // 
            this.pnlBtn.Controls.Add(this.grpBtns);
            this.pnlBtn.Dock = System.Windows.Forms.DockStyle.Top;
            this.pnlBtn.Location = new System.Drawing.Point(0, 0);
            this.pnlBtn.Name = "pnlBtn";
            this.pnlBtn.Size = new System.Drawing.Size(694, 133);
            this.pnlBtn.TabIndex = 6;
            // 
            // grpBtns
            // 
            this.grpBtns.Controls.Add(this.pnlLytBtns);
            this.grpBtns.Dock = System.Windows.Forms.DockStyle.Fill;
            this.grpBtns.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.grpBtns.Location = new System.Drawing.Point(0, 0);
            this.grpBtns.Name = "grpBtns";
            this.grpBtns.Size = new System.Drawing.Size(694, 133);
            this.grpBtns.TabIndex = 0;
            this.grpBtns.TabStop = false;
            this.grpBtns.Text = "Ações";
            // 
            // pnlLytBtns
            // 
            this.pnlLytBtns.ColumnCount = 4;
            this.pnlLytBtns.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 25F));
            this.pnlLytBtns.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 25F));
            this.pnlLytBtns.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 25F));
            this.pnlLytBtns.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 25F));
            this.pnlLytBtns.Controls.Add(this.btnIconListarArq, 2, 0);
            this.pnlLytBtns.Controls.Add(this.btnIconCopiar, 1, 0);
            this.pnlLytBtns.Controls.Add(this.btnIconMover, 0, 0);
            this.pnlLytBtns.Controls.Add(this.btnIconExcluir, 3, 0);
            this.pnlLytBtns.Location = new System.Drawing.Point(0, 26);
            this.pnlLytBtns.Name = "pnlLytBtns";
            this.pnlLytBtns.RowCount = 1;
            this.pnlLytBtns.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.pnlLytBtns.Size = new System.Drawing.Size(687, 101);
            this.pnlLytBtns.TabIndex = 1;
            // 
            // btnIconListarArq
            // 
            this.btnIconListarArq.IconChar = FontAwesome.Sharp.IconChar.FolderOpen;
            this.btnIconListarArq.IconColor = System.Drawing.Color.Black;
            this.btnIconListarArq.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconListarArq.Location = new System.Drawing.Point(345, 3);
            this.btnIconListarArq.Name = "btnIconListarArq";
            this.btnIconListarArq.Size = new System.Drawing.Size(165, 95);
            this.btnIconListarArq.TabIndex = 2;
            this.btnIconListarArq.Text = "Listar Arquivos";
            this.btnIconListarArq.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.btnIconListarArq.UseVisualStyleBackColor = true;
            this.btnIconListarArq.Click += new System.EventHandler(this.btnIconListarArq_Click);
            // 
            // btnIconCopiar
            // 
            this.btnIconCopiar.IconChar = FontAwesome.Sharp.IconChar.Clone;
            this.btnIconCopiar.IconColor = System.Drawing.Color.Black;
            this.btnIconCopiar.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconCopiar.Location = new System.Drawing.Point(174, 3);
            this.btnIconCopiar.Name = "btnIconCopiar";
            this.btnIconCopiar.Size = new System.Drawing.Size(165, 95);
            this.btnIconCopiar.TabIndex = 1;
            this.btnIconCopiar.Text = "Copiar";
            this.btnIconCopiar.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.btnIconCopiar.UseVisualStyleBackColor = true;
            this.btnIconCopiar.Click += new System.EventHandler(this.btnIconCopiar_Click);
            // 
            // btnIconMover
            // 
            this.btnIconMover.IconChar = FontAwesome.Sharp.IconChar.ArrowsSplitUpAndLeft;
            this.btnIconMover.IconColor = System.Drawing.Color.Black;
            this.btnIconMover.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconMover.Location = new System.Drawing.Point(3, 3);
            this.btnIconMover.Name = "btnIconMover";
            this.btnIconMover.Size = new System.Drawing.Size(165, 95);
            this.btnIconMover.TabIndex = 0;
            this.btnIconMover.Text = "Mover";
            this.btnIconMover.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.btnIconMover.UseVisualStyleBackColor = true;
            this.btnIconMover.Click += new System.EventHandler(this.btnIconMover_Click);
            // 
            // btnIconExcluir
            // 
            this.btnIconExcluir.IconChar = FontAwesome.Sharp.IconChar.TrashAlt;
            this.btnIconExcluir.IconColor = System.Drawing.Color.Black;
            this.btnIconExcluir.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconExcluir.Location = new System.Drawing.Point(516, 3);
            this.btnIconExcluir.Name = "btnIconExcluir";
            this.btnIconExcluir.Size = new System.Drawing.Size(168, 95);
            this.btnIconExcluir.TabIndex = 3;
            this.btnIconExcluir.Text = "Excluir Arquivos";
            this.btnIconExcluir.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.btnIconExcluir.UseVisualStyleBackColor = true;
            this.btnIconExcluir.Click += new System.EventHandler(this.btnIconExcluir_Click);
            // 
            // pnlInformacoes
            // 
            this.pnlInformacoes.Controls.Add(this.gbxInformacoes);
            this.pnlInformacoes.Dock = System.Windows.Forms.DockStyle.Top;
            this.pnlInformacoes.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.pnlInformacoes.Location = new System.Drawing.Point(0, 133);
            this.pnlInformacoes.Name = "pnlInformacoes";
            this.pnlInformacoes.Size = new System.Drawing.Size(694, 202);
            this.pnlInformacoes.TabIndex = 7;
            // 
            // gbxInformacoes
            // 
            this.gbxInformacoes.Controls.Add(this.tableLayoutPanel1);
            this.gbxInformacoes.Dock = System.Windows.Forms.DockStyle.Fill;
            this.gbxInformacoes.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbxInformacoes.Location = new System.Drawing.Point(0, 0);
            this.gbxInformacoes.Name = "gbxInformacoes";
            this.gbxInformacoes.Size = new System.Drawing.Size(694, 202);
            this.gbxInformacoes.TabIndex = 0;
            this.gbxInformacoes.TabStop = false;
            this.gbxInformacoes.Text = "Informações";
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.ColumnCount = 2;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 75.84856F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 24.15144F));
            this.tableLayoutPanel1.Controls.Add(this.txtCaminhoRaiz, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.btnIconlocalizarPastaRaiz, 1, 1);
            this.tableLayoutPanel1.Controls.Add(this.btnIconlocalizarPastaDestino, 1, 3);
            this.tableLayoutPanel1.Controls.Add(this.lblRaiz, 0, 0);
            this.tableLayoutPanel1.Controls.Add(this.txtCaminhoDestino, 0, 3);
            this.tableLayoutPanel1.Controls.Add(this.lblDestino, 0, 2);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(3, 26);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 4;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 21.36752F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 45.29914F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 35F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(688, 173);
            this.tableLayoutPanel1.TabIndex = 0;
            // 
            // txtCaminhoRaiz
            // 
            this.txtCaminhoRaiz.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtCaminhoRaiz.Location = new System.Drawing.Point(3, 32);
            this.txtCaminhoRaiz.Name = "txtCaminhoRaiz";
            this.txtCaminhoRaiz.Size = new System.Drawing.Size(515, 30);
            this.txtCaminhoRaiz.TabIndex = 0;
            this.txtCaminhoRaiz.TextChanged += new System.EventHandler(this.txtCaminhoRaiz_TextChanged);
            // 
            // btnIconlocalizarPastaRaiz
            // 
            this.btnIconlocalizarPastaRaiz.IconChar = FontAwesome.Sharp.IconChar.FolderOpen;
            this.btnIconlocalizarPastaRaiz.IconColor = System.Drawing.Color.Black;
            this.btnIconlocalizarPastaRaiz.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconlocalizarPastaRaiz.Location = new System.Drawing.Point(524, 32);
            this.btnIconlocalizarPastaRaiz.Name = "btnIconlocalizarPastaRaiz";
            this.btnIconlocalizarPastaRaiz.Size = new System.Drawing.Size(55, 38);
            this.btnIconlocalizarPastaRaiz.TabIndex = 2;
            this.btnIconlocalizarPastaRaiz.UseVisualStyleBackColor = true;
            this.btnIconlocalizarPastaRaiz.Click += new System.EventHandler(this.btnIconlocalizarPastaRaiz_Click);
            // 
            // btnIconlocalizarPastaDestino
            // 
            this.btnIconlocalizarPastaDestino.IconChar = FontAwesome.Sharp.IconChar.FolderPlus;
            this.btnIconlocalizarPastaDestino.IconColor = System.Drawing.Color.Black;
            this.btnIconlocalizarPastaDestino.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconlocalizarPastaDestino.Location = new System.Drawing.Point(524, 129);
            this.btnIconlocalizarPastaDestino.Name = "btnIconlocalizarPastaDestino";
            this.btnIconlocalizarPastaDestino.Size = new System.Drawing.Size(55, 39);
            this.btnIconlocalizarPastaDestino.TabIndex = 3;
            this.btnIconlocalizarPastaDestino.UseVisualStyleBackColor = true;
            this.btnIconlocalizarPastaDestino.Click += new System.EventHandler(this.btnIconlocalizarPastaDestino_Click);
            // 
            // lblRaiz
            // 
            this.lblRaiz.AutoSize = true;
            this.lblRaiz.Location = new System.Drawing.Point(3, 0);
            this.lblRaiz.Name = "lblRaiz";
            this.lblRaiz.Size = new System.Drawing.Size(126, 23);
            this.lblRaiz.TabIndex = 5;
            this.lblRaiz.Text = "Diretório Raiz:";
            // 
            // txtCaminhoDestino
            // 
            this.txtCaminhoDestino.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtCaminhoDestino.Location = new System.Drawing.Point(3, 129);
            this.txtCaminhoDestino.Name = "txtCaminhoDestino";
            this.txtCaminhoDestino.Size = new System.Drawing.Size(515, 30);
            this.txtCaminhoDestino.TabIndex = 1;
            // 
            // lblDestino
            // 
            this.lblDestino.AutoSize = true;
            this.lblDestino.Location = new System.Drawing.Point(3, 91);
            this.lblDestino.Name = "lblDestino";
            this.lblDestino.Size = new System.Drawing.Size(149, 23);
            this.lblDestino.TabIndex = 4;
            this.lblDestino.Text = "Diretório Destino";
            // 
            // pnlGreey
            // 
            this.pnlGreey.Controls.Add(this.grpBxResultados);
            this.pnlGreey.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pnlGreey.Location = new System.Drawing.Point(0, 335);
            this.pnlGreey.Name = "pnlGreey";
            this.pnlGreey.Size = new System.Drawing.Size(694, 170);
            this.pnlGreey.TabIndex = 8;
            // 
            // grpBxResultados
            // 
            this.grpBxResultados.Controls.Add(this.tlpFinalTela);
            this.grpBxResultados.Dock = System.Windows.Forms.DockStyle.Fill;
            this.grpBxResultados.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.grpBxResultados.Location = new System.Drawing.Point(0, 0);
            this.grpBxResultados.Name = "grpBxResultados";
            this.grpBxResultados.Size = new System.Drawing.Size(694, 170);
            this.grpBxResultados.TabIndex = 0;
            this.grpBxResultados.TabStop = false;
            this.grpBxResultados.Text = "Resultados";
            this.grpBxResultados.Enter += new System.EventHandler(this.grpBxResultados_Enter);
            // 
            // tlpFinalTela
            // 
            this.tlpFinalTela.ColumnCount = 2;
            this.tlpFinalTela.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 76.46199F));
            this.tlpFinalTela.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 23.53801F));
            this.tlpFinalTela.Controls.Add(this.btnIconIniciar, 1, 0);
            this.tlpFinalTela.Controls.Add(this.lstvResultados, 0, 0);
            this.tlpFinalTela.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tlpFinalTela.Location = new System.Drawing.Point(3, 26);
            this.tlpFinalTela.Name = "tlpFinalTela";
            this.tlpFinalTela.RowCount = 1;
            this.tlpFinalTela.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tlpFinalTela.Size = new System.Drawing.Size(688, 141);
            this.tlpFinalTela.TabIndex = 0;
            // 
            // btnIconIniciar
            // 
            this.btnIconIniciar.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.btnIconIniciar.IconChar = FontAwesome.Sharp.IconChar.Play;
            this.btnIconIniciar.IconColor = System.Drawing.Color.Black;
            this.btnIconIniciar.IconFont = FontAwesome.Sharp.IconFont.Auto;
            this.btnIconIniciar.IconSize = 30;
            this.btnIconIniciar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnIconIniciar.Location = new System.Drawing.Point(529, 92);
            this.btnIconIniciar.Name = "btnIconIniciar";
            this.btnIconIniciar.Size = new System.Drawing.Size(156, 46);
            this.btnIconIniciar.TabIndex = 1;
            this.btnIconIniciar.Text = "Iniciar";
            this.btnIconIniciar.UseVisualStyleBackColor = true;
            this.btnIconIniciar.Click += new System.EventHandler(this.btnIconIniciar_Click);
            // 
            // lstvResultados
            // 
            this.lstvResultados.HideSelection = false;
            this.lstvResultados.Location = new System.Drawing.Point(3, 3);
            this.lstvResultados.Name = "lstvResultados";
            this.lstvResultados.Size = new System.Drawing.Size(520, 121);
            this.lstvResultados.TabIndex = 0;
            this.lstvResultados.UseCompatibleStateImageBehavior = false;
            this.lstvResultados.SelectedIndexChanged += new System.EventHandler(this.lstvResultados_SelectedIndexChanged);
            this.lstvResultados.DoubleClick += new System.EventHandler(this.lstvResultados_DoubleClick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Window;
            this.ClientSize = new System.Drawing.Size(694, 505);
            this.Controls.Add(this.pnlGreey);
            this.Controls.Add(this.pnlInformacoes);
            this.Controls.Add(this.pnlBtn);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Ex-01 | Gestão de Arquivos";
            this.pnlBtn.ResumeLayout(false);
            this.grpBtns.ResumeLayout(false);
            this.pnlLytBtns.ResumeLayout(false);
            this.pnlInformacoes.ResumeLayout(false);
            this.gbxInformacoes.ResumeLayout(false);
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            this.pnlGreey.ResumeLayout(false);
            this.grpBxResultados.ResumeLayout(false);
            this.tlpFinalTela.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Panel pnlBtn;
        private System.Windows.Forms.GroupBox grpBtns;
        private FontAwesome.Sharp.IconButton btnIconMover;
        private System.Windows.Forms.TableLayoutPanel pnlLytBtns;
        private FontAwesome.Sharp.IconButton btnIconExcluir;
        private FontAwesome.Sharp.IconButton btnIconListarArq;
        private FontAwesome.Sharp.IconButton btnIconCopiar;
        private System.Windows.Forms.Panel pnlInformacoes;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.GroupBox gbxInformacoes;
        private System.Windows.Forms.TextBox txtCaminhoRaiz;
        private FontAwesome.Sharp.IconButton btnIconlocalizarPastaRaiz;
        private FontAwesome.Sharp.IconButton btnIconlocalizarPastaDestino;
        private System.Windows.Forms.Label lblDestino;
        private System.Windows.Forms.TextBox txtCaminhoDestino;
        private System.Windows.Forms.Label lblRaiz;
        private System.Windows.Forms.Panel pnlGreey;
        private System.Windows.Forms.GroupBox grpBxResultados;
        private System.Windows.Forms.TableLayoutPanel tlpFinalTela;
        private System.Windows.Forms.ListView lstvResultados;
        private FontAwesome.Sharp.IconButton btnIconIniciar;
    }
}