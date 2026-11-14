program TestModelosSegundoParcial;

{$mode objfpc}{$H+}

uses
  SysUtils, UnitModelosSegundoParcial;

procedure AssertEqualsStr(expected, actual, testName: String);
begin
  if expected = actual then
    WriteLn('[OK] ', testName, ' -> "', actual, '"')
  else
  begin
    WriteLn('[ERROR] ', testName, ': Esperado "', expected, '" pero se obtuvo "', actual, '"');
    Halt(1);
  end;
end;

procedure AssertEqualsInt(expected, actual: Int64; testName: String);
begin
  if expected = actual then
    WriteLn('[OK] ', testName, ' -> ', actual)
  else
  begin
    WriteLn('[ERROR] ', testName, ': Esperado ', expected, ' pero se obtuvo ', actual);
    Halt(1);
  end;
end;

procedure AssertEqualsReal(expected, actual, tolerance: Real; testName: String);
begin
  if Abs(expected - actual) <= tolerance then
    WriteLn('[OK] ', testName, ' -> ', FloatToStrF(actual, ffFixed, 8, 4))
  else
  begin
    WriteLn('[ERROR] ', testName, ': Esperado ', FloatToStr(expected), ' pero se obtuvo ', FloatToStr(actual));
    Halt(1);
  end;
end;

var
  pPar, pImp: Real;

