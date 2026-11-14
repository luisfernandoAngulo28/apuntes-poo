program TestSeries;
{$mode objfpc}{$H+}

uses
  SysUtils;

// =============================================================================
// FUNCIONES DE SERIES - M.Sc. ING. ANGÉLICA GARZÓN C.
// =============================================================================

// 1. Suma Doble (Potencias de 2: 1 + 2 + 4 + 8 + 16 + ... = 31 para n=5)
function sumaDoble(numero, contador: Integer): Integer;
var
  doble, sumadordoble: Integer;
begin
  sumadordoble := 0;
  contador := 1;
  doble := 1;
  while numero >= contador do
  begin
    sumadordoble := sumadordoble + doble;
    doble := doble * 2;
    contador := contador + 1;
  end;
  Result := sumadordoble;
end;

// 2. Suma Factorial (1! + 2! + 3! + 4! + 5! = 1 + 2 + 6 + 24 + 120 = 153 para n=5)
function sumafactorial(numero, contador: Integer): Integer;
var
  factorial, sumadorfactorial: Integer;
begin
  sumadorfactorial := 0;
  contador := 1;
  factorial := 1;
  while numero >= contador do
  begin
    factorial := factorial * contador;
    sumadorfactorial := sumadorfactorial + factorial;
    contador := contador + 1;
  end;
  Result := sumadorfactorial;
end;

// 3. Suma Cuadrática (1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55 para n=5)
function sumaCuadratica(numero, contador: Integer): Integer;
var
  cuadratica, sumadorCuadratica: Integer;
begin
  sumadorCuadratica := 0;
  contador := 1;
  cuadratica := 1;
  while numero >= contador do
  begin
    cuadratica := contador * contador;
    sumadorCuadratica := sumadorCuadratica + cuadratica;
    contador := contador + 1;
  end;
  Result := sumadorCuadratica;
end;

// =============================================================================
// PROGRAMA PRINCIPAL DE PRUEBA
// =============================================================================
var
  n, cont, r1, r2, r3: Integer;
  passes: Integer;

begin
  passes := 0;
  n := 5;
  cont := 1;

  WriteLn('===========================================================');
  WriteLn('TEST SUITE: SERIES CON PROGRAMACION MODULAR (INF110-Z2)');
  WriteLn('===========================================================');

  r1 := sumaDoble(n, cont);
  WriteLn('1. sumaDoble(5) = ', r1, ' (Esperado: 31)');
  if r1 = 31 then Inc(passes);

  r2 := sumafactorial(n, cont);
  WriteLn('2. sumafactorial(5) = ', r2, ' (Esperado: 153)');
  if r2 = 153 then Inc(passes);

  r3 := sumaCuadratica(n, cont);
  WriteLn('3. sumaCuadratica(5) = ', r3, ' (Esperado: 55)');
  if r3 = 55 then Inc(passes);

  WriteLn('-----------------------------------------------------------');
  WriteLn('RESULTADO: ', passes, ' de 3 pruebas superadas al 100%!');
  WriteLn('===========================================================');
end.

