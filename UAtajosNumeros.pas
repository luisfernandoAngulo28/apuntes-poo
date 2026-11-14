unit UAtajosNumeros;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

{ ============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE CIENCIAS DE LA COMPUTACIÓN Y TECNOLOGÍA
  MATERIA: INTRODUCCIÓN A LA INFORMÁTICA (INF-110)
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
  
  LIBRERÍA MODULAR ATÓMICA: HOJA DE ATAJOS MAESTRA PARA NÚMEROS Y DÍGITOS
  Filosofía: "Divide y Vencerás" · Clean Code · Estándares Delphi
  ============================================================================ }

interface

uses
  SysUtils;

// ============================================================================
// BLOQUE 0: OPERACIONES ATÓMICAS FUNDAMENTALES (MOD 10 Y DIV 10)
// ============================================================================
function ExtraerUltimoDigito(N: Cardinal): Byte;
function EliminarUltimoDigito(N: Cardinal): Cardinal;
function AgregarDigitoDerecha(N: Cardinal; Digito: Byte): Cardinal;
function Potencia10(Exponente: Byte): Cardinal;
function PrimerDigito(N: Cardinal): Byte;
function UltimoDigito(N: Cardinal): Byte;
function ContarDigitos(N: Cardinal): Byte;

// ============================================================================
// BLOQUE 1: INVERSIÓN, CAPICÚAS Y SIMETRÍAS
// ============================================================================
function InvertirNumero(N: Cardinal): Cardinal;
function EsCapicua(N: Cardinal): Boolean;
function ExtraerMitadIzquierda(N: Cardinal): Cardinal;
function ExtraerMitadDerecha(N: Cardinal): Cardinal;
// Examen 2024-1 Z2: Mitad derecha capicúa
function MitadDerechaEsCapicua(N: Cardinal; out MitadExtraida: Cardinal): Boolean;
// Examen 2024-1 R: Mitad izquierda capicúa
function MitadIzquierdaEsCapicua(N: Cardinal; out MitadExtraida: Cardinal): Boolean;

// ============================================================================
// BLOQUE 2: PROPIEDADES MATEMÁTICAS, PRIMOS Y RAÍCES DIGITALES
// ============================================================================
function EsDigitoPrimo(Digito: Byte): Boolean;
function TodosDigitosPrimos(N: Cardinal): Boolean;
function PrimeroYUltimoDigitoPrimos(N: Cardinal): Boolean;
function SumarDigitos(N: Cardinal): Cardinal;
function MultiplicarDigitos(N: Cardinal): Cardinal;
// Examen 2023-1 SF: Sumar dígitos recursivamente hasta que sea < 10 (Raíz Digital)
function RaizDigital(N: Cardinal): Byte;
function EsNumeroPrimo(N: Cardinal): Boolean;

// ============================================================================
// BLOQUE 3: CONTEO, FILTRADO Y TRANSFORMACIÓN DE DÍGITOS
// ============================================================================
function ContarDigitosPares(N: Cardinal): Byte;
function ContarDigitosImpares(N: Cardinal): Byte;
procedure SumarParesEImpares(N: Cardinal; out SumaPares, SumaImpares: Cardinal);
function EliminarCeros(N: Cardinal): Cardinal;
function TodosDigitosIguales(N: Cardinal): Boolean;
function DigitosOrdenadosAsc(N: Cardinal): Boolean;
function FrecuenciaDigito(N: Cardinal; DigitoBuscado: Byte): Byte;
function TieneDigitosRepetidos(N: Cardinal): Boolean;
// Examen 2023-2 Z2: Eliminar dígitos repetidos dejando solo los únicos
function EliminarDigitosRepetidos(N: Cardinal): Cardinal;
// Examen 2024-1 SF: Separar dígitos menores y mayores/iguales a un criterio
procedure SepararDigitosMenoresYMayores(N: Cardinal; Criterio: Byte; out Menores, Mayores: Cardinal);

