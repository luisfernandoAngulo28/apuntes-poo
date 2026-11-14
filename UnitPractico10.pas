unit UnitPractico10;
{==============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE INGENIERÍA EN CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES
  INTRODUCCIÓN A LA INFORMÁTICA (INF110 - GRUPO Z2)
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
  
  PRÁCTICO # 10 : MÓDULOS DE SUMATORIAS DE SERIES (20 EJERCICIOS)
  FECHA LÍMITE DE PRESENTACIÓN: Jueves 05/11/2026 23:59
  
  METODOLOGÍA OFICIAL DE CÁTEDRA:
  - Formato de Función: function Nombre(numero, contador: Integer): Tipo;
  - Inicialización: sumador := 0; contador := 1;
  - Bucle canónico: while numero >= contador do
  - Avance: contador := contador + 1;
  - Retorno: Result := sumador;
==============================================================================}

{$mode objfpc}{$H+}

interface

uses
  SysUtils;

// --- FUNCIONES OFICIALES DE CLASE (FOTO DE PIZARRA) ---
function sumaDoble(numero, contador: Integer): Integer;
function sumafactorial(numero, contador: Integer): Integer;
function sumaCuadratica(numero, contador: Integer): Integer;
function sumaParImpar(numero, contador: Integer): Integer;

// --- PRÁCTICO # 10: 20 SERIES OFICIALES ---
// 1. SF = 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + ... (Fibonacci desde 0)
function Serie01_Fibonacci(numero, contador: Integer): Int64;

// 2. SF = 1 + 2 + 6 + 120 + 720 + 8 + 16 + 32 + 64 + 120 (Serie Mixta)
function Serie02_FactorialPotencias(numero, contador: Integer): Int64;

// 3. SF = 1 + 5 + 4 + 10 + 9 + 15 + 16 + 20 + 25 + 25 + ... (Entrelazada: k^2 y 5*k)
function Serie03_CuadradosMultiplos5(numero, contador: Integer): Int64;

// 4. SF = 3 + 6 + 12 + 24 + 48 + 96 + 192 + 384 + ... (Prog. Geométrica base 3)
function Serie04_DobleBase3(numero, contador: Integer): Int64;

// 5. SF = 3 + 9 + 13 + 39 + 43 + 129 + 133 + ... (Operaciones alternas: x3, +4)
function Serie05_Por3Mas4(numero, contador: Integer): Int64;

// 6. F = 3 + 6 + 12 + 24 + 48 + ... + n (Suma de términos base 3)
function Serie06_GeometricaBase3(numero, contador: Integer): Int64;

// 7. F = 1 + 4 + 5 + 9 + 14 + 23 + ... (Aditiva semillas 1 y 4)
function Serie07_Aditiva1_4(numero, contador: Integer): Int64;

// 8. F = 1 + 4 + 9 + 16 + 25 + ... (Cuadrados consecutivos i^2)
function Serie08_Cuadrados(numero, contador: Integer): Int64;

// 9. F = 1x2 + 3x4 + 5x6 + ... (Producto de pares consecutivos)
function Serie09_ProductoImparPar(numero, contador: Integer): Int64;

// 10. F = 1 + 2 - 3 + 4 - 5 + 6 - 7 + ... (Signos alternos para i >= 3)
function Serie10_SignosAlternos(numero, contador: Integer): Int64;

// 11. F = 1x1 + 2x3 + 3x4 + 4x7 + 5x11 ... (i * Sucesión Lucas 1,3,4,7,11)
function Serie11_ProductoIndiceLucas(numero, contador: Integer): Int64;

// 12. F = 1/2 + 3/4 + 5/6 + 7/8 + ... (Fraccionaria: (2i-1)/(2i))
function Serie12_FraccionImparPar(numero, contador: Integer): Double;

// 13. F = 1^2 + 3^2 + 5^2 + 7^2 + ... (Cuadrados de números impares)
function Serie13_CuadradosImpares(numero, contador: Integer): Int64;

// 14. F = x/1! + x^3/2! + x^5/3! + ... (Potencias impares de x entre factoriales)
function Serie14_PotenciasXFactorial(x: Double; numero, contador: Integer): Double;

// 15. F = 1 + 1 + 2 + 2 + 4 + 4 + 8 + 8 + ... + 100 (Potencias de 2 duplicadas)
function Serie15_Potencias2Duplicadas(numero, contador: Integer): Int64;

