unit UnitModelosSegundoParcial;

{$mode objfpc}{$H+}

interface

uses
  SysUtils;

{ ============================================================================ }
{                    MÓDULOS DE UTILIDAD GENERAL / AUXILIARES                  }
{ ============================================================================ }

function EsVocal(c: Char): Boolean;
function EsConsonante(c: Char): Boolean;
function EsMayuscula(c: Char): Boolean;
function PotenciaManual(base, exp: Integer): Int64;
function Factorial(n: Integer): Int64;
function FibTermino(k: Integer): Integer; // k=1->0, k=2->1, k=3->1, k=4->2, k=5->3...

{ ============================================================================ }
{                  EXAMEN 1: 2024-1 Z2 (17 de Junio de 2024)                  }
{ ============================================================================ }

// P1 (35 pts): Serie S = 1^1/1 + 2^2/4 + 3^3/5 + 4^4/9 + ...
// Denominador: 1, 4, 5, 9, 14, 23... (Fibonacci aditivo: D[k] = D[k-1] + D[k-2])
function Denominador_2024_1_Z2(k: Integer): Int64;
function SumaSerie_2024_1_Z2(n: Integer): Real;

// P2 (30 pts): Menor dígito impar y mayor dígito par, retornar nuevo número
// Ejemplo: 85239 -> menor impar = 3, mayor par = 8 -> 38
function MenorImparMayorPar(n: LongWord): LongWord;

// P3a (17.5 pts): Invertir la última palabra
// Ejemplo: 'Segundo examen parcial' -> 'Segundo examen laicrap'
function InvertirUltimaPalabra(cad: String): String;

// P3b (17.5 pts): Eliminar consonantes
// Ejemplo: 'Segundo examen parcial' -> 'euo eae aia'
function EliminarConsonantes(cad: String): String;


{ ============================================================================ }
{            EXAMEN 2: 2024-1 Z2-R (Repechaje / Pizarra 2024)                  }
{ ============================================================================ }

// P1 (25 pts): Serie St = X^1 + X^2 + X^3 + ... + X^n
// Ejemplos: X=2, N=3 -> 14 | X=3, N=3 -> 39
function SumaPotenciasX(x, n: Integer): Int64;

// P2 (25 pts): Convertir a MAYÚSCULAS las palabras que comiencen con vocal
// Ejemplo: 'Ana estudia programación' -> 'ANA ESTUDIA programación'
function MayusculasPalabrasInicianVocal(cad: String): String;


{ ============================================================================ }
{                  EXAMEN 3: 2024-1 SF (19 de Junio de 2024)                  }
{ ============================================================================ }

// P1 (35 pts): Serie f = 2/0! + 4/1! + 6/1! + 8/2! + 10/3! + ...
// Numerador = 2*i, Denominador = Fib(i)! con Fib = 0, 1, 1, 2, 3, 5...
// Para N=4 -> 2 + 4 + 6 + 4 = 16
function SumaSerie_2024_1_SF(n: Integer): Real;

// P2 (30 pts): Eliminar todos los dígitos a partir de la posición K (desde la derecha)
// Ejemplo: N = 78143, K = 3 -> 43
function EliminarDesdePosicionK(n: LongWord; k: Byte): LongWord;

// P3 (35 pts): Convertir el primer carácter de cada palabra a mayúscula
// Ejemplo: 'hola mundo de cadena' -> 'Hola Mundo De Cadena'
function PrimerLetraCadaPalabraMayuscula(cad: String): String;


{ ============================================================================ }
{                EXAMEN 4: 2023-2 Z2 (27 de Noviembre de 2023)                }
{ ============================================================================ }

// P1: Serie S = 1^1/1 + 2^2/4 + 3^3/5 + 4^4/9 + ... (Para N=4 -> 35.84)
// (Utiliza la misma función SumaSerie_2024_1_Z2)

// P2: Eliminar un dígito en la posición K (desde la derecha)
// Ejemplo: N = 78143, K = 2 -> 7813
function EliminarDigitoPosicionK(n: LongWord; k: Byte): LongWord;

