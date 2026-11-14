{$mode delphi}
unit UAtajosExamen;

interface

uses
  SysUtils;

// =============================================================================
// BLOQUE 1: FUNCIONES ATÓMICAS PARA SERIES (DIVIDE Y VENCERÁS)
// =============================================================================

// 1. Factorial de un número k! = 1 * 2 * 3 * ... * k
function Factorial(k: Integer): Double;

// 2. Potencia base^exponente (k^k o x^k)
function Potencia(base: Double; exponente: Integer): Double;

// 3. k-ésimo término de Fibonacci (1, 1, 2, 3, 5, 8, 13...)
function Fibonacci(k: Integer): Cardinal;

// 4. Potencia de 2 (2^k = 2, 4, 8, 16, 32...)
function DoblePotencia2(k: Integer): Cardinal;

// 5. k-ésimo número impar (1, 3, 5, 7, 9...) -> 2*k - 1
function N_EsimoImpar(k: Integer): Integer;

// 6. k-ésimo cuadrado perfecto (1, 4, 9, 16, 25...) -> k * k
function Cuadrado(k: Integer): Integer;

// 7. Múltiplo de 5 (5, 10, 15, 20, 25...) -> k * 5
function Multiplo5(k: Integer): Integer;

// 8. Signo alternado: +1 en impares, -1 en pares (o viceversa)
function SignoAlternado(k: Integer): Integer;

// =============================================================================
// BLOQUE 2: SERIES COMPUESTAS DE EXAMEN (CONQUER / VENCERÁS)
// =============================================================================

// Serie 1: Factorial / Doble = 1/2 + 2/4 + 6/8 + 24/16 + 120/32 + ...
function SumaFactorialDoble(n: Integer): Double;

// Serie 2: Cuadrado / Fibonacci = 3/1 + 6/1 + 12/2 + 24/3 + 48/5 + ...
function SumaCuadradoFibonacci(n: Integer): Double;

// Serie 3: Potencia / Múltiplo de 5 = 1^1/5 + 2^2/10 + 3^3/15 + 4^4/20 + ...
function SumaPotenciaMultiplo5(n: Integer): Double;

// Serie 4: Impares / Cuadrados con signo = 1/1 - 3/4 + 5/9 - 7/16 + 9/25 - ...
function SumaImparesCuadrados(n: Integer): Double;

// Serie 5: Sumatoria de Dobles sucesivos = 1 + 2 + 4 + 8 + 16 + ...
function SumaDobleSimple(n: Integer): Int64;

// Serie 6: Sumatoria de Factoriales = 1! + 2! + 3! + ... + n!
function SumaFactorialSimple(n: Integer): Int64;

// Serie 7: Sumatoria de Cuadrados = 1^2 + 2^2 + 3^2 + ... + n^2
function SumaCuadraticaSimple(n: Integer): Int64;

// =============================================================================
// BLOQUE 3: FUNCIONES ATÓMICAS PARA DÍGITOS Y NÚMEROS (POO / MODULAR)
// =============================================================================

// Contar cantidad total de dígitos de un número
function ContarDigitos(numero: Cardinal): Integer;

// Invertir un número entero (ej: 12345 -> 54321)
function InvertirNumero(numero: Cardinal): Cardinal;

// Sumar los dígitos de un número (ej: 15378 -> 24)
function SumarDigitos(numero: Cardinal): Cardinal;

// Raíz digital: sumar dígitos repetidamente hasta < 10 (ej: 15378 -> 24 -> 6)
function RaizDigital(numero: Cardinal): Byte;

// Verificar si un dígito d (0..9) es primo: d in [2, 3, 5, 7]
function EsDigitoPrimo(digito: Byte): Boolean;

// Extraer el primer dígito (más significativo)
function PrimerDigito(numero: Cardinal): Byte;

// Extraer el último dígito (menos significativo)
function UltimoDigito(numero: Cardinal): Byte;

