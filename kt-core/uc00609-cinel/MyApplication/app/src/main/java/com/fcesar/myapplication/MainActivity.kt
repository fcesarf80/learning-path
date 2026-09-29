<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
android:id="@+id/main"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical"
android:gravity="center"
android:padding="32dp">

<!-- Título -->
<TextView
android:id="@+id/txtTitulo"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Bem-vindo!"
android:textSize="30sp"
android:textStyle="bold"
android:layout_marginBottom="8dp" />

<!-- Subtítulo -->
<TextView
android:id="@+id/txtSubtitulo"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Inicia sessão na tua conta"
android:textSize="16sp"
android:layout_marginBottom="32dp" />

<!-- Email -->
<EditText
android:id="@+id/edtEmail"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:hint="Email"
android:inputType="textEmailAddress"
android:padding="14dp"
android:layout_marginBottom="16dp" />

<!-- Palavra-passe -->
<EditText
android:id="@+id/edtPassword"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:hint="Palavra-passe"
android:inputType="textPassword"
android:padding="14dp"
android:layout_marginBottom="24dp" />

<!-- Botão Entrar -->
<Button
android:id="@+id/btnLogin"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="ENTRAR"
android:textSize="16sp"
android:layout_marginBottom="24dp" />

<Button
android:id="@+id/btnRecuperarPassword"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Esqueci-me da palavra-passe"
android:textSize="14sp"
android:layout_marginBottom="16dp" />

<!-- Separador -->
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Ainda não tens conta?"
android:textSize="15sp" />



<!-- Botão Registar -->
<Button
android:id="@+id/btnRegisto"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="REGISTAR"
android:textSize="15sp" />

</LinearLayout>