// P3: Mostrar la cantidad de vocales que tiene cada palabra
// Ejemplo: 'Hola mundo de cadena' -> '2, 2, 1, 3'
function CantidadVocalesPorPalabra(cad: String): String;


{ ============================================================================ }
{                  EXAMEN 5: 2023-1 Z2 (26 de Junio de 2023)                  }
{ ============================================================================ }

// P1: Serie SF = 1^1/5 + 2^2/6 + 3^3/11 + 4^4/17 + 5^5/28 + ... (Sin usar Power)
// Denominadores: 5, 6, 11, 17, 28, 45, 73... (Fibonacci con semillas 5 y 6)
// Para N=4 -> 15.2069
function Denominador_2023_1_Z2(k: Integer): Int64;
function SumaSerie_2023_1_Z2(n: Integer): Real;

// P2: Eliminar un dígito en la posición K -> EliminarDigitoPosicionK (idéntico)

// P3: Invertir cada una de las palabras manteniendo su orden en la frase
// Ejemplo: 'SANTA CRUZ DE LA SIERRA' -> 'ATNAS ZURC ED AL ARREIS'
function InvertirCadaPalabra(cad: String): String;


{ ============================================================================ }
{                   EXAMEN 6: 2023-1 (Pizarra Examen Parcial 2)                }
{ ============================================================================ }

// P1: Serie S = 1/0! + 4/1! + 9/1! + 16/2! + 25/3! + ...
// Numerador = i^2, Denominador = Fib(i)!
// Para N=4 -> 1 + 4 + 9 + 8 = 22
function SumaSerie_2023_1_Pizarra(n: Integer): Real;

// P2: Obtener Promedio de Pares y Promedio de Impares de un número natural
// Ejemplo: N = 12345 -> PromPar = 6/2 = 3.0, PromImpar = 9/3 = 3.0
procedure PromediosParEImpar(n: LongWord; var promPar, promImpar: Real);

// P3: Convertir a mayúsculas primera letra de cada palabra -> PrimerLetraCadaPalabraMayuscula


{ ============================================================================ }
{          EXAMEN 7: 2022-1 (MÓDULOS: SERIE, NATURALES Y CADENA)               }
{ ============================================================================ }

// P1: Dígito mayor que sea múltiplo de 3
// Ejemplo: N = 8326 -> 6 (M3 son 3 y 6, mayor es 6)
function DigitoMayorMultiplo3(n: LongWord): Integer;

// P2: Promedio de la serie entrelazada: 4 + 2 + 8 + 6 + 12 + 18 + 16 + 54 + 20 + 162 + ...
// Pos impares: 4, 8, 12, 16... (+4) | Pos pares: 2, 6, 18, 54... (*3)
// Para N=4 -> Promedio = (4+2+8+6)/4 = 5.0
function TerminoSerieEntrelazada_2022(k: Integer): Int64;
function PromedioSerie_2022_1(n: Integer): Real;

// P3: Cantidad de palabras que terminan en una vocal
// Ejemplo: 'Hola a los alumnos de programacion'
function ContarPalabrasTerminanVocal(cad: String): Integer;

// P4: Contar palabras que comienzan en mayúsculas
// Ejemplo: 'Cadena de Texto de Programacion' -> 3
function ContarPalabrasInicianMayuscula(cad: String): Integer;

// P5: Extraer los caracteres en índices pares (1-based: 2, 4, 6, 8...)
// Ejemplo: 'programa' (1..8) -> 'rgaa'
function ExtraerCaracteresIndicesPares(cad: String): String;


{ ============================================================================ }
{          PLUS: CLASE ORDENACIÓN DE CADENAS DE ESTA SEMANA (BURBUJA)          }
{ ============================================================================ }

// Ordenación interna de una palabra
function OrdenarCaracteresBurbujaAscendente(pal: String): String;
function OrdenarCaracteresBurbujaDescendente(pal: String): String;

