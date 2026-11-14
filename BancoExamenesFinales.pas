{$mode delphi}
unit BancoExamenesFinales;

interface

uses
  SysUtils;

// =============================================================================
// EXAMEN 1: 2024-1 GRUPO Z2 (08/07/2024)
// =============================================================================
function E1_P1_PromedioAscendente(n: Integer; numeros: array of Integer): Double;
function E1_P2_SumatoriaSerieX(X: Double; N: Integer): Double;
function E1_P3_OrdenarPalabraConsonante(cad: string): string;
function E1_P4_MitadDerechaCapicua(N: Cardinal): string;

// =============================================================================
// EXAMEN 2: 2024-1 REPECHAJE (GRUPO R)
// =============================================================================
function E2_P1_SerieFactorialPotencia(n: Integer): Int64;
function E2_P2_SumarDigitosPrimosDeNumeros(numeros: array of Cardinal): Cardinal;
function E2_P3_VerificarPalabrasPalindromes(cad: string; out cant: Integer): string;

// =============================================================================
// EXAMEN 3: 2023-2 GRUPO Z2
// =============================================================================
function E3_P1_RaizDigital(N: Cardinal): Byte;
function E3_P2_SumatoriaCuadradosSobreFactorial(N: Integer): Double;
function E3_P3_PrimeroYUltimoPrimos(N: Cardinal): string;
function E3_P4_InvertirPorMitades(cad: string): string;

// =============================================================================
// EXAMEN 4: 2023-1 GRUPO SF (21/07/2023)
// =============================================================================
procedure E4_P1_DivisionRestasSucesivas(A, B: Cardinal; out cociente, residuo: Cardinal);
function E4_P2_EliminarDigitosRepetidos(N: Cardinal): Cardinal;
function E4_P3_MayorSumaDigitos(numeros: array of Cardinal): Cardinal;
function E4_P4_SerieAlternadaFactorial(N: Integer): Double;
function E4_P5_ContarYMayusculasTerminanEnA(cad: string; out cant: Integer): string;

// =============================================================================
// EXAMEN 5: 2023-2 GRUPO SF (13/12/2023)
// =============================================================================
procedure E5_P1_ContarParesEImparesHastaSuma(X: Integer; numeros: array of Integer; out pares, impares: Integer);
function E5_P2_SumatoriaSerieX_N3(X: Double; N: Integer): Double;
function E5_P3_OrdenarSegundaPalabra(cad: string): string;
function E5_P4_MitadIzquierdaCapicua(N: Cardinal): string;

// =============================================================================
// EXAMEN 6: 2024-1 GRUPO SF (05/07/2024)
// =============================================================================
function E6_P1_SerieFibonacciSobreImparFact(N: Integer): Double;
function E6_P2_SumarSumasDigitosImpares(numeros: array of Cardinal): Cardinal;
procedure E6_P3_SepararMenoresYMayores(N: Cardinal; criterio: Byte; out menores, mayores: Cardinal);
function E6_P4_InvertirPorMitades(cad: string): string;

// =============================================================================
// EXAMEN 7: 2023-1 GRUPO Z2
// =============================================================================
function E7_P1_SerieIntercaladaCuadradosPaso3(N: Integer): Double;
function E7_P2_OrdenarSegundaPalabra(cad: string): string;
function E7_P3_SeriePromedioDigitosImpares(N: Integer): Double;
function E7_P4_RaizDigital(N: Cardinal): Byte;

implementation

// -----------------------------------------------------------------------------
// FUNCIONES AUXILIARES DE SOPORTE GENERAL (CLEAN CODE)
// -----------------------------------------------------------------------------
function EsPrimo(d: Byte): Boolean;
begin
  Result := d in [2, 3, 5, 7];
end;

function SumaDigitosDeNumero(num: Cardinal): Cardinal;
var
  suma: Cardinal;
begin
  suma := 0;
  while num > 0 do
  begin
    suma := suma + (num mod 10);
    num := num div 10;
  end;
  Result := suma;
end;

function ContarDigitosNum(num: Cardinal): Integer;
var
  c: Integer;
begin
  if num = 0 then Exit(1);
  c := 0;
  while num > 0 do
  begin
    Inc(c);
    num := num div 10;
  end;
  Result := c;
end;

function InvertirNumero(num: Cardinal): Cardinal;
var
  inv: Cardinal;
begin
  inv := 0;
  while num > 0 do
  begin
    inv := inv * 10 + (num mod 10);
    num := num div 10;
  end;
  Result := inv;
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

function InvertirCadena(s: string): string;
var
  i: Integer;
  res: string;
begin
  res := '';
  for i := Length(s) downto 1 do
    res := res + s[i];
  Result := res;
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 1 (2024-1 GRUPO Z2)
// =============================================================================
function E1_P1_PromedioAscendente(n: Integer; numeros: array of Integer): Double;
var
  i, c, ultimoValido, num: Integer;
  suma: Double;
