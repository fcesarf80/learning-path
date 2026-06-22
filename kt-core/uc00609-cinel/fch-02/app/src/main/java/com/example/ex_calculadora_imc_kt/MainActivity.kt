package com.example.ex_calculadora_imc_kt

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // 1. Ligar as variáveis do Kotlin com os componentes visuais do XML
        val etPeso = findViewById<EditText>(R.id.etPeso)
        val etAltura = findViewById<EditText>(R.id.etAltura)
        val btnCalcular = findViewById<Button>(R.id.btnCalcular)
        val btnLimpar = findViewById<Button>(R.id.btnLimpar)
        val tvResultado = findViewById<TextView>(R.id.tvResultado)
        val ivStatus = findViewById<ImageView>(R.id.ivStatus)

        // 2. Configurar a ação do botão Calcular
        btnCalcular.setOnClickListener {
            val pesoTexto = etPeso.text.toString()
            val alturaTexto = etAltura.text.toString()

            // Validação de segurança obrigatória
            if (pesoTexto.isEmpty() || alturaTexto.isEmpty()) {
                Toast.makeText(this, "Por favor, preencha todos os campos!", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            val peso = pesoTexto.toDoubleOrNull() ?: 0.0
            val altura = alturaTexto.toDoubleOrNull() ?: 0.0

            if (peso <= 0 || altura <= 0) {
                Toast.makeText(this, "Insira valores válidos e maiores que zero!", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            // Cálculo do IMC
            val imc = peso / (altura * altura)

            // Formatar para mostrar apenas 2 casas decimais
            val imcFormatado = String.format("%.2f", imc)

            // Classificação da OMS usando a estrutura condicional 'when'
            val classificacao: String
            val imagemRes: Int

            when {
                imc < 18.5 -> {
                    classificacao = "Magreza"
                    imagemRes = R.drawable.ic_magreza
                }
                imc in 18.5..24.99 -> {
                    classificacao = "Normal"
                    imagemRes = R.drawable.ic_normal
                }
                imc in 25.0..29.99 -> {
                    classificacao = "Sobrepeso"
                    imagemRes = R.drawable.ic_sobrepeso
                }
                imc in 30.0..39.99 -> {
                    classificacao = "Obesidade"
                    imagemRes = R.drawable.ic_obesidade
                }
                else -> {
                    classificacao = "Obesidade grave"
                    imagemRes = R.drawable.ic_obesidade_grave
                }
            }

            // Exibir o resultado final na tela
            tvResultado.text = "Seu IMC é: $imcFormatado\nClassificação: $classificacao"
            ivStatus.setImageResource(imagemRes)
        }

        // 3. Configurar a ação do botão Limpar
        btnLimpar.setOnClickListener {
            etPeso.text.clear()
            etAltura.text.clear()
            tvResultado.text = ""
            ivStatus.setImageDrawable(null) // Remove a imagem atual
        }
    }
}