// 1. Ordenar última palabra de una frase (Ej: 'Casa de ana' -> 'Casa de aan')
function OrdenarUltimaPalabra(cad: String): String;

// 2. Invertir la segunda palabra (Ej: 'Hola mundo de Cadena' -> 'Hola odnum de Cadena')
function InvertirSegundaPalabra(cad: String): String;

// 3. Ordenar la segunda palabra (Ej: 'Hola mundo de Cadena' -> 'Hola dmnou de Cadena')
function OrdenarSegundaPalabra(cad: String): String;


implementation

{ ============================================================================ }
{                    IMPLEMENTACIÓN DE MÓDULOS AUXILIARES                      }
{ ============================================================================ }

function EsVocal(c: Char): Boolean;
begin
  Result := UpCase(c) in ['A', 'E', 'I', 'O', 'U'];
end;

function EsConsonante(c: Char): Boolean;
begin
  Result := (UpCase(c) in ['A'..'Z']) and not EsVocal(c);
end;

function EsMayuscula(c: Char): Boolean;
begin
  Result := c in ['A'..'Z'];
end;

function PotenciaManual(base, exp: Integer): Int64;
var
  p: Int64;
  c: Integer;
begin
  p := 1;
  c := 1;
  while c <= exp do
  begin
    p := p * base;
    c := c + 1;
  end;
  Result := p;
end;

function Factorial(n: Integer): Int64;
var
  f: Int64;
  c: Integer;
begin
  f := 1;
  c := 1;
  while c <= n do
  begin
    f := f * c;
    c := c + 1;
  end;
  Result := f;
end;

// Términos de Fibonacci: k=1 -> 0, k=2 -> 1, k=3 -> 1, k=4 -> 2, k=5 -> 3, k=6 -> 5...
function FibTermino(k: Integer): Integer;
var
  a, b, c, i: Integer;
begin
  if k <= 1 then
    Result := 0
  else if k = 2 then
    Result := 1
  else
  begin
    a := 0;
    b := 1;
    c := 1;
    i := 3;
    while i <= k do
    begin
      c := a + b;
      a := b;
      b := c;
      i := i + 1;
    end;
    Result := c;
  end;
end;


{ ============================================================================ }
{                              EXAMEN 1: 2024-1 Z2                             }
{ ============================================================================ }

// Denominadores: 1, 4, 5, 9, 14, 23, 37...
function Denominador_2024_1_Z2(k: Integer): Int64;
var
  a, b, c: Int64;
  i: Integer;
begin
  if k = 1 then
    Result := 1
  else if k = 2 then
    Result := 4
  else
  begin
    a := 1;
    b := 4;
    c := 5;
    i := 3;
    while i <= k do
    begin
      c := a + b;
      a := b;
      b := c;
      i := i + 1;
    end;
    Result := c;
  end;
end;

function SumaSerie_2024_1_Z2(n: Integer): Real;
var
  sum: Real;
  i: Integer;
  num, den: Int64;
begin
  sum := 0.0;
  i := 1;
  while i <= n do
  begin
    num := PotenciaManual(i, i);
    den := Denominador_2024_1_Z2(i);
    sum := sum + (num / den);
    i := i + 1;
  end;
  Result := sum;
end;

function MenorImparMayorPar(n: LongWord): LongWord;
var
  d: Byte;
  menorImp, mayorPar: Integer;
begin
  menorImp := 10; // Sentinela de búsqueda mínima
  mayorPar := -1; // Sentinela de búsqueda máxima
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 1) then
    begin
      if d < menorImp then
        menorImp := d;
    end
    else
    begin
      if d > mayorPar then
        mayorPar := d;
    end;
    n := n div 10;
  end;

  if (menorImp < 10) and (mayorPar >= 0) then
    Result := (menorImp * 10) + mayorPar
  else if menorImp < 10 then
    Result := menorImp
  else if mayorPar >= 0 then
    Result := mayorPar
  else
    Result := 0;
end;

