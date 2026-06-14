package com.example.ex01olautilizador

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(
                systemBars.left,
                systemBars.top,
                systemBars.right,
                systemBars.bottom
            )
            insets
        }

        val etPrimeiroNome =
            findViewById<EditText>(R.id.etPrimeiroNome)

        val etUltimoNome =
            findViewById<EditText>(R.id.etUltimoNome)

        val btnSaudacao =
            findViewById<Button>(R.id.btnSaudacao)

        val tvResultado =
            findViewById<TextView>(R.id.tvResultado)

        val imgCapivara =
            findViewById<ImageView>(R.id.imgCapivara)

        btnSaudacao.setOnClickListener {

            val primeiroNome =
                etPrimeiroNome.text.toString().trim()

            val ultimoNome =
                etUltimoNome.text.toString().trim()

            if (primeiroNome.isEmpty()) {

                imgCapivara.setImageResource(
                    R.drawable.capiv1
                )

                tvResultado.text = "nome não inserido"

                Toast.makeText(
                    this,
                    "nome não inserido",
                    Toast.LENGTH_SHORT
                ).show()

            } else {

                imgCapivara.setImageResource(
                    R.drawable.capiv2
                )

                val mensagem =
                    "Olá $primeiroNome $ultimoNome"

                tvResultado.text = mensagem

                Toast.makeText(
                    this,
                    mensagem,
                    Toast.LENGTH_SHORT
                ).show()
            }
        }
    }
}