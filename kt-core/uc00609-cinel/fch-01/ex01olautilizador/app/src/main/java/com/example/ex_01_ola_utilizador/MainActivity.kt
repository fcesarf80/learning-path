package com.example.ex_01_ola_utilizador

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val etPrimeiroNome =
            findViewById<EditText>(R.id.etPrimeiroNome)

        val etUltimoNome =
            findViewById<EditText>(R.id.etUltimoNome)

        val btnSaudacao =
            findViewById<Button>(R.id.btnSaudacao)

        val tvResultado =
            findViewById<TextView>(R.id.tvResultado)

        btnSaudacao.setOnClickListener {

            val primeiroNome =
                etPrimeiroNome.text.toString().trim()

            val ultimoNome =
                etUltimoNome.text.toString().trim()

            if (primeiroNome.isEmpty()) {

                tvResultado.text =
                    "nome não inserido"

                Toast.makeText(
                    this,
                    "nome não inserido",
                    Toast.LENGTH_SHORT
                ).show()

            } else {

                val mensagem =
                    "Olá $primeiroNome $ultimoNome"

                tvResultado.text =
                    mensagem

                Toast.makeText(
                    this,
                    mensagem,
                    Toast.LENGTH_SHORT
                ).show()
            }
        }
    }
}