function InvertirUltimaPalabra(cad: String): String;
var
  n, i, finPal, iniPal, k: Byte;
  palInvertida: String;
begin
  n := Length(cad);
  // 1. Omitir posibles espacios al final
  i := n;
  while (i >= 1) and (cad[i] = ' ') do
    i := i - 1;
  finPal := i;

  // 2. Retroceder hasta encontrar el inicio de la palabra
  while (i >= 1) and (cad[i] <> ' ') do
    i := i - 1;
  iniPal := i + 1;

  if finPal >= iniPal then
  begin
    // Invertir los caracteres entre iniPal y finPal
    palInvertida := '';
    k := finPal;
    while k >= iniPal do
    begin
      palInvertida := palInvertida + cad[k];
      k := k - 1;
    end;
    // Reconstruir: antes + palabra invertida + después
    Result := Copy(cad, 1, iniPal - 1) + palInvertida + Copy(cad, finPal + 1, n - finPal);
  end
  else
    Result := cad;
end;

function EliminarConsonantes(cad: String): String;
var
  res: String;
  i, n: Byte;
begin
  res := '';
  n := Length(cad);
  i := 1;
  while i <= n do
  begin
    // Si no es consonante (es vocal, espacio, número o signo), se conserva
    if not EsConsonante(cad[i]) then
      res := res + cad[i];
    i := i + 1;
  end;
  Result := res;
end;


{ ============================================================================ }
{                             EXAMEN 2: 2024-1 Z2-R                            }
{ ============================================================================ }

function SumaPotenciasX(x, n: Integer): Int64;
var
  sum, ter: Int64;
  i: Integer;
begin
  sum := 0;
  ter := 1;
  i := 1;
  while i <= n do
  begin
    ter := ter * x;
    sum := sum + ter;
    i := i + 1;
  end;
  Result := sum;
end;

function MayusculasPalabrasInicianVocal(cad: String): String;
var
  n, i, pIni, pFin, k: Byte;
  pal, res: String;
begin
  n := Length(cad);
  res := '';
  i := 1;
  while i <= n do
  begin
    if cad[i] = ' ' then
    begin
      res := res + ' ';
      i := i + 1;
    end
    else
    begin
      // Extraer palabra
      pIni := i;
      while (i <= n) and (cad[i] <> ' ') do
        i := i + 1;
      pFin := i - 1;
      pal := Copy(cad, pIni, pFin - pIni + 1);

      // Si la primera letra es vocal, convertir toda la palabra a mayúsculas
      if (Length(pal) > 0) and EsVocal(pal[1]) then
        pal := UpperCase(pal);

      res := res + pal;
    end;
  end;
  Result := res;
end;


{ ============================================================================ }
{                              EXAMEN 3: 2024-1 SF                             }
{ ============================================================================ }

function SumaSerie_2024_1_SF(n: Integer): Real;
var
  sum: Real;
  i, fibVal: Integer;
  num, den: Int64;
begin
  sum := 0.0;
  i := 1;
  while i <= n do
  begin
    num := 2 * i;
    fibVal := FibTermino(i);
    den := Factorial(fibVal);
    sum := sum + (num / den);
    i := i + 1;
  end;
  Result := sum;
end;

function EliminarDesdePosicionK(n: LongWord; k: Byte): LongWord;
var
  res, pot: LongWord;
  pos, d: Byte;
begin
  res := 0;
  pot := 1;
  pos := 1;
  while (n > 0) and (pos < k) do
  begin
    d := n mod 10;
    res := res + (d * pot);
    pot := pot * 10;
    pos := pos + 1;
    n := n div 10;
  end;
  Result := res;
end;

function PrimerLetraCadaPalabraMayuscula(cad: String): String;
var
  i, n: Byte;
  inicioPalabra: Boolean;
begin
  n := Length(cad);
  inicioPalabra := True;
  i := 1;
  while i <= n do
  begin
    if cad[i] <> ' ' then
    begin
      if inicioPalabra then
      begin
        cad[i] := UpCase(cad[i]);
        inicioPalabra := False;
      end;
    end
    else
    begin
      inicioPalabra := True;
    end;
    i := i + 1;
  end;
  Result := cad;
