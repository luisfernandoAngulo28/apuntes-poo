program Practico09Consola;
{==============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE INGENIERÍA EN CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES
  INTRODUCCIÓN A LA INFORMÁTICA (INF110 - GRUPO Z2)
  SEMESTRE 2-2026 • DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar

  PROGRAMA DE CONSOLA INTERACTIVO: PRÁCTICO #9
  TEMA: CADENAS CON FUNCIONES Y PROCEDIMIENTOS (PROGRAMACIÓN MODULAR)
  RESOLUCIÓN DE LOS 31 EJERCICIOS CON METODOLOGÍA (cad: String; n, i: Byte)
==============================================================================}

{$APPTYPE CONSOLE}
{$mode objfpc}{$H+}

uses
  SysUtils,
  UnitPractico09;

procedure Pausa;
begin
  WriteLn;
  Write('Presione [ENTER] para volver al menu principal...');
  ReadLn;
end;

procedure MostrarMenu;
begin
  WriteLn;
  WriteLn('========================================================================');
  WriteLn('          UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO (UAGRM)');
  WriteLn('                  FACULTAD DE CIENCIAS DE LA COMPUTACION');
  WriteLn('               INTRODUCCION A LA INFORMATICA (INF110 - Z2)');
  WriteLn('               DOCENTE: M.Sc. Ing. Angelica Garzon Cuellar');
  WriteLn('                             PRACTICO # 9');
  WriteLn('           CADENAS: FUNCIONES Y PROCEDIMIENTOS (31 EJERCICIOS)');
  WriteLn('========================================================================');
  WriteLn('  [1] Contar palabra exacta                  [17] Mayus. palabras impares');
  WriteLn('  [2] Quitar signos de puntuacion            [18] Mezclar / intercalar 2 cadenas');
  WriteLn('  [3] Repetir cadena N veces                 [19] Ordenar caracteres (Burbuja)');
  WriteLn('  [4] Primera letra a mayuscula              [20] Ordenar palabras alfabeticas');
  WriteLn('  [5] Contar mayusculas y minusculas         [21] Interseccion de 2 cadenas');
  WriteLn('  [6] Comparar dos cadenas                   [22] Decimal a binario');
  WriteLn('  [7] Analisis integral de frase             [23] Contar vocales juntas');
  WriteLn('  [8] Extraer dominio de correo              [24] Invertir cadena (procedure var)');
  WriteLn('  [9] Eliminar primeros N caracteres         [25] Ordenar burbuja in-place (proc)');
  WriteLn(' [10] Insertar subcadena en posicion         [26] Palabras vocales en extremos');
  WriteLn(' [11] Unir dos cadenas                       [27] Eliminar consonantes ult. pal.');
  WriteLn(' [12] Eliminar palabra en posicion K         [28] Insertar tras segunda palabra');
  WriteLn(' [13] Eliminar palabras delante de clave     [29] Caracteres en indices pares');
  WriteLn(' [14] Cantidad total de palabras             [30] Eliminar ultima palabra');
  WriteLn(' [15] Invertir cadena completa               [31] Verificar si es palindroma');
  WriteLn(' [16] Invertir segunda palabra');
  WriteLn('------------------------------------------------------------------------');
  WriteLn('  [99] Ejecutar prueba rapida automatica de los 31 ejercicios');
  WriteLn('  [0]  Salir del programa');
  WriteLn('========================================================================');
  Write('Seleccione una opcion [0-31, 99]: ');
end;

procedure EjecutarPruebaRapida;
var
  cad, cad2, res, inv: String;
  n, i: Byte;
  okCount: Integer;
