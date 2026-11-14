program TestSeriesOficial;
{$mode objfpc}{$H+}

function sumaDoble(numero, contador: integer): integer;
var doble, sumadordoble: integer;
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

function sumafactorial(numero, contador: integer): integer;
var factorial, sumadorfactorial: integer;
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

function sumaCuadratica(numero, contador: integer): integer;
var cuadratica, sumadorCuadratica: integer;
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

var
  c: Integer;
begin
  c := 1;
  WriteLn('Testing Series Oficial:');
  WriteLn('SumaDoble(5): ', sumaDoble(5, c), ' [Expected: 31]');
  WriteLn('SumaFactorial(5): ', sumafactorial(5, c), ' [Expected: 153]');
  WriteLn('SumaCuadratica(5): ', sumaCuadratica(5, c), ' [Expected: 55]');
  if (sumaDoble(5, c) = 31) and (sumafactorial(5, c) = 153) and (sumaCuadratica(5, c) = 55) then
    WriteLn('ALL TESTS PASSED 100%!')
  else
    WriteLn('FAIL');
end.

