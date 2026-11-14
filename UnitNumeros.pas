unit UnitNumeros;

interface

uses
  SysUtils;

// ==========================================
// DECLARACIÓN DE FUNCIONES Y PROCEDIMIENTOS
// ==========================================

// 1. Dado un número natural, mostrar la suma de los dígitos impares mayores a 3 (5, 7, 9)
function SumaImparesMayores3(n: Cardinal): Cardinal;

// 2. Dado un número natural mostrar el dígito mayor de las posiciones/índices impares (1, 3, 5... de izq. a der.)
function DigitoMayorIndicesImpares(n: Cardinal): Integer;

// 3. Dado un número natural sumar los dígitos de un número
function SumaDigitos(n: Cardinal): Cardinal;

// 4. Mostrar el promedio de los dígitos menores a 7
function PromedioDigitosMenores7(n: Cardinal): Double;

// 5. De un número natural, obtener el dígito mayor y el dígito menor
procedure MayorYMenorDigito(n: Cardinal; var digMayor, digMenor: Byte);

// 6. Dado un número natural mostrar otro número formado solo con los dígitos pares
function FormarNumeroPares(n: Cardinal): Cardinal;

// 7. Dado un número mostrar 2 números: uno formado por los pares y otro por los impares
procedure SepararParesImpares(n: Cardinal; var numPares, numImpares: Cardinal);

// 8. Dado un número natural, mostrar el dígito mayor de los dígitos pares (-1 si no tiene)
function MayorDigitoPar(n: Cardinal): Integer;

// 9. De un número natural, mostrar los dígitos múltiplos de 3 (como cadena o lista)
function DigitosMultiplosDe3(n: Cardinal): String;

// 10. Hacer un algoritmo para obtener el primero y el último dígito de un número
procedure PrimerYUltimoDigito(n: Cardinal; var primero, ultimo: Byte);

// 11. Eliminar el primero y el último dígito de un número y retornar dicho número
function EliminarPrimerYUltimoDigito(n: Cardinal): Cardinal;

// 12. Dado un número natural, mostrar dicho número de forma invertida
function InvertirNumero(n: Cardinal): Cardinal;

// 13. Hacer un algoritmo para contar los dígitos múltiplos de cuatro (0, 4, 8)
function ContarMultiplosDeCuatro(n: Cardinal): Cardinal;

// 14. Hacer un algoritmo para mostrar el dígito menor de los múltiplos de tres (0, 3, 6, 9)
function MenorDigitoMultiploDeTres(n: Cardinal): Integer;

// 15. Hacer un algoritmo para saber si un número es capicúa o palíndromo
function EsCapicua(n: Cardinal): Boolean;

// 16. De un número natural llevar a su equivalente a binario
function DecimalABinario(n: Cardinal): String;

// 17. De un número natural convertir a número hexadecimal
function DecimalAHexadecimal(n: Cardinal): String;

// 18. De un número natural convertir a octal
function DecimalAOctal(n: Cardinal): String;

// 19. De un número natural, sumar los dígitos primos (2, 3, 5, 7)
function SumaDigitosPrimos(n: Cardinal): Cardinal;

// 20. De un número natural, mostrar el promedio de los dígitos múltiplos de 3 o 5
function PromedioMultiplos3y5(n: Cardinal): Double;

// 21. De un número natural mostrar el promedio de los dígitos primos
function PromedioDigitosPrimos(n: Cardinal): Double;

// 22. De un número natural mostrar otro número formado por los dígitos primos
function FormarNumeroPrimos(n: Cardinal): Cardinal;

// 23. De un número natural llevar a Hexadecimal
function DecimalAHexadecimal2(n: Cardinal): String;

// 24. De un número decimal llevar a binario
function DecimalABinario2(n: Cardinal): String;

// 25. De un número octal (representado como cadena o número) llevar a Hexadecimal
function OctalAHexadecimal(octalStr: String): String;

// ==========================================
// MODELOS DE EXAMEN PARCIAL (30 PUNTOS C/U)
// ==========================================
// Examen 1: Formar número con menor dígito impar y mayor dígito par (ej. 85239 -> 38)
function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;

// Examen 2: Eliminar todos los dígitos a partir de la posición K (ej. 78143, K=3 -> 43)
function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;

// Examen 3: Eliminar el dígito de la posición K (ej. 78143, K=2 -> 7813)
function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;

// Examen 4: Promedio de pares y promedio de impares (ej. 12345 -> PromPar=3.0, PromImpar=3.0)
procedure PromedioParesImpares(numeroNatural: Cardinal; var promPares, promImpares: Double);