begin
  suma := 0;
  c := 0;
  ultimoValido := -1;
  for i := 0 to High(numeros) do
  begin
    num := numeros[i];
    if (num >= 100) and (num <= 200) then
    begin
      if (c = 0) or (num >= ultimoValido) then
      begin
        suma := suma + num;
        Inc(c);
        ultimoValido := num;
      end;
    end;
  end;
  if c > 0 then
    Result := suma / c
  else
    Result := 0.0;
end;

function E1_P2_SumatoriaSerieX(X: Double; N: Integer): Double;
var
  S, numPot, denFact: Double;
  c, impar, k: Integer;
begin
  if N <= 0 then Exit(0.0);
  S := X; // Término 1
  c := 2;
  impar := 1;
  while c <= N do
  begin
    numPot := 1.0;
    denFact := 1.0;
    for k := 1 to impar do
    begin
      numPot := numPot * X;
      denFact := denFact * k;
    end;
    S := S + (numPot / denFact);
    impar := impar + 2;
    Inc(c);
  end;
  Result := S;
end;

function E1_P3_OrdenarPalabraConsonante(cad: string): string;
var
  pal, res: string;
  i: Integer;
  ch: Char;
begin
  cad := Trim(cad) + ' ';
  pal := '';
  res := '';
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      pal := pal + cad[i]
    else
    begin
      if (pal <> '') and (res = '') then
      begin
        ch := UpCase(pal[1]);
        if (ch in ['A'..'Z']) and not (ch in ['A','E','I','O','U']) then
          res := OrdenarCaracteresAsc(pal);
      end;
      pal := '';
    end;
  end;
  Result := res;
end;

function E1_P4_MitadDerechaCapicua(N: Cardinal): string;
var
  cantDig, mitad, pot, i: Integer;
  parteDer, inv: Cardinal;
begin
  cantDig := ContarDigitosNum(N);
  mitad := cantDig div 2;
  if mitad = 0 then
    Exit('Si es capicua. ' + IntToStr(N));

  pot := 1;
  for i := 1 to mitad do
    pot := pot * 10;

  parteDer := N mod pot;
  inv := InvertirNumero(parteDer);

  if parteDer = inv then
    Result := 'Si es capicúa. ' + IntToStr(parteDer)
  else
    Result := 'no es capicúa ' + IntToStr(inv);
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 2 (2024-1 REPECHAJE GRUPO R)
// =============================================================================
function E2_P1_SerieFactorialPotencia(n: Integer): Int64;
var
  S, fact, pot: Int64;
  i, j: Integer;
begin
  S := 0;
  for i := 1 to n do
  begin
    // i!
    fact := 1;
    for j := 1 to i do
      fact := fact * j;

    // i^i
    pot := 1;
    for j := 1 to i do
      pot := pot * i;

    S := S + (fact * pot);
  end;
  Result := S;
end;

function E2_P2_SumarDigitosPrimosDeNumeros(numeros: array of Cardinal): Cardinal;
var
  i: Integer;
  num: Cardinal;
  dig: Byte;
  sumaTotal: Cardinal;
begin
  sumaTotal := 0;
  for i := 0 to High(numeros) do
  begin
    num := numeros[i];
    while num > 0 do
    begin
      dig := num mod 10;
      if EsPrimo(dig) then
        sumaTotal := sumaTotal + dig;
      num := num div 10;
    end;
  end;
  Result := sumaTotal;
end;

function E2_P3_VerificarPalabrasPalindromes(cad: string; out cant: Integer): string;
var
  pal, res: string;
  i: Integer;
begin
  cad := Trim(cad) + ' ';
  pal := '';
  res := '';
  cant := 0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      pal := pal + cad[i]
    else
    begin
      if pal <> '' then
      begin
        if (Length(pal) > 1) and (pal = InvertirCadena(pal)) then
        begin
          Inc(cant);
          if res <> '' then res := res + ', ';
          res := res + pal;
        end;
      end;
      pal := '';
    end;
  end;
  Result := res;
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 3 (2023-2 GRUPO Z2)
// =============================================================================
function E3_P1_RaizDigital(N: Cardinal): Byte;
var
  suma: Cardinal;
begin
  while N >= 10 do
  begin
    suma := 0;
    while N > 0 do
    begin
      suma := suma + (N mod 10);
      N := N div 10;
    end;
    N := suma;
  end;
  Result := N;
end;

function E3_P2_SumatoriaCuadradosSobreFactorial(N: Integer): Double;
var
  S, fact: Double;
  i, j: Integer;
begin
  S := 0.0;
  for i := 1 to N do
  begin
    fact := 1.0;
    for j := 1 to (i - 1) do
      fact := fact * j;

    S := S + ((i * i) / fact);
  end;
  Result := S;