// 16. F = 1*3 + 3*5 + 5*7 + 7*9 + 9*11 + ... (Producto impares consecutivos)
function Serie16_ProductoImparesConsecutivos(numero, contador: Integer): Int64;

// 17. F = 11 + 22 + 33 + 44 + ... + nn (Múltiplos de 11)
function Serie17_Multiplos11(numero, contador: Integer): Int64;

// 18. F = 3x1 + 5x2 + 7x6 + 9x24 + ... ((2i+1) * i!)
function Serie18_ImparPorFactorial(numero, contador: Integer): Int64;

// 19. S = 6 + 12 + 24 + 48 + 96 + ... + n (Prog. Geométrica base 6)
function Serie19_GeometricaBase6(numero, contador: Integer): Int64;

// 20. SF = 1/2 + 2/6 + 6/10 + 24/14 + 120/18 + ... (i! / (4i-2))
function Serie20_FactorialEntreProgresion(numero, contador: Integer): Double;

implementation

// =============================================================================
// FUNCIONES OFICIALES DE CLASE (DOCENTE ING. ANGÉLICA GARZÓN)
// =============================================================================

function sumaDoble(numero, contador: Integer): Integer;
var doble, sumadordoble: Integer;
begin
  sumadordoble := 0; contador := 1; doble := 1;
  while numero >= contador do
  begin
    sumadordoble := sumadordoble + doble;
    doble := doble * 2;
    contador := contador + 1;
  end;
  Result := sumadordoble;
end;

function sumafactorial(numero, contador: Integer): Integer;
var factorial, sumadorfactorial: Integer;
begin
  sumadorfactorial := 0; contador := 1; factorial := 1;
  while numero >= contador do
  begin
    factorial := factorial * contador;
    sumadorfactorial := sumadorfactorial + factorial;
    contador := contador + 1;
  end;
  Result := sumadorfactorial;
end;

function sumaCuadratica(numero, contador: Integer): Integer;
var cuadratica, sumadorCuadratica: Integer;
begin
  sumadorCuadratica := 0; contador := 1; cuadratica := 1;
  while numero >= contador do
  begin
    cuadratica := contador * contador;
    sumadorCuadratica := sumadorCuadratica + cuadratica;
    contador := contador + 1;
  end;
  Result := sumadorCuadratica;
end;

function sumaParImpar(numero, contador: Integer): Integer;
var Par, Impar, sumadorParImpar: Integer;
begin
  sumadorParImpar := 0; contador := 1; Par := 20; Impar := 1;
  while numero >= contador do
  begin
    Par := Par - 2;
    Impar := Impar + 2;
    sumadorParImpar := sumadorParImpar + Par;
    contador := contador + 1;
  end;
  Result := sumadorParImpar;
end;

// =============================================================================
// PRÁCTICO # 10 : 20 SERIES OFICIALES
// =============================================================================

// 1. Fibonacci
function Serie01_Fibonacci(numero, contador: Integer): Int64;
var a, b, aux, sumadorFibonacci: Int64;
begin
  sumadorFibonacci := 0; contador := 1; a := 0; b := 1;
  while numero >= contador do
  begin
    sumadorFibonacci := sumadorFibonacci + a;
    aux := a + b;
    a := b;
    b := aux;
    contador := contador + 1;
  end;
  Result := sumadorFibonacci;
end;

// 2. Mixta Factorial y Potencias
function Serie02_FactorialPotencias(numero, contador: Integer): Int64;
const VALORES: array[1..10] of Int64 = (1, 2, 6, 120, 720, 8, 16, 32, 64, 120);
var sumadorMixta, pot: Int64;
begin
  sumadorMixta := 0; contador := 1; pot := 128;
  while numero >= contador do
  begin
    if contador <= 10 then
      sumadorMixta := sumadorMixta + VALORES[contador]
    else
    begin
      sumadorMixta := sumadorMixta + pot;
      pot := pot * 2;
    end;
    contador := contador + 1;
  end;
  Result := sumadorMixta;
end;