// Examen 5: Mayor dígito de los múltiplos de 3 (ej. 8326 -> 6)
function MayorDigitoMultiploDe3(numeroNatural: Cardinal): Integer;

// Examen 6: Sumar dígitos hasta que sea menor a 10 / Raíz Digital (ej. 15378 -> 24 -> 6)
function SumarHastaMenorA10(numeroNatural: Cardinal): Byte;

// Examen 7: Promedio de la serie dual S = 4+2+8+6+12+18+16+54... (n términos)
function PromedioSerieDual(cantidadTerminos: Cardinal): Double;

// Examen 8: Sumar dígitos de cada número y sumar los resultados impares (ej. {123,25,281,94,46} -> 31)
function SumaDigitosImparesDeLote(const listaNumeros: array of Cardinal): Cardinal;

// Examen 9: Separar dígitos menores a 6 y mayores o iguales a 6 (ej. 16327 -> <6: 231, >=6: 76)
procedure SepararMenoresYMayores6(numeroNatural: Cardinal; var numMenores6, numMayores6: Cardinal);

// Examen 10: Promedio de números ascendentes en rango [100-200] (ej. 211, 120, 50, 180, 200 -> 166.66)
function PromedioAscendentesRango100_200(const listaNumeros: array of Cardinal): Double;

// Examen 11: Sumatoria global de dígitos primos en lote de N números (ej. {123, 249, 729, 562} -> 23)
function SumatoriaPrimosDeLote(const listaNumeros: array of Cardinal): Cardinal;

// Funciones auxiliares
function EsPrimo(d: Byte): Boolean;
function CantidadDigitos(n: Cardinal): Cardinal;

implementation

// ==========================================
// FUNCIONES AUXILIARES
// ==========================================

function EsPrimo(d: Byte): Boolean;
begin
  Result := (d = 2) or (d = 3) or (d = 5) or (d = 7);
end;

function CantidadDigitos(n: Cardinal): Cardinal;
var
  c: Cardinal;
begin
  if n = 0 then
    Exit(1);
  c := 0;
  while n > 0 do
  begin
    Inc(c);
    n := n div 10;
  end;
  Result := c;
end;

// ==========================================
// IMPLEMENTACIÓN DE LOS EJERCICIOS
// ==========================================

// 1. Suma de dígitos impares mayores a 3 (5, 7, 9)
function SumaImparesMayores3(n: Cardinal): Cardinal;
var
  d, suma: Cardinal;
begin
  suma := 0;
  if n = 0 then
  begin
    Result := 0;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 <> 0) and (d > 3) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;

// 2. Dígito mayor de los índices impares (de izquierda a derecha: pos 1, 3, 5...)
function DigitoMayorIndicesImpares(n: Cardinal): Integer;
var
  s: String;
  i, maxD, valD: Integer;
begin
  s := IntToStr(n);
  maxD := -1;
  i := 1;
  while i <= Length(s) do
  begin
    valD := Ord(s[i]) - Ord('0');
    if valD > maxD then
      maxD := valD;
    i := i + 2;
  end;
  Result := maxD;
end;

// 3. Sumar todos los dígitos de un número
function SumaDigitos(n: Cardinal): Cardinal;
var
  suma: Cardinal;
begin
  suma := 0;
  if n = 0 then Exit(0);
  while n > 0 do
  begin
    suma := suma + (n mod 10);
    n := n div 10;
  end;
  Result := suma;
end;

// 4. Promedio de los dígitos menores a 7
function PromedioDigitosMenores7(n: Cardinal): Double;
var
  d, suma, cont: Cardinal;
begin
  suma := 0;
  cont := 0;
  if n = 0 then
    Exit(0.0);
  while n > 0 do
  begin
    d := n mod 10;
    if d < 7 then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then
    Result := suma / cont
  else
    Result := 0.0;
end;

// 5. Dígito mayor y dígito menor de un número natural
procedure MayorYMenorDigito(n: Cardinal; var digMayor, digMenor: Byte);
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

// 6. Formar otro número con los dígitos pares (manteniendo el orden original)
function FormarNumeroPares(n: Cardinal): Cardinal;
var
  d, res, pot: Cardinal;
begin
  res := 0;
  pot := 1;
  if n = 0 then Exit(0);
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
  Result := res;
end;

// 7. Separar número en dos: uno con dígitos pares y otro con impares
procedure SepararParesImpares(n: Cardinal; var numPares, numImpares: Cardinal);
var
  d, potPar, potImpar: Cardinal;