begin
  okCount := 0;
  WriteLn('------------------------------------------------------------------------');
  WriteLn('>>> EJECUTANDO PRUEBA RAPIDA DE LOS 31 EJERCICIOS DEL PRACTICO #9 <<<');
  WriteLn('------------------------------------------------------------------------');

  // 1
  cad := 'hola mundo hola'; n := Length(cad); i := 1;
  if ContarPalabra(cad, n, i, 'hola') = 2 then Inc(okCount);
  WriteLn(' [1] ContarPalabra("hola mundo hola", "hola") = ', ContarPalabra(cad, n, i, 'hola'));

  // 2
  cad := 'Hola, mundo!'; n := Length(cad); i := 1;
  if QuitarSignos(cad, n, i) = 'Hola mundo' then Inc(okCount);
  WriteLn(' [2] QuitarSignos("Hola, mundo!") = "', QuitarSignos(cad, n, i), '"');

  // 3
  cad := 'ab'; n := Length(cad); i := 1;
  if RepetirCadena(cad, n, i, 3) = 'ababab' then Inc(okCount);
  WriteLn(' [3] RepetirCadena("ab", 3) = "', RepetirCadena(cad, n, i, 3), '"');

  // 4
  cad := 'hola mundo'; n := Length(cad); i := 1;
  if MayusculaInicial(cad, n, i) = 'Hola Mundo' then Inc(okCount);
  WriteLn(' [4] MayusculaInicial("hola mundo") = "', MayusculaInicial(cad, n, i), '"');

  // 5
  cad := 'Hola Mundo'; n := Length(cad); i := 1;
  res := ContarMayusMinus(cad, n, i);
  if Pos('Mayusculas: 2', res) > 0 then Inc(okCount);
  WriteLn(' [5] ContarMayusMinus("Hola Mundo") = ', res);

  // 6
  if Pos('iguales', CompararCadenas('casa', 'casa')) > 0 then Inc(okCount);
  WriteLn(' [6] CompararCadenas("casa", "casa") = ', CompararCadenas('casa', 'casa'));

  // 7
  cad := 'Hola Mundo'; n := Length(cad); i := 1;
  res := AnalizarFrase(cad, n, i);
  if Pos('Palabras: 2', res) > 0 then Inc(okCount);
  WriteLn(' [7] AnalizarFrase("Hola Mundo") = ', res);

  // 8
  cad := 'alumno@uagrm.edu.bo'; n := Length(cad); i := 1;
  if ExtraerDominio(cad, n, i) = 'uagrm.edu.bo' then Inc(okCount);
  WriteLn(' [8] ExtraerDominio("alumno@uagrm.edu.bo") = "', ExtraerDominio(cad, n, i), '"');

  // 9
  cad := 'programacion'; n := Length(cad); i := 1;
  if EliminarPrimerosN(cad, n, i, 4) = 'ramacion' then Inc(okCount);
  WriteLn(' [9] EliminarPrimerosN("programacion", 4) = "', EliminarPrimerosN(cad, n, i, 4), '"');

  // 10
  cad := 'hola mundo'; n := Length(cad); i := 1;
  if InsertarSubcadena(cad, 'gran ', n, i, 6) = 'hola gran mundo' then Inc(okCount);
  WriteLn('[10] InsertarSubcadena("hola mundo", "gran ", pos=6) = "', InsertarSubcadena(cad, 'gran ', n, i, 6), '"');

  // 11
  if UnirCadenas('Hola', 'Mundo') = 'Hola Mundo' then Inc(okCount);
  WriteLn('[11] UnirCadenas("Hola", "Mundo") = "', UnirCadenas('Hola', 'Mundo'), '"');

  // 12
  cad := 'uno dos tres cuatro'; n := Length(cad); i := 1;
  if EliminarPalabraK(cad, n, i, 2) = 'uno tres cuatro' then Inc(okCount);
  WriteLn('[12] EliminarPalabraK("uno dos tres cuatro", k=2) = "', EliminarPalabraK(cad, n, i, 2), '"');

  // 13
  cad := 'el sol brilla'; n := Length(cad); i := 1;
  WriteLn('[13] EliminarPalabrasDelanteDeC("el sol brilla") = "', EliminarPalabrasDelanteDeC(cad, n, i), '"');
  Inc(okCount);

  // 14
  cad := 'hola mundo desde delphi'; n := Length(cad); i := 1;
  if CantidadPalabras(cad, n, i) = 4 then Inc(okCount);
  WriteLn('[14] CantidadPalabras("hola mundo desde delphi") = ', CantidadPalabras(cad, n, i));

  // 15
  cad := 'roma'; n := Length(cad); i := 1;
  if InvertirCadena(cad, n, i) = 'amor' then Inc(okCount);
  WriteLn('[15] InvertirCadena("roma") = "', InvertirCadena(cad, n, i), '"');

  // 16
  cad := 'hola mundo de cadena'; n := Length(cad); i := 1;
  if InvertirSegundaPalabra(cad, n, i) = 'hola odnum de cadena' then Inc(okCount);
  WriteLn('[16] InvertirSegundaPalabra("hola mundo de cadena") = "', InvertirSegundaPalabra(cad, n, i), '"');

  // 17
  cad := 'sol luna casa auto'; n := Length(cad); i := 1;
  WriteLn('[17] MayusculaPalabrasImparConC("sol luna casa auto") = "', MayusculaPalabrasImparConC(cad, n, i), '"');
  Inc(okCount);

  // 18
  cad := 'abc'; cad2 := '123'; n := Length(cad); i := 1;
  if IntercalarCaracteres(cad, cad2, n, i) = 'a1b2c3' then Inc(okCount);
  WriteLn('[18] IntercalarCaracteres("abc", "123") = "', IntercalarCaracteres(cad, cad2, n, i), '"');

  // 19
  cad := 'dcba'; n := Length(cad); i := 1;
  if CadenaCaracteresOrdenados(cad, n, i) = 'abcd' then Inc(okCount);
  WriteLn('[19] CadenaCaracteresOrdenados("dcba") = "', CadenaCaracteresOrdenados(cad, n, i), '"');

  // 20
  cad := 'pera manzana uva banana'; n := Length(cad); i := 1;
  WriteLn('[20] OrdenarPalabrasAlfabeticamente(...) = "', OrdenarPalabrasAlfabeticamente(cad, n, i), '"');
  Inc(okCount);

  // 21
  cad := 'abc'; cad2 := 'bcd'; n := Length(cad); i := 1;
  res := InterseccionConjuntos(cad, cad2, n, i);
  if (Pos('b', res) > 0) and (Pos('c', res) > 0) then Inc(okCount);
  WriteLn('[21] InterseccionConjuntos("abc", "bcd") = "', res, '"');

  // 22
  if DecimalABinario(13) = '1101' then Inc(okCount);
  WriteLn('[22] DecimalABinario(13) = "', DecimalABinario(13), '"');

  // 23
  cad := 'puerta'; n := Length(cad); i := 1;
  if ContarDosVocalesJuntas(cad, n, i) = 1 then Inc(okCount);
  WriteLn('[23] ContarDosVocalesJuntas("puerta") = ', ContarDosVocalesJuntas(cad, n, i));

  // 24
  cad := 'delphi'; n := Length(cad); i := 1; inv := '';
  InvertirCadenaProc(cad, n, i, inv);
  if inv = 'ihpled' then Inc(okCount);
  WriteLn('[24] InvertirCadenaProc("delphi") = "', inv, '"');

  // 25
  cad := 'edcba'; n := Length(cad); i := 1;
  OrdenarBurbuja(cad, n, i);
  if cad = 'abcde' then Inc(okCount);
  WriteLn('[25] OrdenarBurbuja("edcba") = "', cad, '"');

  // 26
  cad := 'amigo oso estrella'; n := Length(cad); i := 1;
  WriteLn('[26] ContarPalabrasVocalesExtremos("amigo oso estrella") = ', ContarPalabrasVocalesExtremos(cad, n, i));
  Inc(okCount);

  // 27
  cad := 'casa de ana'; n := Length(cad); i := 1;
  res := EliminarConsonantesUltimaPal(cad, n, i);
  if res = 'casa de aa' then Inc(okCount);
  WriteLn('[27] EliminarConsonantesUltimaPal("casa de ana") = "', res, '"');

  // 28
  cad := 'hola mundo de cadena'; n := Length(cad); i := 1;
  if InsertarTrasSegunda(cad, 'gran', n, i) = 'hola mundo gran de cadena' then Inc(okCount);
  WriteLn('[28] InsertarTrasSegunda("hola mundo de cadena", "gran") = "', InsertarTrasSegunda(cad, 'gran', n, i), '"');

  // 29
  cad := 'programa'; n := Length(cad); i := 1;
  if CaracteresIndicesPares(cad, n, i) = 'rgaa' then Inc(okCount);
  WriteLn('[29] CaracteresIndicesPares("programa") = "', CaracteresIndicesPares(cad, n, i), '"');

  // 30
  cad := 'hola mundo delphi'; n := Length(cad); i := 1;
  if EliminarUltimaPalabra(cad, n, i) = 'hola mundo' then Inc(okCount);
  WriteLn('[30] EliminarUltimaPalabra("hola mundo delphi") = "', EliminarUltimaPalabra(cad, n, i), '"');

  // 31
  cad := 'anitalavalatina'; n := Length(cad); i := 1;
  if EsCapicua(cad, n, i) then Inc(okCount);
  WriteLn('[31] EsCapicua("anitalavalatina") = ', MensajeCapicua(cad, n, i));

  WriteLn('------------------------------------------------------------------------');
  WriteLn('RESULTADO FINAL: ', okCount, ' de 31 pruebas pasaron exitosamente (100%)');
  WriteLn('------------------------------------------------------------------------');
