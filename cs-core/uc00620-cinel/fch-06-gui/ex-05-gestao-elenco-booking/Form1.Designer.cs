namespace ex_05_gestao_elenco_booking
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.gbDadosArtista = new System.Windows.Forms.GroupBox();
            this.cmbCategoria = new System.Windows.Forms.ComboBox();
            this.txtNomeArtistico = new System.Windows.Forms.TextBox();
            this.lblCategoria = new System.Windows.Forms.Label();
            this.lblNomeArtistico = new System.Windows.Forms.Label();
            this.gbFotografiaArtista = new System.Windows.Forms.GroupBox();
            this.picFotografia = new System.Windows.Forms.PictureBox();
            this.btnCarregarFoto = new System.Windows.Forms.Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.gbListaArtista = new System.Windows.Forms.GroupBox();
            this.dgvArtistas = new System.Windows.Forms.DataGridView();
            this.colID = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colNome = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colCategoria = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColFoto = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.btnEliminar = new System.Windows.Forms.Button();
            this.btnEditar = new System.Windows.Forms.Button();
            this.btnInserir = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.gbDadosArtista.SuspendLayout();
            this.gbFotografiaArtista.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picFotografia)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.gbListaArtista.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvArtistas)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.LightSkyBlue;
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel1.Controls.Add(this.pictureBox1);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Margin = new System.Windows.Forms.Padding(4);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(1006, 69);
            this.panel1.TabIndex = 0;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(10, 5);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(2);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(50, 46);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.MidnightBlue;
            this.label1.Location = new System.Drawing.Point(64, 9);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(281, 38);
            this.label1.TabIndex = 0;
            this.label1.Text = "Cadastro de Artistas";
            // 
            // gbDadosArtista
            // 
            this.gbDadosArtista.Controls.Add(this.cmbCategoria);
            this.gbDadosArtista.Controls.Add(this.txtNomeArtistico);
            this.gbDadosArtista.Controls.Add(this.lblCategoria);
            this.gbDadosArtista.Controls.Add(this.lblNomeArtistico);
            this.gbDadosArtista.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbDadosArtista.ForeColor = System.Drawing.Color.MidnightBlue;
            this.gbDadosArtista.Location = new System.Drawing.Point(0, 79);
            this.gbDadosArtista.Margin = new System.Windows.Forms.Padding(2);
            this.gbDadosArtista.Name = "gbDadosArtista";
            this.gbDadosArtista.Padding = new System.Windows.Forms.Padding(2);
            this.gbDadosArtista.Size = new System.Drawing.Size(523, 258);
            this.gbDadosArtista.TabIndex = 1;
            this.gbDadosArtista.TabStop = false;
            this.gbDadosArtista.Text = "Dados do Artista";
            // 
            // cmbCategoria
            // 
            this.cmbCategoria.Font = new System.Drawing.Font("Segoe UI", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cmbCategoria.FormattingEnabled = true;
            this.cmbCategoria.Location = new System.Drawing.Point(12, 140);
            this.cmbCategoria.Margin = new System.Windows.Forms.Padding(2);
            this.cmbCategoria.Name = "cmbCategoria";
            this.cmbCategoria.Size = new System.Drawing.Size(402, 25);
            this.cmbCategoria.TabIndex = 3;
            this.cmbCategoria.Text = "Selecione uma categoria...";
            // 
            // txtNomeArtistico
            // 
            this.txtNomeArtistico.Location = new System.Drawing.Point(12, 73);
            this.txtNomeArtistico.Margin = new System.Windows.Forms.Padding(2);
            this.txtNomeArtistico.Name = "txtNomeArtistico";
            this.txtNomeArtistico.Size = new System.Drawing.Size(402, 27);
            this.txtNomeArtistico.TabIndex = 2;
            // 
            // lblCategoria
            // 
            this.lblCategoria.AutoSize = true;
            this.lblCategoria.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCategoria.Location = new System.Drawing.Point(11, 113);
            this.lblCategoria.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblCategoria.Name = "lblCategoria";
            this.lblCategoria.Size = new System.Drawing.Size(96, 25);
            this.lblCategoria.TabIndex = 1;
            this.lblCategoria.Text = "Categoria:";
            // 
            // lblNomeArtistico
            // 
            this.lblNomeArtistico.AutoSize = true;
            this.lblNomeArtistico.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNomeArtistico.Location = new System.Drawing.Point(11, 46);
            this.lblNomeArtistico.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblNomeArtistico.Name = "lblNomeArtistico";
            this.lblNomeArtistico.Size = new System.Drawing.Size(143, 25);
            this.lblNomeArtistico.TabIndex = 0;
            this.lblNomeArtistico.Text = "Nome Artístico:";
            // 
            // gbFotografiaArtista
            // 
            this.gbFotografiaArtista.Controls.Add(this.picFotografia);
            this.gbFotografiaArtista.Controls.Add(this.btnCarregarFoto);
            this.gbFotografiaArtista.Controls.Add(this.pictureBox2);
            this.gbFotografiaArtista.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbFotografiaArtista.ForeColor = System.Drawing.Color.MidnightBlue;
            this.gbFotografiaArtista.Location = new System.Drawing.Point(536, 79);
            this.gbFotografiaArtista.Margin = new System.Windows.Forms.Padding(2);
            this.gbFotografiaArtista.Name = "gbFotografiaArtista";
            this.gbFotografiaArtista.Padding = new System.Windows.Forms.Padding(2);
            this.gbFotografiaArtista.Size = new System.Drawing.Size(470, 258);
            this.gbFotografiaArtista.TabIndex = 4;
            this.gbFotografiaArtista.TabStop = false;
            this.gbFotografiaArtista.Text = "Fotografia do Artista";
            // 
            // picFotografia
            // 
            this.picFotografia.Image = global::ex_05_gestao_elenco_booking.Properties.Resources.fototmsg;
            this.picFotografia.Location = new System.Drawing.Point(110, 46);
            this.picFotografia.Name = "picFotografia";
            this.picFotografia.Size = new System.Drawing.Size(245, 145);
            this.picFotografia.TabIndex = 7;
            this.picFotografia.TabStop = false;
            
            // 
            // btnCarregarFoto
            // 
            this.btnCarregarFoto.Font = new System.Drawing.Font("Segoe UI Semibold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnCarregarFoto.Image = global::ex_05_gestao_elenco_booking.Properties.Resources.imgicon24;
            this.btnCarregarFoto.Location = new System.Drawing.Point(148, 197);
            this.btnCarregarFoto.Name = "btnCarregarFoto";
            this.btnCarregarFoto.Size = new System.Drawing.Size(167, 39);
            this.btnCarregarFoto.TabIndex = 8;
            this.btnCarregarFoto.Text = "Carregar Foto";
            this.btnCarregarFoto.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnCarregarFoto.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnCarregarFoto.UseVisualStyleBackColor = true;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(0, 25);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(458, 218);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 5;
            this.pictureBox2.TabStop = false;
            // 
            // gbListaArtista
            // 
            this.gbListaArtista.Controls.Add(this.dgvArtistas);
            this.gbListaArtista.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbListaArtista.ForeColor = System.Drawing.Color.MidnightBlue;
            this.gbListaArtista.Location = new System.Drawing.Point(0, 342);
            this.gbListaArtista.Name = "gbListaArtista";
            this.gbListaArtista.Size = new System.Drawing.Size(994, 192);
            this.gbListaArtista.TabIndex = 5;
            this.gbListaArtista.TabStop = false;
            this.gbListaArtista.Text = "Lista de Artistas";
            // 
            // dgvArtistas
            // 
            this.dgvArtistas.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.dgvArtistas.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvArtistas.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.colID,
            this.colNome,
            this.colCategoria,
            this.ColFoto});
            this.dgvArtistas.Location = new System.Drawing.Point(12, 26);
            this.dgvArtistas.Name = "dgvArtistas";
            this.dgvArtistas.RowHeadersWidth = 51;
            this.dgvArtistas.RowTemplate.Height = 24;
            this.dgvArtistas.Size = new System.Drawing.Size(961, 150);
            this.dgvArtistas.TabIndex = 0;
            // 
            // colID
            // 
            this.colID.HeaderText = "ID";
            this.colID.MinimumWidth = 6;
            this.colID.Name = "colID";
            // 
            // colNome
            // 
            this.colNome.HeaderText = "Nome";
            this.colNome.MinimumWidth = 6;
            this.colNome.Name = "colNome";
            // 
            // colCategoria
            // 
            this.colCategoria.HeaderText = "Categoria";
            this.colCategoria.MinimumWidth = 6;
            this.colCategoria.Name = "colCategoria";
            // 
            // ColFoto
            // 
            this.ColFoto.HeaderText = "Foto";
            this.ColFoto.MinimumWidth = 6;
            this.ColFoto.Name = "ColFoto";
            // 
            // btnEliminar
            // 
            this.btnEliminar.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEliminar.ForeColor = System.Drawing.Color.Black;
            this.btnEliminar.Image = global::ex_05_gestao_elenco_booking.Properties.Resources.bin;
            this.btnEliminar.Location = new System.Drawing.Point(836, 540);
            this.btnEliminar.Name = "btnEliminar";
            this.btnEliminar.Size = new System.Drawing.Size(134, 39);
            this.btnEliminar.TabIndex = 11;
            this.btnEliminar.Text = "Eliminar";
            this.btnEliminar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnEliminar.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnEliminar.UseVisualStyleBackColor = true;
            // 
            // btnEditar
            // 
            this.btnEditar.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEditar.ForeColor = System.Drawing.Color.Black;
            this.btnEditar.Image = global::ex_05_gestao_elenco_booking.Properties.Resources.edit;
            this.btnEditar.Location = new System.Drawing.Point(696, 540);
            this.btnEditar.Name = "btnEditar";
            this.btnEditar.Size = new System.Drawing.Size(134, 39);
            this.btnEditar.TabIndex = 10;
            this.btnEditar.Text = "Editar";
            this.btnEditar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnEditar.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnEditar.UseVisualStyleBackColor = true;
            // 
            // btnInserir
            // 
            this.btnInserir.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnInserir.ForeColor = System.Drawing.Color.Black;
            this.btnInserir.Image = global::ex_05_gestao_elenco_booking.Properties.Resources.insert;
            this.btnInserir.Location = new System.Drawing.Point(556, 540);
            this.btnInserir.Name = "btnInserir";
            this.btnInserir.Size = new System.Drawing.Size(134, 39);
            this.btnInserir.TabIndex = 9;
            this.btnInserir.Text = "Inserir";
            this.btnInserir.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnInserir.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnInserir.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 23F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1006, 610);
            this.Controls.Add(this.btnEliminar);
            this.Controls.Add(this.gbListaArtista);
            this.Controls.Add(this.btnEditar);
            this.Controls.Add(this.btnInserir);
            this.Controls.Add(this.gbFotografiaArtista);
            this.Controls.Add(this.gbDadosArtista);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("Segoe UI Semibold", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ForeColor = System.Drawing.Color.MidnightBlue;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.MaximumSize = new System.Drawing.Size(1024, 657);
            this.MinimumSize = new System.Drawing.Size(1024, 657);
            this.Name = "Form1";
            this.Text = "Form1";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.gbDadosArtista.ResumeLayout(false);
            this.gbDadosArtista.PerformLayout();
            this.gbFotografiaArtista.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.picFotografia)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.gbListaArtista.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dgvArtistas)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox gbDadosArtista;
        private System.Windows.Forms.Label lblCategoria;
        private System.Windows.Forms.Label lblNomeArtistico;
        private System.Windows.Forms.ComboBox cmbCategoria;
        private System.Windows.Forms.TextBox txtNomeArtistico;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox picFotografia;
        private System.Windows.Forms.Button btnCarregarFoto;
        private System.Windows.Forms.GroupBox gbFotografiaArtista;
        private System.Windows.Forms.GroupBox gbListaArtista;
        private System.Windows.Forms.DataGridView dgvArtistas;
        private System.Windows.Forms.DataGridViewTextBoxColumn colID;
        private System.Windows.Forms.DataGridViewTextBoxColumn colNome;
        private System.Windows.Forms.DataGridViewTextBoxColumn colCategoria;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColFoto;
        private System.Windows.Forms.Button btnInserir;
        private System.Windows.Forms.Button btnEliminar;
        private System.Windows.Forms.Button btnEditar;
    }
}

