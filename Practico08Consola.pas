program Practico08Consola;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  UnitCadenas;

procedure Pausa;
begin
  WriteLn;
  Write('Presione [ENTER] para continuar...');
  ReadLn;
end;

procedure MenuPrincipal;
begin
  WriteLn('========================================================================');
  WriteLn('          UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO (UAGRM)');
  WriteLn('                  FACULTAD DE CIENCIAS DE LA COMPUTACION');
  WriteLn('               INTRODUCCION A LA INFORMATICA (INF110)');
  WriteLn('                             PRACTICO # 8');
  WriteLn('                 CADENA DE CARACTERES - MODULAR');
  WriteLn('========================================================================');
  WriteLn('  [1] Contar caracteres                      [21] Ocurrencias de palabra');
  WriteLn('  [2] Mostrar primera letra (Proc.)          [22] Caracter por linea (Proc.)');
  WriteLn('  [3] Retornar ultima letra                  [23] Numeros o solo letras');
  WriteLn('  [4] Contar vocales                         [24] Contar digitos numericos');
  WriteLn('  [5] Contar consonantes                     [25] Extraer primera palabra');
  WriteLn('  [6] Convertir a mayusculas                 [26] Extraer ultima palabra');
  WriteLn('  [7] Convertir a minusculas                 [27] Normalizar espacios');
  WriteLn('  [8] Invertir cadena                        [28] Palabras empiezan vocal');
  WriteLn('  [9] Concatenar 2 cadenas                   [29] Palabras terminan cons.');
  WriteLn(' [10] Ocurrencias de una letra               [30] Intercalar 2 cadenas');
  WriteLn(' [11] Eliminar espacios en blanco            [31] Palabras con > 5 letras');
  WriteLn(' [12] Primeros N caracteres                  [32] Reemplazar vocales por *');
  WriteLn(' [13] Determinar si esta vacia               [33] Eliminar acentos');
  WriteLn(' [14] Codigos ASCII de caracteres            [34] Palabra mas larga');
  WriteLn(' [15] Contar letras mayusculas               [35] Palabra mas corta');
  WriteLn(' [16] Determinar si es palindroma            [36] Contar palabras repetidas');
  WriteLn(' [17] Contar palabras en una frase           [37] Solo contiene letras');
  WriteLn(' [18] Verificar palabra en frase             [38] Caracteres unicos');
  WriteLn(' [19] Reemplazar letra por otra              [39] Son anagramas');
  WriteLn(' [20] Eliminar letra de cadena               [40] Caracteres indice impar');
  WriteLn('------------------------------------------------------------------------');
  WriteLn('  [99] Ejecutar prueba rapida de los 40 ejercicios');
  WriteLn('  [0]  Salir');
  WriteLn('========================================================================');
  Write('Seleccione una opcion [0-40, 99]: ');
end;

var
  opcion, nVal: Integer;
  cad1, cad2, linea: String;
  c1, c2: Char;

