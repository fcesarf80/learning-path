#pragma once

namespace projeto {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for frmproj
	/// </summary>
	public ref class frmproj : public System::Windows::Forms::Form
	{
	public:
		frmproj(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~frmproj()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Label^ label1;
	protected:
	private: System::Windows::Forms::Label^ label2;
	private: System::Windows::Forms::Label^ label3;
	private: System::Windows::Forms::Label^ label4;
	private: System::Windows::Forms::Label^ label5;
	private: System::Windows::Forms::TextBox^ txtCoeficienteA;
	private: System::Windows::Forms::TextBox^ txtCoeficienteB;
	private: System::Windows::Forms::TextBox^ txtCoeficienteC;
	private: System::Windows::Forms::TextBox^ txtRaiz1;

	private: System::Windows::Forms::TextBox^ txtRaiz2;
	private: System::Windows::Forms::Button^ btnCalcular;
	private: System::Windows::Forms::PictureBox^ pctJanela;





	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->label4 = (gcnew System::Windows::Forms::Label());
			this->label5 = (gcnew System::Windows::Forms::Label());
			this->txtCoeficienteA = (gcnew System::Windows::Forms::TextBox());
			this->txtCoeficienteB = (gcnew System::Windows::Forms::TextBox());
			this->txtCoeficienteC = (gcnew System::Windows::Forms::TextBox());
			this->txtRaiz1 = (gcnew System::Windows::Forms::TextBox());
			this->txtRaiz2 = (gcnew System::Windows::Forms::TextBox());
			this->btnCalcular = (gcnew System::Windows::Forms::Button());
			this->pctJanela = (gcnew System::Windows::Forms::PictureBox());
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pctJanela))->BeginInit();
			this->SuspendLayout();
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label1->Location = System::Drawing::Point(24, 24);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(132, 25);
			this->label1->TabIndex = 0;
			this->label1->Text = L"Coeficiente a:";
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label2->Location = System::Drawing::Point(24, 62);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(132, 25);
			this->label2->TabIndex = 1;
			this->label2->Text = L"Coeficiente b:";
			// 
			// label3
			// 
			this->label3->AutoSize = true;
			this->label3->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label3->Location = System::Drawing::Point(24, 96);
			this->label3->Name = L"label3";
			this->label3->Size = System::Drawing::Size(131, 25);
			this->label3->TabIndex = 2;
			this->label3->Text = L"Coeficiente c:";
			// 
			// label4
			// 
			this->label4->AutoSize = true;
			this->label4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label4->Location = System::Drawing::Point(24, 189);
			this->label4->Name = L"label4";
			this->label4->Size = System::Drawing::Size(72, 25);
			this->label4->TabIndex = 3;
			this->label4->Text = L"Raíz 1:";
			// 
			// label5
			// 
			this->label5->AutoSize = true;
			this->label5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label5->Location = System::Drawing::Point(24, 225);
			this->label5->Name = L"label5";
			this->label5->Size = System::Drawing::Size(72, 25);
			this->label5->TabIndex = 4;
			this->label5->Text = L"Raíz 2:";
			// 
			// txtCoeficienteA
			// 
			this->txtCoeficienteA->BorderStyle = System::Windows::Forms::BorderStyle::FixedSingle;
			this->txtCoeficienteA->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->txtCoeficienteA->Location = System::Drawing::Point(162, 28);
			this->txtCoeficienteA->Name = L"txtCoeficienteA";
			this->txtCoeficienteA->Size = System::Drawing::Size(101, 30);
			this->txtCoeficienteA->TabIndex = 5;
			this->txtCoeficienteA->TextChanged += gcnew System::EventHandler(this, &frmproj::txtCoeficienteA_TextChanged);
			// 
			// txtCoeficienteB
			// 
			this->txtCoeficienteB->BorderStyle = System::Windows::Forms::BorderStyle::FixedSingle;
			this->txtCoeficienteB->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->txtCoeficienteB->Location = System::Drawing::Point(162, 66);
			this->txtCoeficienteB->Name = L"txtCoeficienteB";
			this->txtCoeficienteB->Size = System::Drawing::Size(101, 30);
			this->txtCoeficienteB->TabIndex = 6;
			// 
			// txtCoeficienteC
			// 
			this->txtCoeficienteC->BorderStyle = System::Windows::Forms::BorderStyle::FixedSingle;
			this->txtCoeficienteC->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->txtCoeficienteC->Location = System::Drawing::Point(162, 100);
			this->txtCoeficienteC->Name = L"txtCoeficienteC";
			this->txtCoeficienteC->Size = System::Drawing::Size(101, 30);
			this->txtCoeficienteC->TabIndex = 7;
			// 
			// txtRaiz1
			// 
			this->txtRaiz1->BorderStyle = System::Windows::Forms::BorderStyle::FixedSingle;
			this->txtRaiz1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->txtRaiz1->Location = System::Drawing::Point(162, 189);
			this->txtRaiz1->Name = L"txtRaiz1";
			this->txtRaiz1->Size = System::Drawing::Size(101, 30);
			this->txtRaiz1->TabIndex = 8;
			// 
			// txtRaiz2
			// 
			this->txtRaiz2->BorderStyle = System::Windows::Forms::BorderStyle::FixedSingle;
			this->txtRaiz2->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->txtRaiz2->Location = System::Drawing::Point(162, 225);
			this->txtRaiz2->Name = L"txtRaiz2";
			this->txtRaiz2->Size = System::Drawing::Size(101, 30);
			this->txtRaiz2->TabIndex = 9;
			// 
			// btnCalcular
			// 
			this->btnCalcular->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->btnCalcular->Location = System::Drawing::Point(23, 130);
			this->btnCalcular->Name = L"btnCalcular";
			this->btnCalcular->Size = System::Drawing::Size(239, 50);
			this->btnCalcular->TabIndex = 10;
			this->btnCalcular->Text = L"Calcular\r\n";
			this->btnCalcular->UseVisualStyleBackColor = true;
			this->btnCalcular->Click += gcnew System::EventHandler(this, &frmproj::btnCalcular_Click);
			// 
			// pctJanela
			// 
			this->pctJanela->BackColor = System::Drawing::Color::White;
			this->pctJanela->BorderStyle = System::Windows::Forms::BorderStyle::FixedSingle;
			this->pctJanela->Location = System::Drawing::Point(292, 29);
			this->pctJanela->Name = L"pctJanela";
			this->pctJanela->Size = System::Drawing::Size(409, 411);
			this->pctJanela->TabIndex = 11;
			this->pctJanela->TabStop = false;
			// 
			// frmproj
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(848, 452);
			this->Controls->Add(this->pctJanela);
			this->Controls->Add(this->btnCalcular);
			this->Controls->Add(this->txtRaiz2);
			this->Controls->Add(this->txtRaiz1);
			this->Controls->Add(this->txtCoeficienteC);
			this->Controls->Add(this->txtCoeficienteB);
			this->Controls->Add(this->txtCoeficienteA);
			this->Controls->Add(this->label5);
			this->Controls->Add(this->label4);
			this->Controls->Add(this->label3);
			this->Controls->Add(this->label2);
			this->Controls->Add(this->label1);
			this->Name = L"frmproj";
			this->Text = L"Polinómio do 2º Grau";
			this->Load += gcnew System::EventHandler(this, &frmproj::frmproj_Load);
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pctJanela))->EndInit();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void frmproj_Load(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void btnCalcular_Click(System::Object^ sender, System::EventArgs^ e) {
		double a, b, c;

		if (!Double::TryParse(txtCoeficienteA->Text, a)) {
			MessageBox::Show("Digite um valor válido para o coeficiente a.");
			return;
		}

		if (!Double::TryParse(txtCoeficienteB->Text, b)) {
			MessageBox::Show("Digite um valor válido para o coeficiente b.");
			return;
		}

		if (!Double::TryParse(txtCoeficienteC->Text, c)) {
			MessageBox::Show("Digite um valor válido para o coeficiente c.");
			return;
		}

		if (a == 0) {
			MessageBox::Show("O coeficiente 'a' deve ser diferente de zero.");
			return;
		}

		double delta = (b * b) - (4 * a * c);

		if (delta < 0) {
			MessageBox::Show("Não existe raiz real!");
			txtRaiz1->Text = "";
			txtRaiz2->Text = "";
		}
		else {
			double raiz1 = (-b + Math::Sqrt(delta)) / (2 * a);
			double raiz2 = (-b - Math::Sqrt(delta)) / (2 * a);

			txtRaiz1->Text = String::Format("{0:n2}", raiz1);
			txtRaiz2->Text = String::Format("{0:n2}", raiz2);
		}

		double xCentro = pctJanela->Width / 2.0;
		double yCentro = pctJanela->Height / 2.0;
		double escalaX = pctJanela->Width / 20.0;
		double escalaY = pctJanela->Height / 20.0;

		Bitmap^ imagem = gcnew Bitmap(pctJanela->Width, pctJanela->Height);
		Graphics^ g = Graphics::FromImage(imagem);

		g->Clear(Color::White);

		Pen^ eixo = gcnew Pen(Color::Blue, 1.0f);
		Pen^ curva = gcnew Pen(Color::Red, 1.0f);

		// Eixo X
		g->DrawLine(eixo,
			0.0f, (float)yCentro,
			(float)pctJanela->Width, (float)yCentro);

		// Eixo Y
		g->DrawLine(eixo,
			(float)xCentro, 0.0f,
			(float)xCentro, (float)pctJanela->Height);

		for (double i = -10.0; i <= 10.0; i += 0.002) {
			double valorX = i;
			double valorY = a * valorX * valorX + b * valorX + c;

			float xTela = (float)(xCentro + valorX * escalaX);
			float yTela = (float)(yCentro - valorY * escalaY);

			g->DrawLine(curva, xTela, yTela, xTela + 1.0f, yTela);
		}

		pctJanela->Image = imagem;
	}
private: System::Void txtCoeficienteA_TextChanged(System::Object^ sender, System::EventArgs^ e) {
}
};
}