// Verificar si un número es capicúa
function EsCapicua(numero: Cardinal): Boolean;

// Extraer la mitad izquierda de un número
function ExtraerMitadIzquierda(numero: Cardinal): Cardinal;

// Extraer la mitad derecha de un número
function ExtraerMitadDerecha(numero: Cardinal): Cardinal;

// =============================================================================
// BLOQUE 4: FUNCIONES ATÓMICAS PARA CADENAS DE CARACTERES (STRINGS)
// =============================================================================

// Contar cantidad de palabras separadas por espacios
function ContarPalabras(cad: string): Integer;

// Extraer la k-ésima palabra de una frase (1..N)
function ExtraerPalabra(cad: string; indicePalabra: Integer): string;

// Invertir una palabra o cadena (ej: 'cadena' -> 'anedac')
function InvertirCadena(s: string): string;

// Verificar si una palabra es palíndrome (ej: 'ana' -> true, 'reconocer' -> true)
function EsPalindromo(s: string): Boolean;

// Ordenar alfabéticamente los caracteres de una palabra (ej: 'lenguaje' -> 'aeegjlnu')
function OrdenarCaracteres(s: string): string;

// Verificar si un carácter es vocal (mayúscula o minúscula)
function EsVocal(c: Char): Boolean;

// Verificar si un carácter es consonante
function EsConsonante(c: Char): Boolean;

// Invertir por mitades una cadena (ej: 'cadenas' -> 'dacesan', 'mitades' -> 'timased')
function InvertirPorMitades(cad: string): string;

implementation

// =============================================================================
// IMPLEMENTACIÓN BLOQUE 1: FUNCIONES ATÓMICAS PARA SERIES
// =============================================================================

function Factorial(k: Integer): Double;
var
  i: Integer;
  acumulador: Double;
begin
  if k <= 1 then Exit(1.0);
  acumulador := 1.0;
  for i := 2 to k do
    acumulador := acumulador * i;
  Result := acumulador;
end;

function Potencia(base: Double; exponente: Integer): Double;
var
  i: Integer;
  acumulador: Double;
begin
  if exponente = 0 then Exit(1.0);
  acumulador := 1.0;
  for i := 1 to Abs(exponente) do
    acumulador := acumulador * base;
  if exponente < 0 then
    Result := 1.0 / acumulador
  else
    Result := acumulador;
end;

function Fibonacci(k: Integer): Cardinal;
var
  i: Integer;
  a, b, siguiente: Cardinal;
begin
  if k <= 0 then Exit(0);
  if k = 1 then Exit(1);
  if k = 2 then Exit(1);
  a := 1;
  b := 1;
  for i := 3 to k do
  begin
    siguiente := a + b;
    a := b;
    b := siguiente;
  end;
  Result := b;
end;

function DoblePotencia2(k: Integer): Cardinal;
var
  i: Integer;
  acumulador: Cardinal;
begin
  if k <= 0 then Exit(1);
  acumulador := 1;
  for i := 1 to k do
    acumulador := acumulador * 2;
  Result := acumulador;
end;

function N_EsimoImpar(k: Integer): Integer;
begin
  Result := (k * 2) - 1;
end;

function Cuadrado(k: Integer): Integer;
begin
  Result := k * k;
end;

function Multiplo5(k: Integer): Integer;
begin
  Result := k * 5;
end;

function SignoAlternado(k: Integer): Integer;
begin
  if (k mod 2 = 0) then
    Result := -1
  else
    Result := 1;
end;

// =============================================================================
// IMPLEMENTACIÓN BLOQUE 2: SERIES COMPUESTAS (DIVIDE Y VENCERÁS)
// =============================================================================

function SumaFactorialDoble(n: Integer): Double;
var
  k: Integer;
  numFactorial, denDoble, sumatoria: Double;
begin
  sumatoria := 0.0;
  for k := 1 to n do
  begin
    numFactorial := Factorial(k);
    denDoble     := DoblePotencia2(k);
    sumatoria    := sumatoria + (numFactorial / denDoble);
  end;
  Result := sumatoria;