// ============================================================================
// BLOQUE 4: CONVERSIÓN DE BASES Y OPERACIONES DE BITS
// ============================================================================
function ConvertirABinario(N: Cardinal): string;
function ConvertirAOctal(N: Cardinal): string;
function ConvertirAHexadecimal(N: Cardinal): string;
function EsPalindromoBinario(N: Cardinal): Boolean;
function ContarBitsUno(N: Cardinal): Byte;

implementation

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 0: OPERACIONES ATÓMICAS FUNDAMENTALES
// ============================================================================

function ExtraerUltimoDigito(N: Cardinal): Byte;
begin
  Result := N mod 10;
end;

function EliminarUltimoDigito(N: Cardinal): Cardinal;
begin
  Result := N div 10;
end;

function AgregarDigitoDerecha(N: Cardinal; Digito: Byte): Cardinal;
begin
  Result := (N * 10) + Digito;
end;

function Potencia10(Exponente: Byte): Cardinal;
var
  i: Byte;
  P: Cardinal;
begin
  P := 1;
  for i := 1 to Exponente do
    P := P * 10;
  Result := P;
end;

function PrimerDigito(N: Cardinal): Byte;
begin
  while N >= 10 do
    N := N div 10;
  Result := N;
end;

function UltimoDigito(N: Cardinal): Byte;
begin
  Result := N mod 10;
end;

function ContarDigitos(N: Cardinal): Byte;
var
  Contador: Byte;
begin
  Contador := 0;
  repeat
    Inc(Contador);
    N := N div 10;
  until N = 0;
  Result := Contador;
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 1: INVERSIÓN Y SIMETRÍAS
// ============================================================================

function InvertirNumero(N: Cardinal): Cardinal;
var
  Invertido: Cardinal;
begin
  Invertido := 0;
  while N > 0 do
  begin
    Invertido := (Invertido * 10) + (N mod 10);
    N := N div 10;
  end;
  Result := Invertido;
end;

function EsCapicua(N: Cardinal): Boolean;
begin
  Result := (N = InvertirNumero(N));
end;

function ExtraerMitadIzquierda(N: Cardinal): Cardinal;
var
  TotalDigitos, Mitad: Byte;
begin
  TotalDigitos := ContarDigitos(N);
  Mitad := TotalDigitos div 2;
  if Mitad = 0 then
    Result := N
  else
    Result := N div Potencia10(TotalDigitos - Mitad);
end;

function ExtraerMitadDerecha(N: Cardinal): Cardinal;
var
  TotalDigitos, Mitad: Byte;
begin
  TotalDigitos := ContarDigitos(N);
  Mitad := TotalDigitos div 2;
  if Mitad = 0 then
    Result := N
  else
    Result := N mod Potencia10(Mitad);
end;

function MitadDerechaEsCapicua(N: Cardinal; out MitadExtraida: Cardinal): Boolean;
begin
  MitadExtraida := ExtraerMitadDerecha(N);
  Result := EsCapicua(MitadExtraida);
end;

function MitadIzquierdaEsCapicua(N: Cardinal; out MitadExtraida: Cardinal): Boolean;
begin
  MitadExtraida := ExtraerMitadIzquierda(N);
  Result := EsCapicua(MitadExtraida);
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 2: PROPIEDADES MATEMÁTICAS Y PRIMOS
// ============================================================================

function EsDigitoPrimo(Digito: Byte): Boolean;
begin
  Result := Digito in [2, 3, 5, 7];
end;

function TodosDigitosPrimos(N: Cardinal): Boolean;
begin
  repeat
    if not EsDigitoPrimo(N mod 10) then
      Exit(False);
    N := N div 10;
  until N = 0;
  Result := True;
end;

function PrimeroYUltimoDigitoPrimos(N: Cardinal): Boolean;
begin
  Result := EsDigitoPrimo(PrimerDigito(N)) and EsDigitoPrimo(UltimoDigito(N));
end;

