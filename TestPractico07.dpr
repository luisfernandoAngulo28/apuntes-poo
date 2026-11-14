program TestPractico07;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  UnitNumeros in 'UnitNumeros.pas',
  UnitClaseNumero in 'UnitClaseNumero.pas';

var
  totalTests, passedTests: Integer;

procedure AssertEqualsCard(nombreTest: String; actual, esperado: Cardinal);
begin
  Inc(totalTests);
  if actual = esperado then
  begin
    Inc(passedTests);
    Writeln('  [PASO] ', nombreTest, ' = ', actual);
  end
  else
    Writeln('  [FALLO X] ', nombreTest, ': Esperado ', esperado, ', pero se obtuvo ', actual);
end;

procedure AssertEqualsInt(nombreTest: String; actual, esperado: Integer);
begin
  Inc(totalTests);
  if actual = esperado then
  begin
    Inc(passedTests);
    Writeln('  [PASO] ', nombreTest, ' = ', actual);
  end
  else
    Writeln('  [FALLO X] ', nombreTest, ': Esperado ', esperado, ', pero se obtuvo ', actual);
end;

procedure AssertEqualsStr(nombreTest: String; actual, esperado: String);
begin
  Inc(totalTests);
  if actual = esperado then
  begin
    Inc(passedTests);
    Writeln('  [PASO] ', nombreTest, ' = ''', actual, '''');
  end
  else
    Writeln('  [FALLO X] ', nombreTest, ': Esperado ''', esperado, ''', pero se obtuvo ''', actual, '''');
end;

procedure AssertEqualsBool(nombreTest: String; actual, esperado: Boolean);
begin
  Inc(totalTests);
  if actual = esperado then
  begin
    Inc(passedTests);
    Writeln('  [PASO] ', nombreTest, ' = ', BoolToStr(actual, True));
  end
  else
    Writeln('  [FALLO X] ', nombreTest, ': Esperado ', BoolToStr(esperado, True), ', obtenido ', BoolToStr(actual, True));
end;

procedure EjecutarSuiteDePruebas;
var
  p, u, dMayor, dMenor: Byte;
  nPares, nImpares: Cardinal;
  objNum: TNumero;
begin
  totalTests := 0;
  passedTests := 0;

  Writeln('===============================================================');
  Writeln('    SUITE DE PRUEBAS UNITARIAS AUTOMATICAS (PRACTICO #7)      ');
  Writeln('===============================================================');

  Writeln(#10'--- 1. Pruebas de Funciones Modulares (UnitNumeros.pas) ---');
  AssertEqualsCard('1. SumaImparesMayores3(37952)', SumaImparesMayores3(37952), 21);
  AssertEqualsInt('2. DigitoMayorIndicesImpares(48291)', DigitoMayorIndicesImpares(48291), 4);
  AssertEqualsCard('3. SumaDigitos(5821)', SumaDigitos(5821), 16);
  AssertEqualsCard('6. FormarNumeroPares(741829)', FormarNumeroPares(741829), 482);
  AssertEqualsInt('8. MayorDigitoPar(173825)', MayorDigitoPar(173825), 8);
  AssertEqualsStr('9. DigitosMultiplosDe3(439260)', DigitosMultiplosDe3(439260), '3, 9, 6, 0');
  
  PrimerYUltimoDigito(74582, p, u);
  AssertEqualsInt('10a. Primer Digito (74582)', p, 7);
  AssertEqualsInt('10b. Ultimo Digito (74582)', u, 2);

  AssertEqualsCard('11. EliminarPrimerYUltimoDigito(93451)', EliminarPrimerYUltimoDigito(93451), 345);
  AssertEqualsCard('12. InvertirNumero(4782)', InvertirNumero(4782), 2874);
  AssertEqualsCard('13. ContarMultiplosDeCuatro(480124)', ContarMultiplosDeCuatro(480124), 4);
  AssertEqualsInt('14. MenorDigitoMultiploDeTres(79638)', MenorDigitoMultiploDeTres(79638), 3);
  AssertEqualsBool('15a. EsCapicua(12321)', EsCapicua(12321), True);
  AssertEqualsBool('15b. EsCapicua(12345)', EsCapicua(12345), False);
  AssertEqualsStr('16. DecimalABinario(13)', DecimalABinario(13), '1101');
  AssertEqualsStr('17. DecimalAHexadecimal(254)', DecimalAHexadecimal(254), 'FE');
  AssertEqualsStr('18. DecimalAOctal(65)', DecimalAOctal(65), '101');
  AssertEqualsCard('19. SumaDigitosPrimos(24783)', SumaDigitosPrimos(24783), 12);
  AssertEqualsCard('22. FormarNumeroPrimos(427951)', FormarNumeroPrimos(427951), 275);
  AssertEqualsStr('25. OctalAHexadecimal(''752'')', OctalAHexadecimal('752'), '1EA');

  Writeln(#10'--- 2. Pruebas de la Clase POO (TNumero en UnitClaseNumero.pas) ---');
  objNum := TNumero.Create(1234);
  try
    AssertEqualsCard('POO Valor Inicial', objNum.Valor, 1234);
    AssertEqualsCard('POO SumarDigitosPrimos(1234)', objNum.SumarDigitosPrimos, 5); // 2 + 3 = 5
    AssertEqualsCard('POO FormarSoloPares(1234)', objNum.FormarSoloPares, 24);
    AssertEqualsCard('POO InvertirNumero(1234)', objNum.InvertirNumero, 4321);
    AssertEqualsCard('POO SumarMultiplosDe3(1234)', objNum.SumarMultiplosDe3, 3);
  finally
    objNum.Free;
  end;

  Writeln(#10'===============================================================');
  Writeln('  RESUMEN FINAL: ', passedTests, ' de ', totalTests, ' pruebas superadas.');
  if passedTests = totalTests then
    Writeln('  ESTADO: [100% EXITOSO - TODOS LOS ALGORITMOS FUNCIONAN]')
  else
    Writeln('  ESTADO: [HAY ERRORES EN LAS PRUEBAS]');
  Writeln('===============================================================');
end;

begin
  try
    EjecutarSuiteDePruebas;
  except
    on E: Exception do
      Writeln('Excepcion en ejecucion: ', E.Message);
  end;
end.