end;

function SumaCuadradoFibonacci(n: Integer): Double;
var
  k: Integer;
  numerador, denFib, sumatoria: Double;
begin
  sumatoria := 0.0;
  numerador := 3.0; // Inicia en 3 y se duplica: 3, 6, 12, 24, 48...
  for k := 1 to n do
  begin
    denFib    := Fibonacci(k);
    sumatoria := sumatoria + (numerador / denFib);
    numerador := numerador * 2.0;
  end;
  Result := sumatoria;
end;

function SumaPotenciaMultiplo5(n: Integer): Double;
var
  k: Integer;
  numPotencia, denMultiplo, sumatoria: Double;
begin
  sumatoria := 0.0;
  for k := 1 to n do
  begin
    numPotencia := Potencia(k, k);
    denMultiplo := Multiplo5(k);
    sumatoria   := sumatoria + (numPotencia / denMultiplo);
  end;
  Result := sumatoria;
end;

function SumaImparesCuadrados(n: Integer): Double;
var
  k: Integer;
  numImpar, denCuadrado, termino, sumatoria: Double;
begin
  sumatoria := 0.0;
  for k := 1 to n do
  begin
    numImpar    := N_EsimoImpar(k);
    denCuadrado := Cuadrado(k);
    termino     := (numImpar / denCuadrado) * SignoAlternado(k);
    sumatoria   := sumatoria + termino;
  end;
  Result := sumatoria;
end;

function SumaDobleSimple(n: Integer): Int64;
var
  k: Integer;
  doble, sumatoria: Int64;
begin
  sumatoria := 0;
  doble     := 1;
  for k := 1 to n do
  begin
    sumatoria := sumatoria + doble;
    doble     := doble * 2;
  end;
  Result := sumatoria;
end;

function SumaFactorialSimple(n: Integer): Int64;
var
  k: Integer;
  fact, sumatoria: Int64;
begin
  sumatoria := 0;
  fact      := 1;
  for k := 1 to n do
  begin
    fact      := fact * k;
    sumatoria := sumatoria + fact;
  end;
  Result := sumatoria;
end;

function SumaCuadraticaSimple(n: Integer): Int64;
var
  k: Integer;
  sumatoria: Int64;
begin
  sumatoria := 0;
  for k := 1 to n do
    sumatoria := sumatoria + (k * k);
  Result := sumatoria;
end;

// =============================================================================
// IMPLEMENTACIÓN BLOQUE 3: DÍGITOS Y NÚMEROS NATURALES
// =============================================================================

function ContarDigitos(numero: Cardinal): Integer;
var
  cantidad: Integer;
begin
  if numero = 0 then Exit(1);
  cantidad := 0;
  while numero > 0 do
  begin
    Inc(cantidad);
    numero := numero div 10;
  end;
  Result := cantidad;
end;

function InvertirNumero(numero: Cardinal): Cardinal;
var
  invertido: Cardinal;
begin
  invertido := 0;
  while numero > 0 do
  begin
    invertido := (invertido * 10) + (numero mod 10);
    numero := numero div 10;
  end;
  Result := invertido;
end;

function SumarDigitos(numero: Cardinal): Cardinal;
var
  suma: Cardinal;
begin
  suma := 0;
  while numero > 0 do
  begin
    suma := suma + (numero mod 10);
    numero := numero div 10;
  end;
  Result := suma;
end;

function RaizDigital(numero: Cardinal): Byte;
var
  suma: Cardinal;
begin
  while numero >= 10 do
  begin
    suma := 0;
    while numero > 0 do
    begin
      suma := suma + (numero mod 10);
      numero := numero div 10;
    end;
    numero := suma;
  end;
  Result := numero;
end;

function EsDigitoPrimo(digito: Byte): Boolean;
begin
  Result := digito in [2, 3, 5, 7];