function SumarDigitos(N: Cardinal): Cardinal;
var
  Suma: Cardinal;
begin
  Suma := 0;
  while N > 0 do
  begin
    Suma := Suma + (N mod 10);
    N := N div 10;
  end;
  Result := Suma;
end;

function MultiplicarDigitos(N: Cardinal): Cardinal;
var
  Producto: Cardinal;
begin
  if N = 0 then
    Exit(0);
  Producto := 1;
  while N > 0 do
  begin
    Producto := Producto * (N mod 10);
    N := N div 10;
  end;
  Result := Producto;
end;

function RaizDigital(N: Cardinal): Byte;
var
  Suma, Auxiliar: Cardinal;
begin
  while N >= 10 do
  begin
    Suma := 0;
    Auxiliar := N;
    while Auxiliar > 0 do
    begin
      Suma := Suma + (Auxiliar mod 10);
      Auxiliar := Auxiliar div 10;
    end;
    N := Suma;
  end;
  Result := N;
end;

function EsNumeroPrimo(N: Cardinal): Boolean;
var
  i: Cardinal;
begin
  if N < 2 then Exit(False);
  if (N = 2) or (N = 3) then Exit(True);
  if (N mod 2 = 0) or (N mod 3 = 0) then Exit(False);
  i := 5;
  while (i * i) <= N do
  begin
    if (N mod i = 0) or (N mod (i + 2) = 0) then Exit(False);
    i := i + 6;
  end;
  Result := True;
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 3: CONTEO, FILTRADO Y TRANSFORMACIÓN
// ============================================================================

function ContarDigitosPares(N: Cardinal): Byte;
var
  Contador: Byte;
begin
  if N = 0 then Exit(1);
  Contador := 0;
  while N > 0 do
  begin
    if ((N mod 10) mod 2 = 0) then
      Inc(Contador);
    N := N div 10;
  end;
  Result := Contador;
end;

function ContarDigitosImpares(N: Cardinal): Byte;
var
  Contador: Byte;
begin
  if N = 0 then Exit(0);
  Contador := 0;
  while N > 0 do
  begin
    if ((N mod 10) mod 2 <> 0) then
      Inc(Contador);
    N := N div 10;
  end;
  Result := Contador;
end;

procedure SumarParesEImpares(N: Cardinal; out SumaPares, SumaImpares: Cardinal);
var
  Dig: Byte;
begin
  SumaPares := 0;
  SumaImpares := 0;
  while N > 0 do
  begin
    Dig := N mod 10;
    if (Dig mod 2 = 0) then
      SumaPares := SumaPares + Dig
    else
      SumaImpares := SumaImpares + Dig;
    N := N div 10;
  end;
end;

function EliminarCeros(N: Cardinal): Cardinal;
var
  Resultado, Multiplicador: Cardinal;
  Digito: Byte;
begin
  Resultado := 0;
  Multiplicador := 1;
  while N > 0 do
  begin
    Digito := N mod 10;
    if Digito <> 0 then
    begin
      Resultado := Resultado + (Digito * Multiplicador);
      Multiplicador := Multiplicador * 10;
    end;
    N := N div 10;
  end;
  Result := Resultado;
end;

function TodosDigitosIguales(N: Cardinal): Boolean;
var
  PrimerD: Byte;
begin
  PrimerD := N mod 10;
  while N > 0 do
  begin
    if (N mod 10) <> PrimerD then
      Exit(False);
    N := N div 10;
  end;
  Result := True;
end;

function DigitosOrdenadosAsc(N: Cardinal): Boolean;
var
  DigitoDerecho, DigitoIzquierdo: Byte;
begin
  while N >= 10 do
  begin
    DigitoDerecho := N mod 10;
    N := N div 10;
    DigitoIzquierdo := N mod 10;
    if DigitoIzquierdo > DigitoDerecho then
      Exit(False);
  end;
  Result := True;
end;

function FrecuenciaDigito(N: Cardinal; DigitoBuscado: Byte): Byte;
var
  Contador: Byte;
