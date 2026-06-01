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
            this.txtPesquisar = new System.Windows.Forms.TextBox();
            this.btnPesquisar = new System.Windows.Forms.Button();
            this.lblPesquisarArtista = new System.Windows.Forms.Label();
            this.gbDadosBooking = new System.Windows.Forms.GroupBox();
            this.txtObservacoes = new System.Windows.Forms.TextBox();
            this.txtLocal = new System.Windows.Forms.TextBox();
            this.txtHora = new System.Windows.Forms.TextBox();
            this.lblObservacoes = new System.Windows.Forms.Label();
            this.lblLocal = new System.Windows.Forms.Label();
            this.lblHora = new System.Windows.Forms.Label();
            this.txtData = new System.Windows.Forms.TextBox();
            this.lblData = new System.Windows.Forms.Label();
            this.txtCache = new System.Windows.Forms.TextBox();
            this.txtNomeEvento = new System.Windows.Forms.TextBox();
            this.lblCache = new System.Windows.Forms.Label();
            this.lblNomeEvento = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.gbDadosArtista.SuspendLayout();
            this.gbFotografiaArtista.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picFotografia)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.gbListaArtista.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvArtistas)).BeginInit();
            this.gbDadosBooking.SuspendLayout();
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
            this.pictureBox1.ErrorImage = ((System.Drawing.Image)(resources.GetObject("pictureBox1.ErrorImage")));
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
            this.gbDadosArtista.Location = new System.Drawing.Point(11, 78);
            this.gbDadosArtista.Margin = new System.Windows.Forms.Padding(2);
            this.gbDadosArtista.Name = "gbDadosArtista";
            this.gbDadosArtista.Padding = new System.Windows.Forms.Padding(2);
            this.gbDadosArtista.Size = new System.Drawing.Size(438, 78);
            this.gbDadosArtista.TabIndex = 1;
            this.gbDadosArtista.TabStop = false;
            this.gbDadosArtista.Text = "Dados do Artista";
            // 
            // cmbCategoria
            // 
            this.cmbCategoria.Font = new System.Drawing.Font("Segoe UI", 7.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cmbCategoria.ForeColor = System.Drawing.SystemColors.InfoText;
            this.cmbCategoria.FormattingEnabled = true;
            this.cmbCategoria.Location = new System.Drawing.Point(147, 48);
            this.cmbCategoria.Margin = new System.Windows.Forms.Padding(2);
            this.cmbCategoria.Name = "cmbCategoria";
            this.cmbCategoria.Size = new System.Drawing.Size(267, 25);
            this.cmbCategoria.TabIndex = 3;
            this.cmbCategoria.Text = "Selecione uma categoria...";
            // 
            // txtNomeArtistico
            // 
            this.txtNomeArtistico.Location = new System.Drawing.Point(147, 17);
            this.txtNomeArtistico.Margin = new System.Windows.Forms.Padding(2);
            this.txtNomeArtistico.Name = "txtNomeArtistico";
            this.txtNomeArtistico.Size = new System.Drawing.Size(267, 27);
            this.txtNomeArtistico.TabIndex = 2;
            // 
            // lblCategoria
            // 
            this.lblCategoria.AutoSize = true;
            this.lblCategoria.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCategoria.Location = new System.Drawing.Point(11, 48);
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
            this.lblNomeArtistico.Location = new System.Drawing.Point(11, 17);
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
            this.gbFotografiaArtista.Location = new System.Drawing.Point(492, 75);
            this.gbFotografiaArtista.Margin = new System.Windows.Forms.Padding(2);
            this.gbFotografiaArtista.Name = "gbFotografiaArtista";
            this.gbFotografiaArtista.Padding = new System.Windows.Forms.Padding(2);
            this.gbFotografiaArtista.Size = new System.Drawing.Size(470, 234);
            this.gbFotografiaArtista.TabIndex = 4;
            this.gbFotografiaArtista.TabStop = false;
            this.gbFotografiaArtista.Text = "Fotografia do Artista";
            // 
            // picFotografia
            // 
            this.picFotografia.ErrorImage = ((System.Drawing.Image)(resources.GetObject("picFotografia.ErrorImage")));
            this.picFotografia.Image = ((System.Drawing.Image)(resources.GetObject("picFotografia.Image")));
            this.picFotografia.Location = new System.Drawing.Point(4, 35);
            this.picFotografia.Name = "picFotografia";
            this.picFotografia.Size = new System.Drawing.Size(453, 147);
            this.picFotografia.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picFotografia.TabIndex = 7;
            this.picFotografia.TabStop = false;
            // 
            // btnCarregarFoto
            // 
            this.btnCarregarFoto.Font = new System.Drawing.Font("Segoe UI Semibold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnCarregarFoto.Image = ((System.Drawing.Image)(resources.GetObject("btnCarregarFoto.Image")));
            this.btnCarregarFoto.Location = new System.Drawing.Point(155, 186);
            this.btnCarregarFoto.Name = "btnCarregarFoto";
            this.btnCarregarFoto.Size = new System.Drawing.Size(138, 39);
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
            this.pictureBox2.Size = new System.Drawing.Size(458, 201);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 5;
            this.pictureBox2.TabStop = false;
            // 
            // gbListaArtista
            // 
            this.gbListaArtista.Controls.Add(this.dgvArtistas);
            this.gbListaArtista.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbListaArtista.ForeColor = System.Drawing.Color.MidnightBlue;
            this.gbListaArtista.Location = new System.Drawing.Point(11, 396);
            this.gbListaArtista.Name = "gbListaArtista";
            this.gbListaArtista.Size = new System.Drawing.Size(983, 205);
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
            this.dgvArtistas.Size = new System.Drawing.Size(965, 170);
            this.dgvArtistas.TabIndex = 0;
            this.dgvArtistas.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvArtistas_CellClick);
            // 
            // colID
            // 
            this.colID.FillWeight = 25.66844F;
            this.colID.HeaderText = "ID";
            this.colID.MinimumWidth = 6;
            this.colID.Name = "colID";
            // 
            // colNome
            // 
            this.colNome.FillWeight = 127.8555F;
            this.colNome.HeaderText = "Nome";
            this.colNome.MinimumWidth = 6;
            this.colNome.Name = "colNome";
            // 
            // colCategoria
            // 
            this.colCategoria.FillWeight = 131.1992F;
            this.colCategoria.HeaderText = "Categoria";
            this.colCategoria.MinimumWidth = 6;
            this.colCategoria.Name = "colCategoria";
            // 
            // ColFoto
            // 
            this.ColFoto.FillWeight = 115.2767F;
            this.ColFoto.HeaderText = "Foto";
            this.ColFoto.MinimumWidth = 6;
            this.ColFoto.Name = "ColFoto";
            // 
            // btnEliminar
            // 
            this.btnEliminar.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEliminar.ForeColor = System.Drawing.Color.MidnightBlue;
            this.btnEliminar.Image = ((System.Drawing.Image)(resources.GetObject("btnEliminar.Image")));
            this.btnEliminar.Location = new System.Drawing.Point(849, 357);
            this.btnEliminar.Name = "btnEliminar";
            this.btnEliminar.Size = new System.Drawing.Size(123, 39);
            this.btnEliminar.TabIndex = 11;
            this.btnEliminar.Text = "Eliminar";
            this.btnEliminar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnEliminar.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnEliminar.UseVisualStyleBackColor = true;
            // 
            // btnEditar
            // 
            this.btnEditar.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEditar.ForeColor = System.Drawing.Color.MidnightBlue;
            this.btnEditar.Image = ((System.Drawing.Image)(resources.GetObject("btnEditar.Image")));
            this.btnEditar.Location = new System.Drawing.Point(721, 357);
            this.btnEditar.Name = "btnEditar";
            this.btnEditar.Size = new System.Drawing.Size(121, 39);
            this.btnEditar.TabIndex = 10;
            this.btnEditar.Text = "Editar";
            this.btnEditar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnEditar.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnEditar.UseVisualStyleBackColor = true;
            this.btnEditar.Click += new System.EventHandler(this.btnEditar_Click);
            // 
            // btnInserir
            // 
            this.btnInserir.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnInserir.ForeColor = System.Drawing.Color.MidnightBlue;
            this.btnInserir.Image = ((System.Drawing.Image)(resources.GetObject("btnInserir.Image")));
            this.btnInserir.Location = new System.Drawing.Point(593, 357);
            this.btnInserir.Name = "btnInserir";
            this.btnInserir.Size = new System.Drawing.Size(121, 39);
            this.btnInserir.TabIndex = 9;
            this.btnInserir.Text = "Inserir";
            this.btnInserir.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnInserir.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnInserir.UseVisualStyleBackColor = true;
            this.btnInserir.Click += new System.EventHandler(this.btnInserir_Click);
            // 
            // txtPesquisar
            // 
            this.txtPesquisar.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtPesquisar.ForeColor = System.Drawing.Color.Gray;
            this.txtPesquisar.Location = new System.Drawing.Point(589, 324);
            this.txtPesquisar.Name = "txtPesquisar";
            this.txtPesquisar.Size = new System.Drawing.Size(361, 27);
            this.txtPesquisar.TabIndex = 12;
            this.txtPesquisar.Text = "Digite o nome do artista...";
            // 
            // btnPesquisar
            // 
            this.btnPesquisar.Image = ((System.Drawing.Image)(resources.GetObject("btnPesquisar.Image")));
            this.btnPesquisar.Location = new System.Drawing.Point(462, 357);
            this.btnPesquisar.Name = "btnPesquisar";
            this.btnPesquisar.Size = new System.Drawing.Size(123, 39);
            this.btnPesquisar.TabIndex = 13;
            this.btnPesquisar.Text = "Pesquisar";
            this.btnPesquisar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnPesquisar.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.btnPesquisar.UseVisualStyleBackColor = true;
            this.btnPesquisar.Click += new System.EventHandler(this.btnPesquisar_Click_1);
            // 
            // lblPesquisarArtista
            // 
            this.lblPesquisarArtista.AutoSize = true;
            this.lblPesquisarArtista.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblPesquisarArtista.Location = new System.Drawing.Point(454, 327);
            this.lblPesquisarArtista.Name = "lblPesquisarArtista";
            this.lblPesquisarArtista.Size = new System.Drawing.Size(156, 25);
            this.lblPesquisarArtista.TabIndex = 14;
            this.lblPesquisarArtista.Text = "Pesquisar Artista:";
            // 
            // gbDadosBooking
            // 
            this.gbDadosBooking.Controls.Add(this.txtObservacoes);
            this.gbDadosBooking.Controls.Add(this.txtLocal);
            this.gbDadosBooking.Controls.Add(this.txtHora);
            this.gbDadosBooking.Controls.Add(this.lblObservacoes);
            this.gbDadosBooking.Controls.Add(this.lblLocal);
            this.gbDadosBooking.Controls.Add(this.lblHora);
            this.gbDadosBooking.Controls.Add(this.txtData);
            this.gbDadosBooking.Controls.Add(this.lblData);
            this.gbDadosBooking.Controls.Add(this.txtCache);
            this.gbDadosBooking.Controls.Add(this.txtNomeEvento);
            this.gbDadosBooking.Controls.Add(this.lblCache);
            this.gbDadosBooking.Controls.Add(this.lblNomeEvento);
            this.gbDadosBooking.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbDadosBooking.ForeColor = System.Drawing.Color.MidnightBlue;
            this.gbDadosBooking.Location = new System.Drawing.Point(11, 164);
            this.gbDadosBooking.Margin = new System.Windows.Forms.Padding(2);
            this.gbDadosBooking.Name = "gbDadosBooking";
            this.gbDadosBooking.Padding = new System.Windows.Forms.Padding(2);
            this.gbDadosBooking.Size = new System.Drawing.Size(438, 232);
            this.gbDadosBooking.TabIndex = 4;
            this.gbDadosBooking.TabStop = false;
            this.gbDadosBooking.Text = "Dados do Booking";
            // 
            // txtObservacoes
            // 
            this.txtObservacoes.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtObservacoes.ForeColor = System.Drawing.Color.Gray;
            this.txtObservacoes.Location = new System.Drawing.Point(147, 174);
            this.txtObservacoes.Name = "txtObservacoes";
            this.txtObservacoes.Size = new System.Drawing.Size(267, 27);
            this.txtObservacoes.TabIndex = 23;
            // 
            // txtLocal
            // 
            this.txtLocal.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtLocal.ForeColor = System.Drawing.Color.Gray;
            this.txtLocal.Location = new System.Drawing.Point(147, 142);
            this.txtLocal.Name = "txtLocal";
            this.txtLocal.Size = new System.Drawing.Size(267, 27);
            this.txtLocal.TabIndex = 22;
            // 
            // txtHora
            // 
            this.txtHora.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtHora.ForeColor = System.Drawing.Color.Gray;
            this.txtHora.Location = new System.Drawing.Point(147, 111);
            this.txtHora.Name = "txtHora";
            this.txtHora.Size = new System.Drawing.Size(267, 27);
            this.txtHora.TabIndex = 21;
            // 
            // lblObservacoes
            // 
            this.lblObservacoes.AutoSize = true;
            this.lblObservacoes.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblObservacoes.Location = new System.Drawing.Point(13, 176);
            this.lblObservacoes.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblObservacoes.Name = "lblObservacoes";
            this.lblObservacoes.Size = new System.Drawing.Size(122, 25);
            this.lblObservacoes.TabIndex = 20;
            this.lblObservacoes.Text = "Observações:";
            // 
            // lblLocal
            // 
            this.lblLocal.AutoSize = true;
            this.lblLocal.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblLocal.Location = new System.Drawing.Point(13, 144);
            this.lblLocal.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblLocal.Name = "lblLocal";
            this.lblLocal.Size = new System.Drawing.Size(58, 25);
            this.lblLocal.TabIndex = 19;
            this.lblLocal.Text = "Local:";
            // 
            // lblHora
            // 
            this.lblHora.AutoSize = true;
            this.lblHora.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblHora.Location = new System.Drawing.Point(13, 113);
            this.lblHora.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblHora.Name = "lblHora";
            this.lblHora.Size = new System.Drawing.Size(56, 25);
            this.lblHora.TabIndex = 18;
            this.lblHora.Text = "Hora:";
            // 
            // txtData
            // 
            this.txtData.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtData.ForeColor = System.Drawing.Color.Gray;
            this.txtData.Location = new System.Drawing.Point(147, 80);
            this.txtData.Name = "txtData";
            this.txtData.Size = new System.Drawing.Size(267, 27);
            this.txtData.TabIndex = 17;
            // 
            // lblData
            // 
            this.lblData.AutoSize = true;
            this.lblData.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblData.Location = new System.Drawing.Point(13, 79);
            this.lblData.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblData.Name = "lblData";
            this.lblData.Size = new System.Drawing.Size(54, 25);
            this.lblData.TabIndex = 16;
            this.lblData.Text = "Data:";
            // 
            // txtCache
            // 
            this.txtCache.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtCache.ForeColor = System.Drawing.Color.Gray;
            this.txtCache.Location = new System.Drawing.Point(147, 49);
            this.txtCache.Name = "txtCache";
            this.txtCache.Size = new System.Drawing.Size(267, 27);
            this.txtCache.TabIndex = 15;
            // 
            // txtNomeEvento
            // 
            this.txtNomeEvento.Location = new System.Drawing.Point(147, 20);
            this.txtNomeEvento.Margin = new System.Windows.Forms.Padding(2);
            this.txtNomeEvento.Name = "txtNomeEvento";
            this.txtNomeEvento.Size = new System.Drawing.Size(267, 27);
            this.txtNomeEvento.TabIndex = 2;
            // 
            // lblCache
            // 
            this.lblCache.AutoSize = true;
            this.lblCache.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCache.Location = new System.Drawing.Point(11, 49);
            this.lblCache.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblCache.Name = "lblCache";
            this.lblCache.Size = new System.Drawing.Size(64, 25);
            this.lblCache.TabIndex = 1;
            this.lblCache.Text = "Cache:";
            // 
            // lblNomeEvento
            // 
            this.lblNomeEvento.AutoSize = true;
            this.lblNomeEvento.Font = new System.Drawing.Font("Segoe UI Semibold", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNomeEvento.Location = new System.Drawing.Point(11, 21);
            this.lblNomeEvento.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblNomeEvento.Name = "lblNomeEvento";
            this.lblNomeEvento.Size = new System.Drawing.Size(156, 25);
            this.lblNomeEvento.TabIndex = 0;
            this.lblNomeEvento.Text = "Nome do Evento:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 23F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1006, 610);
            this.Controls.Add(this.gbDadosBooking);
            this.Controls.Add(this.lblPesquisarArtista);
            this.Controls.Add(this.gbFotografiaArtista);
            this.Controls.Add(this.btnPesquisar);
            this.Controls.Add(this.txtPesquisar);
            this.Controls.Add(this.btnEliminar);
            this.Controls.Add(this.gbListaArtista);
            this.Controls.Add(this.btnEditar);
            this.Controls.Add(this.btnInserir);
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
            this.Text = "Gestão de Elenco e Booking Artístico";
            this.Load += new System.EventHandler(this.Form1_Load);
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
            this.gbDadosBooking.ResumeLayout(false);
            this.gbDadosBooking.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

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
        private System.Windows.Forms.Button btnInserir;
        private System.Windows.Forms.Button btnEliminar;
        private System.Windows.Forms.Button btnEditar;
        private System.Windows.Forms.TextBox txtPesquisar;
        private System.Windows.Forms.Button btnPesquisar;
        private System.Windows.Forms.Label lblPesquisarArtista;
        private System.Windows.Forms.GroupBox gbDadosBooking;
        private System.Windows.Forms.TextBox txtNomeEvento;
        private System.Windows.Forms.Label lblCache;
        private System.Windows.Forms.Label lblNomeEvento;
        private System.Windows.Forms.TextBox txtCache;
        private System.Windows.Forms.Label lblObservacoes;
        private System.Windows.Forms.Label lblLocal;
        private System.Windows.Forms.Label lblHora;
        private System.Windows.Forms.TextBox txtData;
        private System.Windows.Forms.Label lblData;
        private System.Windows.Forms.TextBox txtObservacoes;
        private System.Windows.Forms.TextBox txtLocal;
        private System.Windows.Forms.TextBox txtHora;
        private System.Windows.Forms.DataGridViewTextBoxColumn colID;
        private System.Windows.Forms.DataGridViewTextBoxColumn colNome;
        private System.Windows.Forms.DataGridViewTextBoxColumn colCategoria;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColFoto;
    }
}

