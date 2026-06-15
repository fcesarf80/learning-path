package com.example.ex_03_maioridade

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)

        val etNome =
            findViewById<EditText>(R.id.etNome)

        val etIdade =
            findViewById<EditText>(R.id.etIdade)

        val btnVerificar =
            findViewById<Button>(R.id.btnVerificar)

        val tvResultado =
            findViewById<TextView>(R.id.tvResultado)

        val imgSeguranca =
            findViewById<ImageView>(R.id.imgSeguranca)

        btnVerificar.setOnClickListener {

            val nome =
                etNome.text.toString()

            val idadeTexto =
                etIdade.text.toString()

            if (idadeTexto.isNotEmpty()) {

                val idade =
                    idadeTexto.toInt()

                if (idade >= 18) {

                    imgSeguranca.setImageResource(
                        R.drawable.capivara_seguranca02
                    )

                    tvResultado.text =
                        "✅ ACESSO AUTORIZADO\n\n" +
                                "Nome: $nome\n" +
                                "Idade: $idade anos"

                } else {

                    imgSeguranca.setImageResource(
                        R.drawable.capivara_seguranca03
                    )

                    tvResultado.text =
                        "❌ ACESSO NEGADO\n\n" +
                                "Nome: $nome\n" +
                                "Idade: $idade anos"
                }
            }
        }
    }
}