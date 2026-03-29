<?php
$a = $_POST['a'];
$b = $_POST['b'];
$c = $_POST['c'];

$delta = ($b ** 2) - (4 * $a * $c);

echo "<h2>Resultado:</h2>";

if ($delta < 0) {
    echo "Delta é $delta. A equação não possui raízes reais.";
} else {
    $x1 = (-$b + sqrt($delta)) / (2 * $a);
    $x2 = (-$b - sqrt($delta)) / (2 * $a);

    echo "Delta: $delta <br>";
    echo "Raiz x1: " . round($x1, 2) . "<br>";
    echo "Raiz x2: " . round($x2, 2) . "<br>";
}

echo "<br><a href='index.php'>Voltar</a>";
?>