end;


{ ============================================================================ }
{                              EXAMEN 4: 2023-2 Z2                             }
{ ============================================================================ }

function EliminarDigitoPosicionK(n: LongWord; k: Byte): LongWord;
var
  res, pot: LongWord;
  pos, d: Byte;
begin
  res := 0;
  pot := 1;
  pos := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if pos <> k then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    pos := pos + 1;
    n := n div 10;
  end;
  Result := res;
end;

function CantidadVocalesPorPalabra(cad: String): String;
var
  n, i, cantVoc: Byte;
  res: String;
  enPalabra: Boolean;
begin
  n := Length(cad);
  res := '';
  cantVoc := 0;
  enPalabra := False;
  i := 1;
  while i <= n do
  begin
    if cad[i] <> ' ' then
    begin
      enPalabra := True;
      if EsVocal(cad[i]) then
        cantVoc := cantVoc + 1;
    end
    else
    begin
      if enPalabra then
      begin
        if res <> '' then
          res := res + ', ';
        res := res + IntToStr(cantVoc);
        cantVoc := 0;
        enPalabra := False;
      end;
    end;
    i := i + 1;
  end;
  // Procesar última palabra
  if enPalabra then
  begin
    if res <> '' then
      res := res + ', ';
    res := res + IntToStr(cantVoc);
  end;
  Result := res;
end;


{ ============================================================================ }
{                              EXAMEN 5: 2023-1 Z2                             }
{ ============================================================================ }

// Denominadores: 5, 6, 11, 17, 28, 45, 73...
function Denominador_2023_1_Z2(k: Integer): Int64;
var
  a, b, c: Int64;
  i: Integer;
begin
  if k = 1 then
    Result := 5
  else if k = 2 then
    Result := 6
  else
  begin
    a := 5;
    b := 6;
    c := 11;
    i := 3;
    while i <= k do
    begin
      c := a + b;
      a := b;
      b := c;
      i := i + 1;
    end;
    Result := c;
  end;
end;

function SumaSerie_2023_1_Z2(n: Integer): Real;
var
  sum: Real;
  i: Integer;
  num, den: Int64;
begin
  sum := 0.0;
  i := 1;
  while i <= n do
  begin
    num := PotenciaManual(i, i);
    den := Denominador_2023_1_Z2(i);
    sum := sum + (num / den);
    i := i + 1;
  end;
  Result := sum;
end;

function InvertirPalabraAux(pal: String): String;
var
  res: String;
  i: Integer;
begin
  res := '';
  i := Length(pal);
  while i >= 1 do
  begin
    res := res + pal[i];
    i := i - 1;
  end;
  Result := res;
end;

function InvertirCadaPalabra(cad: String): String;
var
  n, i, pIni, pFin: Byte;
  pal, res: String;
begin
  n := Length(cad);
  res := '';
  i := 1;
  while i <= n do
  begin
    if cad[i] = ' ' then
    begin
      res := res + ' ';
      i := i + 1;
    end
    else
    begin
      pIni := i;
      while (i <= n) and (cad[i] <> ' ') do
        i := i + 1;
      pFin := i - 1;
      pal := Copy(cad, pIni, pFin - pIni + 1);
      res := res + InvertirPalabraAux(pal);
    end;
  end;
  Result := res;
end;


{ ============================================================================ }
{                              EXAMEN 6: 2023-1 PIZARRA                        }
{ ============================================================================ }

function SumaSerie_2023_1_Pizarra(n: Integer): Real;
var
  sum: Real;
  i, fibVal: Integer;
  num, den: Int64;
begin
  sum := 0.0;
  i := 1;
  while i <= n do
  begin
    num := i * i;
    fibVal := FibTermino(i);
    den := Factorial(fibVal);
    sum := sum + (num / den);
    i := i + 1;
  end;
  Result := sum;
