unit UnitCadenasAvanzadas;

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
  LABORATORIO AVANZADO DE CADENAS: COMPARATIVA NATIVAS VS MANUALES,
  ALGORITMOS ESTRELLA DE EXAMEN E INSPECTOR ASCII
  ============================================================================ }

interface

uses
  SysUtils;

// ============================================================================
// 1. COMPARATIVA: REEMPLAZOS MANUALES DE FUNCIONES NATIVAS DE DELPHI
// ============================================================================

// Reemplazo manual de Copy(cad, desde, cant)
function CopiarManual(cad: string; desde, cant: Integer): string;

// Reemplazo manual de Pos(subcad, cad)
function PosicionManual(subcad, cad: string): Integer;

// Reemplazo manual de Delete(cad, desde, cant)
function EliminarRangoManual(cad: string; desde, cant: Integer): string;

// Reemplazo manual de Insert(subcad, cad, pos)
function InsertarManual(subcad, cad: string; pos: Integer): string;

// Reemplazo manual de Trim(cad) (elimina espacios iniciales y finales)
function TrimManual(cad: string): string;

// Reemplazo manual de UpCase usando matemática ASCII (c - 32)
function UpCaseManual(c: Char): Char;

// ============================================================================
// 2. ALGORITMOS ESTRELLA DE EXAMEN (METODOLOGÍA DE LA DOCENTE)
// ============================================================================

// Algoritmo 1: Invertir cada palabra individualmente manteniendo su orden
// Ejemplo: 'Hola mundo' -> 'aloH odnum'
function InvertirPalabrasIndividuales(cad: string; n, i: byte): string;

// Algoritmo 2: Cifrado César con clave K (desplazamiento modular de caracteres)
// Ejemplo: 'HOLA', k = 3 -> 'KROD'
function CifradoCesar(cad: string; k: Integer; n, i: byte): string;

// Algoritmo 3: Intercalar dos cadenas carácter por carácter
// Ejemplo: 'HOLA', '123456' -> 'H1O2L3A456'
function IntercalarDosCadenas(cad1, cad2: string): string;

// Algoritmo 4: Eliminar caracteres duplicados dejando solo la primera aparición
// Ejemplo: 'programacion' -> 'progamin'
function EliminarCaracteresRepetidos(cad: string; n, i: byte): string;

// Algoritmo 5: Formato Título (Capitalizar primera letra de cada palabra)
// Ejemplo: 'pedro perez' -> 'Pedro Perez'
function FormatoTitulo(cad: string; n, i: byte): string;

implementation

// ============================================================================
// 1. IMPLEMENTACIÓN DE FUNCIONES MANUALES (SIN USAR LIBRERÍAS DE DELPHI)
// ============================================================================

function UpCaseManual(c: Char): Char;
begin
  // 'a' = 97, 'z' = 122 | 'A' = 65, 'Z' = 90 (diferencia 32)
  if (c >= 'a') and (c <= 'z') then
    Result := Chr(Ord(c) - 32)
  else
    Result := c;
end;

function CopiarManual(cad: string; desde, cant: Integer): string;
var
  i, fin, n: Integer;
  res: string;
begin
  res := '';
  n := Length(cad);
  if (desde >= 1) and (desde <= n) and (cant > 0) then
  begin
    fin := desde + cant - 1;
    if fin > n then fin := n;
    for i := desde to fin do
      res := res + cad[i];
  end;
  Result := res;
end;

function PosicionManual(subcad, cad: string): Integer;
var
  i, j, nSub, nCad: Integer;
  coincide: Boolean;
begin
  nSub := Length(subcad);
  nCad := Length(cad);
  Result := 0;
  if (nSub = 0) or (nCad = 0) or (nSub > nCad) then Exit;

  for i := 1 to nCad - nSub + 1 do
  begin
    coincide := True;
    for j := 1 to nSub do
    begin
      if cad[i + j - 1] <> subcad[j] then
      begin
        coincide := False;
        Break;
      end;
    end;
    if coincide then
    begin
      Result := i;
      Exit;
    end;
  end;
end;

function EliminarRangoManual(cad: string; desde, cant: Integer): string;
var
  i, n, fin: Integer;
  res: string;
begin
  res := '';
  n := Length(cad);
  fin := desde + cant - 1;
  for i := 1 to n do
  begin
    // Si la posición i no está dentro del rango que queremos borrar
    if (i < desde) or (i > fin) then
      res := res + cad[i];
  end;
  Result := res;
end;

function InsertarManual(subcad, cad: string; pos: Integer): string;
var
  i, n: Integer;
  res: string;
