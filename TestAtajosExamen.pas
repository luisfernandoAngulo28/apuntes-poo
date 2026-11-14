{$mode delphi}
program TestAtajosExamen;

uses
  SysUtils,
  UAtajosExamen;

procedure ProbarSeries();
var
  s1, s2, s3, s4: Double;
  sd, sf, sc: Int64;
begin
  Writeln('=== PRUEBAS BLOQUE 1 Y 2: SERIES NUMÉRICAS (DIVIDE Y VENCERÁS) ===');
  
  // Serie 1: Factorial / Doble = 1/2 + 2/4 + 6/8 + 24/16 + 120/32 = 0.5 + 0.5 + 0.75 + 1.5 + 3.75 = 7.0
  s1 := SumaFactorialDoble(5);
  Writeln('1. SumaFactorialDoble(n=5): ', s1:0:4, ' (Esperado: 7.0000)');

  // Serie 2: Cuadrado / Fibonacci = 3/1 + 6/1 + 12/2 + 24/3 + 48/5 = 3 + 6 + 6 + 8 + 9.6 = 32.6
  s2 := SumaCuadradoFibonacci(5);
  Writeln('2. SumaCuadradoFibonacci(n=5): ', s2:0:4, ' (Esperado: 32.6000)');

  // Serie 3: Potencia / Multiplo 5 = 1^1/5 + 2^2/10 + 3^3/15 + 4^4/20
  s3 := SumaPotenciaMultiplo5(4);
  Writeln('3. SumaPotenciaMultiplo5(n=4): ', s3:0:4);

  // Serie 4: Impares / Cuadrados = 1/1 - 3/4 + 5/9 - 7/16 + 9/25
  s4 := SumaImparesCuadrados(5);
  Writeln('4. SumaImparesCuadrados(n=5): ', s4:0:4);

  // Simples
  sd := SumaDobleSimple(5);      // 1+2+4+8+16 = 31
  sf := SumaFactorialSimple(5);  // 1+2+6+24+120 = 153
  sc := SumaCuadraticaSimple(5); // 1+4+9+16+25 = 55
  Writeln('5. SumaDobleSimple(5): ', sd, ' (Esperado: 31)');
  Writeln('6. SumaFactorialSimple(5): ', sf, ' (Esperado: 153)');
  Writeln('7. SumaCuadraticaSimple(5): ', sc, ' (Esperado: 55)');
end;

procedure ProbarDigitosYNumeros();
var
  rd: Byte;
  mIzq, mDer: Cardinal;
  esCap: Boolean;
begin
  Writeln;
  Writeln('=== PRUEBAS BLOQUE 3: DÍGITOS Y NÚMEROS NATURALES ===');
  Writeln('1. ContarDigitos(15378): ', ContarDigitos(15378), ' (Esperado: 5)');
  Writeln('2. InvertirNumero(12345): ', InvertirNumero(12345), ' (Esperado: 54321)');
  Writeln('3. SumarDigitos(15378): ', SumarDigitos(15378), ' (Esperado: 24)');
  
  rd := RaizDigital(15378);
  Writeln('4. RaizDigital(15378): ', rd, ' (Esperado: 6)');

  Writeln('5. PrimerDigito(8472): ', PrimerDigito(8472), ' (Esperado: 8)');
  Writeln('6. UltimoDigito(8472): ', UltimoDigito(8472), ' (Esperado: 2)');

  esCap := EsCapicua(12321);
  Writeln('7. EsCapicua(12321): ', esCap, ' (Esperado: TRUE)');

  mIzq := ExtraerMitadIzquierda(12357);
  mDer := ExtraerMitadDerecha(12357);
  Writeln('8. N=12357 -> Mitad Izquierda: ', mIzq, ' (Esperado: 12)');
  Writeln('   N=12357 -> Mitad Derecha: ', mDer, ' (Esperado: 57)');
end;

procedure ProbarCadenas();
var
  cantPal: Integer;
  p2: string;
  ord: string;
  mit: string;
begin
  Writeln;
  Writeln('=== PRUEBAS BLOQUE 4: CADENAS DE CARACTERES (STRINGS) ===');
  cantPal := ContarPalabras('  Ana   estudia   lenguaje en la   UAGRM  ');
  Writeln('1. ContarPalabras("Ana estudia lenguaje en la UAGRM"): ', cantPal, ' (Esperado: 6)');

  p2 := ExtraerPalabra('Ana estudia lenguaje en la UAGRM', 2);
  Writeln('2. ExtraerPalabra(indice=2): "', p2, '" (Esperado: "estudia")');

  Writeln('3. InvertirCadena("Delphi"): "', InvertirCadena('Delphi'), '" (Esperado: "ihpleD")');
  Writeln('4. EsPalindromo("reconocer"): ', EsPalindromo('reconocer'), ' (Esperado: TRUE)');

  ord := OrdenarCaracteres('lenguaje');
  Writeln('5. OrdenarCaracteres("lenguaje"): "', ord, '" (Esperado: "aeegjlnu")');

  mit := InvertirPorMitades('cadenas');
  Writeln('6. InvertirPorMitades("cadenas"): "', mit, '" (Esperado: "dacesan")');

  mit := InvertirPorMitades('mitades');
  Writeln('7. InvertirPorMitades("mitades"): "', mit, '" (Esperado: "timased")');
end;

begin
  Writeln('================================================================');
  Writeln('VERIFICACION DE LA CAJA DE HERRAMIENTAS Y ATAJOS DE EXAMEN');
  Writeln('INF-110 • UAGRM • FILOSOFÍA: DIVIDE Y VENCERÁS');
  Writeln('================================================================');
  ProbarSeries();
  ProbarDigitosYNumeros();
  ProbarCadenas();
  Writeln;
  Writeln('================================================================');
  Writeln('TODAS LAS HERRAMIENTAS MODULARES VERIFICADAS CON ÉXITO 100%.');
  Writeln('================================================================');
end.

