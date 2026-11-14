program TestAtajosCadenas;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

uses
  SysUtils, UAtajosCadenas, UCCadena;

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
  ObjetoCadena: ClaseCadena;
  ResultadoStr: string;
begin
  WriteLn('================================================================');
  WriteLn('VERIFICACION DE LA CAJA DE HERRAMIENTAS Y ATAJOS DE CADENAS');
  WriteLn('INF-110 · UAGRM · DOCENTE: M.SC. ING. ANGELICA GARZON CUELLAR');
  WriteLn('================================================================');

  // BLOQUE 0: AUXILIARES MANUALES
  ReportarPrueba('LongitudManual', LongitudManual('Delphi') = 6, 'Longitud de "Delphi" = 6');
  ReportarPrueba('CopiarManual', CopiarManual('Programacion', 1, 8) = 'Programa', 'CopiarManual("Programacion", 1, 8) = "Programa"');
  ReportarPrueba('PosicionManual', PosicionManual('grama', 'Programacion') = 4, 'Posicion de "grama" en "Programacion" = 4');
  ReportarPrueba('TrimManual', TrimManual('   Hola Mundo   ') = 'Hola Mundo', 'TrimManual("   Hola Mundo   ") = "Hola Mundo"');

  // BLOQUE 1: MÉTODOS BÁSICOS
  ReportarPrueba('PrimeraLetra', PrimeraLetra('Delphi') = 'D', 'Primera letra = "D"');
  ReportarPrueba('UltimaLetra', UltimaLetra('Delphi') = 'i', 'Ultima letra = "i"');
  ReportarPrueba('ContarVocales', ContarVocales('Introduccion') = 5, 'ContarVocales("Introduccion") = 5');
  ReportarPrueba('ContarConsonantes', ContarConsonantes('cadena de texto') = 7, 'ContarConsonantes("cadena de texto") = 7');
  ReportarPrueba('ContarMayusculas', ContarMayusculas('Delphi IDE 2026') = 4, 'ContarMayusculas = 4');
  ReportarPrueba('BuscarPosicionesCaracter', BuscarPosicionesCaracter('Hola cadena de texto', 'a') = '4, 7, 11', 'Posiciones de "a" = 4, 7, 11');

  // BLOQUE 2: INVERSIÓN Y PALÍNDROMOS
  ReportarPrueba('InvertirCadena', InvertirCadena('Delphi') = 'ihpleD', 'Invertir("Delphi") = "ihpleD"');
  ReportarPrueba('EsPalindromo', EsPalindromo('anita lava la tina'), 'EsPalindromo("anita lava la tina") = TRUE');
  ReportarPrueba('InvertirPorMitades Impar', InvertirPorMitades('cadenas') = 'dacesan', 'InvertirPorMitades("cadenas") = "dacesan"');
  ReportarPrueba('InvertirPorMitades Impar 2', InvertirPorMitades('mitades') = 'timased', 'InvertirPorMitades("mitades") = "timased"');
  ReportarPrueba('InvertirPorMitades Par', InvertirPorMitades('abcd') = 'badc', 'InvertirPorMitades("abcd") = "badc"');

  // BLOQUE 3: MANIPULACIÓN DE PALABRAS
  ReportarPrueba('ContarPalabras', ContarPalabras('Hola cadena de texto') = 4, 'ContarPalabras("Hola cadena de texto") = 4');
  ReportarPrueba('ExtraerPalabra', ExtraerPalabra('Hola cadena de texto', 2) = 'cadena', 'ExtraerPalabra 2 = "cadena"');
  ReportarPrueba('InvertirSegundaPalabra', InvertirSegundaPalabra('Hola cadena de texto') = 'Hola anedac de texto', 'InvertirSegundaPalabra = "Hola anedac de texto"');
  ReportarPrueba('EliminarPalabraK', EliminarPalabraK('Hola cadena de texto', 2) = 'Hola de texto', 'EliminarPalabra 2 = "Hola de texto"');
  ReportarPrueba('ContarPalabrasDosVocalesJuntas', ContarPalabrasDosVocalesJuntas('eleccion superior de bolivia') = 3, '2 vocales juntas = 3 palabras');

  // BLOQUE 4: ORDENAMIENTO
  ReportarPrueba('OrdenarCaracteresAscendente', OrdenarCaracteresAscendente('lenguaje') = 'aeegjlnu', 'Ordenar("lenguaje") = "aeegjlnu"');
  ReportarPrueba('OrdenarPalabraQueComienzaEnConsonante', OrdenarPalabraQueComienzaEnConsonante('Ana estudia lenguaje') = 'aeegjlnu', 'Examen 2024-1 Z2 P3 = "aeegjlnu"');
  ReportarPrueba('OrdenarSegundaPalabra', OrdenarSegundaPalabra('Hola mundo') = 'Hola dmnou', 'Ordenar 2da palabra = "Hola dmnou"');

  // BLOQUE 5: TRANSFORMACIONES Y CIFRADO
  ReportarPrueba('FormatoTitulo', FormatoTitulo('hola mundo de delphi') = 'Hola Mundo De Delphi', 'FormatoTitulo = "Hola Mundo De Delphi"');
  ReportarPrueba('EliminarEspaciosRepetidos', EliminarEspaciosRepetidos('  hola   mundo   delphi  ') = 'hola mundo delphi', 'EliminarEspaciosRepetidos = "hola mundo delphi"');
  ReportarPrueba('IntercalarCadenas', IntercalarCadenas('ABC', '12345') = 'A1B2C345', 'Intercalar("ABC", "12345") = "A1B2C345"');
  ReportarPrueba('CifradoCesar', CifradoCesar('HOLA', 3) = 'KROD', 'Cesar("HOLA", 3) = "KROD"');

  // BLOQUE 6: VERIFICACIÓN DE LA CLASE ORIENTADA A OBJETOS (UCCadena.pas)
  ObjetoCadena := ClaseCadena.Create;
  try
    ObjetoCadena.Cargar('cadenas');
    ReportarPrueba('POO Longitud', ObjetoCadena.Longitud = 7, 'Longitud POO = 7');
    ObjetoCadena.InvertirPorMitades;
    ReportarPrueba('POO InvertirPorMitades', ObjetoCadena.Descargar = 'dacesan', 'Descargar POO = "dacesan"');

    ObjetoCadena.Cargar('hola mundo delphi');
    ObjetoCadena.InvertirSegundaPalabra;
    ReportarPrueba('POO InvertirSegundaPalabra', ObjetoCadena.Descargar = 'hola odnum delphi', 'Invertir 2da palabra POO = "hola odnum delphi"');

    ObjetoCadena.FormatoTitulo;
    ReportarPrueba('POO FormatoTitulo', ObjetoCadena.Descargar = 'Hola Odnum Delphi', 'FormatoTitulo POO = "Hola Odnum Delphi"');
  finally
    ObjetoCadena.Free;
  end;

  WriteLn('================================================================');
  WriteLn('TODAS LAS PRUEBAS DE CADENAS PASARON CON EXITO (100% OK)');
  WriteLn('================================================================');
end.

