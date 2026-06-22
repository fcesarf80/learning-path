package com.example.ex_05_lista_nomes

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    private val nomes = mutableListOf<String>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        enableEdgeToEdge()

        setContentView(R.layout.activity_main)

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->

            val systemBars =
                insets.getInsets(WindowInsetsCompat.Type.systemBars())

            v.setPadding(
                systemBars.left,
                systemBars.top,
                systemBars.right,
                systemBars.bottom
            )

            insets
        }

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

                        imgCapivaras.translationY = -520f
                    }

                    2 -> {
                        imgCapivaras.setImageResource(
                            R.drawable.duas_capivaras_adeptas
                        )

                        imgCapivaras.translationY = -650f

                        imgCapivaras.scaleX = 1.3f
                        imgCapivaras.scaleY = 1.3f
                    }

                    else -> {
                        imgCapivaras.setImageResource(
                            R.drawable.grupo_capivaras_adeptos
                        )

                        imgCapivaras.translationY = -780f

                        imgCapivaras.scaleX = 1.60f
                        imgCapivaras.scaleY = 1.60f
                    }
                }

                tvLista.text =
                    nomes.joinToString("\n")

                etNome.text.clear()
            }
        }
    }
}