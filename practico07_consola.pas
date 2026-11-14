program Practico07Consola;

{$APPTYPE CONSOLE} // Compatible con Delphi y Free Pascal

uses
  SysUtils;

// =============================================================================
//                       FUNCIONES AUXILIARES (BÁSICAS)
// =============================================================================

// Función para verificar si un dígito (0..9) es primo
function EsPrimo(digito: Byte): Boolean;
begin
  EsPrimo := (digito = 2) or (digito = 3) or (digito = 5) or (digito = 7);
end;

// Función para contar la cantidad de dígitos de un número natural
function CantidadDigitos(n: LongWord): Byte;
var
  c: Byte;
begin
  if n = 0 then
    CantidadDigitos := 1
  else
  begin
    c := 0;
    while n > 0 do
    begin
      c := c + 1;
      n := n div 10;
    end;
    CantidadDigitos := c;
  end;
end;

// Función para calcular 10 elevado a la potencia k (10^k)
function Potencia10(k: Byte): LongWord;
var
  i: Byte;
  res: LongWord;
begin
  res := 1;
  for i := 1 to k do
    res := res * 10;
  Potencia10 := res;
end;

// =============================================================================
//                   EJERCICIOS DEL PRÁCTICO (MODULARES)
// =============================================================================

// 1. Suma de los dígitos impares mayores a 3 (es decir: 5, 7, 9)
function SumaImparesMayores3(n: LongWord): LongWord;
var
  d, suma: LongWord;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 <> 0) and (d > 3) then
      suma := suma + d;
    n := n div 10;
  end;
  SumaImparesMayores3 := suma;
end;

// 2. Dígito mayor de los índices/posiciones impares (de izq. a der.: 1ª, 3ª, 5ª...)
function DigitoMayorIndicesImpares(n: LongWord): ShortInt;
var
  totalDig, pos, d: Byte;
  mayor: ShortInt;
  pot: LongWord;
begin
  if n = 0 then
  begin
    DigitoMayorIndicesImpares := 0;
    Exit;
  end;
  totalDig := CantidadDigitos(n);
  mayor := -1;
  for pos := 1 to totalDig do
  begin
    pot := Potencia10(totalDig - pos);
    d := (n div pot) mod 10;
    // Si la posición es impar (1, 3, 5, ...)
    if (pos mod 2 <> 0) and (d > mayor) then
      mayor := d;
  end;
  DigitoMayorIndicesImpares := mayor;
end;

// 3. Sumar los dígitos de un número
function SumaDigitos(n: LongWord): LongWord;
var
  suma: LongWord;
begin
  suma := 0;
  while n > 0 do
  begin
    suma := suma + (n mod 10);
    n := n div 10;
  end;
  SumaDigitos := suma;
end;

// 4. Promedio de los dígitos menores a 7
function PromedioDigitosMenores7(n: LongWord): Real;
var
  d, suma, cont: LongWord;
begin
  suma := 0;
  cont := 0;
  if n = 0 then
  begin
    PromedioDigitosMenores7 := 0.0;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if d < 7 then
    begin
      suma := suma + d;
      cont := cont + 1;
    end;
    n := n div 10;
  end;
  if cont > 0 then
    PromedioDigitosMenores7 := suma / cont
  else
    PromedioDigitosMenores7 := 0.0;
end;

// 5. Procedimiento para obtener el dígito mayor y el dígito menor
procedure MayorYMenorDigito(n: LongWord; var digMayor, digMenor: Byte);
var
  d: Byte;
begin
  if n = 0 then
  begin
    digMayor := 0;
    digMenor := 0;
    Exit;
  end;
  digMayor := 0;
  digMenor := 9;
  while n > 0 do
  begin
    d := n mod 10;
    if d > digMayor then digMayor := d;
    if d < digMenor then digMenor := d;
    n := n div 10;
  end;
end;

// 6. Formar otro número con los dígitos pares (conservando el orden)
function FormarNumeroPares(n: LongWord): LongWord;
var
  d, res, pot: LongWord;
begin
  res := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  FormarNumeroPares := res;
end;

// 7. Procedimiento para separar un número en 2 números (uno con pares y otro con impares)
procedure SepararParesImpares(n: LongWord; var numPares, numImpares: LongWord);
var
  d, potP, potI: LongWord;