begin
  numPares := 0;
  numImpares := 0;
  potPar := 1;
  potImpar := 1;
  if n = 0 then
  begin
    numPares := 0;
    numImpares := 0;
    Exit;
  end;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      numPares := numPares + (d * potPar);
      potPar := potPar * 10;
    end
    else
    begin
      numImpares := numImpares + (d * potImpar);
      potImpar := potImpar * 10;
    end;
    n := n div 10;
  end;
end;

// 8. Mayor de los dígitos pares (-1 si no tiene pares)
function MayorDigitoPar(n: Cardinal): Integer;
var
  d: Cardinal;
  mayor: Integer;
begin
  mayor := -1;
  if n = 0 then Exit(0);
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) and (Integer(d) > mayor) then
      mayor := d;
    n := n div 10;
  end;
  Result := mayor;
end;

// 9. Mostrar los dígitos múltiplos de 3 (0, 3, 6, 9)
function DigitosMultiplosDe3(n: Cardinal): String;
var
  s, res: String;
  i: Integer;
  d: Integer;
begin
  s := IntToStr(n);
  res := '';
  for i := 1 to Length(s) do
  begin
    d := Ord(s[i]) - Ord('0');
    if d mod 3 = 0 then
    begin
      if res <> '' then
        res := res + ', ';
      res := res + s[i];
    end;
  end;
  if res = '' then
    Result := 'Ninguno'
  else
    Result := res;
end;

// 10. Primer y último dígito
procedure PrimerYUltimoDigito(n: Cardinal; var primero, ultimo: Byte);
begin
  ultimo := n mod 10;
  while n >= 10 do
    n := n div 10;
  primero := n;
end;

// 11. Eliminar primer y último dígito
function EliminarPrimerYUltimoDigito(n: Cardinal): Cardinal;
var
  pot: Cardinal;
begin
  if n < 100 then
    Exit(0); // Si tiene 1 o 2 dígitos, al quitar el primero y último no queda nada intermedio
  
  // Quitar el último dígito
  n := n div 10;
  
  // Calcular la potencia de 10 para quitar el primer dígito
  pot := 1;
  while (n div pot) >= 10 do
    pot := pot * 10;
  
  // Quitar el primer dígito restante
  n := n mod pot;
  Result := n;
end;

// 12. Invertir número
function InvertirNumero(n: Cardinal): Cardinal;
var
  inv: Cardinal;
begin
  inv := 0;
  while n > 0 do
  begin
    inv := (inv * 10) + (n mod 10);
    n := n div 10;
  end;
  Result := inv;
end;

// 13. Contar los dígitos múltiplos de 4 (0, 4, 8)
function ContarMultiplosDeCuatro(n: Cardinal): Cardinal;
var
  d, c: Cardinal;
begin
  c := 0;
  if n = 0 then Exit(1);
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 4 = 0 then
      Inc(c);
    n := n div 10;
  end;
  Result := c;
end;

// 14. Menor dígito de los múltiplos de 3
function MenorDigitoMultiploDeTres(n: Cardinal): Integer;
var
  d: Cardinal;
  menor: Integer;
begin
  menor := 10;
  if n = 0 then Exit(0);
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) and (Integer(d) < menor) then
      menor := d;
    n := n div 10;
  end;
  if menor = 10 then
    Result := -1
  else
    Result := menor;
end;

// 15. Es capicúa o palíndromo
function EsCapicua(n: Cardinal): Boolean;
begin
  Result := (n = InvertirNumero(n));
end;

// 16. Decimal a Binario
function DecimalABinario(n: Cardinal): String;
var
  res: String;
begin
  if n = 0 then Exit('0');
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 2) + res;
    n := n div 2;
  end;
  Result := res;
end;

// 17. Decimal a Hexadecimal
function DecimalAHexadecimal(n: Cardinal): String;
const
  HexChars: array[0..15] of Char = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F');
var
  res: String;
begin
  if n = 0 then Exit('0');
  res := '';
  while n > 0 do
  begin
    res := HexChars[n mod 16] + res;
    n := n div 16;
  end;
  Result := res;
end;

// 18. Decimal a Octal
function DecimalAOctal(n: Cardinal): String;
var
  res: String;
begin
  if n = 0 then Exit('0');
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 8) + res;
    n := n div 8;
  end;
  Result := res;
end;

// 19. Suma de dígitos primos (2, 3, 5, 7)
function SumaDigitosPrimos(n: Cardinal): Cardinal;
var
  d, suma: Cardinal;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;

// 20. Promedio de los dígitos múltiplos de 3 o 5 (0, 3, 5, 6, 9)
function PromedioMultiplos3y5(n: Cardinal): Double;
var
  d, suma, cont: Cardinal;