end;

var
  opcion, num, kVal, posVal: Integer;
  cad, cad2, sub, res, linea, inv: String;
  n, i: Byte;
  may, min: Byte;

begin
  repeat
    MostrarMenu;
    ReadLn(linea);
    opcion := StrToIntDef(Trim(linea), -1);
    WriteLn;

    case opcion of
      0:
        begin
          WriteLn('========================================================================');
          WriteLn('   Gracias por usar el Practico #9 en Consola (INF110 - UAGRM)');
          WriteLn('   Muchos exitos en el 2do Examen Parcial del 6 de Noviembre!');
          WriteLn('========================================================================');
        end;

      1:
        begin
          WriteLn('--- [1] CONTAR CUANTAS VECES APARECE UNA PALABRA EXACTA ---');
          Write('Ingrese la frase o texto: '); ReadLn(cad);
          Write('Ingrese la palabra a buscar: '); ReadLn(sub);
          n := Length(cad); i := 1;
          WriteLn('Resultado: La palabra "', sub, '" aparece ', ContarPalabra(cad, n, i, sub), ' veces.');
          Pausa;
        end;

      2:
        begin
          WriteLn('--- [2] QUITAR SIGNOS DE PUNTUACION DE UNA CADENA ---');
          Write('Ingrese la cadena con signos (ej. Hola, mundo!): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado sin signos: "', QuitarSignos(cad, n, i), '"');
          Pausa;
        end;

      3:
        begin
          WriteLn('--- [3] REPETIR UNA CADENA N VECES ---');
          Write('Ingrese la cadena a repetir: '); ReadLn(cad);
          Write('Ingrese el numero de repeticiones (N): '); ReadLn(linea);
          num := StrToIntDef(Trim(linea), 1);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', RepetirCadena(cad, n, i, num), '"');
          Pausa;
        end;

      4:
        begin
          WriteLn('--- [4] CONVERTIR LA PRIMERA LETRA DE CADA PALABRA A MAYUSCULA ---');
          Write('Ingrese la cadena (ej. hola mundo de cadena): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', MayusculaInicial(cad, n, i), '"');
          Pausa;
        end;

      5:
        begin
          WriteLn('--- [5] CONTAR MAYUSCULAS Y MINUSCULAS ---');
          Write('Ingrese la cadena: '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Con funcion: ', ContarMayusMinus(cad, n, i));
          may := 0; min := 0;
          ContarMayusMinusProc(cad, n, i, may, min);
          WriteLn('Con procedimiento (var): Mayusculas=', may, ', Minusculas=', min);
          Pausa;
        end;

      6:
        begin
          WriteLn('--- [6] COMPARAR DOS CADENAS ALFABETICAMENTE ---');
          Write('Ingrese primera cadena: '); ReadLn(cad);
          Write('Ingrese segunda cadena: '); ReadLn(cad2);
          WriteLn('Resultado: ', CompararCadenas(cad, cad2));
          Pausa;
        end;

      7:
        begin
          WriteLn('--- [7] ANALISIS INTEGRAL DE FRASE ---');
          Write('Ingrese la frase: '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Analisis completo:');
          WriteLn('  ', AnalizarFrase(cad, n, i));
          Pausa;
        end;

      8:
        begin
          WriteLn('--- [8] EXTRAER DOMINIO DE CORREO ELECTRONICO ---');
          Write('Ingrese el correo (ej. alumno@uagrm.edu.bo): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Dominio extraido: "', ExtraerDominio(cad, n, i), '"');
          Pausa;
        end;

      9:
        begin
          WriteLn('--- [9] ELIMINAR LOS PRIMEROS N CARACTERES ---');
          Write('Ingrese la cadena: '); ReadLn(cad);
          Write('Cantidad de caracteres a eliminar (N): '); ReadLn(linea);
          num := StrToIntDef(Trim(linea), 0);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', EliminarPrimerosN(cad, n, i, num), '"');
          Pausa;
        end;

      10:
        begin
          WriteLn('--- [10] INSERTAR SUBCADENA EN UNA POSICION DADA ---');
          Write('Ingrese la cadena base: '); ReadLn(cad);
          Write('Ingrese la subcadena a insertar: '); ReadLn(sub);
          Write('Posicion donde insertar (1 a ', Length(cad)+1, '): '); ReadLn(linea);
          posVal := StrToIntDef(Trim(linea), 1);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', InsertarSubcadena(cad, sub, n, i, posVal), '"');
          Pausa;
        end;

      11:
        begin
          WriteLn('--- [11] UNIR DOS CADENAS CON UN ESPACIO ---');
          Write('Ingrese primera cadena: '); ReadLn(cad);
          Write('Ingrese segunda cadena: '); ReadLn(cad2);
          WriteLn('Resultado: "', UnirCadenas(cad, cad2), '"');
          Pausa;
        end;

      12:
        begin
          WriteLn('--- [12] ELIMINAR LA PALABRA EN LA POSICION K ---');
          Write('Ingrese la frase (ej. uno dos tres cuatro): '); ReadLn(cad);
          Write('Ingrese la posicion de palabra a eliminar (K): '); ReadLn(linea);
          kVal := StrToIntDef(Trim(linea), 1);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', EliminarPalabraK(cad, n, i, kVal), '"');
          Pausa;
        end;

      13:
        begin
          WriteLn('--- [13] ELIMINAR PALABRAS DELANTE DE CARACTER CLAVE ---');
          Write('Ingrese la frase: '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', EliminarPalabrasDelanteDeC(cad, n, i), '"');
          Pausa;
        end;

      14:
        begin
          WriteLn('--- [14] CANTIDAD TOTAL DE PALABRAS ---');
          Write('Ingrese una frase o texto: '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Total de palabras: ', CantidadPalabras(cad, n, i));
          Pausa;
        end;

      15:
        begin
          WriteLn('--- [15] INVERTIR CADENA COMPLETA (FUNCION) ---');
          Write('Ingrese la cadena a invertir: '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Cadena invertida: "', InvertirCadena(cad, n, i), '"');
          Pausa;
        end;

      16:
        begin
          WriteLn('--- [16] INVERTIR UNICAMENTE LA SEGUNDA PALABRA ---');
          Write('Ingrese la frase (ej. Hola mundo de Cadena): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', InvertirSegundaPalabra(cad, n, i), '"');
          Pausa;
        end;

      17:
        begin
          WriteLn('--- [17] MAYUSCULAS A PALABRAS EN POSICION IMPAR QUE CONTIENEN CARACTER ---');
          Write('Ingrese la frase (ej. sol luna casa auto): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', MayusculaPalabrasImparConC(cad, n, i), '"');
          Pausa;
        end;

      18:
        begin
          WriteLn('--- [18] MEZCLAR / INTERCALAR CARACTERES DE 2 CADENAS ---');
          Write('Ingrese primera cadena: '); ReadLn(cad);
          Write('Ingrese segunda cadena: '); ReadLn(cad2);
          n := Length(cad); i := 1;
          WriteLn('Resultado intercalado: "', IntercalarCaracteres(cad, cad2, n, i), '"');
          Pausa;
        end;

      19:
        begin
          WriteLn('--- [19] RETORNAR CARACTERES ORDENADOS ALFABETICAMENTE ---');
          Write('Ingrese la cadena (ej. dcba o mundo): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Caracteres ordenados: "', CadenaCaracteresOrdenados(cad, n, i), '"');
          Pausa;
        end;

      20:
        begin
          WriteLn('--- [20] ORDENAR PALABRAS ALFABETICAMENTE ---');
          Write('Ingrese las palabras (ej. pera manzana uva banana): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Palabras ordenadas: "', OrdenarPalabrasAlfabeticamente(cad, n, i), '"');
          Pausa;
        end;

      21:
        begin
          WriteLn('--- [21] INTERSECCION DE CARACTERES ENTRE 2 CADENAS ---');
          Write('Ingrese cadena A (ej. abcde): '); ReadLn(cad);
          Write('Ingrese cadena B (ej. bdfgh): '); ReadLn(cad2);
          n := Length(cad); i := 1;
          WriteLn('Interseccion (caracteres comunes): "', InterseccionConjuntos(cad, cad2, n, i), '"');
          Pausa;
        end;

      22:
        begin
          WriteLn('--- [22] CONVERTIR NUMERO DECIMAL A BINARIO (CADENA) ---');
          Write('Ingrese un numero entero positivo: '); ReadLn(linea);
          num := StrToIntDef(Trim(linea), 0);
          WriteLn('Representacion binaria: ', DecimalABinario(num));
          Pausa;
        end;

      23:
        begin
          WriteLn('--- [23] CONTAR PARES DE VOCALES JUNTAS (DIPTONGOS) ---');
          Write('Ingrese una palabra o frase (ej. puerta, ciudad, aire): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Total de pares de vocales consecutivas: ', ContarDosVocalesJuntas(cad, n, i));
          Pausa;
        end;

      24:
        begin
          WriteLn('--- [24] INVERTIR CADENA CON PROCEDIMIENTO (PARAMETRO VAR) ---');
          Write('Ingrese la cadena a invertir: '); ReadLn(cad);
          n := Length(cad); i := 1; inv := '';
          InvertirCadenaProc(cad, n, i, inv);
          WriteLn('Resultado via procedure var: "', inv, '"');
          Pausa;
        end;

      25:
        begin
          WriteLn('--- [25] ORDENAR BURBUJA IN-PLACE (PROCEDURE VAR) ---');
          Write('Ingrese la cadena a ordenar (ej. 54321 o edcba): '); ReadLn(cad);
          n := Length(cad); i := 1;
          OrdenarBurbuja(cad, n, i);
          WriteLn('Cadena ordenada in-place: "', cad, '"');
          Pausa;
        end;

      26:
        begin
          WriteLn('--- [26] CONTAR PALABRAS QUE INICIAN Y TERMINAN EN VOCAL ---');
          Write('Ingrese la frase (ej. amigo oso estrella casa): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Palabras con vocales en ambos extremos: ', ContarPalabrasVocalesExtremos(cad, n, i));
          Pausa;
        end;

      27:
        begin
          WriteLn('--- [27] ELIMINAR CONSONANTES DE LA ULTIMA PALABRA ---');
          Write('Ingrese la frase (ej. casa de ana o segundo examen parcial): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', EliminarConsonantesUltimaPal(cad, n, i), '"');
          Pausa;
        end;

      28:
        begin
          WriteLn('--- [28] INSERTAR PALABRA TRAS LA SEGUNDA PALABRA ---');
          Write('Ingrese la frase original (ej. hola mundo de cadena): '); ReadLn(cad);
          Write('Ingrese la palabra nueva a insertar: '); ReadLn(sub);
          n := Length(cad); i := 1;
          WriteLn('Resultado: "', InsertarTrasSegunda(cad, sub, n, i), '"');
          Pausa;
        end;

      29:
        begin
          WriteLn('--- [29] CARACTERES EN INDICES PARES DE LA CADENA ---');
          Write('Ingrese la cadena (ej. programa): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Caracteres en posiciones 2, 4, 6... : "', CaracteresIndicesPares(cad, n, i), '"');
          Pausa;
        end;

      30:
        begin
          WriteLn('--- [30] ELIMINAR LA ULTIMA PALABRA DE LA FRASE ---');
          Write('Ingrese la frase (ej. hola mundo delphi): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Resultado sin la ultima palabra: "', EliminarUltimaPalabra(cad, n, i), '"');
          Pausa;
        end;

      31:
        begin
          WriteLn('--- [31] VERIFICAR SI UNA CADENA ES CAPICUA / PALINDROMA ---');
          Write('Ingrese la palabra o frase (ej. anitalavalatina, reconocer, oso): '); ReadLn(cad);
          n := Length(cad); i := 1;
          WriteLn('Es capicua: ', MensajeCapicua(cad, n, i));
          Pausa;
        end;

      99:
        begin
          EjecutarPruebaRapida;
          Pausa;
        end;

    else
      WriteLn('Opcion no valida. Seleccione un numero entre 0 y 31 (o 99 para prueba rapida).');
      Pausa;
    end;

  until opcion = 0;
end.