begin
  if (N = 0) and (DigitoBuscado = 0) then Exit(1);
  Contador := 0;
  while N > 0 do
  begin
    if (N mod 10) = DigitoBuscado then
      Inc(Contador);
    N := N div 10;
  end;
  Result := Contador;
end;

function TieneDigitosRepetidos(N: Cardinal): Boolean;
var
  Frecuencias: array[0..9] of Byte;
  d: Byte;
begin
  for d := 0 to 9 do Frecuencias[d] := 0;
  if N = 0 then Exit(False);
  while N > 0 do
  begin
    d := N mod 10;
    Inc(Frecuencias[d]);
    if Frecuencias[d] > 1 then
      Exit(True);
    N := N div 10;
  end;
  Result := False;
end;

function EliminarDigitosRepetidos(N: Cardinal): Cardinal;
var
  NumeroOriginal, Auxiliar, Resultado, Multiplicador: Cardinal;
  Digito: Byte;
  Frecuencia: Byte;
begin
  NumeroOriginal := N;
  Resultado := 0;
  Multiplicador := 1;
  while N > 0 do
  begin
    Digito := N mod 10;
    // Contar frecuencia en el número original
    Frecuencia := 0;
    Auxiliar := NumeroOriginal;
    while Auxiliar > 0 do
    begin
      if (Auxiliar mod 10) = Digito then
        Inc(Frecuencia);
      Auxiliar := Auxiliar div 10;
    end;

    if Frecuencia = 1 then
    begin
      Resultado := Resultado + (Digito * Multiplicador);
      Multiplicador := Multiplicador * 10;
    end;
    N := N div 10;
  end;
  Result := Resultado;
end;

procedure SepararDigitosMenoresYMayores(N: Cardinal; Criterio: Byte; out Menores, Mayores: Cardinal);
var
  Digito: Byte;
begin
  Menores := 0;
  Mayores := 0;
  while N > 0 do
  begin
    Digito := N mod 10;
    if Digito < Criterio then
      Menores := (Menores * 10) + Digito
    else
      Mayores := (Mayores * 10) + Digito;
    N := N div 10;
  end;
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 4: CONVERSIÓN DE BASES Y BITS
// ============================================================================

function ConvertirABinario(N: Cardinal): string;
var
  Resultado: string;
begin
  if N = 0 then Exit('0');
  Resultado := '';
  while N > 0 do
  begin
    Resultado := IntToStr(N mod 2) + Resultado;
    N := N div 2;
  end;
  Result := Resultado;
end;

function ConvertirAOctal(N: Cardinal): string;
var
  Resultado: string;
begin
  if N = 0 then Exit('0');
  Resultado := '';
  while N > 0 do
  begin
    Resultado := IntToStr(N mod 8) + Resultado;
    N := N div 8;
  end;
  Result := Resultado;
end;

function ConvertirAHexadecimal(N: Cardinal): string;
const
  DigitosHex: array[0..15] of Char = '0123456789ABCDEF';
var
  Resultado: string;
begin
  if N = 0 then Exit('0');
  Resultado := '';
  while N > 0 do
  begin
    Resultado := DigitosHex[N mod 16] + Resultado;
    N := N div 16;
  end;
  Result := Resultado;
end;

function EsPalindromoBinario(N: Cardinal): Boolean;
var
  Binario: string;
  i, Len: Integer;
begin
  Binario := ConvertirABinario(N);
  Len := Length(Binario);
  for i := 1 to Len div 2 do
  begin
    if Binario[i] <> Binario[Len - i + 1] then
      Exit(False);
  end;
  Result := True;
end;

function ContarBitsUno(N: Cardinal): Byte;
var
  Contador: Byte;
begin
  Contador := 0;
  while N > 0 do
  begin
    if (N mod 2 = 1) then
      Inc(Contador);
    N := N div 2;
  end;
  Result := Contador;
end;

end.

