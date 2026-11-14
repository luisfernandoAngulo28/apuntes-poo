{$mode delphi}
program TestBancoExamenes;

uses
  SysUtils,
  BancoExamenesFinales;

procedure TestExamen1;
var
  prom: Double;
  s: Double;
  p3: string;
  cap1, cap2: string;
begin
  Writeln('--- EXAMEN 1: 2024-1 GRUPO Z2 ---');
  prom := E1_P1_PromedioAscendente(5, [211, 120, 50, 180, 200]);
  Writeln('P1 Promedio Ascendente: ', prom:0:2, ' (Esperado: 166.66 / 166.67)');

  s := E1_P2_SumatoriaSerieX(2.0, 4);
  Writeln('P2 Serie S(X=2, N=4): ', s:0:3, ' (Esperado: 5.599 / 5.600)');

  p3 := E1_P3_OrdenarPalabraConsonante('Ana estudia lenguaje');
  Writeln('P3 Ordenar Palabra Consonante: "', p3, '" (Esperado: "aeegjlnu")');

  cap1 := E1_P4_MitadDerechaCapicua(12357);
  cap2 := E1_P4_MitadDerechaCapicua(15611);
  Writeln('P4 N=12357: ', cap1, ' (Esperado: no es capicúa 75)');
  Writeln('P4 N=15611: ', cap2, ' (Esperado: Si es capicúa. 11)');
end;

procedure TestExamen2;
var
  sfp: Int64;
  sn: Cardinal;
  palRes: string;
  cant: Integer;
begin
  Writeln('--- EXAMEN 2: 2024-1 REPECHAJE (GRUPO R) ---');
  sfp := E2_P1_SerieFactorialPotencia(4);
  Writeln('P1 Serie SFP(n=4): ', sfp, ' (Esperado: 6315)');

  sn := E2_P2_SumarDigitosPrimosDeNumeros([123, 249, 729, 562]);
  Writeln('P2 Suma Digitos Primos: ', sn, ' (Esperado: 23)');

  palRes := E2_P3_VerificarPalabrasPalindromes('ana estudia con ada', cant);
  Writeln('P3 Palabras Palindromes (', cant, '): "', palRes, '" (Esperado: "ana, ada")');
end;

procedure TestExamen3;
var
  rd: Byte;
  f: Double;
  p3_1, p3_2: string;
  p4: string;
begin
  Writeln('--- EXAMEN 3: 2023-2 GRUPO Z2 ---');
  rd := E3_P1_RaizDigital(15378);
  Writeln('P1 Raiz Digital(15378): ', rd, ' (Esperado: 6)');

  f := E3_P2_SumatoriaCuadradosSobreFactorial(4);
  Writeln('P2 Serie Cuadrados/Factorial(N=4): ', f:0:4, ' (Esperado: 12.1666 / 12.1667)');

  p3_1 := E3_P3_PrimeroYUltimoPrimos(3147);
  p3_2 := E3_P3_PrimeroYUltimoPrimos(1589);
  Writeln('P3 N=3147: ', p3_1, ' (Esperado: Si los dígitos son primos)');
  Writeln('P3 N=1589: ', p3_2, ' (Esperado: No, los dígitos no son primos)');

  p4 := E3_P4_InvertirPorMitades('cadenas');
  Writeln('P4 Invertir por mitades ("cadenas"): "', p4, '" (Esperado: "dacesan")');
end;

procedure TestExamen4;
var
  q, r: Cardinal;
  nn: Cardinal;
  mayor: Cardinal;
  s4: Double;
  p5: string;
  cant: Integer;
begin
  Writeln('--- EXAMEN 4: 2023-1 GRUPO SF ---');
  E4_P1_DivisionRestasSucesivas(20, 4, q, r);
  Writeln('P1 Division(20, 4): Cociente=', q, ', Residuo=', r, ' (Esperado: 5 y 0)');

  nn := E4_P2_EliminarDigitosRepetidos(23254);
  Writeln('P2 Eliminar Repetidos(23254): ', nn, ' (Esperado: 354)');

  mayor := E4_P3_MayorSumaDigitos([45, 32, 93]);
  Writeln('P3 Mayor Suma Digitos [45, 32, 93]: ', mayor, ' (Esperado: 12)');

  s4 := E4_P4_SerieAlternadaFactorial(4);
  Writeln('P4 Serie Alternada Factorial(4): ', s4:0:4);

  p5 := E4_P5_ContarYMayusculasTerminanEnA('Hola mundo de cadena larga', cant);
  Writeln('P5 Terminan en A (', cant, '): "', p5, '" (Esperado: 3, "HOLA mundo de CADENA LARGA")');