end;

procedure PromediosParEImpar(n: LongWord; var promPar, promImpar: Real);
var
  d, cantPar, cantImp: Byte;
  sumPar, sumImp: LongWord;
begin
  cantPar := 0;
  cantImp := 0;
  sumPar := 0;
  sumImp := 0;

  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) then
    begin
      sumPar := sumPar + d;
      cantPar := cantPar + 1;
    end
    else
    begin
      sumImp := sumImp + d;
      cantImp := cantImp + 1;
    end;
    n := n div 10;
  end;

  if cantPar > 0 then
    promPar := sumPar / cantPar
  else
    promPar := 0.0;

  if cantImp > 0 then
    promImpar := sumImp / cantImp
  else
    promImpar := 0.0;
end;


{ ============================================================================ }
{                              EXAMEN 7: 2022-1                                }
{ ============================================================================ }

function DigitoMayorMultiplo3(n: LongWord): Integer;
var
  d: Byte;
  mayor: Integer;
begin
  mayor := -1;
  while n > 0 do
  begin
    d := n mod 10;
    // Múltiplos no nulos de 3 (3, 6, 9)
    if (d mod 3 = 0) and (d > 0) then
    begin
      if d > mayor then
        mayor := d;
    end;
    n := n div 10;
  end;
  Result := mayor;
end;

function TerminoSerieEntrelazada_2022(k: Integer): Int64;
var
  subIndice: Integer;
begin
  if (k mod 2 = 1) then
  begin
    // Posición impar (1->4, 3->8, 5->12, 7->16...): subIndice = (k div 2) + 1
    subIndice := (k div 2) + 1;
    Result := 4 * subIndice;
  end
  else
  begin
    // Posición par (2->2, 4->6, 6->18, 8->54...): 2 * 3^(subIndice - 1)
    subIndice := k div 2;
    Result := 2 * PotenciaManual(3, subIndice - 1);
  end;
end;

function PromedioSerie_2022_1(n: Integer): Real;
var
  sum: Real;
  i: Integer;
begin
  if n <= 0 then
  begin
    Result := 0.0;
    Exit;
  end;

  sum := 0.0;
  i := 1;
  while i <= n do
  begin
    sum := sum + TerminoSerieEntrelazada_2022(i);
    i := i + 1;
  end;
  Result := sum / n;
end;

function ContarPalabrasTerminanVocal(cad: String): Integer;
var
  n, i, pIni, pFin, cant: Byte;
  pal: String;
begin
  n := Length(cad);
  cant := 0;
  i := 1;
  while i <= n do
  begin
    if cad[i] = ' ' then
      i := i + 1
    else
    begin
      pIni := i;
      while (i <= n) and (cad[i] <> ' ') do
        i := i + 1;
      pFin := i - 1;
      pal := Copy(cad, pIni, pFin - pIni + 1);
      if (Length(pal) > 0) and EsVocal(pal[Length(pal)]) then
        cant := cant + 1;
    end;
  end;
  Result := cant;
end;

function ContarPalabrasInicianMayuscula(cad: String): Integer;
var
  n, i, pIni, pFin, cant: Byte;
  pal: String;
begin
  n := Length(cad);
  cant := 0;
  i := 1;
  while i <= n do
  begin
    if cad[i] = ' ' then
      i := i + 1
    else
    begin
      pIni := i;
      while (i <= n) and (cad[i] <> ' ') do
        i := i + 1;
      pFin := i - 1;
      pal := Copy(cad, pIni, pFin - pIni + 1);
      if (Length(pal) > 0) and EsMayuscula(pal[1]) then
        cant := cant + 1;
    end;
  end;
  Result := cant;
end;

function ExtraerCaracteresIndicesPares(cad: String): String;
var
  res: String;
  i, n: Byte;
begin
  res := '';
  n := Length(cad);
  i := 2; // Inicia en el primer índice par
  while i <= n do
  begin
    res := res + cad[i];
    i := i + 2; // Salto de 2 en 2
  end;
  Result := res;
