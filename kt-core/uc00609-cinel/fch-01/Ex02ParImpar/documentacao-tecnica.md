# Documentação Técnica - Ex02ParImpar

## Objetivo do Exercício

Criar uma aplicação Android que permita verificar se um número inteiro é par ou ímpar através de uma interface gráfica simples.

---

## Conceitos Aprendidos

### Activity

A classe MainActivity representa o ecrã principal da aplicação.

```kotlin
class MainActivity : AppCompatActivity()
```

Toda aplicação Android necessita de pelo menos uma Activity para apresentar conteúdo ao utilizador.

---

### Layout XML

A interface gráfica foi construída através do ficheiro:

```text
activity_main.xml
```

Foi utilizado um LinearLayout vertical contendo:

- EditText
- Button
- TextView

---

### EditText

Permite ao utilizador introduzir dados.

```xml
<EditText
    android:id="@+id/etNumero"/>
```

---

### Button

Executa uma ação quando é pressionado.

```xml
<Button
    android:id="@+id/btnVerificar"/>
```

---

### TextView

Apresenta informação no ecrã.

```xml
<TextView
    android:id="@+id/tvResultado"/>
```

---

## Ligação entre Kotlin e XML

Os componentes da interface são obtidos através de:

```kotlin
findViewById()
```

Exemplo:

```kotlin
val btnVerificar = findViewById<Button>(R.id.btnVerificar)
```

---

## Evento de Clique

Foi utilizado o método:

```kotlin
setOnClickListener
```

Exemplo:

```kotlin
btnVerificar.setOnClickListener {
}
```

Este bloco é executado quando o utilizador pressiona o botão.

---

## Conversão de Texto para Número

O valor introduzido no EditText é inicialmente uma String.

```kotlin
val numeroTexto = etNumero.text.toString()
```

Posteriormente é convertido para inteiro:

```kotlin
val numero = numeroTexto.toInt()
```

---

## Estrutura Condicional

Foi utilizada a instrução:

```kotlin
if
else
```

Exemplo:

```kotlin
if (numero % 2 == 0)
```

---

## Operador %

O operador % devolve o resto da divisão.

Exemplos:

```text
8 % 2 = 0
```

Resultado:

```text
PAR
```

```text
7 % 2 = 1
```

Resultado:

```text
ÍMPAR
```

---

## Problemas Encontrados

### 1. Projeto criado sem Activity

Foi necessário criar manualmente:

- MainActivity
- activity_main.xml
- registo da Activity no AndroidManifest.xml

---

### 2. Barra superior (ActionBar)

O tema inicial utilizava:

```xml
Theme.MaterialComponents.DayNight.DarkActionBar
```

A barra superior sobrepunha-se à interface.

Solução:

```xml
Theme.MaterialComponents.DayNight.NoActionBar
```

---

### 3. IDs removidos temporariamente

Durante os testes, os IDs dos componentes foram removidos do XML.

Consequência:

```text
Unresolved reference 'id'
```

Solução:

Restaurar os IDs originais:

- etNumero
- btnVerificar
- tvResultado

---

## Resultado Final

Aplicação funcional capaz de:

- receber um número;
- verificar se é par ou ímpar;
- apresentar o resultado no ecrã.

---

## Conhecimentos Consolidados

- Estrutura de um projeto Android.
- Activity.
- AndroidManifest.xml.
- Layout XML.
- EditText.
- Button.
- TextView.
- findViewById().
- setOnClickListener().
- if / else.
- Operador %.
- Conversão String → Int.
- Execução em emulador Android.