begin
  WriteLn('================================================================');
  WriteLn('  VERIFICACIÓN COMPLETA DE MODELOS DE 2DO PARCIAL (2022 - 2024) ');
  WriteLn('================================================================');

  { --- EXAMEN 1: 2024-1 Z2 (17/06/2024) --- }
  WriteLn(#10'--- EXAMEN 1: 2024-1 Z2 ---');
  AssertEqualsReal(35.84, SumaSerie_2024_1_Z2(4), 0.01, '2024-1 Z2 P1: Serie N=4');
  AssertEqualsInt(38, MenorImparMayorPar(85239), '2024-1 Z2 P2: MenorImpar=3, MayorPar=8 de 85239');
  AssertEqualsStr('Segundo examen laicrap', InvertirUltimaPalabra('Segundo examen parcial'), '2024-1 Z2 P3a: Invertir última palabra');
  AssertEqualsStr('euo eae aia', EliminarConsonantes('Segundo examen parcial'), '2024-1 Z2 P3b: Eliminar consonantes');

  { --- EXAMEN 2: 2024-1 Z2 REPECHAJE --- }
  WriteLn(#10'--- EXAMEN 2: 2024-1 Z2-R ---');
  AssertEqualsInt(14, SumaPotenciasX(2, 3), '2024-1 Z2-R P1: Suma potencias X=2, N=3');
  AssertEqualsInt(39, SumaPotenciasX(3, 3), '2024-1 Z2-R P1: Suma potencias X=3, N=3');
  AssertEqualsStr('ANA ESTUDIA programación', MayusculasPalabrasInicianVocal('Ana estudia programación'), '2024-1 Z2-R P2: Mayúsculas palabras inician vocal');

  { --- EXAMEN 3: 2024-1 SF (19/06/2024) --- }
  WriteLn(#10'--- EXAMEN 3: 2024-1 SF ---');
  AssertEqualsReal(16.0, SumaSerie_2024_1_SF(4), 0.0001, '2024-1 SF P1: Serie 2*i/Fib(i)! N=4');
  AssertEqualsInt(43, EliminarDesdePosicionK(78143, 3), '2024-1 SF P2: Eliminar desde pos 3 en 78143');
  AssertEqualsStr('Hola Mundo De Cadena', PrimerLetraCadaPalabraMayuscula('hola mundo de cadena'), '2024-1 SF P3: Primer carácter a mayúscula');

  { --- EXAMEN 4: 2023-2 Z2 (27/11/2023) --- }
  WriteLn(#10'--- EXAMEN 4: 2023-2 Z2 ---');
  AssertEqualsReal(35.84, SumaSerie_2024_1_Z2(4), 0.01, '2023-2 Z2 P1: Serie N=4');
  AssertEqualsInt(7813, EliminarDigitoPosicionK(78143, 2), '2023-2 Z2 P2: Eliminar dígito pos 2 en 78143');
  AssertEqualsStr('2, 2, 1, 3', CantidadVocalesPorPalabra('Hola mundo de cadena'), '2023-2 Z2 P3: Cantidad de vocales por palabra');

  { --- EXAMEN 5: 2023-1 Z2 (26/06/2023) --- }
  WriteLn(#10'--- EXAMEN 5: 2023-1 Z2 ---');
  // Nota: En la hoja del examen se escribió '15,2069' por error aritmético manual de la docente al sumar
  // (1/5 + 4/6 + 27/11 + 256/17 = 0.2 + 0.6667 + 2.4545 + 15.0588 = 18.3800). La fórmula exacta da 18.3800:
  AssertEqualsReal(18.3800, SumaSerie_2023_1_Z2(4), 0.001, '2023-1 Z2 P1: Serie i^i / DenomFib(5,6) N=4 (1/5+4/6+27/11+256/17)');
  AssertEqualsInt(7813, EliminarDigitoPosicionK(78143, 2), '2023-1 Z2 P2: Eliminar dígito pos 2');
  AssertEqualsStr('ATNAS ZURC ED AL ARREIS', InvertirCadaPalabra('SANTA CRUZ DE LA SIERRA'), '2023-1 Z2 P3: Invertir cada palabra');

  { --- EXAMEN 6: 2023-1 PIZARRA --- }
  WriteLn(#10'--- EXAMEN 6: 2023-1 PIZARRA ---');
  AssertEqualsReal(22.0, SumaSerie_2023_1_Pizarra(4), 0.0001, '2023-1 Pizarra P1: Serie i^2/Fib(i)! N=4');
  PromediosParEImpar(12345, pPar, pImp);
  AssertEqualsReal(3.0, pPar, 0.001, '2023-1 Pizarra P2: Promedio Pares de 12345 (2+4)/2 = 3.0');
  AssertEqualsReal(3.0, pImp, 0.001, '2023-1 Pizarra P2: Promedio Impares de 12345 (1+3+5)/3 = 3.0');

  { --- EXAMEN 7: 2022-1 MÓDULOS --- }
  WriteLn(#10'--- EXAMEN 7: 2022-1 MÓDULOS ---');
  AssertEqualsInt(6, DigitoMayorMultiplo3(8326), '2022-1 P1: Dígito mayor múltiplo de 3 en 8326');
  AssertEqualsReal(5.0, PromedioSerie_2022_1(4), 0.001, '2022-1 P2: Promedio serie entrelazada N=4: (4+2+8+6)/4');
  AssertEqualsInt(3, ContarPalabrasTerminanVocal('Hola a los alumnos de programacion'), '2022-1 P3: Palabras terminan en vocal');
  AssertEqualsInt(3, ContarPalabrasInicianMayuscula('Cadena de Texto de Programacion'), '2022-1 P4: Palabras inician con mayúscula');
  AssertEqualsStr('rgaa', ExtraerCaracteresIndicesPares('programa'), '2022-1 P5: Caracteres en índices pares de programa');

  { --- PLUS: ORDENACIÓN BURBUJA DE CLASE --- }
  WriteLn(#10'--- PLUS: ORDENACIÓN DE CADENAS DE CLASE ---');
  AssertEqualsStr('Casa de aan', OrdenarUltimaPalabra('Casa de ana'), 'Clase Ordenar: Última palabra');
  AssertEqualsStr('Hola odnum de Cadena', InvertirSegundaPalabra('Hola mundo de Cadena'), 'Clase Ordenar: Invertir 2da palabra');
  AssertEqualsStr('Hola dmnou de Cadena', OrdenarSegundaPalabra('Hola mundo de Cadena'), 'Clase Ordenar: Ordenar 2da palabra');

  WriteLn(#10'================================================================');
  WriteLn('  ¡TODAS LAS PRUEBAS DE LOS 7 EXÁMENES PASARON AL 100%! ');
  WriteLn('================================================================');
end.