end;

function PrimerDigito(numero: Cardinal): Byte;
begin
  while numero >= 10 do
    numero := numero div 10;
  Result := numero;
end;

function UltimoDigito(numero: Cardinal): Byte;
begin
  Result := numero mod 10;
end;

function EsCapicua(numero: Cardinal): Boolean;
begin
  Result := (numero = InvertirNumero(numero));
end;

function ExtraerMitadIzquierda(numero: Cardinal): Cardinal;
var
  totalDigitos, mitad, factor, i: Integer;
begin
  totalDigitos := ContarDigitos(numero);
  mitad := totalDigitos div 2;
  if mitad = 0 then Exit(numero);

  factor := 1;
  for i := 1 to (totalDigitos - mitad) do
    factor := factor * 10;

  Result := numero div factor;
end;

function ExtraerMitadDerecha(numero: Cardinal): Cardinal;
var
  totalDigitos, mitad, factor, i: Integer;
begin
  totalDigitos := ContarDigitos(numero);
  mitad := totalDigitos div 2;
  if mitad = 0 then Exit(numero);

  factor := 1;
  for i := 1 to mitad do
    factor := factor * 10;

  Result := numero mod factor;
end;

// =============================================================================
// IMPLEMENTACIÓN BLOQUE 4: CADENAS DE CARACTERES
// =============================================================================

function ContarPalabras(cad: string): Integer;
var
  i, cantidad: Integer;
  enPalabra: Boolean;
begin
  cantidad  := 0;
  enPalabra := False;
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
    begin
      if not enPalabra then
      begin
        Inc(cantidad);
        enPalabra := True;
      end;
    end
    else
      enPalabra := False;
  end;
  Result := cantidad;
end;

function ExtraerPalabra(cad: string; indicePalabra: Integer): string;
var
  i, contador: Integer;
  palabraActual: string;
begin
  cad := Trim(cad) + ' ';
  palabraActual := '';
  contador := 0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      palabraActual := palabraActual + cad[i]
    else
    begin
      if palabraActual <> '' then
      begin
        Inc(contador);
        if contador = indicePalabra then
          Exit(palabraActual);
        palabraActual := '';
      end;
    end;
  end;
  Result := '';
end;

function InvertirCadena(s: string): string;
var
  i: Integer;
  invertida: string;
begin
  invertida := '';
  for i := Length(s) downto 1 do
    invertida := invertida + s[i];
  Result := invertida;
end;

function EsPalindromo(s: string): Boolean;
begin
  s := LowerCase(Trim(s));
  Result := (Length(s) > 1) and (s = InvertirCadena(s));
end;

function OrdenarCaracteres(s: string): string;
var
  i, j: Integer;
  aux: Char;
begin
  for i := 1 to Length(s) - 1 do
    for j := i + 1 to Length(s) do
      if s[i] > s[j] then
      begin
        aux := s[i];
        s[i] := s[j];
        s[j] := aux;
      end;
  Result := s;
end;

function EsVocal(c: Char): Boolean;
begin
  c := UpCase(c);
  Result := c in ['A', 'E', 'I', 'O', 'U'];
end;

function EsConsonante(c: Char): Boolean;
begin
  c := UpCase(c);
  Result := (c in ['A'..'Z']) and not EsVocal(c);
end;

function InvertirPorMitades(cad: string): string;
var
  longitud, m: Integer;
  mitadIzq, mitadDer, centro: string;
begin
  longitud := Length(cad);
  m := longitud div 2;
  mitadIzq := Copy(cad, 1, m);
  if (longitud mod 2 <> 0) then
  begin
    centro   := cad[m + 1];
    mitadDer := Copy(cad, m + 2, m);
  end
  else
  begin
    centro   := '';
    mitadDer := Copy(cad, m + 1, m);
  end;
  Result := InvertirCadena(mitadIzq) + centro + InvertirCadena(mitadDer);
end;

end.