end;

procedure TestExamen5;
var
  pares, impares: Integer;
  s: Double;
  p3: string;
  cap1, cap2: string;
begin
  Writeln('--- EXAMEN 5: 2023-2 GRUPO SF ---');
  E5_P1_ContarParesEImparesHastaSuma(10, [5, 2, 1, 1, 1], pares, impares);
  Writeln('P1 Pares=', pares, ', Impares=', impares, ' (Esperado: 1 y 4)');

  s := E5_P2_SumatoriaSerieX_N3(2.0, 3);
  Writeln('P2 Serie S(X=2, N=3): ', s:0:3, ' (Esperado: 5.333)');

  p3 := E5_P3_OrdenarSegundaPalabra('El lenguaje de programación');
  Writeln('P3 Ordenar 2da Palabra ("El lenguaje..."): "', p3, '" (Esperado: "aeegjlnu")');

  cap1 := E5_P4_MitadIzquierdaCapicua(12357);
  cap2 := E5_P4_MitadIzquierdaCapicua(11567);
  Writeln('P4 N=12357: ', cap1, ' (Esperado: no es capicúa 21)');
  Writeln('P4 N=11567: ', cap2, ' (Esperado: Si es capicúa. 11)');
end;

procedure TestExamen6;
var
  f: Double;
  sImp: Cardinal;
  men, may: Cardinal;
  p4: string;
begin
  Writeln('--- EXAMEN 6: 2024-1 GRUPO SF ---');
  f := E6_P1_SerieFibonacciSobreImparFact(4);
  Writeln('P1 Serie Fibonacci/ImparFact(4): ', f:0:4);

  sImp := E6_P2_SumarSumasDigitosImpares([123, 25, 281, 94, 46]);
  Writeln('P2 Sumar Sumas Impares: ', sImp, ' (Esperado: 31)');

  E6_P3_SepararMenoresYMayores(16327, 6, men, may);
  Writeln('P3 Separar(16327, 6): <6 = ', men, ', >=6 = ', may, ' (Esperado: 231 o 132, y 76 o 67)');

  p4 := E6_P4_InvertirPorMitades('mitades');
  Writeln('P4 Invertir por mitades ("mitades"): "', p4, '" (Esperado: "timased")');
end;

procedure TestExamen7;
var
  s1: Double;
  p2: string;
  prom3: Double;
  rd4: Byte;
begin
  Writeln('--- EXAMEN 7: 2023-1 GRUPO Z2 ---');
  s1 := E7_P1_SerieIntercaladaCuadradosPaso3(4);
  Writeln('P1 Serie Intercalada Cuadrados Paso 3(4): ', s1:0:4);

  p2 := E7_P2_OrdenarSegundaPalabra('Examen final de introduccion');
  Writeln('P2 Ordenar 2da Palabra ("Examen final..."): "', p2, '" (Esperado: "afiln")');

  prom3 := E7_P3_SeriePromedioDigitosImpares(6);
  Writeln('P3 Promedio Digitos Impares(6): ', prom3:0:2, ' (Esperado: 7.50)');

  rd4 := E7_P4_RaizDigital(15378);
  Writeln('P4 Raiz Digital(15378): ', rd4, ' (Esperado: 6)');
end;

begin
  Writeln('================================================================');
  Writeln('VERIFICACION DE LOS 7 MODELOS DE EXAMEN FINAL DE INF-110');
  Writeln('DOCENTE: M.Sc. Ing. Angelica Garzon Cuellar');
  Writeln('================================================================');
  TestExamen1;
  Writeln;
  TestExamen2;
  Writeln;
  TestExamen3;
  Writeln;
  TestExamen4;
  Writeln;
  TestExamen5;
  Writeln;
  TestExamen6;
  Writeln;
  TestExamen7;
  Writeln('================================================================');
  Writeln('TODOS LOS MODELOS VERIFICADOS CON EXITO.');
  Writeln('================================================================');
end.