// 3. Entrelazada Cuadrados e Impares x 5
function Serie03_CuadradosMultiplos5(numero, contador: Integer): Int64;
var termino, kImpar, kPar, sumadorEntrelazada: Int64;
begin
  sumadorEntrelazada := 0; contador := 1; kImpar := 1; kPar := 1;
  while numero >= contador do
  begin
    if (contador mod 2 <> 0) then
    begin
      termino := kImpar * kImpar;
      kImpar := kImpar + 1;
    end
    else
    begin
      termino := 5 * kPar;
      kPar := kPar + 1;
    end;
    sumadorEntrelazada := sumadorEntrelazada + termino;
    contador := contador + 1;
  end;
  Result := sumadorEntrelazada;
end;

// 4. Doble Base 3
function Serie04_DobleBase3(numero, contador: Integer): Int64;
var termino, sumadorDoble3: Int64;
begin
  sumadorDoble3 := 0; contador := 1; termino := 3;
  while numero >= contador do
  begin
    sumadorDoble3 := sumadorDoble3 + termino;
    termino := termino * 2;
    contador := contador + 1;
  end;
  Result := sumadorDoble3;
end;

// 5. x3, +4
function Serie05_Por3Mas4(numero, contador: Integer): Int64;
var termino, sumadorPor3Mas4: Int64;
begin
  sumadorPor3Mas4 := 0; contador := 1; termino := 3;
  while numero >= contador do
  begin
    sumadorPor3Mas4 := sumadorPor3Mas4 + termino;
    if (contador mod 2 <> 0) then
      termino := termino * 3
    else
      termino := termino + 4;
    contador := contador + 1;
  end;
  Result := sumadorPor3Mas4;
end;

// 6. Geométrica base 3
function Serie06_GeometricaBase3(numero, contador: Integer): Int64;
var termino, sumadorBase3: Int64;
begin
  sumadorBase3 := 0; contador := 1; termino := 3;
  while numero >= contador do
  begin
    sumadorBase3 := sumadorBase3 + termino;
    termino := termino * 2;
    contador := contador + 1;
  end;
  Result := sumadorBase3;
end;

// 7. Aditiva 1 y 4
function Serie07_Aditiva1_4(numero, contador: Integer): Int64;
var a, b, aux, sumadorAditiva: Int64;
begin
  sumadorAditiva := 0; contador := 1; a := 1; b := 4;
  while numero >= contador do
  begin
    sumadorAditiva := sumadorAditiva + a;
    aux := a + b;
    a := b;
    b := aux;
    contador := contador + 1;
  end;
  Result := sumadorAditiva;
end;

// 8. Cuadrados
function Serie08_Cuadrados(numero, contador: Integer): Int64;
var cuadratica, sumadorCuadratica: Int64;
begin
  sumadorCuadratica := 0; contador := 1; cuadratica := 1;
  while numero >= contador do
  begin
    cuadratica := contador * contador;
    sumadorCuadratica := sumadorCuadratica + cuadratica;
    contador := contador + 1;
  end;
  Result := sumadorCuadratica;
end;

// 9. Impar x Par
function Serie09_ProductoImparPar(numero, contador: Integer): Int64;
var imp, par, producto, sumadorProd: Int64;
begin
  sumadorProd := 0; contador := 1;
  while numero >= contador do
  begin
    imp := 2 * contador - 1;
    par := 2 * contador;
    producto := imp * par;
    sumadorProd := sumadorProd + producto;
    contador := contador + 1;
  end;
  Result := sumadorProd;
end;

// 10. Signos Alternos
function Serie10_SignosAlternos(numero, contador: Integer): Int64;
var sumadorAlterno: Int64;
begin
  sumadorAlterno := 0; contador := 1;
  while numero >= contador do
  begin
    if contador = 1 then
      sumadorAlterno := sumadorAlterno + 1
    else if (contador mod 2 = 0) then
      sumadorAlterno := sumadorAlterno + contador
    else
      sumadorAlterno := sumadorAlterno - contador;
    contador := contador + 1;
  end;
  Result := sumadorAlterno;
end;

// 11. Lucas x Contador
function Serie11_ProductoIndiceLucas(numero, contador: Integer): Int64;
var l1, l2, aux, termino, sumadorLucas: Int64;
begin
  sumadorLucas := 0; contador := 1; l1 := 1; l2 := 3;
  while numero >= contador do
  begin
    termino := contador * l1;
    sumadorLucas := sumadorLucas + termino;
    aux := l1 + l2;
    l1 := l2;
    l2 := aux;
    contador := contador + 1;
  end;
  Result := sumadorLucas;
end;