begin
  numPares := 0;
  numImpares := 0;
  potP := 1;
  potI := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      numPares := numPares + (d * potP);
      potP := potP * 10;
    end
    else
    begin
      numImpares := numImpares + (d * potI);
      potI := potI * 10;
    end;
    n := n div 10;
  end;
end;

// 8. Dígito mayor de los dígitos pares (-1 si no tiene pares)
function MayorDigitoPar(n: LongWord): ShortInt;
var
  d: LongWord;
  mayor: ShortInt;
begin
  mayor := -1;
  if n = 0 then
  begin
    MayorDigitoPar := 0;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) and (d > mayor) then
      mayor := d;
    n := n div 10;
  end;
  MayorDigitoPar := mayor;
end;

// 9. Procedimiento para mostrar los dígitos múltiplos de 3 (0, 3, 6, 9)
procedure MostrarMultiplosDe3(n: LongWord);
var
  totalDig, pos, d: Byte;
  pot: LongWord;
  encontrado: Boolean;
begin
  if n = 0 then
  begin
    Writeln('0');
    Exit;
  end;
  totalDig := CantidadDigitos(n);
  encontrado := False;
  Write('Digitos multiplos de 3: ');
  for pos := 1 to totalDig do
  begin
    pot := Potencia10(totalDig - pos);
    d := (n div pot) mod 10;
    if d mod 3 = 0 then
    begin
      Write(d, ' ');
      encontrado := True;
    end;
  end;
  if not encontrado then
    Write('Ninguno');
  Writeln;
end;

// 10. Procedimiento para obtener el primer y último dígito
procedure PrimerYUltimoDigito(n: LongWord; var primero, ultimo: Byte);
begin
  ultimo := n mod 10;
  while n >= 10 do
    n := n div 10;
  primero := n;
end;

// 11. Eliminar el primero y último dígito
function EliminarPrimerYUltimoDigito(n: LongWord): LongWord;
var
  pot: LongWord;
begin
  if n < 100 then
  begin
    EliminarPrimerYUltimoDigito := 0;
    Exit;
  end;
  // Quitar el último
  n := n div 10;
  // Quitar el primero usando la potencia correspondiente
  pot := Potencia10(CantidadDigitos(n) - 1);
  EliminarPrimerYUltimoDigito := n mod pot;
end;

// 12. Invertir número
function InvertirNumero(n: LongWord): LongWord;
var
  inv: LongWord;
begin
  inv := 0;
  while n > 0 do
  begin
    inv := (inv * 10) + (n mod 10);
    n := n div 10;
  end;
  InvertirNumero := inv;
end;

// 13. Contar dígitos múltiplos de 4 (0, 4, 8)
function ContarMultiplosDeCuatro(n: LongWord): LongWord;
var
  d, cont: LongWord;
begin
  cont := 0;
  if n = 0 then
  begin
    ContarMultiplosDeCuatro := 1;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 4 = 0 then
      cont := cont + 1;
    n := n div 10;
  end;
  ContarMultiplosDeCuatro := cont;
end;

// 14. Dígito menor de los múltiplos de 3 (0, 3, 6, 9)
function MenorDigitoMultiploDeTres(n: LongWord): ShortInt;
var
  d: LongWord;
  menor: ShortInt;
begin
  menor := 10;
  if n = 0 then
  begin
    MenorDigitoMultiploDeTres := 0;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) and (d < menor) then
      menor := d;
    n := n div 10;
  end;
  if menor = 10 then
    MenorDigitoMultiploDeTres := -1
  else
    MenorDigitoMultiploDeTres := menor;
end;

// 15. Verificar si es capicúa o palíndromo
function EsCapicua(n: LongWord): Boolean;
begin
  EsCapicua := (n = InvertirNumero(n));
end;

// 16. Convertir a binario
function DecimalABinario(n: LongWord): String;
var
  res: String;
begin
  if n = 0 then
  begin
    DecimalABinario := '0';
    Exit;
  end;
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 2) + res;
    n := n div 2;
  end;
  DecimalABinario := res;
end;