begin
  suma := 0;
  cont := 0;
  if n = 0 then Exit(0.0);
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) or (d mod 5 = 0) then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then
    Result := suma / cont
  else
    Result := 0.0;
end;

// 21. Promedio de los dígitos primos
function PromedioDigitosPrimos(n: Cardinal): Double;
var
  d, suma, cont: Cardinal;
begin
  suma := 0;
  cont := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then
    Result := suma / cont
  else
    Result := 0.0;
end;

// 22. Formar número con los dígitos primos
function FormarNumeroPrimos(n: Cardinal): Cardinal;
var
  d, res, pot: Cardinal;
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
  Result := res;
end;

// 23. Decimal a Hexadecimal
function DecimalAHexadecimal2(n: Cardinal): String;
begin
  Result := DecimalAHexadecimal(n);
end;

// 24. Decimal a Binario
function DecimalABinario2(n: Cardinal): String;
begin
  Result := DecimalABinario(n);
end;

// 25. Octal a Hexadecimal
function OctalAHexadecimal(octalStr: String): String;
var
  i: Integer;
  valDec: Cardinal;
  pot: Cardinal;
  d: Integer;
begin
  // Primero convertimos de Octal a Decimal
  valDec := 0;
  pot := 1;
  for i := Length(octalStr) downto 1 do
  begin
    d := Ord(octalStr[i]) - Ord('0');
    valDec := valDec + (Cardinal(d) * pot);
    pot := pot * 8;
  end;
  // Luego de Decimal a Hexadecimal
  Result := DecimalAHexadecimal(valDec);
end;

// ==========================================
// IMPLEMENTACIÓN DE LOS MODELOS DE EXAMEN
// ==========================================

// Examen 1: Formar número con menor dígito impar y mayor dígito par (ej. 85239 -> 38)
function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;
var
  digitoActual: Cardinal;
  menorImpar, mayorPar: Integer;
begin
  menorImpar := 10;
  mayorPar   := -1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 2 <> 0) then
    begin
      if Integer(digitoActual) < menorImpar then
        menorImpar := digitoActual;
    end
    else
    begin
      if Integer(digitoActual) > mayorPar then
        mayorPar := digitoActual;
    end;
    numeroNatural := numeroNatural div 10;
  end;
  if (menorImpar <> 10) and (mayorPar <> -1) then
    Result := (Cardinal(menorImpar) * 10) + Cardinal(mayorPar)
  else
    Result := 0;
end;

// Examen 2: Eliminar todos los dígitos a partir de la posición K (ej. 78143, K=3 -> 43)
function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  potencia: Cardinal;
  i: Byte;
begin
  if posicionK <= 1 then
    Exit(0);
  potencia := 1;
  for i := 1 to (posicionK - 1) do
    potencia := potencia * 10;
  Result := numeroNatural mod potencia;
end;

// Examen 3: Eliminar el dígito de la posición K (ej. 78143, K=2 -> 7813)
function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  digitoActual: Cardinal;
  numeroResultado, potencia: Cardinal;
  posicionActual: Byte;
begin
  numeroResultado := 0;
  potencia := 1;
  posicionActual := 1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if posicionActual <> posicionK then
    begin
      numeroResultado := numeroResultado + (digitoActual * potencia);
      potencia := potencia * 10;
    end;
    Inc(posicionActual);
    numeroNatural := numeroNatural div 10;
  end;
  Result := numeroResultado;
end;

// Examen 4: Promedio de pares y promedio de impares (ej. 12345 -> PromPar=3.0, PromImpar=3.0)
procedure PromedioParesImpares(numeroNatural: Cardinal; var promPares, promImpares: Double);
var
  digitoActual: Cardinal;
  sumaPares, cantPares, sumaImpares, cantImpares: Cardinal;
begin
  sumaPares := 0;   cantPares := 0;
  sumaImpares := 0; cantImpares := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual mod 2 = 0 then
    begin
      sumaPares := sumaPares + digitoActual;
      Inc(cantPares);
    end
    else
    begin
      sumaImpares := sumaImpares + digitoActual;
      Inc(cantImpares);
    end;
    numeroNatural := numeroNatural div 10;
  end;
  if cantPares > 0 then promPares := sumaPares / cantPares else promPares := 0.0;
  if cantImpares > 0 then promImpares := sumaImpares / cantImpares else promImpares := 0.0;
end;

// Examen 5: Mayor dígito de los múltiplos de 3 (ej. 8326 -> 6)
function MayorDigitoMultiploDe3(numeroNatural: Cardinal): Integer;
var
  digitoActual: Cardinal;
  mayor: Integer;
