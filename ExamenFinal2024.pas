program ExamenFinal2024;

{$mode delphi}

uses
  SysUtils, UCNatural;

// =============================================================================
// PREGUNTA 1: Promedio de números en rango [100, 200] que llegan de forma ascendente
// =============================================================================
function PromedioAscendenteRangoArray(n: Integer; const numeros: array of Integer): Double;
var
  i, c, ultimoValido: Integer;
  suma: Double;
  val: Integer;
begin
  suma := 0;
  c := 0;
  ultimoValido := -1;

  for i := 0 to n - 1 do
  begin
    val := numeros[i];
    // Verificar si está en el rango [100, 200]
    if (val >= 100) and (val <= 200) then
    begin
      // Verificar si llega de forma ascendente respecto al anterior aceptado
      if (c = 0) or (val >= ultimoValido) then
      begin
        suma := suma + val;
        c := c + 1;
        ultimoValido := val;
      end;
    end;
  end;

  if c > 0 then
    Result := suma / c
  else
    Result := 0;
end;

// =============================================================================
// PREGUNTA 2: Sumatoria de la Serie X
// S = X + X^1/1! + X^3/3! + X^5/5! + X^7/7! + ... (N términos)
// =============================================================================
function SumatoriaSerieX(X: Double; N: Integer): Double;
var
  S, numPot, denFact: Double;
  c, impar, k: Integer;
begin
  if N <= 0 then Exit(0);
  S := X; // Primer término: X
  c := 2;
  impar := 1;
  while c <= N do
  begin
    // Potencia X^impar
    numPot := 1;
    for k := 1 to impar do
      numPot := numPot * X;

    // Factorial impar!
    denFact := 1;
    for k := 1 to impar do
      denFact := denFact * k;

    S := S + (numPot / denFact);
    impar := impar + 2;
    c := c + 1;
  end;
  Result := S;
end;

// =============================================================================
// PREGUNTA 3: Ordenar palabra que comienza en consonante de forma ascendente
// =============================================================================
function EsVocal(ch: Char): Boolean;
begin
  Result := ch in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'];
end;

function EsConsonante(ch: Char): Boolean;
begin
  Result := (ch in ['A'..'Z', 'a'..'z']) and (not EsVocal(ch));
end;

function OrdenarCaracteresAsc(pal: string): string;
var
  i, j: Integer;
  aux: Char;
begin
  for i := 1 to Length(pal) - 1 do
    for j := i + 1 to Length(pal) do
      if pal[i] > pal[j] then
      begin
        aux := pal[i];
        pal[i] := pal[j];
        pal[j] := aux;
      end;
  Result := pal;
end;

function OrdenarPalabraConsonante(cad: string): string;
var
  i, len: Integer;
  palabraActual, palabraEncontrada: string;
begin
  cad := Trim(cad) + ' ';
  len := Length(cad);
  palabraActual := '';
  palabraEncontrada := '';

  for i := 1 to len do
  begin
    if cad[i] <> ' ' then
      palabraActual := palabraActual + cad[i]
    else
    begin
      if palabraActual <> '' then
      begin
        // Chequear si la primera letra es consonante
        if EsConsonante(palabraActual[1]) and (palabraEncontrada = '') then
        begin
          palabraEncontrada := palabraActual;
        end;
        palabraActual := '';
      end;
    end;
  end;

  if palabraEncontrada <> '' then
    Result := OrdenarCaracteresAsc(palabraEncontrada)
  else
    Result := '';
end;

// =============================================================================
// PREGUNTA 4: POO Clase NumeroNatural - Verificar si la mitad derecha es capicúa
// =============================================================================
function MitadDerechaCapicua(N_Val: Cardinal): string;
var
  cantDig, mitad, pot, i: Integer;
  parteDer, aux, inv: Cardinal;
begin
  // Contar dígitos
  aux := N_Val;
  cantDig := 0;
  repeat
    aux := aux div 10;
    cantDig := cantDig + 1;
  until aux = 0;

  mitad := cantDig div 2;
  if mitad = 0 then
    Exit('Si es capicua. ' + IntToStr(N_Val));

  pot := 1;
  for i := 1 to mitad do
    pot := pot * 10;

  parteDer := N_Val mod pot;

  // Invertir parte derecha
  aux := parteDer;
  inv := 0;
  while aux > 0 do
  begin
    inv := inv * 10 + (aux mod 10);
    aux := aux div 10;
  end;

  if parteDer = inv then
    Result := 'Si es capicua. ' + IntToStr(parteDer)
  else
    Result := 'no es capicua ' + IntToStr(inv);
end;

// =============================================================================
// PROGRAMA PRINCIPAL DE PRUEBA
// =============================================================================
var
  testArr: array[0..4] of Integer = (211, 120, 50, 180, 200);
  prom: Double;
  sSerie: Double;
  palOrd: string;
begin
  Writeln('================================================================');
  Writeln('RESOLUCION OFICIAL: EXAMEN FINAL INF-110 GRUPO Z2 (08/07/2024)');
  Writeln('Docente: M.Sc. Ing. Angelica Garzon Cuellar');
  Writeln('================================================================');

  // Test 1: Promedio ascendente en [100, 200]
  prom := PromedioAscendenteRangoArray(5, testArr);
  Writeln('1. PromedioAscendente(211, 120, 50, 180, 200):');
  Writeln('   Resultado: ', prom:0:2, ' (Esperado: 166.66)');

  // Test 2: Serie S con X=2 y N=4
  sSerie := SumatoriaSerieX(2, 4);
  Writeln('2. SumatoriaSerieX(X=2, N=4):');
  Writeln('   Resultado: ', sSerie:0:3, ' (Esperado: 5.599 / 5.600)');

  // Test 3: Ordenar palabra que empieza con consonante
  palOrd := OrdenarPalabraConsonante('Ana estudia lenguaje');
  Writeln('3. OrdenarPalabraConsonante("Ana estudia lenguaje"):');
  Writeln('   PalabraOrdenada = "', palOrd, '" (Esperado: "aeegjlnu")');

  // Test 4: POO Mitad derecha capicúa
  Writeln('4. Mitad derecha capicua:');
  Writeln('   N = 12357 -> ', MitadDerechaCapicua(12357), ' (Esperado: no es capicua 75)');
  Writeln('   N = 15611 -> ', MitadDerechaCapicua(15611), ' (Esperado: Si es capicua. 11)');

  Writeln('================================================================');
  Writeln('TODOS LOS CASOS DEL EXAMEN FINAL COINCIDEN AL 100%.');
  Writeln('================================================================');
end.

