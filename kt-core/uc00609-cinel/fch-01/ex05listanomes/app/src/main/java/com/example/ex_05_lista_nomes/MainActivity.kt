package com.example.ex_05_lista_nomes

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private val nomes = mutableListOf<String>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        //enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val etNome =
            findViewById<EditText>(R.id.etNome)

        val btnAdicionar =
            findViewById<Button>(R.id.btnAdicionar)

        val tvLista =
            findViewById<TextView>(R.id.tvLista)
        val imgCapivaras =
            findViewById<ImageView>(R.id.imgCapivaras)

        btnAdicionar.setOnClickListener {

            val nome =
                etNome.text.toString().trim()

            if (nome.isNotEmpty()) {

                nomes.add(nome)

                when (nomes.size) {

                    1 -> {
                        imgCapivaras.setImageResource(
                            R.drawable.capivara_adepta
                        )

                        imgCapivaras.translationY = 125f
                    }

                    2 -> {
                        imgCapivaras.setImageResource(
                            R.drawable.duas_capivaras_adeptas
                        )

                        imgCapivaras.translationY = 115f

                        imgCapivaras.scaleX = 1.3f
                        imgCapivaras.scaleY = 1.3f
                    }

                    else -> {
                        imgCapivaras.setImageResource(
                            R.drawable.grupo_capivaras_adeptos
                        )

                        imgCapivaras.translationY = -230f

                        imgCapivaras.scaleX = 1.7f
                        imgCapivaras.scaleY = 1.7f
                    }
                }

                tvLista.text =
                    nomes.joinToString("\n")

                etNome.text.clear()
            }
        }
    }
}