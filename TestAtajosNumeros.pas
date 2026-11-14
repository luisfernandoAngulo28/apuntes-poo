program TestAtajosNumeros;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

uses
  SysUtils, UAtajosNumeros, UCNatural;

procedure ReportarPrueba(const Nombre: string; Condicion: Boolean; const Detalle: string);
begin
  if Condicion then
    WriteLn('[OK] ', Nombre, ' -> ', Detalle)
  else
  begin
    WriteLn('[FALLO] ', Nombre, ' -> ', Detalle);
    Halt(1);
  end;
end;

var
  ObjetoNum: NumeroNatural;
  MitadExt, Men, May: Cardinal;
  SumaP, SumaI: Cardinal;
begin
  WriteLn('================================================================');
  WriteLn('VERIFICACION DE LA CAJA DE HERRAMIENTAS Y ATAJOS DE NUMEROS');
  WriteLn('INF-110 · UAGRM · DOCENTE: M.SC. ING. ANGELICA GARZON CUELLAR');
  WriteLn('================================================================');

  // BLOQUE 0: OPERACIONES ATÓMICAS FUNDAMENTALES
  ReportarPrueba('ContarDigitos(15378)', ContarDigitos(15378) = 5, 'ContarDigitos(15378) = 5');
  ReportarPrueba('ContarDigitos(0)', ContarDigitos(0) = 1, 'ContarDigitos(0) = 1');
  ReportarPrueba('PrimerDigito(8472)', PrimerDigito(8472) = 8, 'PrimerDigito(8472) = 8');
  ReportarPrueba('UltimoDigito(8472)', UltimoDigito(8472) = 2, 'UltimoDigito(8472) = 2');
  ReportarPrueba('ExtraerUltimoDigito(123)', ExtraerUltimoDigito(123) = 3, 'ExtraerUltimoDigito(123) = 3');
  ReportarPrueba('EliminarUltimoDigito(123)', EliminarUltimoDigito(123) = 12, 'EliminarUltimoDigito(123) = 12');

  // BLOQUE 1: INVERSIÓN Y CAPICÚAS
  ReportarPrueba('InvertirNumero(12345)', InvertirNumero(12345) = 54321, 'InvertirNumero(12345) = 54321');
  ReportarPrueba('EsCapicua(12321)', EsCapicua(12321), 'EsCapicua(12321) = TRUE');
  ReportarPrueba('ExtraerMitadDerecha(12357)', ExtraerMitadDerecha(12357) = 57, 'ExtraerMitadDerecha(12357) = 57');
  ReportarPrueba('ExtraerMitadIzquierda(12357)', ExtraerMitadIzquierda(12357) = 12, 'ExtraerMitadIzquierda(12357) = 12');
  
  // Examen 2024-1 Z2: Mitad derecha capicúa
  ReportarPrueba('MitadDerechaEsCapicua(15611)', MitadDerechaEsCapicua(15611, MitadExt) and (MitadExt = 11), 'N=15611 -> Mitad Derecha 11 es capicúa');
  ReportarPrueba('MitadDerechaEsCapicua(12357) No', not MitadDerechaEsCapicua(12357, MitadExt) and (MitadExt = 57), 'N=12357 -> Mitad Derecha 57 NO es capicúa');

  // Examen 2024-1 R: Mitad izquierda capicúa
  ReportarPrueba('MitadIzquierdaEsCapicua(44512)', MitadIzquierdaEsCapicua(44512, MitadExt) and (MitadExt = 44), 'N=44512 -> Mitad Izquierda 44 es capicúa');
  ReportarPrueba('MitadIzquierdaEsCapicua(24431) No', not MitadIzquierdaEsCapicua(24431, MitadExt) and (MitadExt = 24), 'N=24431 -> Mitad Izquierda 24 no es capicúa');

  // BLOQUE 2: PROPIEDADES MATEMÁTICAS Y PRIMOS
  ReportarPrueba('EsDigitoPrimo(7)', EsDigitoPrimo(7) and not EsDigitoPrimo(9), '7 es primo, 9 no es primo');
  ReportarPrueba('PrimeroYUltimoDigitoPrimos(2457)', PrimeroYUltimoDigitoPrimos(2457), 'N=2457 -> 2 y 7 son primos (TRUE)');
  ReportarPrueba('PrimeroYUltimoDigitoPrimos(4457)', not PrimeroYUltimoDigitoPrimos(4457), 'N=4457 -> 4 no es primo (FALSE)');
  ReportarPrueba('SumarDigitos(15378)', SumarDigitos(15378) = 24, 'SumarDigitos(15378) = 24');
  ReportarPrueba('MultiplicarDigitos(423)', MultiplicarDigitos(423) = 24, 'MultiplicarDigitos(423) = 24');
  ReportarPrueba('RaizDigital(15378)', RaizDigital(15378) = 6, 'RaizDigital(15378) = 6');

  // BLOQUE 3: CONTEO, FILTRADO Y TRANSFORMACIÓN
  ReportarPrueba('ContarDigitosPares(48263)', ContarDigitosPares(48263) = 4, 'Pares en 48263 = 4');
  ReportarPrueba('ContarDigitosImpares(48263)', ContarDigitosImpares(48263) = 1, 'Impares en 48263 = 1');
  ReportarPrueba('EliminarCeros(10203040)', EliminarCeros(10203040) = 1234, 'EliminarCeros(10203040) = 1234');
  ReportarPrueba('TodosDigitosIguales(7777)', TodosDigitosIguales(7777), 'TodosDigitosIguales(7777) = TRUE');
  ReportarPrueba('DigitosOrdenadosAsc(12356)', DigitosOrdenadosAsc(12356), 'DigitosOrdenadosAsc(12356) = TRUE');
  ReportarPrueba('FrecuenciaDigito(232523, 2)', FrecuenciaDigito(232523, 2) = 3, 'Frecuencia de 2 en 232523 = 3');
  
  // Examen 2023-2 Z2: Eliminar repetidos
  ReportarPrueba('EliminarDigitosRepetidos(1537831)', EliminarDigitosRepetidos(1537831) = 578, 'Eliminar repetidos de 1537831 = 578');

  // Examen 2024-1 SF: Separar por criterio
  SepararDigitosMenoresYMayores(16327, 6, Men, May);
  ReportarPrueba('SepararDigitosMenoresYMayores', (Men = 231) and (May = 76), 'N=16327 Criterio=6 -> Menores: 231, Mayores: 76');

  // BLOQUE 4: CONVERSIÓN DE BASES
  ReportarPrueba('ConvertirABinario(9)', ConvertirABinario(9) = '1001', 'ConvertirABinario(9) = "1001"');
  ReportarPrueba('EsPalindromoBinario(9)', EsPalindromoBinario(9), '9 en binario (1001) es palíndromo = TRUE');
  ReportarPrueba('EsPalindromoBinario(10)', not EsPalindromoBinario(10), '10 en binario (1010) NO es palíndromo = FALSE');
  ReportarPrueba('ContarBitsUno(7)', ContarBitsUno(7) = 3, '7 en binario (111) tiene 3 bits 1');
  ReportarPrueba('ConvertirAOctal(18)', ConvertirAOctal(18) = '22', '18 en octal = "22"');
  ReportarPrueba('ConvertirAHexadecimal(29)', ConvertirAHexadecimal(29) = '1D', '29 en hex = "1D"');

  // BLOQUE 5: VERIFICACIÓN CON LA CLASE NumeroNatural (POO)
  ObjetoNum := NumeroNatural.Create;
  try
    ObjetoNum.CambiarValor(15378);
    ReportarPrueba('POO ContarDigitos', ObjetoNum.ContarDigitos = 5, 'POO ContarDigitos = 5');
    ReportarPrueba('POO SumarDigitosHastaMenor10', ObjetoNum.SumarDigitosHastaMenor10 = 6, 'POO Raiz Digital = 6');
    
    ObjetoNum.CambiarValor(15611);
    ReportarPrueba('POO MitadDerechaCapicua', Pos('Si es capicua', ObjetoNum.MitadDerechaCapicua) > 0, 'POO Mitad Derecha 11 es capicúa');
  finally
    ObjetoNum.Free;
  end;

  WriteLn('================================================================');
  WriteLn('TODAS LAS PRUEBAS DE NUMEROS PASARON CON EXITO (100% OK)');
  WriteLn('================================================================');
end.