end;

function E3_P3_PrimeroYUltimoPrimos(N: Cardinal): string;
var
  primerDig, ultimoDig: Byte;
  aux: Cardinal;
begin
  ultimoDig := N mod 10;
  aux := N;
  while aux >= 10 do
    aux := aux div 10;
  primerDig := aux;

  if EsPrimo(primerDig) and EsPrimo(ultimoDig) then
    Result := 'Si los dígitos son primos'
  else
    Result := 'No, los dígitos no son primos';
end;

function E3_P4_InvertirPorMitades(cad: string): string;
var
  len, m: Integer;
  izq, der, centro: string;
begin
  len := Length(cad);
  m := len div 2;
  izq := Copy(cad, 1, m);
  if (len mod 2 <> 0) then
  begin
    centro := cad[m + 1];
    der := Copy(cad, m + 2, m);
  end
  else
  begin
    centro := '';
    der := Copy(cad, m + 1, m);
  end;
  Result := InvertirCadena(izq) + centro + InvertirCadena(der);
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 4 (2023-1 GRUPO SF)
// =============================================================================
procedure E4_P1_DivisionRestasSucesivas(A, B: Cardinal; out cociente, residuo: Cardinal);
begin
  cociente := 0;
  if B = 0 then
  begin
    residuo := A;
    Exit;
  end;
  while A >= B do
  begin
    A := A - B;
    Inc(cociente);
  end;
  residuo := A;
end;

function E4_P2_EliminarDigitosRepetidos(N: Cardinal): Cardinal;
var
  frec: array[0..9] of Integer;
  aux, numReconstruido, p: Cardinal;
  dig: Byte;
  i: Integer;
begin
  for i := 0 to 9 do frec[i] := 0;
  aux := N;
  while aux > 0 do
  begin
    Inc(frec[aux mod 10]);
    aux := aux div 10;
  end;

  aux := N;
  numReconstruido := 0;
  p := 1;
  while aux > 0 do
  begin
    dig := aux mod 10;
    if frec[dig] = 1 then
    begin
      numReconstruido := numReconstruido + (dig * p);
      p := p * 10;
    end;
    aux := aux div 10;
  end;
  Result := numReconstruido;
end;

function E4_P3_MayorSumaDigitos(numeros: array of Cardinal): Cardinal;
var
  i: Integer;
  suma, mayor: Cardinal;
begin
  mayor := 0;
  for i := 0 to High(numeros) do
  begin
    suma := SumaDigitosDeNumero(numeros[i]);
    if suma > mayor then
      mayor := suma;
  end;
  Result := mayor;
end;

function E4_P4_SerieAlternadaFactorial(N: Integer): Double;
var
  S, fact: Double;
  num, den, i, j: Integer;
begin
  S := 0.0;
  num := 4;
  den := 1;
  for i := 1 to N do
  begin
    fact := 1.0;
    for j := 1 to den do
      fact := fact * j;

    S := S + (num / fact);

    // Numerador alterna: *3, +2, *3, +2...
    if (i mod 2 <> 0) then
      num := num * 3
    else
      num := num + 2;

    // Denominador: 1, 3, 4, 5, 6, 7...
    if i = 1 then
      den := 3
    else
      Inc(den);
  end;
  Result := S;
end;

function E4_P5_ContarYMayusculasTerminanEnA(cad: string; out cant: Integer): string;
var
  pal, res: string;
  i: Integer;
begin
  cad := Trim(cad) + ' ';
  pal := '';
  res := '';
  cant := 0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      pal := pal + cad[i]
    else
    begin
      if pal <> '' then
      begin
        if (pal[Length(pal)] in ['a', 'A']) then
        begin
          Inc(cant);
          pal := UpperCase(pal);
        end;
        if res <> '' then res := res + ' ';
        res := res + pal;
      end;
      pal := '';
    end;
  end;
  Result := res;
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 5 (2023-2 GRUPO SF)
// =============================================================================
procedure E5_P1_ContarParesEImparesHastaSuma(X: Integer; numeros: array of Integer; out pares, impares: Integer);
var
  suma, i, num: Integer;
begin
  suma := 0;
  pares := 0;
  impares := 0;
  for i := 0 to High(numeros) do
  begin
    num := numeros[i];
    if (num mod 2 = 0) then
      Inc(pares)
    else
      Inc(impares);

    suma := suma + num;
    if suma >= X then Break;
  end;
end;

function E5_P2_SumatoriaSerieX_N3(X: Double; N: Integer): Double;
begin
  Result := E1_P2_SumatoriaSerieX(X, N);
end;

function E5_P3_OrdenarSegundaPalabra(cad: string): string;
var
  pal, res: string;
  i, cPal: Integer;
