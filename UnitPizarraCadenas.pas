unit UnitPizarraCadenas;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

{ ============================================================================
  UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO (UAGRM)
  FACULTAD DE CIENCIAS DE LA COMPUTACION Y TECNOLOGIA
  CARRERA: INGENIERIA INFORMATICA / SISTEMAS
  MATERIA: INTRODUCCION A LA INFORMATICA (INF110-Z2)
  DOCENTE: M.Sc. Ing. Angelica Garzon Cuellar
  CLASE: MIERCOLES 21 DE OCTUBRE & TAREA PARA EL VIERNES
  TEMA: CADENAS DE CARACTERES - BANCO COMPLETO DE EJERCICIOS Y TAREAS
  ============================================================================ }

interface

uses
  SysUtils;

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================
function EsVocal(c: Char): Boolean;
function EsConsonante(c: Char): Boolean;
function TieneDosVocalesJuntas(pal: string): Boolean;

// Firma de la docente en el IDE: inspecciona si hay 2 vocales juntas en la palabra
function contarVocalesJuntas(Cad: string; n, i: Byte): Byte;

// ============================================================================
// EJERCICIOS DE CLASE (AVANCE PIZARRA E IDE)
// ============================================================================

// 1. Invertir Cadena (Algoritmo Vectorial N - I + 1)
procedure InvertirCadena(var Cad: string);
function InvertirCadenaFn(Cad: string): string;

// 2. Contar palabras donde existan 2 vocales juntas
// Ejemplo: 'eleccion superior de bolivia' -> 3 palabras
function ContarPalabrasDosVocalesJuntas(Cad: string): Integer;

// 3. Leer una cadena y verificar si es Capicua al invertir
function EsCapicua(Cad: string): Boolean;

// 4. Contar palabras de una cadena
// Ejemplo IDE: 'Hola cadena de texto' -> 4 palabras
function ContarPalabras(Cad: string): Integer;

// 5. Mostrar los caracteres de los indices impares (omite espacios)
// Ejemplo IDE: |H|o|l|a| |M|u|n|d|o| -> 'hlud'
function MostrarIndicesImpares(Cad: string): string;

// 6. Contar las consonantes que tiene una cadena
// Ejemplo IDE: 'cadena de texto' -> 7 consonantes
function ContarConsonantes(Cad: string): Integer;

// ============================================================================
// TAREA PARA EL VIERNES (2 EJERCICIOS)
// ============================================================================

// Tarea 1: Buscar Caracter y mostrar posiciones
// Ejemplo: 'Hola cadena de texto', 'a' -> '4, 7, 11'
function BuscarCaracterPosiciones(Cad: string; c: Char): string;

// Tarea 2: Contar las veces que se repite un caracter buscado
// Ejemplo: 'Hola cadena de texto', 'a' -> 3
function ContarRepeticionesCaracter(Cad: string; c: Char): Integer;

implementation

// ============================================================================
// IMPLEMENTACION DE FUNCIONES AUXILIARES
// ============================================================================

function EsVocal(c: Char): Boolean;
begin
  c := UpCase(c);
  Result := (c = 'A') or (c = 'E') or (c = 'I') or (c = 'O') or (c = 'U');
end;

function EsConsonante(c: Char): Boolean;
begin
  c := UpCase(c);
  Result := (c in ['A'..'Z']) and not (c in ['A', 'E', 'I', 'O', 'U']);
end;

function TieneDosVocalesJuntas(pal: string): Boolean;
var
  i: Integer;
begin
  Result := False;
  for i := 1 to Length(pal) - 1 do
  begin
    if EsVocal(pal[i]) and EsVocal(pal[i + 1]) then
    begin
      Result := True;
      Exit;
    end;
  end;
end;

// Firma exacta del IDE del docente:
// n: longitud de la palabra, i: indice inicial de busqueda
function contarVocalesJuntas(Cad: string; n, i: Byte): Byte;
begin
  if (i >= n) or (n < 2) then
    Result := 0
  else
  begin
    if EsVocal(Cad[i]) and EsVocal(Cad[i + 1]) then
      Result := 1
    else
      Result := contarVocalesJuntas(Cad, n, i + 1);
  end;
end;

// ============================================================================
// IMPLEMENTACION DE LOS EJERCICIOS DE CLASE
// ============================================================================

procedure InvertirCadena(var Cad: string);
var
  i, n, n1, opp: Integer;
  aux: Char;
begin
  n := Length(Cad);
  n1 := n div 2;
  for i := 1 to n1 do
  begin
    opp := n - i + 1;
    aux := Cad[i];
    Cad[i] := Cad[opp];
    Cad[opp] := aux;
  end;
end;

function InvertirCadenaFn(Cad: string): string;
begin
  InvertirCadena(Cad);
  Result := Cad;
end;

function ContarPalabrasDosVocalesJuntas(Cad: string): Integer;
var
  i, cant: Integer;
  pal: string;
begin
  Cad := Trim(Cad) + ' ';
  cant := 0;
  pal := '';
  for i := 1 to Length(Cad) do
  begin
    if Cad[i] <> ' ' then
      pal := pal + Cad[i]
    else
    begin
      // Utiliza la funcion modular de la docente
      if (pal <> '') and (contarVocalesJuntas(pal, Length(pal), 1) > 0) then
        Inc(cant);
      pal := '';
    end;
  end;
  Result := cant;
end;

function EsCapicua(Cad: string): Boolean;
var
  inv: string;
begin
  inv := InvertirCadenaFn(Cad);
  Result := (AnsiLowerCase(Cad) = AnsiLowerCase(inv));
end;

function ContarPalabras(Cad: string): Integer;
var
  i, cant: Integer;
  enPalabra: Boolean;
begin
  cant := 0;
  enPalabra := False;
  for i := 1 to Length(Cad) do
  begin
    if Cad[i] <> ' ' then
    begin
      if not enPalabra then
      begin
        Inc(cant);
        enPalabra := True;
      end;
    end
    else
      enPalabra := False;
  end;
  Result := cant;
end;

function MostrarIndicesImpares(Cad: string): string;
var
  i: Integer;
  res: string;
begin
  res := '';
  for i := 1 to Length(Cad) do
  begin
    // Posicion impar (1, 3, 5, 7, 9...) y que no sea espacio
    if (i mod 2 <> 0) and (Cad[i] <> ' ') then
      res := res + LowerCase(Cad[i]);
  end;
  Result := res;
end;

function ContarConsonantes(Cad: string): Integer;
var
  i, cant: Integer;
begin
  cant := 0;
  for i := 1 to Length(Cad) do
  begin
    if EsConsonante(Cad[i]) then
      Inc(cant);
  end;
  Result := cant;
end;

// ============================================================================
// IMPLEMENTACION DE LA TAREA PARA EL VIERNES
// ============================================================================

function BuscarCaracterPosiciones(Cad: string; c: Char): string;
var
  i: Integer;
  res: string;
begin
  res := '';
  c := UpCase(c);
  for i := 1 to Length(Cad) do
  begin
    if UpCase(Cad[i]) = c then
    begin
      if res <> '' then
        res := res + ', ' + IntToStr(i)
      else
        res := IntToStr(i);
    end;
  end;
  if res = '' then
    Result := 'No encontrado'
  else
    Result := res;
end;

function ContarRepeticionesCaracter(Cad: string; c: Char): Integer;
var
  i, cant: Integer;
begin
  cant := 0;
  c := UpCase(c);
  for i := 1 to Length(Cad) do
  begin
    if UpCase(Cad[i]) = c then
      Inc(cant);
  end;
  Result := cant;
end;

end.
