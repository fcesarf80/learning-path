package com.example.ex_04_numeros_pares

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)

        val btnMissao =
            findViewById<Button>(R.id.btnMissao)

        val tvResultado =
            findViewById<TextView>(R.id.tvResultado)

        val imgCarimbo =
            findViewById<ImageView>(R.id.imgCarimbo)

        btnMissao.setOnClickListener {

            var resultado =
                "MISSÃO CONCLUÍDA\n\n"

            for (numero in 1..20) {

                if (numero % 2 == 0) {

                    resultado += "$numero\n"
                }
            }

            tvResultado.text = resultado

            imgCarimbo.visibility = View.VISIBLE
        }
    }
}