begin
  cad := Trim(cad) + ' ';
  pal := '';
  res := '';
  cPal := 0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      pal := pal + cad[i]
    else
    begin
      if pal <> '' then
      begin
        Inc(cPal);
        if cPal = 2 then
          res := OrdenarCaracteresAsc(pal);
      end;
      pal := '';
    end;
  end;
  Result := res;
end;

function E5_P4_MitadIzquierdaCapicua(N: Cardinal): string;
var
  cantDig, mitad, pot, i: Integer;
  parteIzq, inv: Cardinal;
begin
  cantDig := ContarDigitosNum(N);
  mitad := cantDig div 2;
  if mitad = 0 then
    Exit('Si es capicua. ' + IntToStr(N));

  pot := 1;
  for i := 1 to (cantDig - mitad) do
    pot := pot * 10;

  parteIzq := N div pot;
  inv := InvertirNumero(parteIzq);

  if parteIzq = inv then
    Result := 'Si es capicúa. ' + IntToStr(parteIzq)
  else
    Result := 'no es capicúa ' + IntToStr(inv);
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 6 (2024-1 GRUPO SF)
// =============================================================================
function E6_P1_SerieFibonacciSobreImparFact(N: Integer): Double;
var
  S, fact: Double;
  num1, num2, numAct, impar, i, k: Integer;
begin
  S := 0.0;
  num1 := 1;
  num2 := 9;
  impar := 1;
  for i := 1 to N do
  begin
    if i = 1 then
      numAct := num1
    else if i = 2 then
      numAct := num2
    else
    begin
      numAct := num1 + num2;
      num1 := num2;
      num2 := numAct;
    end;

    fact := 1.0;
    for k := 1 to impar do
      fact := fact * k;

    S := S + (numAct / fact);
    impar := impar + 2;
  end;
  Result := S;
end;

function E6_P2_SumarSumasDigitosImpares(numeros: array of Cardinal): Cardinal;
var
  i: Integer;
  sumaDig, sumaTotal: Cardinal;
begin
  sumaTotal := 0;
  for i := 0 to High(numeros) do
  begin
    sumaDig := SumaDigitosDeNumero(numeros[i]);
    if (sumaDig mod 2 <> 0) then
      sumaTotal := sumaTotal + sumaDig;
  end;
  Result := sumaTotal;
end;

procedure E6_P3_SepararMenoresYMayores(N: Cardinal; criterio: Byte; out menores, mayores: Cardinal);
var
  dig: Byte;
  aux: Cardinal;
begin
  menores := 0;
  mayores := 0;
  aux := N;
  while aux > 0 do
  begin
    dig := aux mod 10;
    if dig < criterio then
      menores := menores * 10 + dig
    else
      mayores := mayores * 10 + dig;
    aux := aux div 10;
  end;
end;

function E6_P4_InvertirPorMitades(cad: string): string;
begin
  Result := E3_P4_InvertirPorMitades(cad);
end;

// =============================================================================
// IMPLEMENTACIÓN EXAMEN 7 (2023-1 GRUPO Z2)
// =============================================================================
function E7_P1_SerieIntercaladaCuadradosPaso3(N: Integer): Double;
var
  S, num: Double;
  den: Double;
  i, idxCuad, paso3: Integer;
begin
  S := 0.0;
  num := 4;
  idxCuad := 1;
  paso3 := 5;
  for i := 1 to N do
  begin
    if (i mod 2 <> 0) then
    begin
      den := idxCuad * idxCuad;
      Inc(idxCuad);
    end
    else
    begin
      den := paso3;
      paso3 := paso3 + 3;
    end;

    S := S + (num / den);

    if (i mod 2 <> 0) then
      num := num * 3
    else
      num := num + 2;
  end;
  Result := S;
end;

function E7_P2_OrdenarSegundaPalabra(cad: string): string;
begin
  Result := E5_P3_OrdenarSegundaPalabra(cad);
end;

function E7_P3_SeriePromedioDigitosImpares(N: Integer): Double;
var
  i, cImp: Integer;
  termino, tImpar, tPar, sumaDig, sumaImp: Cardinal;
begin
  tImpar := 7;
  tPar := 6;
  sumaImp := 0;
  cImp := 0;
  for i := 1 to N do
  begin
    if (i mod 2 <> 0) then
    begin
      termino := tImpar;
      tImpar := tImpar * 2;
    end
    else
    begin
      termino := tPar;
      tPar := tPar * 3;
    end;

    sumaDig := SumaDigitosDeNumero(termino);
    if (sumaDig mod 2 <> 0) then
    begin
      sumaImp := sumaImp + sumaDig;
      Inc(cImp);
    end;
  end;

  if cImp > 0 then
    Result := sumaImp / cImp
  else
    Result := 0.0;
end;

function E7_P4_RaizDigital(N: Cardinal): Byte;
begin
  Result := E3_P1_RaizDigital(N);
end;

end.
