package com.example.ex02parimpar

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)

        val etNumero = findViewById<EditText>(R.id.etNumero)
        val btnVerificar = findViewById<Button>(R.id.btnVerificar)
        val tvResultado = findViewById<TextView>(R.id.tvResultado)

        btnVerificar.setOnClickListener {

            val numeroTexto = etNumero.text.toString()

            if (numeroTexto.isNotEmpty()) {

                val numero = numeroTexto.toInt()

                if (numero % 2 == 0) {
                    tvResultado.text = "O número $numero é PAR"
                } else {
                    tvResultado.text = "O número $numero é ÍMPAR"
                }

            } else {
                tvResultado.text = "Digite um número"
            }
        }
    }
}