begin
  repeat
    MenuPrincipal;
    ReadLn(linea);
    opcion := StrToIntDef(Trim(linea), -1);
    WriteLn;

    case opcion of
      0:
        WriteLn('Saliendo del programa... ¡Hasta pronto!');

      1:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Total de caracteres: ', ContarCaracteres(cad1));
          Pausa;
        end;

      2:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          MostrarPrimeraLetra(cad1);
          Pausa;
        end;

      3:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Ultima letra: ', UltimaLetra(cad1));
          Pausa;
        end;

      4:
        begin
          Write('Ingrese una palabra: ');
          ReadLn(cad1);
          WriteLn('Cantidad de vocales: ', ContarVocales(cad1));
          Pausa;
        end;

      5:
        begin
          Write('Ingrese una palabra: ');
          ReadLn(cad1);
          WriteLn('Cantidad de consonantes: ', ContarConsonantes(cad1));
          Pausa;
        end;

      6:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('En mayusculas: ', CadenaMayusculas(cad1));
          Pausa;
        end;

      7:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('En minusculas: ', CadenaMinusculas(cad1));
          Pausa;
        end;

      8:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Invertida: ', InvertirCadena(cad1));
          Pausa;
        end;

      9:
        begin
          Write('Ingrese primera cadena: ');
          ReadLn(cad1);
          Write('Ingrese segunda cadena: ');
          ReadLn(cad2);
          WriteLn('Concatenada: ', ConcatenarCadenas(cad1, cad2));
          Pausa;
        end;

      10:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          Write('Ingrese letra a buscar: ');
          ReadLn(linea);
          if Length(linea) > 0 then c1 := linea[1] else c1 := ' ';
          WriteLn('Apariciones de ''', c1, ''': ', ContarOcurrenciasLetra(cad1, c1));
          Pausa;
        end;

      11:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Sin espacios: ', EliminarEspacios(cad1));
          Pausa;
        end;

      12:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          Write('Ingrese N: ');
          ReadLn(nVal);
          WriteLn('Primeros ', nVal, ' caracteres: "', PrimerosNCaracteres(cad1, nVal), '"');
          Pausa;
        end;

      13:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          if EstaVacia(cad1) then
            WriteLn('Resultado: La cadena esta VACIA.')
          else
            WriteLn('Resultado: La cadena CONTIENE TEXTO.');
          Pausa;
        end;

      14:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          MostrarCodigosASCII(cad1);
          Pausa;
        end;

      15:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Cantidad de mayusculas: ', ContarMayusculas(cad1));
          Pausa;
        end;

      16:
        begin
          Write('Ingrese una cadena o frase: ');
          ReadLn(cad1);
          if EsPalindroma(cad1) then
            WriteLn('Resultado: SI es palindroma.')
          else
            WriteLn('Resultado: NO es palindroma.');
          Pausa;
        end;

      17:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          WriteLn('Cantidad de palabras: ', ContarPalabras(cad1));
          Pausa;
        end;

      18:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          Write('Ingrese palabra a buscar: ');
          ReadLn(cad2);
          if ExistePalabra(cad1, cad2) then
            WriteLn('Resultado: SI se encuentra en la frase.')
          else
            WriteLn('Resultado: NO se encuentra en la frase.');
          Pausa;
        end;

      19:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          Write('Letra vieja a reemplazar: ');
          ReadLn(linea);
          if Length(linea) > 0 then c1 := linea[1] else c1 := ' ';
          Write('Letra nueva: ');
          ReadLn(linea);
          if Length(linea) > 0 then c2 := linea[1] else c2 := ' ';
          WriteLn('Resultado: ', ReemplazarLetra(cad1, c1, c2));
          Pausa;
        end;

      20:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          Write('Letra a eliminar: ');
          ReadLn(linea);
          if Length(linea) > 0 then c1 := linea[1] else c1 := ' ';
          WriteLn('Resultado: ', EliminarLetra(cad1, c1));
          Pausa;
        end;

      21:
        begin
          Write('Ingrese el texto: ');
          ReadLn(cad1);
          Write('Ingrese la palabra: ');
          ReadLn(cad2);
          WriteLn('Apariciones: ', ContarOcurrenciasPalabra(cad1, cad2));
          Pausa;
        end;

      22:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          MostrarCaracteresPorLinea(cad1);
          Pausa;
        end;

      23:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Clasificacion: ', DeterminarContenido(cad1));
          Pausa;
        end;

      24:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Digitos numericos: ', ContarDigitos(cad1));
          Pausa;
        end;

      25:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          WriteLn('Primera palabra: "', ExtraerPrimeraPalabra(cad1), '"');
          Pausa;
        end;

      26:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          WriteLn('Ultima palabra: "', ExtraerUltimaPalabra(cad1), '"');
          Pausa;
        end;

      27:
        begin
          Write('Ingrese cadena con multiples espacios: ');
          ReadLn(cad1);
          WriteLn('Normalizada: "', NormalizarEspacios(cad1), '"');
          Pausa;
        end;

      28:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          MostrarPalabrasEmpiezanVocal(cad1);
          Pausa;
        end;

      29:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          MostrarPalabrasTerminanConsonante(cad1);
          Pausa;
        end;

      30:
        begin
          Write('Cadena 1: ');
          ReadLn(cad1);
          Write('Cadena 2: ');
          ReadLn(cad2);
          WriteLn('Intercalada: ', IntercalarCadenas(cad1, cad2));
          Pausa;
        end;

      31:
        begin
          Write('Ingrese una oracion: ');
          ReadLn(cad1);
          WriteLn('Palabras con mas de 5 letras: ', ContarPalabrasMasDe5Letras(cad1));
          Pausa;
        end;

      32:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Resultado con *: ', ReemplazarVocalesPorAsterisco(cad1));
          Pausa;
        end;

      33:
        begin
          Write('Ingrese cadena con acentos: ');
          ReadLn(cad1);
          WriteLn('Sin acentos: ', EliminarAcentos(cad1));
          Pausa;
        end;

      34:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          WriteLn('Palabra mas larga: "', PalabraMasLarga(cad1), '"');
          Pausa;
        end;

      35:
        begin
          Write('Ingrese una frase: ');
          ReadLn(cad1);
          WriteLn('Palabra mas corta: "', PalabraMasCorta(cad1), '"');
          Pausa;
        end;

      36:
        begin
          Write('Ingrese un texto: ');
          ReadLn(cad1);
          WriteLn('Palabras repetidas distintas: ', ContarPalabrasRepetidas(cad1));
          Pausa;
        end;

      37:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          if SoloContieneLetras(cad1) then
            WriteLn('Resultado: SI contiene solo letras.')
          else
            WriteLn('Resultado: NO contiene solo letras (tiene digitos o simbolos).');
          Pausa;
        end;

      38:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Caracteres unicos: "', CaracteresUnicos(cad1), '"');
          Pausa;
        end;

      39:
        begin
          Write('Cadena 1: ');
          ReadLn(cad1);
          Write('Cadena 2: ');
          ReadLn(cad2);
          if SonAnagramas(cad1, cad2) then
            WriteLn('Resultado: SI son anagramas.')
          else
            WriteLn('Resultado: NO son anagramas.');
          Pausa;
        end;

      40:
        begin
          Write('Ingrese una cadena: ');
          ReadLn(cad1);
          WriteLn('Caracteres de indice impar: ', CaracteresIndiceImpar(cad1));
          Pausa;
        end;

      99:
        begin
          WriteLn('Llamando al banco de pruebas completas...');
          // Ejecuta un resumen directo
          WriteLn('1. Contar "Hola": ', ContarCaracteres('Hola'));
          WriteLn('4. Vocales "Computadora": ', ContarVocales('Computadora'));
          WriteLn('8. Invertir "UAGRM": ', InvertirCadena('UAGRM'));
          WriteLn('16. Palindroma "reconocer": ', EsPalindroma('reconocer'));
          WriteLn('30. Intercalar "ABC"+"123": ', IntercalarCadenas('ABC', '123'));
          WriteLn('39. Anagramas "amor"+"roma": ', SonAnagramas('amor', 'roma'));
          WriteLn('Todo funcionando correctamente.');
          Pausa;
        end;
    else
      WriteLn('Opcion no valida. Ingrese un numero del 0 al 40.');
      Pausa;
    end;
  until opcion = 0;
end.
