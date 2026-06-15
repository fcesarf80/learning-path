package com.example.ex_02_dados_pessoais

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

        val etAltura =
            findViewById<EditText>(R.id.etAltura)

        val btnRegistar =
            findViewById<Button>(R.id.btnRegistar)

        val tvResultado =
            findViewById<TextView>(R.id.tvResultado)

        val imgCapivara =
            findViewById<ImageView>(R.id.imgCapivara)

        btnRegistar.setOnClickListener {

            val nome = etNome.text.toString()
            val idade = etIdade.text.toString()
            val altura = etAltura.text.toString()

            tvResultado.text =
                "FICHA DO CANDIDATO\n\n" +
                        "Nome: $nome\n" +
                        "Idade: $idade anos\n" +
                        "Altura: $altura m"

            imgCapivara.setImageResource(
                R.drawable.capivara_rh02
            )
        }
    }
}