// 12. Fracciones
function Serie12_FraccionImparPar(numero, contador: Integer): Double;
var num, den, sumadorFraccion: Double;
begin
  sumadorFraccion := 0.0; contador := 1;
  while numero >= contador do
  begin
    num := 2 * contador - 1;
    den := 2 * contador;
    sumadorFraccion := sumadorFraccion + (num / den);
    contador := contador + 1;
  end;
  Result := sumadorFraccion;
end;

// 13. Cuadrados Impares
function Serie13_CuadradosImpares(numero, contador: Integer): Int64;
var impar, termino, sumadorCuadImp: Int64;
begin
  sumadorCuadImp := 0; contador := 1;
  while numero >= contador do
  begin
    impar := 2 * contador - 1;
    termino := impar * impar;
    sumadorCuadImp := sumadorCuadImp + termino;
    contador := contador + 1;
  end;
  Result := sumadorCuadImp;
end;

// 14. x / Factorial
function Serie14_PotenciasXFactorial(x: Double; numero, contador: Integer): Double;
var fact, potX, sumadorPotFact: Double; k, expImpar: Integer;
begin
  sumadorPotFact := 0.0; contador := 1; fact := 1.0;
  while numero >= contador do
  begin
    fact := fact * contador;
    expImpar := 2 * contador - 1;
    potX := 1.0;
    for k := 1 to expImpar do
      potX := potX * x;
    sumadorPotFact := sumadorPotFact + (potX / fact);
    contador := contador + 1;
  end;
  Result := sumadorPotFact;
end;

// 15. Potencias de 2 duplicadas
function Serie15_Potencias2Duplicadas(numero, contador: Integer): Int64;
var valor, sumadorDuplicadas: Int64;
begin
  sumadorDuplicadas := 0; contador := 1; valor := 1;
  while numero >= contador do
  begin
    sumadorDuplicadas := sumadorDuplicadas + valor;
    if (contador mod 2 = 0) then
      valor := valor * 2;
    contador := contador + 1;
  end;
  Result := sumadorDuplicadas;
end;

// 16. Impares Consecutivos
function Serie16_ProductoImparesConsecutivos(numero, contador: Integer): Int64;
var a, b, producto, sumadorImpares: Int64;
begin
  sumadorImpares := 0; contador := 1;
  while numero >= contador do
  begin
    a := 2 * contador - 1;
    b := 2 * contador + 1;
    producto := a * b;
    sumadorImpares := sumadorImpares + producto;
    contador := contador + 1;
  end;
  Result := sumadorImpares;
end;

// 17. Múltiplos 11
function Serie17_Multiplos11(numero, contador: Integer): Int64;
var termino, sumador11: Int64;
begin
  sumador11 := 0; contador := 1;
  while numero >= contador do
  begin
    termino := 11 * contador;
    sumador11 := sumador11 + termino;
    contador := contador + 1;
  end;
  Result := sumador11;
end;

// 18. (2i+1) * i!
function Serie18_ImparPorFactorial(numero, contador: Integer): Int64;
var fact, imp, termino, sumadorImpFact: Int64;
begin
  sumadorImpFact := 0; contador := 1; fact := 1;
  while numero >= contador do
  begin
    fact := fact * contador;
    imp := 2 * contador + 1;
    termino := imp * fact;
    sumadorImpFact := sumadorImpFact + termino;
    contador := contador + 1;
  end;
  Result := sumadorImpFact;
end;

// 19. Geométrica base 6
function Serie19_GeometricaBase6(numero, contador: Integer): Int64;
var termino, sumadorBase6: Int64;
begin
  sumadorBase6 := 0; contador := 1; termino := 6;
  while numero >= contador do
  begin
    sumadorBase6 := sumadorBase6 + termino;
    termino := termino * 2;
    contador := contador + 1;
  end;
  Result := sumadorBase6;
end;

// 20. Factorial / (4i-2)
function Serie20_FactorialEntreProgresion(numero, contador: Integer): Double;
var fact, den, sumadorFracFact: Double;
begin
  sumadorFracFact := 0.0; contador := 1; fact := 1.0;
  while numero >= contador do
  begin
    fact := fact * contador;
    den := 4 * contador - 2;
    sumadorFracFact := sumadorFracFact + (fact / den);
    contador := contador + 1;
  end;
  Result := sumadorFracFact;
end;

end.
