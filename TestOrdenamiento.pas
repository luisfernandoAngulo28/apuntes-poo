program TestOrdenamiento;
{$mode objfpc}{$H+}

uses
  SysUtils;

// =============================================================================
// 1. MÉTODOS BASE DE ORDENACIÓN EN CADENAS (METODOLOGÍA DE LA DOCENTE)
// =============================================================================

// Orden Ascendente ('A'..'Z') usando Burbuja / Intercambio Directo
function OrdenarCadenaAscendente(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  // Para i := 1 hasta n - 1
  for i := 1 to n - 1 do
  begin
    // Para j := i + 1 hasta n
    for j := i + 1 to n do
    begin
      if cad[i] > cad[j] then
      begin
        // Intercambio de 3 pasos
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
    end;
  end;
  Result := cad;
end;

// Versión equivalente con bucles WHILE (para traza estricta de examen)
function OrdenarCadenaAscendenteWhile(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  i := 1;
  while i <= n - 1 do
  begin
    j := i + 1;
    while j <= n do
    begin
      if cad[i] > cad[j] then
      begin
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
      j := j + 1;
    end;
    i := i + 1;
  end;
  Result := cad;
end;

// Orden Descendente ('Z'..'A')
function OrdenarCadenaDescendente(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  for i := 1 to n - 1 do
  begin
    for j := i + 1 to n do
    begin
      if cad[i] < cad[j] then
      begin
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
    end;
  end;
  Result := cad;
end;

// =============================================================================
// 2. INVERSIÓN DE UNA PALABRA / CADENA
// =============================================================================
function InvertirTexto(cad: String; n: Byte): String;
var
  i: Byte;
  res: String;
begin
  res := '';
  i := n;
  while i >= 1 do
  begin
    res := res + cad[i];
    i := i - 1;
  end;
  Result := res;
end;

// =============================================================================
// 3. MANEJO DE PALABRAS (SEGUNDA Y ÚLTIMA PALABRA)
// =============================================================================

// Extrae los límites [ini, fin] de la k-ésima palabra (k = 2 para la segunda)
procedure ObtenerLimitesPalabra(cad: String; n, k: Byte; var pIni, pFin: Byte);
var
  i, numPalabra: Byte;
  enPalabra: Boolean;
begin
  pIni := 0;
  pFin := 0;
  numPalabra := 0;
  enPalabra := false;
  i := 1;

  while i <= n do
  begin
    if cad[i] <> ' ' then
    begin
      if not enPalabra then
      begin
        enPalabra := true;
        numPalabra := numPalabra + 1;
        if numPalabra = k then
          pIni := i;
      end;
    end
    else
    begin
      if enPalabra then
      begin
        if numPalabra = k then
        begin
          pFin := i - 1;
          Exit;
        end;
        enPalabra := false;
      end;
    end;
    i := i + 1;
  end;

  if enPalabra and (numPalabra = k) then
    pFin := n;
end;

// Extrae los límites [ini, fin] de la ÚLTIMA palabra
procedure ObtenerLimitesUltimaPalabra(cad: String; n: Byte; var pIni, pFin: Byte);
var
  i: Byte;
begin
  pIni := 0;
  pFin := 0;
  if n = 0 then Exit;

  // Retroceder espacios finales si los hubiera
  i := n;
  while (i >= 1) and (cad[i] = ' ') do
    i := i - 1;

  if i = 0 then Exit; // Solo había espacios
  pFin := i;

  // Retroceder hasta encontrar un espacio o el inicio
  while (i >= 1) and (cad[i] <> ' ') do
    i := i - 1;

  pIni := i + 1;
end;

// =============================================================================
// 4. EJERCICIOS DE LA PIZARRA
// =============================================================================

// Ejercicio 4 de la pizarra: Invertir la segunda palabra de la cadena
// Entrada: 'Hola mundo de Cadena' -> Salida: 'Hola odnum de Cadena'
function InvertirSegundaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palInv, res: String;
begin
  ObtenerLimitesPalabra(cad, n, 2, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;

  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palInv := InvertirTexto(pal, lenPal);

  res := Copy(cad, 1, pIni - 1) + palInv + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;

// Ejercicio 5 de la pizarra: Ordenar la segunda palabra de la cadena
// Entrada: 'Hola mundo de Cadena' -> Salida: 'Hola dmnou de Cadena'
function OrdenarSegundaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palOrd, res: String;
begin
  ObtenerLimitesPalabra(cad, n, 2, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;

  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palOrd := OrdenarCadenaAscendente(pal, lenPal);

  res := Copy(cad, 1, pIni - 1) + palOrd + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;

// Ejercicio 3 de la pizarra: Ordenar la última palabra de la cadena
// Entrada: 'Casa de ana' -> Salida: 'Casa de aan'
function OrdenarUltimaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palOrd, res: String;
begin
  ObtenerLimitesUltimaPalabra(cad, n, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;

  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palOrd := OrdenarCadenaAscendente(pal, lenPal);

  res := Copy(cad, 1, pIni - 1) + palOrd + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;

// =============================================================================
// PROGRAMA PRINCIPAL DE PRUEBAS AUTOMÁTICAS
// =============================================================================
var
  res: String;
  passCount: Integer;

begin
  passCount := 0;
  WriteLn('=================================================================');
  WriteLn('TEST SUITE: METODOS DE ORDENACION (BURBUJA) - INTRODUCCION UAGRM');
  WriteLn('=================================================================');

  // Test 1: Vector pizarra V = '45123' -> '12345'
  res := OrdenarCadenaAscendente('45123', 5);
  WriteLn('1. OrdenarAscendente(''45123'') = ''', res, '''');
  if res = '12345' then Inc(passCount);

  // Test 2: While version
  res := OrdenarCadenaAscendenteWhile('45123', 5);
  WriteLn('2. OrdenarAscendenteWhile(''45123'') = ''', res, '''');
  if res = '12345' then Inc(passCount);

  // Test 3: Ordenar Descendente
  res := OrdenarCadenaDescendente('12345', 5);
  WriteLn('3. OrdenarDescendente(''12345'') = ''', res, '''');
  if res = '54321' then Inc(passCount);

  // Test 4: Invertir segunda palabra (Pizarra Ej 4)
  // 'Hola mundo de Cadena' -> 'Hola odnum de Cadena'
  res := InvertirSegundaPalabra('Hola mundo de Cadena', Length('Hola mundo de Cadena'));
  WriteLn('4. InvertirSegundaPalabra(''Hola mundo de Cadena'') = ''', res, '''');
  if res = 'Hola odnum de Cadena' then Inc(passCount);

  // Test 5: Ordenar segunda palabra (Pizarra Ej 5)
  // 'Hola mundo de Cadena' -> 'Hola dmnou de Cadena' ('mundo' -> 'd, m, n, o, u')
  res := OrdenarSegundaPalabra('Hola mundo de Cadena', Length('Hola mundo de Cadena'));
  WriteLn('5. OrdenarSegundaPalabra(''Hola mundo de Cadena'') = ''', res, '''');
  if res = 'Hola dmnou de Cadena' then Inc(passCount);

  // Test 6: Ordenar última palabra (Pizarra Ej 3)
  // 'Casa de ana' -> 'Casa de aan'
  res := OrdenarUltimaPalabra('Casa de ana', Length('Casa de ana'));
  WriteLn('6. OrdenarUltimaPalabra(''Casa de ana'') = ''', res, '''');
  if res = 'Casa de aan' then Inc(passCount);

  WriteLn('-----------------------------------------------------------------');
  WriteLn('RESULTADO FINAL: ', passCount, ' de 6 pruebas superadas exitosamente!');
  WriteLn('=================================================================');
end.