// 17. Convertir a Hexadecimal
function DecimalAHexadecimal(n: LongWord): String;
const
  HexChars: array[0..15] of Char = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F');
var
  res: String;
begin
  if n = 0 then
  begin
    DecimalAHexadecimal := '0';
    Exit;
  end;
  res := '';
  while n > 0 do
  begin
    res := HexChars[n mod 16] + res;
    n := n div 16;
  end;
  DecimalAHexadecimal := res;
end;

// 18. Convertir a Octal
function DecimalAOctal(n: LongWord): String;
var
  res: String;
begin
  if n = 0 then
  begin
    DecimalAOctal := '0';
    Exit;
  end;
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 8) + res;
    n := n div 8;
  end;
  DecimalAOctal := res;
end;

// 19. Sumar dígitos primos (2, 3, 5, 7)
function SumaDigitosPrimos(n: LongWord): LongWord;
var
  d, suma: LongWord;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
      suma := suma + d;
    n := n div 10;
  end;
  SumaDigitosPrimos := suma;
end;

// 20. Promedio de los dígitos múltiplos de 3 o 5
function PromedioMultiplos3y5(n: LongWord): Real;
var
  d, suma, cont: LongWord;
begin
  suma := 0;
  cont := 0;
  if n = 0 then
  begin
    PromedioMultiplos3y5 := 0.0;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) or (d mod 5 = 0) then
    begin
      suma := suma + d;
      cont := cont + 1;
    end;
    n := n div 10;
  end;
  if cont > 0 then
    PromedioMultiplos3y5 := suma / cont
  else
    PromedioMultiplos3y5 := 0.0;
end;

// 21. Promedio de los dígitos primos
function PromedioDigitosPrimos(n: LongWord): Real;
var
  d, suma, cont: LongWord;
begin
  suma := 0;
  cont := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
    begin
      suma := suma + d;
      cont := cont + 1;
    end;
    n := n div 10;
  end;
  if cont > 0 then
    PromedioDigitosPrimos := suma / cont
  else
    PromedioDigitosPrimos := 0.0;
end;

// 22. Formar otro número con los dígitos primos
function FormarNumeroPrimos(n: LongWord): LongWord;
var
  d, res, pot: LongWord;
begin
  res := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  FormarNumeroPrimos := res;
end;

// 23. Decimal a Hexadecimal
function DecimalAHexadecimal2(n: LongWord): String;
begin
  DecimalAHexadecimal2 := DecimalAHexadecimal(n);
end;

// 24. Decimal a Binario
function DecimalABinario2(n: LongWord): String;
begin
  DecimalABinario2 := DecimalABinario(n);
end;

// 25. Octal a Hexadecimal
function OctalAHexadecimal(octalStr: String): String;
var
  i: Integer;
  valDec, pot: LongWord;
  d: Integer;
begin
  valDec := 0;
  pot := 1;
  for i := Length(octalStr) downto 1 do
  begin
    d := Ord(octalStr[i]) - Ord('0');
    valDec := valDec + (d * pot);
    pot := pot * 8;
  end;
  OctalAHexadecimal := DecimalAHexadecimal(valDec);
end;

// =============================================================================
//                             MENÚ PRINCIPAL
// =============================================================================
var
  opcion: Integer;
  num, pares, impares: LongWord;
  dMayor, dMenor, pDig, uDig: Byte;
  cadOctal: String;