begin
  res := '';
  n := Length(cad);
  if pos <= 1 then
    res := subcad + cad
  else if pos > n then
    res := cad + subcad
  else
  begin
    for i := 1 to pos - 1 do
      res := res + cad[i];
    res := res + subcad;
    for i := pos to n do
      res := res + cad[i];
  end;
  Result := res;
end;

function TrimManual(cad: string): string;
var
  ini, fin, n: Integer;
  res: string;
begin
  n := Length(cad);
  ini := 1;
  while (ini <= n) and (cad[ini] = ' ') do
    ini := ini + 1;

  fin := n;
  while (fin >= ini) and (cad[fin] = ' ') do
    fin := fin - 1;

  res := '';
  while ini <= fin do
  begin
    res := res + cad[ini];
    ini := ini + 1;
  end;
  Result := res;
end;

// ============================================================================
// 2. IMPLEMENTACIÓN DE ALGORITMOS ESTRELLA DE EXAMEN
// ============================================================================

// Algoritmo 1: Invertir cada palabra individualmente
// 'Hola mundo' -> 'aloH odnum'
function InvertirPalabrasIndividuales(cad: string; n, i: byte): string;
var
  palabra, salida: string;
  j: Integer;
begin
  cad := cad + ' '; // centinela
  n := Length(cad);
  salida := '';
  palabra := '';
  i := 1;
  while i <= n do
  begin
    if cad[i] <> ' ' then
      palabra := palabra + cad[i]
    else
    begin
      if palabra <> '' then
      begin
        // Invertir la palabra acumulada
        for j := Length(palabra) downto 1 do
          salida := salida + palabra[j];
        salida := salida + ' ';
        palabra := '';
      end;
    end;
    i := i + 1;
  end;
  // Quitar el último espacio sobrante
  if (Length(salida) > 0) and (salida[Length(salida)] = ' ') then
    SetLength(salida, Length(salida) - 1);
  Result := salida;
end;

// Algoritmo 2: Cifrado César
function CifradoCesar(cad: string; k: Integer; n, i: byte): string;
var
  c: Char;
  res: string;
begin
  res := '';
  k := k mod 26;
  if k < 0 then k := k + 26;
  i := 1;
  while i <= n do
  begin
    c := cad[i];
    if (c >= 'A') and (c <= 'Z') then
      c := Chr(Ord('A') + ((Ord(c) - Ord('A') + k) mod 26))
    else if (c >= 'a') and (c <= 'z') then
      c := Chr(Ord('a') + ((Ord(c) - Ord('a') + k) mod 26));
    res := res + c;
    i := i + 1;
  end;
  Result := res;
end;

// Algoritmo 3: Intercalar dos cadenas
function IntercalarDosCadenas(cad1, cad2: string): string;
var
  i, n1, n2, maxLen: Integer;
  res: string;
begin
  res := '';
  n1 := Length(cad1);
  n2 := Length(cad2);
  if n1 > n2 then maxLen := n1 else maxLen := n2;

  for i := 1 to maxLen do
  begin
    if i <= n1 then res := res + cad1[i];
    if i <= n2 then res := res + cad2[i];
  end;
  Result := res;
end;

// Algoritmo 4: Eliminar caracteres repetidos
function EliminarCaracteresRepetidos(cad: string; n, i: byte): string;
var
  res: string;
  j: Integer;
  yaExiste: Boolean;
begin
  res := '';
  i := 1;
  while i <= n do
  begin
    yaExiste := False;
    for j := 1 to Length(res) do
    begin
      if UpCase(res[j]) = UpCase(cad[i]) then
      begin
        yaExiste := True;
        Break;
      end;
    end;
    if (not yaExiste) or (cad[i] = ' ') then
      res := res + cad[i];
    i := i + 1;
  end;
  Result := res;
end;

// Algoritmo 5: Formato Título (Capitalizar primera letra de cada palabra)
function FormatoTitulo(cad: string; n, i: byte): string;
var
  res: string;
  esInicio: Boolean;
  c: Char;
begin
  res := '';
  esInicio := True;
  i := 1;
  while i <= n do
  begin
    c := cad[i];
    if c <> ' ' then
    begin
      if esInicio then
      begin
        c := UpCaseManual(c);
        esInicio := False;
      end
      else
      begin
        if (c >= 'A') and (c <= 'Z') then
          c := Chr(Ord(c) + 32); // minúscula
      end;
    end
    else
      esInicio := True;

    res := res + c;
    i := i + 1;
  end;
  Result := res;
end;

end.