end;


{ ============================================================================ }
{          PLUS: CLASE ORDENACIÓN DE CADENAS DE ESTA SEMANA (BURBUJA)          }
{ ============================================================================ }

function OrdenarCaracteresBurbujaAscendente(pal: String): String;
var
  n, i, j: Byte;
  aux: Char;
begin
  n := Length(pal);
  i := 1;
  while i <= n - 1 do
  begin
    j := i + 1;
    while j <= n do
    begin
      if pal[i] > pal[j] then
      begin
        aux := pal[i];
        pal[i] := pal[j];
        pal[j] := aux;
      end;
      j := j + 1;
    end;
    i := i + 1;
  end;
  Result := pal;
end;

function OrdenarCaracteresBurbujaDescendente(pal: String): String;
var
  n, i, j: Byte;
  aux: Char;
begin
  n := Length(pal);
  i := 1;
  while i <= n - 1 do
  begin
    j := i + 1;
    while j <= n do
    begin
      if pal[i] < pal[j] then
      begin
        aux := pal[i];
        pal[i] := pal[j];
        pal[j] := aux;
      end;
      j := j + 1;
    end;
    i := i + 1;
  end;
  Result := pal;
end;

function OrdenarUltimaPalabra(cad: String): String;
var
  n, i, finPal, iniPal: Byte;
  palOrdenada: String;
begin
  n := Length(cad);
  i := n;
  while (i >= 1) and (cad[i] = ' ') do
    i := i - 1;
  finPal := i;

  while (i >= 1) and (cad[i] <> ' ') do
    i := i - 1;
  iniPal := i + 1;

  if finPal >= iniPal then
  begin
    palOrdenada := OrdenarCaracteresBurbujaAscendente(Copy(cad, iniPal, finPal - iniPal + 1));
    Result := Copy(cad, 1, iniPal - 1) + palOrdenada + Copy(cad, finPal + 1, n - finPal);
  end
  else
    Result := cad;
end;

// Obtener límites (inicio y fin) de la k-ésima palabra
procedure ObtenerLimitesPalabraK(cad: String; k: Byte; var iniPal, finPal: Byte);
var
  n, i, contPal: Byte;
begin
  n := Length(cad);
  iniPal := 0;
  finPal := 0;
  contPal := 0;
  i := 1;
  while i <= n do
  begin
    if cad[i] = ' ' then
      i := i + 1
    else
    begin
      contPal := contPal + 1;
      if contPal = k then
      begin
        iniPal := i;
        while (i <= n) and (cad[i] <> ' ') do
          i := i + 1;
        finPal := i - 1;
        Exit;
      end
      else
      begin
        while (i <= n) and (cad[i] <> ' ') do
          i := i + 1;
      end;
    end;
  end;
end;

function InvertirSegundaPalabra(cad: String): String;
var
  n, pIni, pFin: Byte;
  palInvertida: String;
begin
  n := Length(cad);
  ObtenerLimitesPalabraK(cad, 2, pIni, pFin);
  if (pIni > 0) and (pFin >= pIni) then
  begin
    palInvertida := InvertirPalabraAux(Copy(cad, pIni, pFin - pIni + 1));
    Result := Copy(cad, 1, pIni - 1) + palInvertida + Copy(cad, pFin + 1, n - pFin);
  end
  else
    Result := cad;
end;

function OrdenarSegundaPalabra(cad: String): String;
var
  n, pIni, pFin: Byte;
  palOrdenada: String;
begin
  n := Length(cad);
  ObtenerLimitesPalabraK(cad, 2, pIni, pFin);
  if (pIni > 0) and (pFin >= pIni) then
  begin
    palOrdenada := OrdenarCaracteresBurbujaAscendente(Copy(cad, pIni, pFin - pIni + 1));
    Result := Copy(cad, 1, pIni - 1) + palOrdenada + Copy(cad, pFin + 1, n - pFin);
  end
  else
    Result := cad;
end;

end.

