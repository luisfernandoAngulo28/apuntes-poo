# -*- coding: utf-8 -*-
"""
Datos completos de los 31 ejercicios del Práctico #9 (Cadenas, Funciones y Procedimientos)
Materia: INF110 - Introducción a la Informática
Docente: M.Sc. Angélica Garzón Cuéllar - UAGRM
METODOLOGÍA DOCENTE: function Nombre(cad:String; n,i:Byte):Tipo;
"""

EJERCICIOS_P9_DATA = [
    {
        "num": 1,
        "titulo": "Crear una función ContarPalabra que cuente cuántas veces aparece una palabra dentro de un texto.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud calculada con <code>Length(cad)</code>), <code>i</code> (Byte: índice de posición), <code>palBuscada</code> (String: palabra a contabilizar).<br>• <strong>Proceso:</strong> Inicializar <code>i := 1</code> y <code>contador := 0</code>. Recorrer la cadena con ciclo <code>while i &lt;= n</code> saltando espacios en blanco y extrayendo cada palabra continua. Comparar en minúsculas cada palabra extraída contra <code>palBuscada</code>; si coinciden, incrementar <code>contador := contador + 1</code>.<br>• <strong>Salida:</strong> Cantidad de apariciones (Byte).",
        "pseudo": """Funcion ContarPalabra(cad: Cadena; n, i: Entero; palBuscada: Cadena): Entero
  contador <- 0
  palBuscada <- Minusculas(palBuscada)
  i <- 1
  Mientras i <= n Hacer
    Mientras (i <= n) Y (cad[i] = ' ') Hacer
      i <- i + 1
    FinMientras
    palActual <- ''
    Mientras (i <= n) Y (cad[i] <> ' ') Hacer
      palActual <- palActual + cad[i]
      i <- i + 1
    FinMientras
    Si (palActual <> '') Y (Minusculas(palActual) = palBuscada) Entonces
      contador <- contador + 1
    FinSi
  FinMientras
  Retornar contador
FinFuncion""",
        "traza_headers": ['Paso', 'i', 'texto[i]', 'palActual', "palActual = 'hola'", 'c'],
        "traza_rows": [
            ['Inicio', '1', "'h'", "''", '-', '0'],
            ['Extrae 1', '5', "' '", "'hola'", "SÍ ('hola' = 'hola')", '1'],
            ['Espacios', '6', "'m'", "''", '-', '1'],
            ['Extrae 2', '11', "' '", "'mundo'", "NO ('mundo' <> 'hola')", '1'],
            ['Espacios', '12', "'h'", "''", '-', '1'],
            ['Extrae 3', '16', 'fin', "'hola'", "SÍ ('hola' = 'hola')", '2'],
            ['Fin', '> 15', '-', '-', '-', 'Retorna 2'],
        ],
        "codigo_pascal": """// Ejercicio 1: Contar cuantas veces aparece una palabra dentro de un texto
// cad='hola mundo hola', palBuscada='hola' -> 2
function ContarPalabra(cad:String; n,i:Byte; palBuscada:String):Byte;
var
  palActual:String;
  contador:Byte;
begin
  contador:=0;
  palBuscada:=LowerCase(Trim(palBuscada));
  i:=1;
  while i<=n do begin
    // Saltar espacios en blanco
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    palActual:='';
    // Extraer palabra actual
    while (i<=n) and (cad[i]<>' ') do begin
      palActual:=palActual+cad[i];
      i:=i+1;
    end;
    if (palActual<>'') and (LowerCase(palActual)=palBuscada) then
      contador:=contador+1;
  end;
  Result:=contador;
end;""",
        "codigo_vcl": """// Evento OnClick - Llamada con cad, n, i globales
procedure TForm1.MenuContarPalabraClick(Sender: TObject);
var textoEntrada:String;
begin
  textoEntrada:=InputBox('Buscar','Ingrese la palabra a contar',' ');
  Edit3.Text:=IntToStr(ContarPalabra(cad,n,i,textoEntrada))+' veces';
end;""",
        "entrada_ejemplo": "hola mundo hola",
        "salida_ejemplo": "La palabra \"hola\" aparece 2 veces",
        "extra_req": True,
        "extra_label": "Palabra a contar:",
        "extra_default": "hola",
    },
    {
        "num": 2,
        "titulo": "Crear una función QuitarSignos que elimine todos los signos de puntuación del texto.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud calculada con <code>Length(cad)</code>), <code>i</code> (Byte: índice de recorrido).<br>• <strong>Proceso:</strong> Definir conjunto constante de signos de puntuación (<code>const signos: set of char</code>). Recorrer desde <code>i := 1</code> hasta <code>n</code> con ciclo <code>while</code>; si <code>cad[i]</code> no pertenece al conjunto, concatenarlo a la cadena resultante.<br>• <strong>Salida:</strong> Cadena limpia de signos de puntuación (String).",
        "pseudo": """Funcion QuitarSignos(cad: Cadena; n, i: Entero): Cadena
  res <- ''
  i <- 1
  signos <- ['.', ',', ';', ':', '!', '?', '"', ''', '(', ')', '[', ']', '{', '}', '-', '_']
  Mientras i <= n Hacer
    Si No (cad[i] En signos) Entonces
      res <- res + cad[i]
    FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['i', 'texto[i]', '¿Es signo?', 'res'],
        "traza_rows": [
            ['1', "'H'", 'NO', "'H'"],
            ['2..4', "'ola'", 'NO', "'Hola'"],
            ['5', "','", 'SÍ (Eliminar)', "'Hola'"],
            ['6', "' '", 'NO', "'Hola '"],
            ['7..11', "'mundo'", 'NO', "'Hola mundo'"],
            ['12', "'!'", 'SÍ (Eliminar)', "'Hola mundo'"],
        ],
        "codigo_pascal": """// Ejercicio 2: Eliminar signos de puntuacion del texto
// cad='Hola, mundo!' -> 'Hola mundo'
function QuitarSignos(cad:String; n,i:Byte):String;
const signos:set of char=['.', ',', ';', ':', '!', '?', '"', #39, '(', ')', '[', ']', '{', '}', '-', '_'];
var res:String;
begin
  res:='';
  i:=1;
  while i<=n do begin
    if not (cad[i] in signos) then
      res:=res+cad[i];
    i:=i+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuQuitarSignosClick(Sender: TObject);
begin
  Edit3.Text:=QuitarSignos(cad,n,i);
end;""",
        "entrada_ejemplo": "Hola, mundo!",
        "salida_ejemplo": "Hola mundo",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 3,
        "titulo": "Crear una función RepetirCadena que repita una cadena N veces.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), <code>nVeces</code> (Byte: repeticiones requeridas).<br>• <strong>Proceso:</strong> Con un ciclo externo <code>j &lt;= nVeces</code> y un ciclo interno <code>while i &lt;= n</code> (con <code>i := 1</code>), acumular los caracteres de <code>cad</code> sucesivamente.<br>• <strong>Salida:</strong> Cadena replicada <code>nVeces</code> (String).",
        "pseudo": """Funcion RepetirCadena(cad: Cadena; n, i, nVeces: Entero): Cadena
  res <- ''
  j <- 1
  Mientras j <= nVeces Hacer
    i <- 1
    Mientras i <= n Hacer
      res <- res + cad[i]
      i <- i + 1
    FinMientras
    j <- j + 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['Paso', 'i', 'Operación', 'res'],
        "traza_rows": [
            ['Inicio', '-', "res <- ''", "''"],
            ['1', '1', "res <- '' + 'Ok'", "'Ok'"],
            ['2', '2', "res <- 'Ok' + 'Ok'", "'OkOk'"],
            ['3', '3', "res <- 'OkOk' + 'Ok'", "'OkOkOk'"],
            ['Fin', '4 > 3', 'Termina ciclo', "Retorna 'OkOkOk'"],
        ],
        "codigo_pascal": """// Ejercicio 3: Repetir una cadena N veces
// cad='Hola', nVeces=3 -> 'HolaHolaHola'
function RepetirCadena(cad:String; n,i,nVeces:Byte):String;
var res:String;
    j:Byte;
begin
  res:='';
  j:=1;
  while j<=nVeces do begin
    i:=1;
    while i<=n do begin
      res:=res+cad[i];
      i:=i+1;
    end;
    j:=j+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuRepetirCadenaClick(Sender: TObject);
var nVeces:Byte;
begin
  nVeces:=StrToIntDef(InputBox('Repetir','Cuantas veces?','3'),3);
  Edit3.Text:=RepetirCadena(cad,n,i,nVeces);
end;""",
        "entrada_ejemplo": "Ok",
        "salida_ejemplo": "OkOkOk",
        "extra_req": True,
        "extra_label": "Valor de N (repeticiones):",
        "extra_default": "3",
    },
    {
        "num": 4,
        "titulo": "Crear una función MayusculaInicial que coloque en mayúscula la primera letra de cada palabra.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Inicializar <code>i := 1</code> y bandera booleana <code>nuevaPalabra := True</code>. Recorrer con ciclo <code>while i &lt;= n</code>; si se encuentra espacio, se conserva y se activa la bandera. Al encontrar un carácter alfabético bajo la bandera activa, se convierte a mayúscula con <code>UpCase</code> y se apaga la bandera.<br>• <strong>Salida:</strong> Cadena en formato título / mayúscula inicial (String).",
        "pseudo": """Funcion MayusculaInicial(cad: Cadena; n, i: Entero): Cadena
  res <- ''
  nuevaPalabra <- Verdadero
  i <- 1
  Mientras i <= n Hacer
    Si cad[i] = ' ' Entonces
      res <- res + ' '
      nuevaPalabra <- Verdadero
    Sino
      Si nuevaPalabra Entonces
        res <- res + Mayuscula(cad[i])
        nuevaPalabra <- Falso
      Sino
        res <- res + Minuscula(cad[i])
      FinSi
    FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['i', 'texto[i]', 'nuevaPalabra', 'Acción', 'res'],
        "traza_rows": [
            ['1', "'h'", 'True', "UpCase('h') -> 'H', nuevaPalabra := False", "'H'"],
            ['2..4', "'ola'", 'False', "Minuscula -> 'ola'", "'Hola'"],
            ['5', "' '", 'False', 'Espacio -> nuevaPalabra := True', "'Hola '"],
            ['6', "'m'", 'True', "UpCase('m') -> 'M', nuevaPalabra := False", "'Hola M'"],
            ['7..10', "'undo'", 'False', "Minuscula -> 'undo'", "'Hola Mundo'"],
        ],
        "codigo_pascal": """// Ejercicio 4: Mayuscula inicial en cada palabra (Title Case)
// cad='hola mundo' -> 'Hola Mundo'
function MayusculaInicial(cad:String; n,i:Byte):String;
var
  res:String;
  nuevaPalabra:Boolean;
begin
  res:='';
  nuevaPalabra:=True;
  i:=1;
  while i<=n do begin
    if cad[i]=' ' then begin
      res:=res+' ';
      nuevaPalabra:=True;
    end else begin
      if nuevaPalabra then begin
        res:=res+UpCase(cad[i]);
        nuevaPalabra:=False;
      end else
        res:=res+LowerCase(cad[i]);
    end;
    i:=i+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuMayusculaInicialClick(Sender: TObject);
begin
  Edit3.Text:=MayusculaInicial(cad,n,i);
end;""",
        "entrada_ejemplo": "hola mundo",
        "salida_ejemplo": "Hola Mundo",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 5,
        "titulo": "Crear una función ContarMayusMinus que cuente letras mayúsculas y minúsculas.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice). En la variante procedimiento: parámetros por referencia <code>var may, min: Byte</code>.<br>• <strong>Proceso:</strong> Contadores en 0 e <code>i := 1</code>. Recorrer con <code>while i &lt;= n</code> verificando pertenencia a conjuntos <code>['A'..'Z']</code> y <code>['a'..'z']</code> e incrementando el contador correspondiente.<br>• <strong>Salida:</strong> Reporte textual o asignación en parámetros por referencia.",
        "pseudo": """Funcion ContarMayusMinus(cad: Cadena; n, i: Entero): Cadena
  contMay <- 0; contMin <- 0
  i <- 1
  Mientras i <= n Hacer
    Si cad[i] En ['A'..'Z'] Entonces
      contMay <- contMay + 1
    Sino
      Si cad[i] En ['a'..'z'] Entonces
        contMin <- contMin + 1
      FinSi
    FinSi
    i <- i + 1
  FinMientras
  Retornar 'Mayusculas: ' + ConvertirATexto(contMay) + ', Minusculas: ' + ConvertirATexto(contMin)
FinFuncion""",
        "traza_headers": ['i', 'cad[i]', 'Tipo', 'may', 'min'],
        "traza_rows": [
            ['1', "'D'", 'Mayúscula', '1', '0'],
            ['2..6', "'elphi'", 'Minúsculas (5)', '1', '5'],
            ['7', "' '", 'Espacio', '1', '5'],
            ['8..10', "'IDE'", 'Mayúsculas (2)', '3', '5'],
            ['Fin', '-', 'Resultado Final', '3', '5'],
        ],
        "codigo_pascal": """// Ejercicio 5: Contar letras mayusculas y minusculas
// cad='Hola Mundo' -> 'Mayusculas: 2, Minusculas: 7'
function ContarMayusMinus(cad:String; n,i:Byte):String;
const
  may:set of char=['A'..'Z'];
  min:set of char=['a'..'z'];
var contMay,contMin:Byte;
begin
  contMay:=0; contMin:=0;
  i:=1;
  while i<=n do begin
    if cad[i] in may then
      contMay:=contMay+1
    else if cad[i] in min then
      contMin:=contMin+1;
    i:=i+1;
  end;
  Result:='Mayusculas: '+IntToStr(contMay)+', Minusculas: '+IntToStr(contMin);
end;

// Version procedimiento con parametros var
procedure ContarMayusMinusProc(cad:String; n,i:Byte; var may,min:Byte);
const
  conjMay:set of char=['A'..'Z'];
  conjMin:set of char=['a'..'z'];
begin
  may:=0; min:=0;
  i:=1;
  while i<=n do begin
    if cad[i] in conjMay then
      may:=may+1
    else if cad[i] in conjMin then
      min:=min+1;
    i:=i+1;
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuContarMayusMinusClick(Sender: TObject);
begin
  Edit3.Text:=ContarMayusMinus(cad,n,i);
end;""",
        "entrada_ejemplo": "Delphi IDE",
        "salida_ejemplo": "Mayúsculas: 3, Minúsculas: 5",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 6,
        "titulo": "Crear una función CompararCadenas que indique cuál cadena va primero en orden alfabético.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad1</code> (String), <code>cad2</code> (String).<br>• <strong>Proceso:</strong> Normalizar ambas cadenas a minúsculas y compararlas mediante operadores relacionales lexicográficos (<code>&lt;</code>, <code>&gt;</code>, <code>=</code>) para dictaminar su orden en el abecedario.<br>• <strong>Salida:</strong> Mensaje detallando cuál cadena precede a la otra.",
        "pseudo": """Funcion CompararCadenas(cad1, cad2: Cadena): Cadena
  c1 <- Minusculas(cad1)
  c2 <- Minusculas(cad2)
  Si c1 < c2 Entonces
    Retornar '"' + cad1 + '" va antes que "' + cad2 + '"'
  Sino
    Si c1 > c2 Entonces
      Retornar '"' + cad2 + '" va antes que "' + cad1 + '"'
    Sino
      Retornar 'Ambas cadenas son alfabeticamente iguales'
    FinSi
  FinSi
FinFuncion""",
        "traza_headers": ['cad1', 'cad2', 'c1 = Lower(cad1)', 'c2 = Lower(cad2)', 'Comparación (ASCII)', 'Resultado'],
        "traza_rows": [
            ["'Casa'", "'Perro'", "'casa'", "'perro'", "'casa' < 'perro' ('c' < 'p')", "'Casa va antes que Perro'"],
            ["'Zorro'", "'Aguila'", "'zorro'", "'aguila'", "'aguila' < 'zorro'", "'Aguila va antes que Zorro'"],
            ["'Auto'", "'auto'", "'auto'", "'auto'", "'auto' = 'auto'", "'Ambas cadenas son alfabéticamente iguales'"],
        ],
        "codigo_pascal": """// Ejercicio 6: Comparar dos cadenas alfabeticamente
// cad1='Ana', cad2='Pedro' -> '"Ana" va antes que "Pedro"'
function CompararCadenas(cad1,cad2:String):String;
var c1,c2:String;
begin
  c1:=LowerCase(cad1);
  c2:=LowerCase(cad2);
  if c1<c2 then
    Result:='"'+cad1+'" va antes que "'+cad2+'"'
  else if c1>c2 then
    Result:='"'+cad2+'" va antes que "'+cad1+'"'
  else
    Result:='Ambas cadenas son alfabeticamente iguales';
end;""",
        "codigo_vcl": """procedure TForm1.MenuCompararCadenasClick(Sender: TObject);
var cad2:String;
begin
  cad2:=InputBox('Comparar','Ingrese la segunda cadena',' ');
  Edit3.Text:=CompararCadenas(cad,cad2);
end;""",
        "entrada_ejemplo": "Casa",
        "salida_ejemplo": "\"Casa\" va antes que \"Perro\"",
        "extra_req": True,
        "extra_label": "Segunda cadena a comparar:",
        "extra_default": "Perro",
    },
    {
        "num": 7,
        "titulo": "Crear un programa que lea una frase y determine palabras, letras, vocales, consonantes, mayúsculas y minúsculas con funciones individuales.",
        "tipo": "Procedimiento",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Orquestar funciones modulares independientes, cada una con firma <code>(cad: String; n, i: Byte)</code>: contar palabras, letras totales, vocales, consonantes, mayúsculas y minúsculas usando ciclos <code>while i &lt;= n</code>.<br>• <strong>Salida:</strong> Cadena formateada con el diagnóstico integral.",
        "pseudo": """Funcion AnalizarFrase(cad: Cadena; n, i: Entero): Cadena
  cantP <- ContarPalabras(cad, n, i)
  cantL <- ContarLetrasTotales(cad, n, i)
  cantV <- ContarVocalesP9(cad, n, i)
  cantC <- ContarConsonantesP9(cad, n, i)
  cantM <- ContarMayusculas(cad, n, i)
  cantMin <- ContarMinusculas(cad, n, i)
  Retornar 'Palabras: ' + cantP + ' | Letras: ' + cantL + ' | Vocales: ' + cantV + ' | Consonantes: ' + cantC + ' | Mayusculas: ' + cantM + ' | Minusculas: ' + cantMin
FinFuncion""",
        "traza_headers": ['Métrica', 'Función Invocada', "Evaluación sobre 'Delphi 12'", 'Resultado'],
        "traza_rows": [
            ['Palabras', 'ContarPalabras()', "'Delphi' (1) + '12' (2)", '2 palabras'],
            ['Letras Totales', 'ContarLetrasTotales()', "'D','e','l','p','h','i'", '6 letras'],
            ['Vocales', 'ContarVocales()', "'e','i'", '2 vocales'],
            ['Consonantes', 'ContarConsonantes()', "'D','l','p','h'", '4 consonantes'],
            ['Mayúsculas', 'ContarMayus()', "'D'", '1 mayúscula'],
            ['Minúsculas', 'ContarMinus()', "'e','l','p','h','i'", '5 minúsculas'],
        ],
        "codigo_pascal": """// Ejercicio 7: Analisis completo de frase
// Sub-funciones con (cad:String; n,i:Byte)

function ContarPalabras(cad:String; n,i:Byte):Byte;
var cantPal:Byte; enPalabra:Boolean;
begin
  cantPal:=0; enPalabra:=false;
  i:=1;
  while i<=n do begin
    if cad[i]<>' ' then begin
      if enPalabra=false then begin
        cantPal:=cantPal+1;
        enPalabra:=true;
      end;
    end else
      enPalabra:=false;
    i:=i+1;
  end;
  Result:=cantPal;
end;

function ContarLetrasTotales(cad:String; n,i:Byte):Byte;
const letras:set of char=['A'..'Z','a'..'z'];
var contador:Byte;
begin
  contador:=0; i:=1;
  while i<=n do begin
    if cad[i] in letras then
      contador:=contador+1;
    i:=i+1;
  end;
  Result:=contador;
end;

function ContarVocalesP9(cad:String; n,i:Byte):Byte;
const voc:set of char=['A','E','I','O','U'];
var contador:Byte;
begin
  contador:=0; i:=1;
  while i<=n do begin
    if UpCase(cad[i]) in voc then
      contador:=contador+1;
    i:=i+1;
  end;
  Result:=contador;
end;

function ContarConsonantesP9(cad:String; n,i:Byte):Byte;
const
  letras:set of char=['A'..'Z','a'..'z'];
  voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var contador:Byte;
begin
  contador:=0; i:=1;
  while i<=n do begin
    if (cad[i] in letras) and not (cad[i] in voc) then
      contador:=contador+1;
    i:=i+1;
  end;
  Result:=contador;
end;

function ContarMayusculas(cad:String; n,i:Byte):Byte;
const may:set of char=['A'..'Z'];
var contador:Byte;
begin
  contador:=0; i:=1;
  while i<=n do begin
    if cad[i] in may then
      contador:=contador+1;
    i:=i+1;
  end;
  Result:=contador;
end;

function ContarMinusculas(cad:String; n,i:Byte):Byte;
const min:set of char=['a'..'z'];
var contador:Byte;
begin
  contador:=0; i:=1;
  while i<=n do begin
    if cad[i] in min then
      contador:=contador+1;
    i:=i+1;
  end;
  Result:=contador;
end;

function AnalizarFrase(cad:String; n,i:Byte):String;
begin
  Result:='Palabras: '+IntToStr(ContarPalabras(cad,n,i))+
          ' | Letras: '+IntToStr(ContarLetrasTotales(cad,n,i))+
          ' | Vocales: '+IntToStr(ContarVocalesP9(cad,n,i))+
          ' | Consonantes: '+IntToStr(ContarConsonantesP9(cad,n,i))+
          ' | Mayusculas: '+IntToStr(ContarMayusculas(cad,n,i))+
          ' | Minusculas: '+IntToStr(ContarMinusculas(cad,n,i));
end;""",
        "codigo_vcl": """procedure TForm1.MenuAnalizarFraseClick(Sender: TObject);
begin
  Edit3.Text:=AnalizarFrase(cad,n,i);
end;""",
        "entrada_ejemplo": "Introduccion a la Informatica INF110",
        "salida_ejemplo": "Palabras: 5 | Letras: 32 | Vocales: 14 | Consonantes: 18 | Mayúsculas: 6 | Minúsculas: 26",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 8,
        "titulo": "Crear una función ExtraerDominio(email: string): string; que retorne el dominio de un correo.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String: correo), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Localizar con <code>while (i &lt;= n) and (encontrado = false)</code> la posición del carácter <code>'@'</code>. Si existe, inicializar nuevo recorrido desde <code>posArroba + 1</code> hasta <code>n</code> concatenando caracteres del dominio.<br>• <strong>Salida:</strong> Nombre del servidor/dominio o mensaje de error.",
        "pseudo": """Funcion ExtraerDominio(cad: Cadena; n, i: Entero): Cadena
  posArroba <- 0; encontrado <- Falso; i <- 1
  Mientras (i <= n) Y (encontrado = Falso) Hacer
    Si cad[i] = '@' Entonces
      posArroba <- i
      encontrado <- Verdadero
    FinSi
    i <- i + 1
  FinMientras
  Si posArroba > 0 Entonces
    dominio <- ''; i <- posArroba + 1
    Mientras i <= n Hacer
      dominio <- dominio + cad[i]
      i <- i + 1
    FinMientras
    Retornar dominio
  Sino
    Retornar 'Correo sin arroba valida'
  FinSi
FinFuncion""",
        "traza_headers": ['email', "Pos('@', email)", 'p + 1', 'Subcadena Extraída', 'Retorno'],
        "traza_rows": [
            ["'usuario@gmail.com'", '8', '9', 'email[9..17]', "'gmail.com'"],
            ["'profesora@uagrm.edu.bo'", '10', '11', 'email[11..23]', "'uagrm.edu.bo'"],
            ["'sincorreo'", '0', '-', '-', "'Correo sin arroba válida'"],
        ],
        "codigo_pascal": """// Ejercicio 8: Extraer dominio de un correo electronico
// cad='alumno@uagrm.edu.bo' -> 'uagrm.edu.bo'
function ExtraerDominio(cad:String; n,i:Byte):String;
var
  posArroba:Byte;
  encontrado:Boolean;
  dominio:String;
begin
  posArroba:=0;
  encontrado:=false;
  i:=1;
  while (i<=n) and (encontrado=false) do begin
    if cad[i]='@' then begin
      posArroba:=i;
      encontrado:=True;
    end;
    i:=i+1;
  end;
  if posArroba>0 then begin
    dominio:='';
    i:=posArroba+1;
    while i<=n do begin
      dominio:=dominio+cad[i];
      i:=i+1;
    end;
    Result:=dominio;
  end else
    Result:='Correo sin arroba valida';
end;""",
        "codigo_vcl": """procedure TForm1.MenuExtraerDominioClick(Sender: TObject);
begin
  Edit3.Text:=ExtraerDominio(cad,n,i);
end;""",
        "entrada_ejemplo": "usuario@gmail.com",
        "salida_ejemplo": "gmail.com",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 9,
        "titulo": "Eliminar los primeros n caracteres y retornar el resultado.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), <code>nDel</code> (Byte: caracteres a suprimir).<br>• <strong>Proceso:</strong> Si <code>nDel &gt;= n</code>, retornar cadena vacía. En caso contrario, iniciar índice <code>i := nDel + 1</code> y con ciclo <code>while i &lt;= n</code> copiar los caracteres restantes.<br>• <strong>Salida:</strong> Subcadena sin los primeros <code>nDel</code> elementos.",
        "pseudo": """Funcion EliminarPrimerosN(cad: Cadena; n, i, nDel: Entero): Cadena
  res <- ''
  Si nDel >= n Entonces
    Retornar ''
  FinSi
  i <- nDel + 1
  Mientras i <= n Hacer
    res <- res + cad[i]
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['cad', 'Length(cad)', 'n', 'Operación', 'Resultado'],
        "traza_rows": [
            ["'Universidad'", '11', '3', "Copy('Universidad', 4, 8)", "'versidad'"],
            ["'Pascal'", '6', '2', "Copy('Pascal', 3, 4)", "'scal'"],
            ["'Hola'", '4', '5', '5 >= 4 -> Cadena vacía', "''"],
        ],
        "codigo_pascal": """// Ejercicio 9: Eliminar los primeros nDel caracteres
// cad='Hola Mundo', nDel=5 -> 'Mundo'
function EliminarPrimerosN(cad:String; n,i,nDel:Byte):String;
var res:String;
begin
  res:='';
  if nDel>=n then begin
    Result:='';
    Exit;
  end;
  i:=nDel+1;
  while i<=n do begin
    res:=res+cad[i];
    i:=i+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuEliminarPrimerosNClick(Sender: TObject);
var nDel:Byte;
begin
  nDel:=StrToIntDef(InputBox('Eliminar','Cuantos caracteres eliminar?','5'),5);
  Edit3.Text:=EliminarPrimerosN(cad,n,i,nDel);
end;""",
        "entrada_ejemplo": "Universidad",
        "salida_ejemplo": "versidad",
        "extra_req": True,
        "extra_label": "Cantidad de caracteres N a eliminar:",
        "extra_default": "3",
    },
    {
        "num": 10,
        "titulo": "Insertar una subcadena en otra cadena en una posición específica.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>sub</code> (String), <code>n</code> (Byte: longitud de cad), <code>i</code> (Byte: índice), <code>posIndex</code> (Byte: posición de inserción).<br>• <strong>Proceso:</strong> Copiar con <code>while</code> los primeros <code>posIndex - 1</code> caracteres de <code>cad</code>, luego todos los caracteres de <code>sub</code>, y finalmente los caracteres restantes de <code>cad</code>.<br>• <strong>Salida:</strong> Cadena modificada con la subcadena insertada.",
        "pseudo": """Funcion InsertarSubcadena(cad, sub: Cadena; n, i, posIndex: Entero): Cadena
  res <- ''; nSub <- Longitud(sub)
  Si posIndex <= 1 Entonces
    res <- sub + cad
  Sino
    Si posIndex > n Entonces
      res <- cad + sub
    Sino
      i <- 1
      Mientras i < posIndex Hacer
        res <- res + cad[i]; i <- i + 1
      FinMientras
      j <- 1
      Mientras j <= nSub Hacer
        res <- res + sub[j]; j <- j + 1
      FinMientras
      Mientras i <= n Hacer
        res <- res + cad[i]; i <- i + 1
      FinMientras
    FinSi
  FinSi
  Retornar res
FinFuncion""",
        "traza_headers": ['cad', 'sub', 'pos', 'Copy(1..pos-1)', 'Copy(pos..n)', 'Resultado'],
        "traza_rows": [
            ["'Holamundo'", "' '", '5', "'Hola'", "'mundo'", "'Hola mundo'"],
            ["'Pascal'", "'Turbo '", '1', "''", "'Pascal'", "'Turbo Pascal'"],
            ["'Delphi'", "' 12'", '7', "'Delphi'", "''", "'Delphi 12'"],
        ],
        "codigo_pascal": """// Ejercicio 10: Insertar una subcadena en una posicion dada
// cad='HolaMundo', sub=' ', posIndex=5 -> 'Hola Mundo'
function InsertarSubcadena(cad,sub:String; n,i,posIndex:Byte):String;
var
  res:String;
  j,nSub:Byte;
begin
  res:='';
  nSub:=Length(sub);
  if posIndex<=1 then begin
    j:=1;
    while j<=nSub do begin
      res:=res+sub[j]; j:=j+1;
    end;
    i:=1;
    while i<=n do begin
      res:=res+cad[i]; i:=i+1;
    end;
  end else if posIndex>n then begin
    i:=1;
    while i<=n do begin
      res:=res+cad[i]; i:=i+1;
    end;
    j:=1;
    while j<=nSub do begin
      res:=res+sub[j]; j:=j+1;
    end;
  end else begin
    i:=1;
    while i<posIndex do begin
      res:=res+cad[i]; i:=i+1;
    end;
    j:=1;
    while j<=nSub do begin
      res:=res+sub[j]; j:=j+1;
    end;
    while i<=n do begin
      res:=res+cad[i]; i:=i+1;
    end;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInsertarSubcadenaClick(Sender: TObject);
var sub:String; posIndex:Byte;
begin
  sub:=InputBox('Insertar','Subcadena a insertar',' ');
  posIndex:=StrToIntDef(InputBox('Posicion','En que posicion?','5'),5);
  Edit3.Text:=InsertarSubcadena(cad,sub,n,i,posIndex);
end;""",
        "entrada_ejemplo": "Holamundo",
        "salida_ejemplo": "Hola mundo",
        "extra_req": True,
        "extra_label": "Posición de inserción (1..N):",
        "extra_default": "5",
    },
    {
        "num": 11,
        "titulo": "Hacer una función para unir dos cadenas en una sola.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad1</code> (String), <code>cad2</code> (String).<br>• <strong>Proceso:</strong> Concatenar ambas cadenas interponiendo un espacio separador si ninguna de ellas se encuentra vacía.<br>• <strong>Salida:</strong> Cadena resultante unificada.",
        "pseudo": """Funcion UnirCadenas(cad1, cad2: Cadena): Cadena
  Si (cad1 <> '') Y (cad2 <> '') Entonces
    Retornar cad1 + ' ' + cad2
  Sino
    Retornar cad1 + cad2
  FinSi
FinFuncion""",
        "traza_headers": ['cad1', 'cad2', 'Operación', 'Resultado'],
        "traza_rows": [
            ["'Hola'", "'Mundo'", "cad1 + ' ' + cad2", "'Hola Mundo'"],
            ["'Santa'", "'Cruz'", "cad1 + ' ' + cad2", "'Santa Cruz'"],
            ["'INF'", "'110'", "cad1 + ' ' + cad2", "'INF 110'"],
        ],
        "codigo_pascal": """// Ejercicio 11: Unir dos cadenas en una sola
// cad1='Hola', cad2='Mundo' -> 'Hola Mundo'
function UnirCadenas(cad1,cad2:String):String;
begin
  if (cad1<>'') and (cad2<>'') then
    Result:=cad1+' '+cad2
  else
    Result:=cad1+cad2;
end;""",
        "codigo_vcl": """procedure TForm1.MenuUnirCadenasClick(Sender: TObject);
var cad2:String;
begin
  cad2:=InputBox('Unir','Ingrese la segunda cadena',' ');
  Edit3.Text:=UnirCadenas(cad,cad2);
end;""",
        "entrada_ejemplo": "Hola",
        "salida_ejemplo": "Hola Mundo",
        "extra_req": True,
        "extra_label": "Segunda cadena a unir:",
        "extra_default": "Mundo",
    },
    {
        "num": 12,
        "titulo": "Elaborar un programa que elimine la palabra número k de una cadena de caracteres.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), <code>k</code> (Byte: ordinal de la palabra a suprimir).<br>• <strong>Proceso:</strong> Recorrer con ciclo <code>while i &lt;= n</code> extrayendo cada palabra. Llevar un contador <code>numPal</code>. Si <code>numPal &lt;&gt; k</code>, concatenar la palabra al acumulador con espacio separador.<br>• <strong>Salida:</strong> Frase sin la palabra número <code>k</code>.",
        "pseudo": """Funcion EliminarPalabraK(cad: Cadena; n, i, k: Entero): Cadena
  i <- 1; numPal <- 0; res <- ''
  Mientras i <= n Hacer
    Mientras (i <= n) Y (cad[i] = ' ') Hacer i <- i + 1 FinMientras
    pal <- ''
    Mientras (i <= n) Y (cad[i] <> ' ') Hacer
      pal <- pal + cad[i]; i <- i + 1
    FinMientras
    Si pal <> '' Entonces
      numPal <- numPal + 1
      Si numPal <> k Entonces
        Si res <> '' Entonces res <- res + ' ' FinSi
        res <- res + pal
      FinSi
    FinSi
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['numPal', 'Palabra Extraída', '¿Es k=3?', 'res acumulado'],
        "traza_rows": [
            ['1', "'Hoy'", 'NO (1 <> 3)', "'Hoy'"],
            ['2', "'es'", 'NO (2 <> 3)', "'Hoy es'"],
            ['3', "'un'", 'SÍ (3 = 3) -> Omitir', "'Hoy es'"],
            ['4', "'buen'", 'NO (4 <> 3)', "'Hoy es buen'"],
            ['5', "'dia'", 'NO (5 <> 3)', "'Hoy es buen dia'"],
        ],
        "codigo_pascal": """// Ejercicio 12: Eliminar la palabra numero k
// cad='Hola mundo cruel', k=2 -> 'Hola cruel'
function EliminarPalabraK(cad:String; n,i,k:Byte):String;
var
  pal,res:String;
  numPal:Byte;
begin
  i:=1; numPal:=0; res:='';
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      numPal:=numPal+1;
      if numPal<>k then begin
        if res<>'' then res:=res+' ';
        res:=res+pal;
      end;
    end;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuEliminarPalabraKClick(Sender: TObject);
var k:Byte;
begin
  k:=StrToIntDef(InputBox('Eliminar','Numero de palabra a eliminar?','2'),2);
  Edit3.Text:=EliminarPalabraK(cad,n,i,k);
end;""",
        "entrada_ejemplo": "Hoy es un buen dia",
        "salida_ejemplo": "Hoy es buen dia",
        "extra_req": True,
        "extra_label": "Número de palabra k a eliminar:",
        "extra_default": "3",
    },
    {
        "num": 13,
        "titulo": "Elaborar un programa que elimine todas las palabras que tengan delante de ellas una palabra con la consonante 'c'.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Segmentar la cadena en un arreglo de palabras. Analizar si la palabra anterior contenía la consonante 'c' o 'C'; si es así, descartar la palabra actual al reconstruir.<br>• <strong>Salida:</strong> Frase filtrada sin palabras precedidas por términos con 'c'.",
        "pseudo": """Funcion EliminarPalabrasDelanteDeC(cad: Cadena; n, i: Entero): Cadena
  // 1. Extraer palabras con i <- 1; Mientras i <= n
  // 2. Por cada palabra j desde 1 hasta totalP:
  //    Verificar si palabra[j - 1] contiene consonante 'c'
  //    Si no la contiene, añadir palabra[j] a res
  Retornar res
FinFuncion""",
        "traza_headers": ['i', 'Palabra actual P[i]', 'Palabra anterior P[i-1]', "¿P[i-1] tiene 'c'?", 'Acción', 'res'],
        "traza_rows": [
            ['1', "'el'", '-', 'No tiene anterior', 'Se conserva', "'el'"],
            ['2', "'cielo'", "'el'", "NO ('el' no tiene 'c')", 'Se conserva', "'el cielo'"],
            ['3', "'azul'", "'cielo'", "SÍ ('cielo' TIENE 'c')", 'SE ELIMINA', "'el cielo'"],
            ['4', "'con'", "'azul'", "NO ('azul' no tiene 'c')", 'Se conserva', "'el cielo con'"],
            ['5', "'nubes'", "'con'", "SÍ ('con' TIENE 'c')", 'SE ELIMINA', "'el cielo con'"],
            ['6', "'claras'", "'nubes'", "NO ('nubes' no tiene 'c')", 'Se conserva', "'el cielo con claras'"],
        ],
        "codigo_pascal": """// Ejercicio 13: Eliminar palabras que tengan delante una palabra con 'c'
// cad='la casa bonita' -> 'la casa' (bonita va despues de casa que tiene c)
function EliminarPalabrasDelanteDeC(cad:String; n,i:Byte):String;
const
  letras:set of char=['A'..'Z','a'..'z'];
  voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
  teniaCAnterior,tieneC:Boolean;
begin
  // Extraer todas las palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;
  // Reconstruir sin las que van despues de una con 'c'
  res:='';
  j:=1;
  while j<=totalP do begin
    teniaCAnterior:=false;
    if j>1 then begin
      tieneC:=false;
      k:=1;
      while k<=Length(palabras[j-1]) do begin
        if (UpCase(palabras[j-1][k])='C') and
           (palabras[j-1][k] in letras) and
           not (palabras[j-1][k] in voc) then
          tieneC:=true;
        k:=k+1;
      end;
      teniaCAnterior:=tieneC;
    end;
    if not teniaCAnterior then begin
      if res<>'' then res:=res+' ';
      res:=res+palabras[j];
    end;
    j:=j+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuElimPalDelanteDeC(Sender: TObject);
begin
  Edit3.Text:=EliminarPalabrasDelanteDeC(cad,n,i);
end;""",
        "entrada_ejemplo": "el cielo azul con nubes claras",
        "salida_ejemplo": "el cielo con claras",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 14,
        "titulo": "Elaborar un programa que determine cuántas palabras existen en una cadena introducida por teclado.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Máquina de estados con bandera booleana <code>enPalabra := False</code> e <code>i := 1</code>. Al encontrar un carácter no espacio cuando <code>enPalabra = False</code>, se incrementa el contador y se activa la bandera.<br>• <strong>Salida:</strong> Cantidad total de palabras (Byte).",
        "pseudo": """Funcion CantidadPalabras(cad: Cadena; n, i: Entero): Entero
  cantPal <- 0; enPalabra <- Falso; i <- 1
  Mientras i <= n Hacer
    Si cad[i] <> ' ' Entonces
      Si enPalabra = Falso Entonces
        cantPal <- cantPal + 1
        enPalabra <- Verdadero
      FinSi
    Sino
      enPalabra <- Falso
    FinSi
    i <- i + 1
  FinMientras
  Retornar cantPal
FinFuncion""",
        "traza_headers": ['Paso', 'i', 'cad[i]', 'Acción', 'c (Palabras)'],
        "traza_rows": [
            ['1', '1..2', "'  '", 'Salta espacios iniciales', '0'],
            ['2', '3', "'F'", "Detecta palabra 'Facultad' -> Inc(c)", '1'],
            ['3', '11..13', "'   '", 'Salta espacios intermedios', '1'],
            ['4', '14', "'d'", "Detecta palabra 'de' -> Inc(c)", '2'],
            ['5', '16..17', "'  '", 'Salta espacios', '2'],
            ['6', '18', "'C'", "Detecta palabra 'Ciencias' -> Inc(c)", '3'],
            ['Fin', '> 25', '-', 'Termina cadena', 'Retorna 3'],
        ],
        "codigo_pascal": """// Ejercicio 14: Determinar cuantas palabras existen en una cadena
// cad='Hola mundo cruel' -> 3
function CantidadPalabras(cad:String; n,i:Byte):Byte;
var
  cantPal:Byte;
  enPalabra:Boolean;
begin
  cantPal:=0; enPalabra:=false;
  i:=1;
  while i<=n do begin
    if cad[i]<>' ' then begin
      if enPalabra=false then begin
        cantPal:=cantPal+1;
        enPalabra:=true;
      end;
    end else
      enPalabra:=false;
    i:=i+1;
  end;
  Result:=cantPal;
end;""",
        "codigo_vcl": """procedure TForm1.MenuCantidadPalabrasClick(Sender: TObject);
begin
  Edit3.Text:=IntToStr(CantidadPalabras(cad,n,i))+' palabras';
end;""",
        "entrada_ejemplo": "   Facultad  de   Ciencias  ",
        "salida_ejemplo": "Total de palabras: 3",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 15,
        "titulo": "Elaborar un programa que invierta una cadena de caracteres introducida por teclado.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Iniciar índice en <code>i := n</code> y mediante ciclo regresivo <code>while i &gt;= 1</code> acumular <code>cad[i]</code> decrementando <code>i := i - 1</code>.<br>• <strong>Salida:</strong> Cadena invertida de caracteres.",
        "pseudo": """Funcion InvertirCadena(cad: Cadena; n, i: Entero): Cadena
  res <- ''; i <- n
  Mientras i >= 1 Hacer
    res <- res + cad[i]
    i <- i - 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['i', 'cad[i]', 'res acumulado'],
        "traza_rows": [
            ['5', "'a'", "'a'"],
            ['4', "'l'", "'al'"],
            ['3', "'o'", "'alo'"],
            ['2', "'h'", "'aloh'"],
            ['1', "'-'", "Finaliza ciclo -> Retorna 'aloh'"],
        ],
        "codigo_pascal": """// Ejercicio 15: Invertir una cadena de caracteres
// cad='Hola' -> 'aloH'
function InvertirCadena(cad:String; n,i:Byte):String;
var res:String;
begin
  res:='';
  i:=n;
  while i>=1 do begin
    res:=res+cad[i];
    if i=0 then Break;
    i:=i-1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInvertirCadenaClick(Sender: TObject);
begin
  Edit3.Text:=InvertirCadena(cad,n,i);
end;""",
        "entrada_ejemplo": "algoritmo",
        "salida_ejemplo": "omtirogla",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 16,
        "titulo": "Elaborar un programa que invierta la segunda palabra de una cadena de caracteres.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer las palabras de la cadena. Si existen al menos 2 palabras, invertir los caracteres de <code>palabras[2]</code> con ciclo decreciente y recomponer la frase completa.<br>• <strong>Salida:</strong> Frase con la segunda palabra invertida.",
        "pseudo": """Funcion InvertirSegundaPalabra(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Invertir caracteres de palabras[2]
  // Reconstruir frase uniendo con espacios
  Retornar res
FinFuncion""",
        "traza_headers": ['Palabra #', 'Original', 'Proceso', 'Resultado Final'],
        "traza_rows": [
            ['1', "'Aprender'", 'Conservar igual', "'Aprender'"],
            ['2', "'Pascal'", "Invertir -> 'lacsaP'", "'lacsaP'"],
            ['3', "'es'", 'Conservar igual', "'es'"],
            ['4', "'genial'", 'Conservar igual', "'genial'"],
            ['Salida', '-', 'Unión completa', "'Aprender lacsaP es genial'"],
        ],
        "codigo_pascal": """// Ejercicio 16: Invertir la segunda palabra de una cadena
// cad='Hola Mundo cruel' -> 'Hola odnuM cruel'
function InvertirSegundaPalabra(cad:String; n,i:Byte):String;
var
  pal,res,invertida:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  // Extraer palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;
  // Invertir la segunda
  if totalP>=2 then begin
    invertida:='';
    j:=Length(palabras[2]);
    while j>=1 do begin
      invertida:=invertida+palabras[2][j];
      if j=0 then Break;
      j:=j-1;
    end;
    palabras[2]:=invertida;
  end;
  // Reconstruir
  res:='';
  k:=1;
  while k<=totalP do begin
    if res<>'' then res:=res+' ';
    res:=res+palabras[k];
    k:=k+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInvertirSegundaPalClick(Sender: TObject);
begin
  Edit3.Text:=InvertirSegundaPalabra(cad,n,i);
end;""",
        "entrada_ejemplo": "Aprender Pascal es genial",
        "salida_ejemplo": "Aprender lacsaP es genial",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 17,
        "titulo": "Elaborar un programa que convierta a mayúscula las palabras con longitud impar y que contengan la consonante 'c'.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer palabras con ciclo <code>while i &lt;= n</code>. Para cada palabra evaluar si <code>(Length(p) mod 2 &lt;&gt; 0)</code> y si contiene el carácter 'c'/'C'. Si ambas condiciones se cumplen, transformar a mayúsculas con <code>UpperCase</code>.<br>• <strong>Salida:</strong> Frase con las palabras impares con 'c' en mayúsculas.",
        "pseudo": """Funcion MayusculaPalabrasImparConC(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Para cada palabra j:
  //   Si (Longitud(pal[j]) Mod 2 <> 0) Y (Tiene 'c') Entonces
  //     pal[j] <- Mayusculas(pal[j])
  // Reconstruir frase
  Retornar res
FinFuncion""",
        "traza_headers": ['Palabra', 'Longitud', '¿Impar?', "¿Tiene 'c'?", '¿Aplica Mayúsculas?', 'Salida'],
        "traza_rows": [
            ["'el'", '2', 'NO (Par)', 'NO', 'NO', "'el'"],
            ["'coche'", '5', 'SÍ (Impar)', "SÍ ('coche')", "SÍ -> 'COCHE'", "'COCHE'"],
            ["'chico'", '5', 'SÍ (Impar)', "SÍ ('chico')", "SÍ -> 'CHICO'", "'CHICO'"],
            ["'de'", '2', 'NO (Par)', 'NO', 'NO', "'de'"],
            ["'carlos'", '6', 'NO (Par)', 'SÍ', 'NO (por ser par)', "'carlos'"],
            ["'cinco'", '5', 'SÍ (Impar)', "SÍ ('cinco')", "SÍ -> 'CINCO'", "'CINCO'"],
        ],
        "codigo_pascal": """// Ejercicio 17: Convertir a mayuscula palabras de longitud impar con consonante 'c'
// cad='casa color bonita' -> 'casa COLOR bonita'
function MayusculaPalabrasImparConC(cad:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
  esImpar,tieneCFlag:Boolean;
begin
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;
  res:='';
  j:=1;
  while j<=totalP do begin
    esImpar:=(Length(palabras[j]) mod 2 <> 0);
    tieneCFlag:=false;
    k:=1;
    while k<=Length(palabras[j]) do begin
      if UpCase(palabras[j][k])='C' then
        tieneCFlag:=true;
      k:=k+1;
    end;
    if esImpar and tieneCFlag then
      palabras[j]:=UpperCase(palabras[j]);
    if res<>'' then res:=res+' ';
    res:=res+palabras[j];
    j:=j+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuMayusPalImparConCClick(Sender: TObject);
begin
  Edit3.Text:=MayusculaPalabrasImparConC(cad,n,i);
end;""",
        "entrada_ejemplo": "el coche chico de carlos es cinco",
        "salida_ejemplo": "el COCHE CHICO de carlos es CINCO",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 18,
        "titulo": "Elaborar un programa que lea dos cadenas y realice la mezcla de caracteres (cad1=ana, cad2=jose, cad3=anajose).",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad1</code> (String), <code>cad2</code> (String), <code>n</code> (Byte: longitud de cad1), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Proporciona dos modalidades: concatenación directa con <code>MezclarCadenas</code> o intercalado carácter a carácter con <code>IntercalarCaracteres</code> usando ciclo <code>while i &lt;= maxLen</code>.<br>• <strong>Salida:</strong> Cadena mezclada o intercalada.",
        "pseudo": """Funcion IntercalarCaracteres(cad1, cad2: Cadena; n, i: Entero): Cadena
  res <- ''; n1 <- Longitud(cad1); n2 <- Longitud(cad2)
  maxLen <- n1; Si n2 > maxLen Entonces maxLen <- n2 FinSi
  i <- 1
  Mientras i <= maxLen Hacer
    Si i <= n1 Entonces res <- res + cad1[i] FinSi
    Si i <= n2 Entonces res <- res + cad2[i] FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['cad1', 'cad2', 'Fusión Oficial (PDF)', 'Variante Intercalada'],
        "traza_rows": [
            ["'ana'", "'jose'", "'anajose'", "'ajonase'"],
            ["'sol'", "'luna'", "'solluna'", "'sloulna'"],
            ["'abc'", "'12345'", "'abc12345'", "'a1b2c345'"],
        ],
        "codigo_pascal": """// Ejercicio 18: Mezclar dos cadenas
// MezclarCadenas: cad1+cad2 concatenado
// IntercalarCaracteres: intercalar caracter a caracter
// cad1='abc', cad2='123' -> 'a1b2c3'

function MezclarCadenas(cad1,cad2:String):String;
begin
  Result:=cad1+cad2;
end;

function IntercalarCaracteres(cad1,cad2:String; n,i:Byte):String;
var
  res:String;
  n1,n2,maxLen:Byte;
begin
  res:='';
  n1:=Length(cad1);
  n2:=Length(cad2);
  maxLen:=n1;
  if n2>maxLen then maxLen:=n2;
  i:=1;
  while i<=maxLen do begin
    if i<=n1 then res:=res+cad1[i];
    if i<=n2 then res:=res+cad2[i];
    i:=i+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuMezclarCadenasClick(Sender: TObject);
var cad2:String;
begin
  cad2:=InputBox('Mezclar','Ingrese la segunda cadena',' ');
  Edit3.Text:='Mezcla: '+MezclarCadenas(cad,cad2)+
              ' | Intercalar: '+IntercalarCaracteres(cad,cad2,n,i);
end;""",
        "entrada_ejemplo": "ana",
        "salida_ejemplo": "anajose",
        "extra_req": True,
        "extra_label": "Segunda cadena cad2:",
        "extra_default": "jose",
    },
    {
        "num": 19,
        "titulo": "Elaborar un programa que lea por teclado n caracteres y los coloque en una cadena en orden alfabético (sin usar algoritmo de ordenación).",
        "tipo": "Procedimiento",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Recorrer la cadena carácter por carácter con ciclo <code>while i &lt;= n</code>. Cada carácter no espacio se inserta directamente en su posición ordenada dentro de la cadena resultado mediante comparación secuencial.<br>• <strong>Salida:</strong> Cadena con caracteres ordenados alfabéticamente.",
        "pseudo": """Funcion CadenaCaracteresOrdenados(cad: Cadena; n, i: Entero): Cadena
  res <- ''; i <- 1
  Mientras i <= n Hacer
    Si cad[i] <> ' ' Entonces
      // Insertar ordenadamente cad[i] en res
    FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['Carácter Leído', 'cad antes', 'Posición de inserción j', 'cad después'],
        "traza_rows": [
            ["'m'", "''", 'Fin (cad vacía)', "'m'"],
            ["'a'", "'m'", "1 (ya que 'a' < 'm')", "'am'"],
            ["'z'", "'am'", 'Fin (mayor que todos)', "'amz'"],
            ["'b'", "'amz'", "2 (entre 'a' y 'm')", "'abmz'"],
        ],
        "codigo_pascal": """// Ejercicio 19: Insercion ordenada de caracteres en tiempo real (sin burbuja)
// cad='dcba' -> 'abcd'
function CadenaCaracteresOrdenados(cad:String; n,i:Byte):String;
var
  res:String;
  j,nRes:Byte;
  c:Char;
  insertado:Boolean;
  temp:String;
begin
  res:='';
  i:=1;
  while i<=n do begin
    if cad[i]<>' ' then begin
      c:=cad[i];
      insertado:=false;
      nRes:=Length(res);
      j:=1;
      while (j<=nRes) and (insertado=false) do begin
        if c<res[j] then begin
          temp:=Copy(res,1,j-1)+c+Copy(res,j,nRes-j+1);
          res:=temp;
          insertado:=true;
        end;
        j:=j+1;
      end;
      if insertado=false then
        res:=res+c;
    end;
    i:=i+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuCaracteresOrdenadosClick(Sender: TObject);
begin
  Edit3.Text:=CadenaCaracteresOrdenados(cad,n,i);
end;""",
        "entrada_ejemplo": "mazb",
        "salida_ejemplo": "abmz",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 20,
        "titulo": "Elaborar un programa que pida n palabras por teclado y los coloque en una cadena separados por espacio en orden alfabético.",
        "tipo": "Procedimiento",
        "categoria": "palabras",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Conforme se extrae cada palabra con ciclo <code>while i &lt;= n</code>, se busca su posición alfabética en un arreglo y se realiza desplazamiento de elementos para insertarla en tiempo real.<br>• <strong>Salida:</strong> Cadena con las palabras ordenadas de la A a la Z.",
        "pseudo": """Funcion OrdenarPalabrasAlfabeticamente(cad: Cadena; n, i: Entero): Cadena
  // Extraer cada palabra y desplazar elementos para insercion ordenada
  // Reconstruir la oracion con las palabras ordenadas
  Retornar res
FinFuncion""",
        "traza_headers": ['Palabra Leída', 'Lista Existente', 'Posición j', 'Lista Actualizada'],
        "traza_rows": [
            ["'perro'", '[]', '1', "['perro']"],
            ["'arbol'", "['perro']", "1 ('arbol' < 'perro')", "['arbol', 'perro']"],
            ["'gato'", "['arbol', 'perro']", "2 ('gato' < 'perro')", "['arbol', 'gato', 'perro']"],
            ["'casa'", "['arbol', 'gato', 'perro']", "2 ('casa' < 'gato')", "['arbol', 'casa', 'gato', 'perro']"],
        ],
        "codigo_pascal": """// Ejercicio 20: Insercion ordenada de palabras en tiempo real
// cad='banana apple cherry' -> 'apple banana cherry'
function OrdenarPalabrasAlfabeticamente(cad:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      // Insercion ordenada
      j:=1;
      while (j<=totalP) and (LowerCase(palabras[j])<LowerCase(pal)) do
        j:=j+1;
      k:=totalP;
      while k>=j do begin
        palabras[k+1]:=palabras[k];
        if k=0 then Break;
        k:=k-1;
      end;
      palabras[j]:=pal;
      totalP:=totalP+1;
    end;
  end;
  res:='';
  j:=1;
  while j<=totalP do begin
    if res<>'' then res:=res+' ';
    res:=res+palabras[j];
    j:=j+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuOrdenarPalabrasClick(Sender: TObject);
begin
  Edit3.Text:=OrdenarPalabrasAlfabeticamente(cad,n,i);
end;""",
        "entrada_ejemplo": "perro arbol gato casa",
        "salida_ejemplo": "arbol casa gato perro",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 21,
        "titulo": "Dado dos conjuntos de caracteres (A y B), realizar un diagrama y un programa para la intersección de conjuntos (C = A ∩ B).",
        "tipo": "Procedimiento",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cadA</code> (String), <code>cadB</code> (String), <code>n</code> (Byte: longitud cadA), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Poblar dos conjuntos tipo <code>set of Char</code> recorriendo cada cadena con ciclos <code>while</code>. Calcular la intersección matemática con el operador <code>*</code> (<code>setC := setA * setB</code>) y retornar los elementos comunes formateados.<br>• <strong>Salida:</strong> Representación textual del conjunto intersección (ej: <code>{c, d, e}</code>).",
        "pseudo": """Funcion InterseccionConjuntos(cadA, cadB: Cadena; n, i: Entero): Cadena
  // Poblar setA con cadA usando i <- 1; Mientras i <= nA
  // Poblar setB con cadB usando i <- 1; Mientras i <= nB
  // setC <- setA * setB
  // Retornar '{' + elementos comunes + '}'
FinFuncion""",
        "traza_headers": ['Carácter de A', '¿Existe en B?', '¿Ya está en C?', 'C acumulado'],
        "traza_rows": [
            ["'k'", 'SÍ', 'NO', "'k'"],
            ["'b'", 'NO', '-', "'k'"],
            ["'c'", 'NO', '-', "'k'"],
            ["'a'", 'SÍ', 'NO', "'k, a'"],
            ["'l'", 'SÍ', 'NO', "'k, a, l'"],
            ["'t','e','q'", 'NO', '-', "'k, a, l'"],
            ["'p'", 'SÍ', 'NO', "'k, a, l, p'"],
        ],
        "codigo_pascal": """// Ejercicio 21: Interseccion de dos conjuntos de caracteres (C = A inter B)
// cadA='abcde', cadB='cdefg' -> '{c, d, e}'
function InterseccionConjuntos(cadA,cadB:String; n,i:Byte):String;
var
  setA,setB,setC:set of Char;
  ch:Char;
  res:String;
  nA,nB:Byte;
begin
  setA:=[]; setB:=[];
  nA:=Length(cadA);
  i:=1;
  while i<=nA do begin
    if cadA[i] in ['a'..'z','A'..'Z'] then
      Include(setA,cadA[i]);
    i:=i+1;
  end;
  nB:=Length(cadB);
  i:=1;
  while i<=nB do begin
    if cadB[i] in ['a'..'z','A'..'Z'] then
      Include(setB,cadB[i]);
    i:=i+1;
  end;
  setC:=setA*setB;
  res:='{';
  for ch:=#0 to #255 do begin
    if ch in setC then begin
      if res<>'{' then res:=res+', ';
      res:=res+ch;
    end;
  end;
  res:=res+'}';
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInterseccionConjuntosClick(Sender: TObject);
var cadB:String;
begin
  cadB:=InputBox('Interseccion','Ingrese el conjunto B',' ');
  Edit3.Text:=InterseccionConjuntos(cad,cadB,n,i);
end;""",
        "entrada_ejemplo": "k, b, c, a, l, t, e, q, p",
        "salida_ejemplo": "{a, k, l, p}",
        "extra_req": True,
        "extra_label": "Conjunto B de caracteres:",
        "extra_default": "a, m, g, p, l, h, k, n",
    },
    {
        "num": 22,
        "titulo": "Hacer un programa utilizando cadenas para convertir un número decimal a binario.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>num</code> (Integer: valor decimal).<br>• <strong>Proceso:</strong> Algoritmo de divisiones sucesivas entre 2 con ciclo <code>while num &gt; 0</code>; el residuo (<code>num mod 2</code>) se convierte a carácter y se antepone a la cadena binaria.<br>• <strong>Salida:</strong> Representación binaria en String.",
        "pseudo": """Funcion DecimalABinario(num: Entero): Cadena
  Si num = 0 Entonces Retornar '0' FinSi
  res <- ''
  Mientras num > 0 Hacer
    dig <- num Mod 2
    res <- ConvertirATexto(dig) + res
    num <- num Div 2
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['Iteración', 'n', 'n mod 2 (residuo)', 'cadBin acumulado', 'n div 2'],
        "traza_rows": [
            ['1', '25', '1', "'1'", '12'],
            ['2', '12', '0', "'01'", '6'],
            ['3', '6', '0', "'001'", '3'],
            ['4', '3', '1', "'1001'", '1'],
            ['5', '1', '1', "'11001'", '0'],
            ['Fin', '0', '-', "Retorna '11001'", '-'],
        ],
        "codigo_pascal": """// Ejercicio 22: Convertir un numero decimal a binario usando cadenas
// num=10 -> '1010'
function DecimalABinario(num:Integer):String;
var
  res:String;
  dig:Integer;
begin
  if num=0 then begin
    Result:='0';
    Exit;
  end;
  res:='';
  while num>0 do begin
    dig:=num mod 2;
    res:=IntToStr(dig)+res;
    num:=num div 2;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuDecimalABinarioClick(Sender: TObject);
var num:Integer;
begin
  num:=StrToIntDef(InputBox('Decimal a Binario','Ingrese el numero','10'),10);
  Edit3.Text:=IntToStr(num)+' en binario = '+DecimalABinario(num);
end;""",
        "entrada_ejemplo": "25",
        "salida_ejemplo": "Binario: 11001",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 23,
        "titulo": "Dada una cadena introducida por teclado; mostrar la cantidad de veces que existen 2 vocales juntas.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Inicializar <code>contador := 0</code> e <code>i := 1</code>. Recorrer con ciclo <code>while i &lt;= n</code> evaluando parejas adyacentes <code>cad[i]</code> y <code>cad[i + 1]</code>; si ambas pertenecen al conjunto de vocales <code>voc: set of char</code>, incrementar el contador.<br>• <strong>Salida:</strong> Cantidad de parejas vocálicas contiguas (Byte).",
        "pseudo": """Funcion ContarDosVocalesJuntas(cad: Cadena; n, i: Entero): Entero
  contador <- 0; i <- 1
  Mientras i <= n Hacer
    ayudante <- i + 1
    Si ayudante <= n Entonces
      Si (cad[i] En Vocales) Y (cad[ayudante] En Vocales) Entonces
        contador <- contador + 1
      FinSi
    FinSi
    i <- i + 1
  FinMientras
  Retornar contador
FinFuncion""",
        "traza_headers": [
            'Posición i, i+1',
            'Subcadena evaluada',
            'cad[i] vocal?',
            'cad[i+1] vocal?',
            '¿Par vocálico?',
            'c',
        ],
        "traza_rows": [
            ["11, 12 ('educación')", "'ió'", "SÍ ('i')", "SÍ ('ó')", 'SÍ (1ra pareja)', '1'],
            ["19, 20 ('superior')", "'io'", "SÍ ('i')", "SÍ ('o')", 'SÍ (2da pareja)', '2'],
            ["27, 28 ('país')", "'aí'", "SÍ ('a')", "SÍ ('í')", 'SÍ (3ra pareja)', '3'],
            ['Total', '-', '-', '-', '-', 'Retorna 3'],
        ],
        "codigo_pascal": """// Ejercicio 23: Contar la cantidad de veces que existen 2 vocales juntas
// cad='bueno aeiou' -> 5
function ContarDosVocalesJuntas(cad:String; n,i:Byte):Byte;
const voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var contador:Byte;
    ayudante:Byte;
begin
  contador:=0;
  i:=1;
  while i<=n do begin
    ayudante:=i+1;
    if ayudante<=n then begin
      if (cad[i] in voc) and (cad[ayudante] in voc) then
        contador:=contador+1;
    end;
    i:=i+1;
  end;
  Result:=contador;
end;""",
        "codigo_vcl": """procedure TForm1.MenuContarVocalesJuntasClick(Sender: TObject);
begin
  Edit3.Text:=IntToStr(ContarDosVocalesJuntas(cad,n,i))+' pares de vocales juntas';
end;""",
        "entrada_ejemplo": "La educación superior del país",
        "salida_ejemplo": "Cantidad de 2 vocales juntas: 3",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 24,
        "titulo": "Dada una cadena de caracteres, mostrar la cadena en forma invertida.",
        "tipo": "Procedimiento",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), parámetro por referencia <code>var invertida: String</code>.<br>• <strong>Proceso:</strong> Limpiar <code>invertida := ''</code> e iniciar <code>i := n</code>. Mediante ciclo regresivo <code>while i &gt;= 1</code> acumular <code>cad[i]</code> en <code>invertida</code> y decrementar <code>i := i - 1</code>.<br>• <strong>Salida:</strong> Retorno en el parámetro por referencia <code>invertida</code>.",
        "pseudo": """Procedimiento InvertirCadenaProc(cad: Cadena; n, i: Entero; Var invertida: Cadena)
  invertida <- ''; i <- n
  Mientras i >= 1 Hacer
    invertida <- invertida + cad[i]
    i <- i - 1
  FinMientras
FinProcedimiento""",
        "traza_headers": ['Paso', 'i', 'cad[i]', 'salida acumulada'],
        "traza_rows": [
            ['1', '8', "'d'", "'d'"],
            ['2', '7', "'a'", "'da'"],
            ['3..7', '6..2', "'tluca'", "'datluca'"],
            ['8', '1', "'F'", "'datlucaF'"],
        ],
        "codigo_pascal": """// Ejercicio 24: Procedimiento para invertir una cadena
// cad='Hola' -> invertida='aloH'
procedure InvertirCadenaProc(cad:String; n,i:Byte; var invertida:String);
begin
  invertida:='';
  i:=n;
  while i>=1 do begin
    invertida:=invertida+cad[i];
    if i=0 then Break;
    i:=i-1;
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInvertirCadenaProcClick(Sender: TObject);
var invertida:String;
begin
  InvertirCadenaProc(cad,n,i,invertida);
  Edit3.Text:=invertida;
end;""",
        "entrada_ejemplo": "Facultad",
        "salida_ejemplo": "datlucaF",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 25,
        "titulo": "Dado un conjunto de caracteres, realizar el proceso de ordenación con el método de burbuja y mostrar su resultado.",
        "tipo": "Procedimiento",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> Parámetro por referencia <code>var cad: String</code>, <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Método clásico de ordenación por intercambio directo (burbuja) adaptado a ciclo <code>while huboIntercambio</code> e índice interno <code>while i &lt;= n - 1</code>, permutando caracteres contiguos con variable auxiliar.<br>• <strong>Salida:</strong> Modificación directa de la variable de entrada por referencia.",
        "pseudo": """Procedimiento OrdenarBurbuja(Var cad: Cadena; n, i: Entero)
  huboIntercambio <- Verdadero
  Mientras huboIntercambio Hacer
    huboIntercambio <- Falso
    i <- 1
    Mientras i <= n - 1 Hacer
      Si cad[i] > cad[i + 1] Entonces
        aux <- cad[i]; cad[i] <- cad[i + 1]; cad[i + 1] <- aux
        huboIntercambio <- Verdadero
      FinSi
      i <- i + 1
    FinMientras
  FinMientras
FinProcedimiento""",
        "traza_headers": ['Pasada i', 'j', 'cad[j] vs cad[j+1]', '¿Intercambio?', 'Estado de cad'],
        "traza_rows": [
            ['Inicio', '-', '-', '-', "'cba'"],
            ['i=1', 'j=1', "'c' > 'b'", 'SÍ (Intercambia)', "'bca'"],
            ['i=1', 'j=2', "'c' > 'a'", 'SÍ (Intercambia)', "'bac'"],
            ['i=2', 'j=1', "'b' > 'a'", 'SÍ (Intercambia)', "'abc'"],
            ['Fin', '-', '-', '-', "Retorna 'abc'"],
        ],
        "codigo_pascal": """// Ejercicio 25: Ordenar conjunto de caracteres con metodo de burbuja
// cad='dcba' -> cad='abcd'
procedure OrdenarBurbuja(var cad:String; n,i:Byte);
var
  aux:Char;
  huboIntercambio:Boolean;
begin
  huboIntercambio:=true;
  while huboIntercambio do begin
    huboIntercambio:=false;
    i:=1;
    while i<=n-1 do begin
      if cad[i]>cad[i+1] then begin
        aux:=cad[i];
        cad[i]:=cad[i+1];
        cad[i+1]:=aux;
        huboIntercambio:=true;
      end;
      i:=i+1;
    end;
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuOrdenarBurbujaClick(Sender: TObject);
var cadTemp:String;
begin
  cadTemp:=cad;
  OrdenarBurbuja(cadTemp,n,i);
  Edit3.Text:=cadTemp;
end;""",
        "entrada_ejemplo": "delphi",
        "salida_ejemplo": "dehilp",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 26,
        "titulo": "Contar las palabras de una cadena que comienzan y terminan en una vocal.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer cada palabra individualmente con ciclo <code>while i &lt;= n</code>. Para cada palabra extraída verificar si tanto el primer carácter <code>pal[1]</code> como el último <code>pal[Length(pal)]</code> pertenecen al conjunto de vocales <code>voc: set of char</code>.<br>• <strong>Salida:</strong> Cantidad de palabras con inicio y fin vocálico (Byte).",
        "pseudo": """Funcion ContarPalabrasVocalesExtremos(cad: Cadena; n, i: Entero): Entero
  contador <- 0; i <- 1
  Mientras i <= n Hacer
    Mientras (i <= n) Y (cad[i] = ' ') Hacer i <- i + 1 FinMientras
    pal <- ''
    Mientras (i <= n) Y (cad[i] <> ' ') Hacer
      pal <- pal + cad[i]; i <- i + 1
    FinMientras
    Si pal <> '' Entonces
      nPal <- Longitud(pal)
      Si (pal[1] En Vocales) Y (pal[nPal] En Vocales) Entonces
        contador <- contador + 1
      FinSi
    FinSi
  FinMientras
  Retornar contador
FinFuncion""",
        "traza_headers": ['Palabra P', 'P[1]', 'P[fin]', '¿P[1] vocal?', '¿P[fin] vocal?', 'Cumple?', 'c'],
        "traza_rows": [
            ["'oso'", "'o'", "'o'", 'SÍ', 'SÍ', 'SÍ', '1'],
            ["'come'", "'c'", "'e'", 'NO', 'SÍ', 'NO', '1'],
            ["'uva'", "'u'", "'a'", 'SÍ', 'SÍ', 'SÍ', '2'],
            ["'en'", "'e'", "'n'", 'SÍ', 'NO', 'NO', '2'],
            ["'el'", "'e'", "'l'", 'SÍ', 'NO', 'NO', '2'],
        ],
        "codigo_pascal": """// Ejercicio 26: Contar palabras que comienzan y terminan en vocal
// cad='ala este gol uno' -> 3 (ala, este, uno)
function ContarPalabrasVocalesExtremos(cad:String; n,i:Byte):Byte;
const voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal:String;
  contador,nPal:Byte;
begin
  contador:=0;
  i:=1;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      nPal:=Length(pal);
      if (pal[1] in voc) and (pal[nPal] in voc) then
        contador:=contador+1;
    end;
  end;
  Result:=contador;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPalabrasVocExtremosClick(Sender: TObject);
begin
  Edit3.Text:=IntToStr(ContarPalabrasVocalesExtremos(cad,n,i))+' palabras';
end;""",
        "entrada_ejemplo": "oso come uva en el arbol",
        "salida_ejemplo": "Palabras con vocales en ambos extremos: 2",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 27,
        "titulo": "Eliminar todas las consonantes de la última palabra.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer las palabras al arreglo. Tomar la última palabra (<code>palabras[totalP]</code>) y filtrar sus caracteres eliminando todas las consonantes mediante verificación con conjuntos <code>letras - voc</code>.<br>• <strong>Salida:</strong> Frase con la última palabra desprovista de consonantes.",
        "pseudo": """Funcion EliminarConsonantesUltimaPal(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Filtrar palabras[totalP] omitiendo consonantes
  // Reconstruir frase con palabras unidas por espacios
  Retornar res
FinFuncion""",
        "traza_headers": ['Última Palabra Original', 'Consonantes a remover', 'Vocales que quedan', 'Resultado Cadena'],
        "traza_rows": [
            ["'dificil'", "'d', 'f', 'c', 'l'", "'iii'", "'El examen es muy iii'"],
            ["'programacion'", "'p','r','g','r','m','c','n'", "'oaio'", "'estudio para el oaio'"],
            ["'delphi'", "'d', 'l', 'p', 'h'", "'ei'", "'lenguaje ei'"],
        ],
        "codigo_pascal": """// Ejercicio 27: Eliminar consonantes de la ultima palabra
// cad='Hola Mundo' -> 'Hola uo'
function EliminarConsonantesUltimaPal(cad:String; n,i:Byte):String;
const
  letras:set of char=['A'..'Z','a'..'z'];
  voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal,res,ultLimpia:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;
  if totalP>=1 then begin
    ultLimpia:='';
    j:=1;
    while j<=Length(palabras[totalP]) do begin
      if not ((palabras[totalP][j] in letras) and
              not (palabras[totalP][j] in voc)) then
        ultLimpia:=ultLimpia+palabras[totalP][j];
      j:=j+1;
    end;
    palabras[totalP]:=ultLimpia;
  end;
  res:='';
  k:=1;
  while k<=totalP do begin
    if res<>'' then res:=res+' ';
    res:=res+palabras[k];
    k:=k+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuElimConsUltimaPalClick(Sender: TObject);
begin
  Edit3.Text:=EliminarConsonantesUltimaPal(cad,n,i);
end;""",
        "entrada_ejemplo": "El examen es muy dificil",
        "salida_ejemplo": "El examen es muy iii",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 28,
        "titulo": "Insertar una palabra en la cadena a partir de la segunda palabra y mostrar la cadena completa.",
        "tipo": "Procedimiento",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>palNueva</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer palabras al arreglo. Desplazar los elementos a partir de la tercera posición hacia adelante con ciclo regresivo para liberar la posición 3, asignando <code>palabras[3] := palNueva</code>.<br>• <strong>Salida:</strong> Frase con la nueva palabra insertada tras la segunda palabra.",
        "pseudo": """Funcion InsertarTrasSegunda(cad, palNueva: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Desplazar palabras desde totalP hacia 3
  // palabras[3] <- palNueva
  // Reconstruir frase
  Retornar res
FinFuncion""",
        "traza_headers": ['P[1]', 'P[2]', 'Palabra a Insertar', 'Cadena Resultante'],
        "traza_rows": [
            ["'Aprender'", "'Pascal'", "'divertido'", "'Aprender Pascal es divertido'"],
            ["'Hola'", "'mundo'", "'hermoso'", "'Hola mundo hermoso cruel'"],
        ],
        "codigo_pascal": """// Ejercicio 28: Insertar una palabra a partir de la segunda palabra
// cad='Hola Mundo Cruel', palNueva='Bello' -> 'Hola Mundo Bello Cruel'
function InsertarTrasSegunda(cad,palNueva:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;
  if totalP>=2 then begin
    k:=totalP;
    while k>=3 do begin
      palabras[k+1]:=palabras[k];
      if k=0 then Break;
      k:=k-1;
    end;
    palabras[3]:=palNueva;
    totalP:=totalP+1;
  end else begin
    totalP:=totalP+1;
    palabras[totalP]:=palNueva;
  end;
  res:='';
  j:=1;
  while j<=totalP do begin
    if res<>'' then res:=res+' ';
    res:=res+palabras[j];
    j:=j+1;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInsertarTrasSegundaClick(Sender: TObject);
var palNueva:String;
begin
  palNueva:=InputBox('Insertar','Palabra a insertar despues de la 2da',' ');
  Edit3.Text:=InsertarTrasSegunda(cad,palNueva,n,i);
end;""",
        "entrada_ejemplo": "Aprender Pascal divertido",
        "salida_ejemplo": "Aprender Pascal es divertido",
        "extra_req": True,
        "extra_label": "Palabra a insertar:",
        "extra_default": "es",
    },
    {
        "num": 29,
        "titulo": "Mostrar los caracteres que se encuentran en los índices pares de una cadena.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Iniciar índice par en <code>i := 2</code>. Mediante ciclo <code>while i &lt;= n</code> concatenar <code>cad[i]</code> e incrementar de dos en dos con <code>i := i + 2</code>.<br>• <strong>Salida:</strong> Cadena compuesta únicamente por los caracteres en índices pares.",
        "pseudo": """Funcion CaracteresIndicesPares(cad: Cadena; n, i: Entero): Cadena
  res <- ''; i <- 2
  Mientras i <= n Hacer
    res <- res + cad[i]
    i <- i + 2
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ['Índice Par i', 'cad[i]', 'res acumulado'],
        "traza_rows": [
            ['2', "'N'", "'N'"],
            ['4', "'O'", "'NO'"],
            ['6', "'M'", "'NOM'"],
            ['8', "'T'", "'NOMT'"],
            ['10', "'C'", "'NOMTC'"],
            ['12 > 11', '-', "Fin bucle -> Retorna 'NOMTC'"],
        ],
        "codigo_pascal": """// Ejercicio 29: Mostrar caracteres en los indices pares
// cad='abcdef' -> 'bdf' (posiciones 2,4,6)
function CaracteresIndicesPares(cad:String; n,i:Byte):String;
var res:String;
begin
  res:='';
  i:=2;
  while i<=n do begin
    res:=res+cad[i];
    i:=i+2;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuCaracteresParesClick(Sender: TObject);
begin
  Edit3.Text:=CaracteresIndicesPares(cad,n,i);
end;""",
        "entrada_ejemplo": "INFORMATICA",
        "salida_ejemplo": "NOMTC",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 30,
        "titulo": "Eliminar la última palabra de la cadena.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer todas las palabras al arreglo. Al reconstruir la frase resultante, recorrer únicamente desde 1 hasta <code>totalP - 1</code>, suprimiendo la última palabra.<br>• <strong>Salida:</strong> Frase sin la última palabra.",
        "pseudo": """Funcion EliminarUltimaPalabra(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Reconstruir frase concatenando desde 1 hasta totalP - 1
  Retornar res
FinFuncion""",
        "traza_headers": ['cad original', 'Última palabra detectada', 'i resultante', 'Copy(1, i)'],
        "traza_rows": [
            ["'Hoy es un buen dia'", "'dia'", '14', "'Hoy es un buen'"],
            ["'Universidad Gabriel Rene'", "'Rene'", '19', "'Universidad Gabriel'"],
            ["'Palabra'", "'Palabra'", '0', "'' (Cadena vacía)"],
        ],
        "codigo_pascal": """// Ejercicio 30: Eliminar la ultima palabra de la cadena
// cad='Hola Mundo Cruel' -> 'Hola Mundo'
function EliminarUltimaPalabra(cad:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j:Byte;
  palabras:array[1..100] of String;
begin
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i]; i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;
  res:='';
  if totalP>=2 then begin
    j:=1;
    while j<=totalP-1 do begin
      if res<>'' then res:=res+' ';
      res:=res+palabras[j];
      j:=j+1;
    end;
  end;
  Result:=res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuEliminarUltimaPalClick(Sender: TObject);
begin
  Edit3.Text:=EliminarUltimaPalabra(cad,n,i);
end;""",
        "entrada_ejemplo": "Hoy es un buen dia",
        "salida_ejemplo": "Hoy es un buen",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    },
    {
        "num": 31,
        "titulo": "Verificar si la cadena es capicúa (palíndroma). Ejemplo: ada=ada.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Normalizar la cadena eliminando espacios y convirtiendo a mayúsculas con ciclo <code>while i &lt;= n</code>. Recorrer la cadena limpia con dos índices convergentes (<code>i := 1</code> y <code>j := nLimpia</code>); si en algún momento <code>limpia[i] &lt;&gt; limpia[j]</code>, se determina que no es capicúa.<br>• <strong>Salida:</strong> Booleano <code>True/False</code> o mensaje descriptivo.",
        "pseudo": """Funcion EsCapicua(cad: Cadena; n, i: Entero): Booleano
  // 1. Limpiar espacios y pasar a mayusculas con i <- 1; Mientras i <= n
  // 2. Comprobar simetria:
  i <- 1; j <- Longitud(limpia); esCap <- Verdadero
  Mientras (i < j) Y esCap Hacer
    Si limpia[i] <> limpia[j] Entonces
      esCap <- Falso
    FinSi
    i <- i + 1; j <- j - 1
  FinMientras
  Retornar esCap
FinFuncion""",
        "traza_headers": ['ini', 'fin', 'cad[ini]', 'cad[fin]', '¿Coinciden?', 'cap'],
        "traza_rows": [
            ['1', '3', "'a'", "'a'", 'SÍ', 'True'],
            ['2', '2', "'d'", "'d'", 'ini = fin (Centro)', 'True (Es Capicúa)'],
            ['-', '-', '-', '-', '-', "Retorna 'Es Capicúa: ada = ada'"],
        ],
        "codigo_pascal": """// Ejercicio 31: Verificar si la cadena es capicua / palindroma
// cad='anilina' -> True
function EsCapicua(cad:String; n,i:Byte):Boolean;
var
  limpia:String;
  j,nLimpia:Byte;
begin
  limpia:='';
  i:=1;
  while i<=n do begin
    if cad[i]<>' ' then
      limpia:=limpia+UpCase(cad[i]);
    i:=i+1;
  end;
  nLimpia:=Length(limpia);
  i:=1;
  j:=nLimpia;
  Result:=True;
  while i<j do begin
    if limpia[i]<>limpia[j] then begin
      Result:=False;
      Exit;
    end;
    i:=i+1;
    j:=j-1;
  end;
end;

function MensajeCapicua(cad:String; n,i:Byte):String;
begin
  if EsCapicua(cad,n,i) then
    Result:='Es Capicua / Palindroma ('+cad+')'
  else
    Result:='No es Capicua ('+cad+')';
end;""",
        "codigo_vcl": """procedure TForm1.MenuEsCapicuaClick(Sender: TObject);
begin
  Edit3.Text:=MensajeCapicua(cad,n,i);
end;""",
        "entrada_ejemplo": "ada",
        "salida_ejemplo": "Es Capicúa / Palíndroma (ada)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": "",
    }
]