begin
  repeat
    Writeln('==================================================================');
    Writeln('       PRACTICO # 7 - PROGRAMACION MODULAR (NUMEROS NATURALES)    ');
    Writeln('==================================================================');
    Writeln(' 1. Suma de digitos impares mayores a 3 (5, 7, 9)');
    Writeln(' 2. Digito mayor de los indices impares');
    Writeln(' 3. Sumar digitos de un numero');
    Writeln(' 4. Promedio de digitos menores a 7');
    Writeln(' 5. Digito mayor y digito menor');
    Writeln(' 6. Formar numero con digitos pares');
    Writeln(' 7. Separar numero en pares e impares');
    Writeln(' 8. Mayor de los digitos pares');
    Writeln(' 9. Mostrar digitos multiplos de 3');
    Writeln('10. Obtener primer y ultimo digito');
    Writeln('11. Eliminar primer y ultimo digito');
    Writeln('12. Invertir numero');
    Writeln('13. Contar digitos multiplos de 4');
    Writeln('14. Menor digito multiplo de 3');
    Writeln('15. Verificar si es Capicua');
    Writeln('16. Convertir a Binario');
    Writeln('17. Convertir a Hexadecimal');
    Writeln('18. Convertir a Octal');
    Writeln('19. Sumar digitos primos');
    Writeln('20. Promedio digitos multiplos de 3 o 5');
    Writeln('21. Promedio digitos primos');
    Writeln('22. Formar numero con digitos primos');
    Writeln('23. Decimal a Hexadecimal');
    Writeln('24. Decimal a Binario');
    Writeln('25. Octal a Hexadecimal');
    Writeln(' 0. Salir');
    Writeln('==================================================================');
    Write('Seleccione una opcion (0-25): ');
    Readln(opcion);

    if (opcion >= 1) and (opcion <= 24) then
    begin
      Write('Ingrese un numero natural: ');
      Readln(num);
    end;

    Writeln;
    case opcion of
      1: Writeln('Suma impares > 3: ', SumaImparesMayores3(num));
      2: Writeln('Mayor digito en indices impares: ', DigitoMayorIndicesImpares(num));
      3: Writeln('Suma de todos los digitos: ', SumaDigitos(num));
      4: Writeln('Promedio digitos < 7: ', PromedioDigitosMenores7(num):0:2);
      5:
        begin
          MayorYMenorDigito(num, dMayor, dMenor);
          Writeln('Digito Mayor: ', dMayor, ' | Digito Menor: ', dMenor);
        end;
      6: Writeln('Numero formado con pares: ', FormarNumeroPares(num));
      7:
        begin
          SepararParesImpares(num, pares, impares);
          Writeln('Numero Pares: ', pares, ' | Numero Impares: ', impares);
        end;
      8:
        begin
          if MayorDigitoPar(num) = -1 then
            Writeln('No contiene digitos pares.')
          else
            Writeln('Mayor digito par: ', MayorDigitoPar(num));
        end;
      9: MostrarMultiplosDe3(num);
      10:
        begin
          PrimerYUltimoDigito(num, pDig, uDig);
          Writeln('Primer digito: ', pDig, ' | Ultimo digito: ', uDig);
        end;
      11: Writeln('Numero sin extremos: ', EliminarPrimerYUltimoDigito(num));
      12: Writeln('Numero invertido: ', InvertirNumero(num));
      13: Writeln('Cantidad multiplos de 4: ', ContarMultiplosDeCuatro(num));
      14:
        begin
          if MenorDigitoMultiploDeTres(num) = -1 then
            Writeln('No tiene digitos multiplos de 3')
          else
            Writeln('Menor digito multiplo de 3: ', MenorDigitoMultiploDeTres(num));
        end;
      15:
        begin
          if EsCapicua(num) then
            Writeln(num, ' SI es capicua')
          else
            Writeln(num, ' NO es capicua');
        end;
      16: Writeln('Binario: ', DecimalABinario(num));
      17: Writeln('Hexadecimal: ', DecimalAHexadecimal(num));
      18: Writeln('Octal: ', DecimalAOctal(num));
      19: Writeln('Suma de digitos primos: ', SumaDigitosPrimos(num));
      20: Writeln('Promedio multiplos de 3 o 5: ', PromedioMultiplos3y5(num):0:2);
      21: Writeln('Promedio digitos primos: ', PromedioDigitosPrimos(num):0:2);
      22: Writeln('Numero formado con primos: ', FormarNumeroPrimos(num));
      23: Writeln('Hexadecimal: ', DecimalAHexadecimal2(num));
      24: Writeln('Binario: ', DecimalABinario2(num));
      25:
        begin
          Write('Ingrese numero en base Octal (ej. 752): ');
          Readln(cadOctal);
          Writeln('Hexadecimal: ', OctalAHexadecimal(cadOctal));
        end;
      0: Writeln('Fin del programa.');
    else
      Writeln('Opcion invalida.');
    end;

    if opcion <> 0 then
    begin
      Writeln;
      Write('Presione [ENTER] para continuar...');
      Readln;
    end;

  until opcion = 0;
end.