begin
  mayor := -1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 3 = 0) and (Integer(digitoActual) > mayor) then
      mayor := digitoActual;
    numeroNatural := numeroNatural div 10;
  end;
  Result := mayor;
end;

// Examen 6: Sumar dígitos hasta que sea menor a 10 / Raíz Digital (ej. 15378 -> 24 -> 6)
function SumarHastaMenorA10(numeroNatural: Cardinal): Byte;
var
  suma, temp: Cardinal;
begin
  while numeroNatural >= 10 do
  begin
    suma := 0;
    temp := numeroNatural;
    while temp > 0 do
    begin
      suma := suma + (temp mod 10);
      temp := temp div 10;
    end;
    numeroNatural := suma;
  end;
  Result := numeroNatural;
end;

// Examen 7: Promedio de la serie dual S = 4+2+8+6+12+18+16+54... (n términos)
function PromedioSerieDual(cantidadTerminos: Cardinal): Double;
var
  i, terminoImpar, terminoPar, terminoActual: Cardinal;
  sumaTotal: Double;
begin
  if cantidadTerminos = 0 then Exit(0.0);
  terminoImpar := 4; // Razón +4
  terminoPar   := 2; // Razón *3
  sumaTotal    := 0.0;
  for i := 1 to cantidadTerminos do
  begin
    if (i mod 2 <> 0) then
    begin
      terminoActual := terminoImpar;
      terminoImpar := terminoImpar + 4;
    end
    else
    begin
      terminoActual := terminoPar;
      terminoPar := terminoPar * 3;
    end;
    sumaTotal := sumaTotal + terminoActual;
  end;
  Result := sumaTotal / cantidadTerminos;
end;

// Examen 8: Sumar dígitos de cada número y sumar los resultados impares (ej. {123,25,281,94,46} -> 31)
function SumaDigitosImparesDeLote(const listaNumeros: array of Cardinal): Cardinal;
var
  i: Integer;
  numActual, temp, sumaDigitos, sumaTotalImpares: Cardinal;
begin
  sumaTotalImpares := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    sumaDigitos := 0;
    temp := numActual;
    while temp > 0 do
    begin
      sumaDigitos := sumaDigitos + (temp mod 10);
      temp := temp div 10;
    end;
    if (sumaDigitos mod 2 <> 0) then
      sumaTotalImpares := sumaTotalImpares + sumaDigitos;
  end;
  Result := sumaTotalImpares;
end;

// Examen 9: Separar dígitos menores a 6 y mayores o iguales a 6 (ej. 16327 -> <6: 231, >=6: 76)
procedure SepararMenoresYMayores6(numeroNatural: Cardinal; var numMenores6, numMayores6: Cardinal);
var
  digitoActual: Cardinal;
begin
  numMenores6 := 0;
  numMayores6 := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual < 6 then
      numMenores6 := (numMenores6 * 10) + digitoActual
    else
      numMayores6 := (numMayores6 * 10) + digitoActual;
    numeroNatural := numeroNatural div 10;
  end;
end;

// Examen 10: Promedio de números ascendentes en rango [100-200] (ej. 211, 120, 50, 180, 200 -> 166.66)
function PromedioAscendentesRango100_200(const listaNumeros: array of Cardinal): Double;
var
  i: Integer;
  numActual, ultimoValido, sumaValidos, cantValidos: Cardinal;
begin
  sumaValidos := 0;
  cantValidos := 0;
  ultimoValido := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    if (numActual >= 100) and (numActual <= 200) and (numActual > ultimoValido) then
    begin
      sumaValidos := sumaValidos + numActual;
      Inc(cantValidos);
      ultimoValido := numActual;
    end;
  end;
  if cantValidos > 0 then
    Result := sumaValidos / cantValidos
  else
    Result := 0.0;
end;

// Examen 11: Sumatoria global de dígitos primos en lote de N números (ej. {123, 249, 729, 562} -> 23)
function SumatoriaPrimosDeLote(const listaNumeros: array of Cardinal): Cardinal;
var
  i: Integer;
  numActual, digito, temp, sumaTotalPrimos: Cardinal;
begin
  sumaTotalPrimos := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    temp := numActual;
    while temp > 0 do
    begin
      digito := temp mod 10;
      if (digito = 2) or (digito = 3) or (digito = 5) or (digito = 7) then
        sumaTotalPrimos := sumaTotalPrimos + digito;
      temp := temp div 10;
    end;
  end;
  Result := sumaTotalPrimos;
end;

end.
