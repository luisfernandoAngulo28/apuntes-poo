# -*- coding: utf-8 -*-
"""
Script maestro para integrar la Solución Completa del Práctico #8 (40 Ejercicios de Cadenas)
en teoria_programacion_modular.html y generar la unidad completa Cadena.pas para Delphi 12.
"""

import sys
import re

# Datos de los 40 ejercicios basados en el PDF oficial y UnitCadenas.pas
EJERCICIOS_DATA = [
    {
        "num": 1,
        "titulo": "Crear una función que cuente los caracteres de una cadena.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer la cadena con un bucle while o for incrementando un contador por cada posición válida desde 1 hasta Length(cad).<br>• Salida: total (Integer / Byte).",
        "pseudo": """Funcion ContarCaracteres(cad: Cadena): Entero
  total <- 0
  Para i <- 1 Hasta Longitud(cad) Hacer
    total <- total + 1
  FinPara
  Retornar total
FinFuncion""",
        "traza_headers": ["Paso", "i", "cad[i]", "total := total + 1"],
        "traza_rows": [
            ["Inicio", "-", "-", "0"],
            ["1", "1", "'H'", "1"],
            ["2", "2", "'O'", "2"],
            ["3", "3", "'L'", "3"],
            ["4", "4", "'A'", "4"],
            ["Fin", "5 > 4", "-", "Retorna 4"]
        ],
        "codigo_pascal": """// Ejercicio 1: Contar caracteres de una cadena
function ContarCaracteres(cad: String): Integer;
var
  i, total: Integer;
begin
  total := 0;
  for i := 1 to Length(cad) do
    total := total + 1;
  Result := total;
end;""",
        "codigo_vcl": """// Evento en TForm1 para el Ejercicio 1
procedure TForm1.MenuContarCaracteresClick(Sender: TObject);
begin
  n := ContarCaracteres(cad);
  Edit2.Text := IntToStr(n) + ' caracteres';
  Edit3.Text := 'Total caracteres: ' + IntToStr(n);
end;""",
        "entrada_ejemplo": "Universidad Gabriel Rene Moreno",
        "salida_ejemplo": "31 caracteres",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 2,
        "titulo": "Diseñar un procedimiento que muestre la primera letra de una cadena.",
        "tipo": "Procedimiento",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer de izquierda a derecha. Al encontrar el primer carácter que pertenezca al abecedario ('A'..'Z', 'a'..'z'), mostrarlo o asignarlo y terminar.<br>• Salida: Mensaje o texto con la primera letra encontrada.",
        "pseudo": """Procedimiento MostrarPrimeraLetra(cad: Cadena)
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si EsLetra(cad[i]) Entonces
      Mostrar("Primera letra: ", cad[i])
      SalirProcedimiento
    FinSi
  FinPara
  Mostrar("No contiene letras")
FinProcedimiento""",
        "traza_headers": ["i", "cad[i]", "¿EsLetra?", "Acción"],
        "traza_rows": [
            ["1", "' ' (espacio)", "No", "i := i + 1"],
            ["2", "' ' (espacio)", "No", "i := i + 1"],
            ["3", "'I'", "Sí ('I' en 'A'..'Z')", "Muestra 'I' y termina"]
        ],
        "codigo_pascal": """// Ejercicio 2: Mostrar la primera letra
procedure MostrarPrimeraLetra(cad: String; var letra: Char);
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
var
  i: Integer;
begin
  letra := #0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] in letras then
    begin
      letra := cad[i];
      Exit;
    end;
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPrimeraLetraClick(Sender: TObject);
var
  prim: Char;
begin
  MostrarPrimeraLetra(cad, prim);
  if prim <> #0 then
    Edit3.Text := 'Primera letra: ' + prim
  else
    Edit3.Text := 'No se encontro ninguna letra en la cadena';
end;""",
        "entrada_ejemplo": "  Ingenieria Informatica",
        "salida_ejemplo": "Primera letra: I",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 3,
        "titulo": "Crear una función que retorne la última letra de una cadena.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer la cadena en sentido inverso desde Length(cad) hacia 1. Al hallar el primer carácter alfabético, retornarlo.<br>• Salida: Char (última letra alfabética).",
        "pseudo": """Funcion UltimaLetra(cad: Cadena): Caracter
  Para i <- Longitud(cad) Hasta 1 Con Paso -1 Hacer
    Si EsLetra(cad[i]) Entonces
      Retornar cad[i]
    FinSi
  FinPara
  Retornar #0
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿EsLetra?", "Acción"],
        "traza_rows": [
            ["27", "'!' (símbolo)", "No", "i := i - 1"],
            ["26", "'a'", "Sí ('a' en letras)", "Retorna 'a' inmediatamente"]
        ],
        "codigo_pascal": """// Ejercicio 3: Retornar la última letra
function UltimaLetra(cad: String): Char;
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
var
  i: Integer;
begin
  Result := #0;
  for i := Length(cad) downto 1 do
  begin
    if cad[i] in letras then
    begin
      Result := cad[i];
      Exit;
    end;
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuUltimaLetraClick(Sender: TObject);
var
  ult: Char;
begin
  ult := UltimaLetra(cad);
  if ult <> #0 then
    Edit3.Text := 'Ultima letra: ' + ult
  else
    Edit3.Text := 'No contiene letras';
end;""",
        "entrada_ejemplo": "Santa Cruz de la Sierra!",
        "salida_ejemplo": "Ultima letra: a",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 4,
        "titulo": "Contar cuántas vocales tiene una palabra ingresada.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Definir conjunto de vocales voc = ['A','E','I','O','U']. Recorrer con while i <= n o for; si UpCase(cad[i]) está en voc, c := c + 1.<br>• Salida: Conteo total de vocales (Byte / Integer).",
        "pseudo": """Funcion ContarVocales(pal: Cadena): Entero
  c <- 0
  voc <- ['A','E','I','O','U']
  Para i <- 1 Hasta Longitud(pal) Hacer
    Si Mayuscula(pal[i]) en voc Entonces
      c <- c + 1
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["i", "pal[i]", "UpCase(pal[i])", "¿En voc?", "c"],
        "traza_rows": [
            ["1", "'C'", "'C'", "No", "0"],
            ["2", "'O'", "'O'", "Sí", "1"],
            ["3", "'M'", "'M'", "No", "1"],
            ["4", "'P'", "'P'", "No", "1"],
            ["5", "'U'", "'U'", "Sí", "2"],
            ["...", "...", "...", "...", "5 vocales en total"]
        ],
        "codigo_pascal": """// Ejercicio 4: Contar vocales
function ContarVocales(pal: String): Integer;
const
  voc: set of char = ['A','E','I','O','U'];
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(pal) do
  begin
    if UpCase(pal[i]) in voc then
      c := c + 1;
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.Vocales1Click(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := IntToStr(ContarVocales(cad)) + ' vocales';
end;""",
        "entrada_ejemplo": "COMPUTADORA",
        "salida_ejemplo": "5 vocales (O, U, A, O, A)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 5,
        "titulo": "Contar cuántas consonantes tiene una palabra.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: pal (String)<br>• Proceso: Letras que no son vocales: cons = ['A'..'Z'] - ['A','E','I','O','U']. Si UpCase(pal[i]) in cons, c := c + 1.<br>• Salida: Total consonantes (Integer).",
        "pseudo": """Funcion ContarConsonantes(pal: Cadena): Entero
  c <- 0
  cons <- ['A'..'Z'] - ['A','E','I','O','U']
  Para i <- 1 Hasta Longitud(pal) Hacer
    Si Mayuscula(pal[i]) en cons Entonces
      c <- c + 1
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["i", "pal[i]", "UpCase", "¿Consonante?", "c"],
        "traza_rows": [
            ["1", "'A'", "'A'", "No (Vocal)", "0"],
            ["2", "'l'", "'L'", "Sí", "1"],
            ["3", "'g'", "'G'", "Sí", "2"],
            ["4", "'o'", "'O'", "No", "2"],
            ["5", "'r'", "'R'", "Sí", "3"],
            ["Fin", "-", "-", "-", "7 consonantes"]
        ],
        "codigo_pascal": """// Ejercicio 5: Contar consonantes
function ContarConsonantes(pal: String): Integer;
const
  cons: set of char = ['A'..'Z'] - ['A','E','I','O','U'];
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(pal) do
  begin
    if UpCase(pal[i]) in cons then
      c := c + 1;
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.MenuConsonantesClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarConsonantes(cad)) + ' consonantes';
end;""",
        "entrada_ejemplo": "Algoritmos",
        "salida_ejemplo": "7 consonantes (l, g, r, t, m, s)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 6,
        "titulo": "Mostrar la cadena en mayúsculas usando una función.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer cada carácter. Si cad[i] está entre 'a' y 'z', convertir restando 32 a su código ASCII o usar UpCase.<br>• Salida: String en mayúsculas.",
        "pseudo": """Funcion CadenaMayusculas(cad: Cadena): Cadena
  res <- ""
  Para i <- 1 Hasta Longitud(cad) Hacer
    res <- res + Mayuscula(cad[i])
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "ASCII", "ASCII - 32", "res"],
        "traza_rows": [
            ["1", "'h'", "104", "72 ('H')", "'H'"],
            ["2", "'o'", "111", "79 ('O')", "'HO'"],
            ["3", "'l'", "108", "76 ('L')", "'HOL'"],
            ["4", "'a'", "97", "65 ('A')", "'HOLA'"]
        ],
        "codigo_pascal": """// Ejercicio 6: Cadena a mayúsculas
function CadenaMayusculas(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if (cad[i] >= 'a') and (cad[i] <= 'z') then
      res := res + Chr(Ord(cad[i]) - 32)
    else
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuMayusculasClick(Sender: TObject);
begin
  Edit3.Text := CadenaMayusculas(cad);
end;""",
        "entrada_ejemplo": "programacion modular",
        "salida_ejemplo": "PROGRAMACION MODULAR",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 7,
        "titulo": "Mostrar la cadena en minúsculas.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Si cad[i] está entre 'A' y 'Z', sumar 32 al código ASCII: Chr(Ord(c) + 32).<br>• Salida: String en minúsculas.",
        "pseudo": """Funcion CadenaMinusculas(cad: Cadena): Cadena
  res <- ""
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si (cad[i] >= 'A') Y (cad[i] <= 'Z') Entonces
      res <- res + Caracter(Ascii(cad[i]) + 32)
    Sino
      res <- res + cad[i]
    FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿Mayúscula?", "Transformación", "res"],
        "traza_rows": [
            ["1", "'D'", "Sí (ASCII 68)", "68 + 32 = 100 ('d')", "'d'"],
            ["2", "'E'", "Sí (ASCII 69)", "69 + 32 = 101 ('e')", "'de'"],
            ["3", "'L'", "Sí (ASCII 76)", "76 + 32 = 108 ('l')", "'del'"]
        ],
        "codigo_pascal": """// Ejercicio 7: Cadena a minúsculas
function CadenaMinusculas(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if (cad[i] >= 'A') and (cad[i] <= 'Z') then
      res := res + Chr(Ord(cad[i]) + 32)
    else
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.Minuscula1Click(Sender: TObject);
begin
  Edit3.Text := CadenaMinusculas(cad);
end;""",
        "entrada_ejemplo": "DELPHI Y PASCAL INF-110",
        "salida_ejemplo": "delphi y pascal inf-110",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 8,
        "titulo": "Invertir una cadena carácter por carácter.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer desde Length(cad) hacia 1 con downto o while decreciente, concatenando cada carácter a res.<br>• Salida: String invertido.",
        "pseudo": """Funcion InvertirCadena(cad: Cadena): Cadena
  res <- ""
  Para i <- Longitud(cad) Hasta 1 Con Paso -1 Hacer
    res <- res + cad[i]
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "res acumulado"],
        "traza_rows": [
            ["4", "'L'", "'L'"],
            ["3", "'A'", "'LA'"],
            ["2", "'O'", "'LAO'"],
            ["1", "'H'", "'LAOH'"]
        ],
        "codigo_pascal": """// Ejercicio 8: Invertir cadena
function InvertirCadena(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := Length(cad) downto 1 do
    res := res + cad[i];
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuInvertirClick(Sender: TObject);
begin
  Edit3.Text := InvertirCadena(cad);
end;""",
        "entrada_ejemplo": "RENE MORENO",
        "salida_ejemplo": "ONEROM ENER",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 9,
        "titulo": "Concatenar dos cadenas ingresadas por el usuario.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad1, cad2 (String)<br>• Proceso: Usar el operador de concatenación '+' o función Concat.<br>• Salida: Cadena resultante unificada.",
        "pseudo": """Funcion ConcatenarCadenas(cad1, cad2: Cadena): Cadena
  Retornar cad1 + cad2
FinFuncion""",
        "traza_headers": ["cad1", "cad2", "cad1 + cad2"],
        "traza_rows": [
            ["'Hola '", "'Mundo Delphi'", "'Hola Mundo Delphi'"]
        ],
        "codigo_pascal": """// Ejercicio 9: Concatenar cadenas
function ConcatenarCadenas(cad1, cad2: String): String;
begin
  Result := cad1 + cad2;
end;""",
        "codigo_vcl": """procedure TForm1.MenuConcatenarClick(Sender: TObject);
var
  cad2: String;
begin
  cad2 := InputBox('Concatenar', 'Ingrese segunda cadena:', 'UAGRM');
  Edit3.Text := ConcatenarCadenas(cad, ' ' + cad2);
end;""",
        "entrada_ejemplo": "cad1='Hola ', cad2='Mundo Delphi'",
        "salida_ejemplo": "Hola Mundo Delphi",
        "extra_req": True,
        "extra_label": "Segunda cadena a concatenar:",
        "extra_default": "UAGRM"
    },
    {
        "num": 10,
        "titulo": "Calcular cuántas veces aparece una letra específica dentro de una cadena.",
        "tipo": "Función",
        "categoria": "basicos",
        "analisis": "• Entrada: cad (String), letra (Char)<br>• Proceso: Recorrer la cadena comparando UpCase(cad[i]) con UpCase(letra). Contar coincidencias.<br>• Salida: Conteo total (Integer).",
        "pseudo": """Funcion ContarOcurrenciasLetra(cad: Cadena, letra: Caracter): Entero
  c <- 0
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si Mayuscula(cad[i]) = Mayuscula(letra) Entonces
      c <- c + 1
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿Es igual a letra?", "c"],
        "traza_rows": [
            ["1", "'E'", "No ('E' <> 'a')", "0"],
            ["2", "'s'", "No", "0"],
            ["11", "'a'", "Sí ('a' = 'a')", "1"],
            ["17", "'a'", "Sí ('a' = 'a')", "2"],
            ["20", "'a'", "Sí ('a' = 'a')", "3"]
        ],
        "codigo_pascal": """// Ejercicio 10: Ocurrencias de una letra
function ContarOcurrenciasLetra(cad: String; letra: Char): Integer;
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(cad) do
  begin
    if UpCase(cad[i]) = UpCase(letra) then
      c := c + 1;
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.BuscarCaracter1Click(Sender: TObject);
var
  letraStr: String;
begin
  letraStr := InputBox('Buscar Letra', 'Ingrese caracter a buscar:', 'a');
  if Length(letraStr) > 0 then
    Edit3.Text := 'La letra ' + letraStr[1] + ' aparece ' +
                  IntToStr(ContarOcurrenciasLetra(cad, letraStr[1])) + ' veces';
end;""",
        "entrada_ejemplo": "cad='Estructuras de Datos', letra='a'",
        "salida_ejemplo": "3 veces",
        "extra_req": True,
        "extra_label": "Letra a buscar:",
        "extra_default": "a"
    },
    {
        "num": 11,
        "titulo": "Crear una función que elimine espacios en blanco de una cadena.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Acumular en un nuevo String solo los caracteres que sean distintos del espacio en blanco (' ').<br>• Salida: String compacto sin espacios.",
        "pseudo": """Funcion EliminarEspacios(cad: Cadena): Cadena
  res <- ""
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si cad[i] <> ' ' Entonces
      res <- res + cad[i]
    FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿cad[i] <> ' '?", "res acumulado"],
        "traza_rows": [
            ["1", "' '", "No", "''"],
            ["2", "'F'", "Sí", "'F'"],
            ["3", "' '", "No", "'F'"],
            ["4", "'I'", "Sí", "'FI'"]
        ],
        "codigo_pascal": """// Ejercicio 11: Eliminar espacios en blanco
function EliminarEspacios(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.Cargar1Click(Sender: TObject);
begin
  Edit3.Text := EliminarEspacios(cad);
end;""",
        "entrada_ejemplo": " F I C C T   U A G R M ",
        "salida_ejemplo": "FICCTUAGRM",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 12,
        "titulo": "Mostrar solo los n primeros caracteres de una cadena.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String), cant (Integer)<br>• Proceso: Extraer con bucle o Copy desde 1 hasta cant (sin superar Length(cad)).<br>• Salida: Subcadena con los primeros n caracteres.",
        "pseudo": """Funcion PrimerosNCaracteres(cad: Cadena, n: Entero): Cadena
  res <- ""
  limite <- n
  Si limite > Longitud(cad) Entonces
    limite <- Longitud(cad)
  FinSi
  Para i <- 1 Hasta limite Hacer
    res <- res + cad[i]
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "res acumulado"],
        "traza_rows": [
            ["1..8", "'Facultad'", "'Facultad'"]
        ],
        "codigo_pascal": """// Ejercicio 12: Primeros n caracteres
function PrimerosNCaracteres(cad: String; n: Integer): String;
var
  i, limite: Integer;
  res: String;
begin
  res := '';
  limite := n;
  if limite > Length(cad) then
    limite := Length(cad);
  for i := 1 to limite do
    res := res + cad[i];
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPrimerosNClick(Sender: TObject);
var
  nCant: Integer;
begin
  nCant := StrToIntDef(InputBox('Primeros N', 'Cantidad de caracteres:', '8'), 0);
  Edit3.Text := PrimerosNCaracteres(cad, nCant);
end;""",
        "entrada_ejemplo": "cad='Facultad de Ciencias', n=8",
        "salida_ejemplo": "Facultad",
        "extra_req": True,
        "extra_label": "Cantidad N de caracteres:",
        "extra_default": "8"
    },
    {
        "num": 13,
        "titulo": "Determinar si una cadena está vacía o contiene texto.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Verificar si Length(Trim(cad)) = 0.<br>• Salida: Boolean (True si está vacía, False si contiene texto).",
        "pseudo": """Funcion EstaVacia(cad: Cadena): Booleano
  Retornar (Longitud(Recortar(cad)) = 0)
FinFuncion""",
        "traza_headers": ["cad", "Trim(cad)", "Length", "Resultado"],
        "traza_rows": [
            ["'   '", "''", "0", "TRUE (Vacía)"],
            ["'Hola'", "'Hola'", "4", "FALSE (Contiene texto)"]
        ],
        "codigo_pascal": """// Ejercicio 13: Determinar si está vacía
function EstaVacia(cad: String): Boolean;
begin
  Result := (Length(Trim(cad)) = 0);
end;""",
        "codigo_vcl": """procedure TForm1.MenuEstaVaciaClick(Sender: TObject);
begin
  if EstaVacia(cad) then
    Edit3.Text := 'La cadena esta VACIA'
  else
    Edit3.Text := 'La cadena CONTIENE TEXTO';
end;""",
        "entrada_ejemplo": "   ",
        "salida_ejemplo": "TRUE (Vacía)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 14,
        "titulo": "Mostrar los códigos ASCII de cada carácter de una cadena.",
        "tipo": "Procedimiento",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer la cadena y para cada carácter cad[i] obtener su valor numérico con la función nativa Ord(cad[i]).<br>• Salida: Muestra la lista de 'carácter -> código ASCII'.",
        "pseudo": """Procedimiento MostrarCodigosASCII(cad: Cadena)
  Para i <- 1 Hasta Longitud(cad) Hacer
    Mostrar(cad[i], " -> ASCII: ", Ascii(cad[i]))
  FinPara
FinProcedimiento""",
        "traza_headers": ["i", "cad[i]", "Ord(cad[i])", "Mapeo"],
        "traza_rows": [
            ["1", "'U'", "85", "U -> 85"],
            ["2", "'A'", "65", "A -> 65"],
            ["3", "'G'", "71", "G -> 71"],
            ["4", "'R'", "82", "R -> 82"],
            ["5", "'M'", "77", "M -> 77"]
        ],
        "codigo_pascal": """// Ejercicio 14: Mostrar códigos ASCII
procedure MostrarCodigosASCII(cad: String; var salida: String);
var
  i: Integer;
begin
  salida := '';
  for i := 1 to Length(cad) do
  begin
    salida := salida + cad[i] + '->' + IntToStr(Ord(cad[i])) + '  ';
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuAsciiClick(Sender: TObject);
var
  info: String;
begin
  MostrarCodigosASCII(cad, info);
  Edit3.Text := info;
  ShowMessage('Codigos ASCII:' + #13#10 + info);
end;""",
        "entrada_ejemplo": "UAGRM",
        "salida_ejemplo": "U->85  A->65  G->71  R->82  M->77",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 15,
        "titulo": "Contar cuántas letras mayúsculas hay en una cadena.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer la cadena con while o for; si cad[i] está en ['A'..'Z'] incrementar contador.<br>• Salida: Total de letras mayúsculas.",
        "pseudo": """Funcion ContarMayusculas(cad: Cadena): Entero
  c <- 0
  may <- ['A'..'Z']
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si cad[i] en may Entonces
      c <- c + 1
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿En ['A'..'Z']?", "c"],
        "traza_rows": [
            ["1", "'I'", "Sí", "1"],
            ["12", "'I'", "Sí", "2"],
            ["24", "'S'", "Sí", "3"]
        ],
        "codigo_pascal": """// Ejercicio 15: Contar mayúsculas
function ContarMayusculas(cad: String): Integer;
const
  may: set of char = ['A'..'Z'];
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] in may then
      c := c + 1;
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.Cargar2Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarMayusculas(cad)) + ' Mayusculas';
end;""",
        "entrada_ejemplo": "Ingenieria Informatica Sem 2-2025",
        "salida_ejemplo": "3 Mayusculas (I, I, S)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 16,
        "titulo": "Determinar si una cadena es palíndroma (igual al derecho y al revés).",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Limpiar espacios y pasar a mayúsculas. Comparar punteros i (desde inicio) y j (desde fin) acercándose al centro.<br>• Salida: Boolean (True si es palíndroma).",
        "pseudo": """Funcion EsPalindroma(cad: Cadena): Booleano
  limpia <- QuitarEspaciosYMayusculas(cad)
  i <- 1
  j <- Longitud(limpia)
  Mientras i < j Hacer
    Si limpia[i] <> limpia[j] Entonces
      Retornar Falso
    FinSi
    i <- i + 1
    j <- j - 1
  FinMientras
  Retornar Verdadero
FinFuncion""",
        "traza_headers": ["i", "j", "limpia[i]", "limpia[j]", "¿Coinciden?"],
        "traza_rows": [
            ["1", "15", "'A'", "'A'", "Sí"],
            ["2", "14", "'N'", "'N'", "Sí"],
            ["3", "13", "'I'", "'I'", "Sí"],
            ["4", "12", "'T'", "'T'", "Sí"],
            ["...", "...", "...", "...", "Es Palíndroma: TRUE"]
        ],
        "codigo_pascal": """// Ejercicio 16: Es palíndroma
function EsPalindroma(cad: String): Boolean;
var
  limpia: String;
  i, j: Integer;
begin
  limpia := '';
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      limpia := limpia + UpCase(cad[i]);
  end;
  i := 1;
  j := Length(limpia);
  Result := True;
  while i < j do
  begin
    if limpia[i] <> limpia[j] then
    begin
      Result := False;
      Exit;
    end;
    i := i + 1;
    j := j - 1;
  end;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPalindromaClick(Sender: TObject);
begin
  if EsPalindroma(cad) then
    Edit3.Text := 'Es Palindroma (SI)'
  else
    Edit3.Text := 'No es Palindroma (NO)';
end;""",
        "entrada_ejemplo": "anita lava la tina",
        "salida_ejemplo": "TRUE (Es Palíndroma)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 17,
        "titulo": "Contar cuántas palabras hay en una frase.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Usar una bandera booleana enPalabra iniciada en False. Cuando se encuentre un carácter distinto de espacio y no se estaba dentro de una palabra, incrementar contador.<br>• Salida: Total de palabras (Integer).",
        "pseudo": """Funcion ContarPalabras(frase: Cadena): Entero
  c <- 0
  enPalabra <- Falso
  Para i <- 1 Hasta Longitud(frase) Hacer
    Si frase[i] <> ' ' Entonces
      Si No enPalabra Entonces
        c <- c + 1
        enPalabra <- Verdadero
      FinSi
    Sino
      enPalabra <- Falso
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["i", "frase[i]", "enPalabra", "Acción", "c"],
        "traza_rows": [
            ["1", "' '", "False", "Espacio", "0"],
            ["2", "'E'", "False -> True", "Nueva palabra", "1 ('El')"],
            ["3", "'l'", "True", "Continúa", "1"],
            ["4", "' '", "True -> False", "Fin palabra", "1"],
            ["5", "'s'", "False -> True", "Nueva palabra", "2 ('sol')"]
        ],
        "codigo_pascal": """// Ejercicio 17: Contar palabras
function ContarPalabras(frase: String): Integer;
var
  i, c: Integer;
  enPalabra: Boolean;
begin
  c := 0;
  enPalabra := False;
  for i := 1 to Length(frase) do
  begin
    if frase[i] <> ' ' then
    begin
      if not enPalabra then
      begin
        c := c + 1;
        enPalabra := True;
      end;
    end
    else
      enPalabra := False;
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.MenuContarPalabrasClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarPalabras(cad)) + ' palabras';
end;""",
        "entrada_ejemplo": "  El sol brilla hoy en Santa Cruz ",
        "salida_ejemplo": "7 palabras",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 18,
        "titulo": "Verificar si una palabra se encuentra dentro de una frase.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: frase, palabra (String)<br>• Proceso: Convertir ambas a mayúsculas y comprobar si Pos(palabraMayus, fraseMayus) > 0.<br>• Salida: Boolean (True si existe).",
        "pseudo": """Funcion ExistePalabra(frase, palabra: Cadena): Booleano
  fMayus <- CadenaMayusculas(frase)
  pMayus <- CadenaMayusculas(palabra)
  Retornar (Posicion(pMayus, fMayus) > 0)
FinFuncion""",
        "traza_headers": ["frase", "palabra", "Pos()", "Resultado"],
        "traza_rows": [
            ["'LA TECNOLOGIA AVANZA'", "'AVANZA'", "15", "TRUE (Encontrada en pos 15)"]
        ],
        "codigo_pascal": """// Ejercicio 18: Verificar si existe palabra
function ExistePalabra(frase, palabra: String): Boolean;
var
  fMayus, pMayus: String;
begin
  fMayus := UpperCase(frase);
  pMayus := UpperCase(palabra);
  Result := (Pos(pMayus, fMayus) > 0);
end;""",
        "codigo_vcl": """procedure TForm1.BuscarPalabraClick(Sender: TObject);
var
  buscada: String;
begin
  buscada := InputBox('Buscar Palabra', 'Ingrese palabra a buscar:', 'avanza');
  if ExistePalabra(cad, buscada) then
    Edit3.Text := 'SI se encuentra la palabra "' + buscada + '"'
  else
    Edit3.Text := 'NO se encuentra la palabra "' + buscada + '"';
end;""",
        "entrada_ejemplo": "frase='La tecnologia avanza', palabra='avanza'",
        "salida_ejemplo": "TRUE (Existe)",
        "extra_req": True,
        "extra_label": "Palabra a buscar en la frase:",
        "extra_default": "avanza"
    },
    {
        "num": 19,
        "titulo": "Reemplazar todas las apariciones de una letra por otra.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String), vieja, nueva (Char)<br>• Proceso: Recorrer carácter a carácter. Si cad[i] = vieja, concatenar nueva, de lo contrario concatenar cad[i].<br>• Salida: String modificado.",
        "pseudo": """Funcion ReemplazarLetra(cad: Cadena, vieja, nueva: Caracter): Cadena
  res <- ""
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si cad[i] = vieja Entonces
      res <- res + nueva
    Sino
      res <- res + cad[i]
    FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿cad[i] = 'a'?", "res"],
        "traza_rows": [
            ["1", "'b'", "No", "'b'"],
            ["2", "'a'", "Sí -> 'o'", "'bo'"],
            ["3", "'n'", "No", "'bon'"],
            ["4", "'a'", "Sí -> 'o'", "'bono'"],
            ["5", "'n'", "No", "'bonon'"],
            ["6", "'a'", "Sí -> 'o'", "'bonono'"]
        ],
        "codigo_pascal": """// Ejercicio 19: Reemplazar letra
function ReemplazarLetra(cad: String; vieja, nueva: Char): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if cad[i] = vieja then
      res := res + nueva
    else
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuReemplazarLetraClick(Sender: TObject);
var
  vStr, nStr: String;
begin
  vStr := InputBox('Reemplazar', 'Letra vieja:', 'a');
  nStr := InputBox('Reemplazar', 'Letra nueva:', 'o');
  if (Length(vStr) > 0) and (Length(nStr) > 0) then
    Edit3.Text := ReemplazarLetra(cad, vStr[1], nStr[1]);
end;""",
        "entrada_ejemplo": "cad='banana', vieja='a', nueva='o'",
        "salida_ejemplo": "bonono",
        "extra_req": True,
        "extra_label": "Letra vieja y nueva separadas por coma (ej: a,o):",
        "extra_default": "a,o"
    },
    {
        "num": 20,
        "titulo": "Eliminar todas las apariciones de una letra dentro de la cadena.",
        "tipo": "Función",
        "categoria": "espacios",
        "analisis": "• Entrada: cad (String), letra (Char)<br>• Proceso: Recorrer la cadena y acumular únicamente los caracteres cuyo UpCase sea diferente de UpCase(letra).<br>• Salida: String sin la letra indicada.",
        "pseudo": """Funcion EliminarLetra(cad: Cadena, letra: Caracter): Cadena
  res <- ""
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si Mayuscula(cad[i]) <> Mayuscula(letra) Entonces
      res <- res + cad[i]
    FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿Diferente de 'e'?", "res acumulado"],
        "traza_rows": [
            ["1", "'P'", "Sí", "'P'"],
            ["2", "'a'", "Sí", "'Pa'"],
            ["3", "'r'", "Sí", "'Par'"],
            ["4", "'a'", "Sí", "'Para'"],
            ["5", "'l'", "Sí", "'Paral'"],
            ["6", "'e'", "No (se omite)", "'Paral'"]
        ],
        "codigo_pascal": """// Ejercicio 20: Eliminar letra
function EliminarLetra(cad: String; letra: Char): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if UpCase(cad[i]) <> UpCase(letra) then
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuEliminarLetraClick(Sender: TObject);
var
  letraStr: String;
begin
  letraStr := InputBox('Eliminar Letra', 'Ingrese letra a eliminar:', 'e');
  if Length(letraStr) > 0 then
    Edit3.Text := EliminarLetra(cad, letraStr[1]);
end;""",
        "entrada_ejemplo": "cad='Paralelepipedo', letra='e'",
        "salida_ejemplo": "Parallpipdo",
        "extra_req": True,
        "extra_label": "Letra a eliminar:",
        "extra_default": "e"
    },
    {
        "num": 21,
        "titulo": "Contar cuántas veces aparece una palabra en un texto.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: texto, palabra (String)<br>• Proceso: Buscar con Pos(palabra, texto). Mientras se encuentre, incrementar contador y borrar hasta la posición encontrada con Delete().<br>• Salida: Conteo de repeticiones de la palabra (Integer).",
        "pseudo": """Funcion ContarOcurrenciasPalabra(texto, palabra: Cadena): Entero
  c <- 0
  tMayus <- Mayusculas(texto)
  pMayus <- Mayusculas(palabra)
  posic <- Posicion(pMayus, tMayus)
  Mientras posic > 0 Hacer
    c <- c + 1
    Eliminar(tMayus, 1, posic + Longitud(pMayus) - 1)
    posic <- Posicion(pMayus, tMayus)
  FinMientras
  Retornar c
FinFuncion""",
        "traza_headers": ["Iteración", "Pos", "tMayus restante", "c"],
        "traza_rows": [
            ["1", "1", "' LUNA SOL ESTRELLA SOL'", "1"],
            ["2", "7", "' ESTRELLA SOL'", "2"],
            ["3", "10", "''", "3"],
            ["Fin", "0", "Termina", "Retorna 3"]
        ],
        "codigo_pascal": """// Ejercicio 21: Contar ocurrencias de palabra
function ContarOcurrenciasPalabra(texto, palabra: String): Integer;
var
  p, c: Integer;
  tMayus, pMayus: String;
begin
  c := 0;
  tMayus := UpperCase(texto);
  pMayus := UpperCase(palabra);
  if (Length(pMayus) = 0) or (Length(tMayus) = 0) then Exit(0);
  p := Pos(pMayus, tMayus);
  while p > 0 do
  begin
    c := c + 1;
    Delete(tMayus, 1, p + Length(pMayus) - 1);
    p := Pos(pMayus, tMayus);
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.MenuOcurrPalabraClick(Sender: TObject);
var
  pal: String;
begin
  pal := InputBox('Ocurrencias de Palabra', 'Palabra a contar:', 'sol');
  Edit3.Text := 'La palabra "' + pal + '" aparece ' +
                IntToStr(ContarOcurrenciasPalabra(cad, pal)) + ' veces';
end;""",
        "entrada_ejemplo": "texto='sol luna sol estrella sol', pal='sol'",
        "salida_ejemplo": "3",
        "extra_req": True,
        "extra_label": "Palabra a contar:",
        "extra_default": "sol"
    },
    {
        "num": 22,
        "titulo": "Crear un procedimiento que muestre cada carácter de la cadena en una línea diferente.",
        "tipo": "Procedimiento",
        "categoria": "palabras",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer con un bucle del 1 al Length(cad) imprimiendo cada cad[i] con su índice en una línea separada.<br>• Salida: Impresión línea por línea.",
        "pseudo": """Procedimiento MostrarCaracteresPorLinea(cad: Cadena)
  Para i <- 1 Hasta Longitud(cad) Hacer
    Mostrar("[", i, "]: ", cad[i])
  FinPara
FinProcedimiento""",
        "traza_headers": ["i", "cad[i]", "Línea generada"],
        "traza_rows": [
            ["1", "'P'", "[1]: P"],
            ["2", "'A'", "[2]: A"],
            ["3", "'S'", "[3]: S"],
            ["4", "'C'", "[4]: C"],
            ["5", "'A'", "[5]: A"],
            ["6", "'L'", "[6]: L"]
        ],
        "codigo_pascal": """// Ejercicio 22: Carácter por línea
procedure MostrarCaracteresPorLinea(cad: String; var lineas: String);
var
  i: Integer;
begin
  lineas := '';
  for i := 1 to Length(cad) do
    lineas := lineas + '[' + IntToStr(i) + ']: ' + cad[i] + #13#10;
end;""",
        "codigo_vcl": """procedure TForm1.MenuLineasClick(Sender: TObject);
var
  reporte: String;
begin
  MostrarCaracteresPorLinea(cad, reporte);
  ShowMessage('Caracteres por linea:' + #13#10 + reporte);
  Edit3.Text := 'Ver ventana emergente (ShowMessage)';
end;""",
        "entrada_ejemplo": "PASCAL",
        "salida_ejemplo": "[1]: P  [2]: A  [3]: S  [4]: C  [5]: A  [6]: L",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 23,
        "titulo": "Determinar si una cadena contiene números o solo letras.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Evaluar caracteres mediante banderas tieneLetras, tieneDigitos, otros. Clasificar el resultado.<br>• Salida: String descriptivo ('Solo letras', 'Solo digitos', 'Alfanumerica', etc.).",
        "pseudo": """Funcion DeterminarContenido(cad: Cadena): Cadena
  tieneLetras <- Falso
  tieneDigitos <- Falso
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si EsLetra(cad[i]) Entonces tieneLetras <- Verdadero
    Sino Si EsDigito(cad[i]) Entonces tieneDigitos <- Verdadero
    FinSi
  FinPara
  Si tieneLetras Y No tieneDigitos Entonces Retornar 'Solo letras'
  Sino Si tieneDigitos Y No tieneLetras Entonces Retornar 'Solo digitos'
  Sino Retornar 'Alfanumerica'
  FinSi
FinFuncion""",
        "traza_headers": ["Carácter", "Letra?", "Dígito?", "Estado"],
        "traza_rows": [
            ["'H'..'o'", "Sí", "No", "tieneLetras := True"],
            ["Resultado", "-", "-", "'Solo letras'"]
        ],
        "codigo_pascal": """// Ejercicio 23: Determinar contenido
function DeterminarContenido(cad: String): String;
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
  digitos: set of char = ['0'..'9'];
var
  i: Integer;
  tLetras, tDigitos, tOtros: Boolean;
begin
  tLetras := False; tDigitos := False; tOtros := False;
  for i := 1 to Length(cad) do
  begin
    if cad[i] in letras then tLetras := True
    else if cad[i] in digitos then tDigitos := True
    else if cad[i] <> ' ' then tOtros := True;
  end;
  if tDigitos and not tLetras and not tOtros then
    Result := 'Solo digitos numericos'
  else if tLetras and not tDigitos and not tOtros then
    Result := 'Solo letras'
  else if tLetras and tDigitos then
    Result := 'Contiene numeros y letras (Alfanumerica)'
  else
    Result := 'Contiene caracteres especiales o simbolos';
end;""",
        "codigo_vcl": """procedure TForm1.MenuTipoContenidoClick(Sender: TObject);
begin
  Edit3.Text := DeterminarContenido(cad);
end;""",
        "entrada_ejemplo": "HolaMundo",
        "salida_ejemplo": "Solo letras",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 24,
        "titulo": "Calcular cuántos dígitos numéricos hay en la cadena.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Definir conjunto dig = ['0'..'9']. Recorrer y si cad[i] in dig, c := c + 1.<br>• Salida: Cantidad de dígitos numéricos (Integer).",
        "pseudo": """Funcion ContarDigitos(cad: Cadena): Entero
  c <- 0
  dig <- ['0'..'9']
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si cad[i] en dig Entonces
      c <- c + 1
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿Dígito '0'..'9'?", "c"],
        "traza_rows": [
            ["1..5", "'Aula '", "No", "0"],
            ["6..8", "'236'", "Sí ('2','3','6')", "3"],
            ["17..19", "'225'", "Sí ('2','2','5')", "6"],
            ["26", "'3'", "Sí ('3')", "7"]
        ],
        "codigo_pascal": """// Ejercicio 24: Contar dígitos
function ContarDigitos(cad: String): Integer;
const
  dig: set of char = ['0'..'9'];
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(cad) do
  begin
    if cad[i] in dig then
      c := c + 1;
  end;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.MenuContarDigitosClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarDigitos(cad)) + ' digitos numericos';
end;""",
        "entrada_ejemplo": "Aula 236 Modulo 225 Piso 3",
        "salida_ejemplo": "7 digitos",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 25,
        "titulo": "Extraer la primera palabra de una frase.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Saltar espacios iniciales hasta el inicio de la primera palabra. Avanzar hasta encontrar el siguiente espacio o fin de cadena. Extraer con Copy.<br>• Salida: String con la primera palabra.",
        "pseudo": """Funcion ExtraerPrimeraPalabra(frase: Cadena): Cadena
  inicio <- 1
  Mientras (inicio <= Longitud(frase)) Y (frase[inicio] = ' ') Hacer
    inicio <- inicio + 1
  FinMientras
  finP <- inicio
  Mientras (finP <= Longitud(frase)) Y (frase[finP] <> ' ') Hacer
    finP <- finP + 1
  FinMientras
  Retornar SubCadena(frase, inicio, finP - inicio)
FinFuncion""",
        "traza_headers": ["inicio", "finP", "Subcadena extraída"],
        "traza_rows": [
            ["3 (salta 2 espacios)", "10 (espacio tras 'Gabriel')", "'Gabriel'"]
        ],
        "codigo_pascal": """// Ejercicio 25: Extraer primera palabra
function ExtraerPrimeraPalabra(frase: String): String;
var
  inicio, finP: Integer;
begin
  inicio := 1;
  while (inicio <= Length(frase)) and (frase[inicio] = ' ') do
    inicio := inicio + 1;
  if inicio > Length(frase) then Exit('');
  finP := inicio;
  while (finP <= Length(frase)) and (frase[finP] <> ' ') do
    finP := finP + 1;
  Result := Copy(frase, inicio, finP - inicio);
end;""",
        "codigo_vcl": """procedure TForm1.MenuPrimeraPalabraClick(Sender: TObject);
begin
  Edit3.Text := 'Primera palabra: "' + ExtraerPrimeraPalabra(cad) + '"';
end;""",
        "entrada_ejemplo": "  Gabriel Rene Moreno fue ilustre",
        "salida_ejemplo": "Gabriel",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 26,
        "titulo": "Extraer la última palabra de una frase.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Retroceder desde Length(frase) saltando espacios finales hasta encontrar el final de la última palabra. Retroceder hasta encontrar un espacio o inicio. Extraer con Copy.<br>• Salida: String con la última palabra.",
        "pseudo": """Funcion ExtraerUltimaPalabra(frase: Cadena): Cadena
  finP <- Longitud(frase)
  Mientras (finP >= 1) Y (frase[finP] = ' ') Hacer
    finP <- finP - 1
  FinMientras
  inicio <- finP
  Mientras (inicio >= 1) Y (frase[inicio] <> ' ') Hacer
    inicio <- inicio - 1
  FinMientras
  Retornar SubCadena(frase, inicio + 1, finP - inicio)
FinFuncion""",
        "traza_headers": ["finP", "inicio", "Extracción"],
        "traza_rows": [
            ["31 (antes del espacio final)", "26 (espacio antes de 'final')", "'final'"]
        ],
        "codigo_pascal": """// Ejercicio 26: Extraer última palabra
function ExtraerUltimaPalabra(frase: String): String;
var
  finP, inicio: Integer;
begin
  finP := Length(frase);
  while (finP >= 1) and (frase[finP] = ' ') do
    finP := finP - 1;
  if finP < 1 then Exit('');
  inicio := finP;
  while (inicio >= 1) and (frase[inicio] <> ' ') do
    inicio := inicio - 1;
  Result := Copy(frase, inicio + 1, finP - inicio);
end;""",
        "codigo_vcl": """procedure TForm1.MenuUltimaPalabraClick(Sender: TObject);
begin
  Edit3.Text := 'Ultima palabra: "' + ExtraerUltimaPalabra(cad) + '"';
end;""",
        "entrada_ejemplo": "Estudiar para el examen final ",
        "salida_ejemplo": "final",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 27,
        "titulo": "Convertir una cadena con espacios múltiples a una con un solo espacio entre palabras.",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer usando una bandera espacioAnterior iniciada en True para omitir espacios iniciales y múltiples seguidos.<br>• Salida: String limpio con espaciado simple.",
        "pseudo": """Funcion NormalizarEspacios(cad: Cadena): Cadena
  res <- ""
  espacioAnterior <- Verdadero
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si cad[i] <> ' ' Entonces
      res <- res + cad[i]
      espacioAnterior <- Falso
    Sino Si No espacioAnterior Entonces
      res <- res + ' '
      espacioAnterior <- Verdadero
    FinSi
  FinPara
  Si Longitud(res) > 0 Y UltimoCaracter(res) = ' ' Entonces
    QuitarUltimo(res)
  FinSi
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "espacioAnterior", "res"],
        "traza_rows": [
            ["1..3", "'   '", "True", "''"],
            ["4..12", "'Programar'", "False", "'Programar'"],
            ["13..15", "'   '", "False -> True (1 solo)", "'Programar '"]
        ],
        "codigo_pascal": """// Ejercicio 27: Normalizar espacios
function NormalizarEspacios(cad: String): String;
var
  i: Integer;
  res: String;
  espacioAnterior: Boolean;
begin
  res := '';
  espacioAnterior := True;
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
    begin
      res := res + cad[i];
      espacioAnterior := False;
    end
    else if not espacioAnterior then
    begin
      res := res + ' ';
      espacioAnterior := True;
    end;
  end;
  if (Length(res) > 0) and (res[Length(res)] = ' ') then
    Delete(res, Length(res), 1);
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuNormalizarClick(Sender: TObject);
begin
  Edit3.Text := NormalizarEspacios(cad);
end;""",
        "entrada_ejemplo": "   Programar   en   Pascal   ",
        "salida_ejemplo": "Programar en Pascal",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 28,
        "titulo": "Mostrar las palabras que empiezan con vocal de una frase.",
        "tipo": "Procedimiento",
        "categoria": "palabras",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Extraer palabras individuales. Si UpCase(palabra[1]) in ['A','E','I','O','U'], agregar a la lista.<br>• Salida: Lista de palabras que inician en vocal.",
        "pseudo": """Procedimiento MostrarPalabrasEmpiezanVocal(frase: Cadena)
  norm <- NormalizarEspacios(frase)
  Para cada palabra en norm Hacer
    Si Mayuscula(palabra[1]) en ['A','E','I','O','U'] Entonces
      Mostrar(palabra)
    FinSi
  FinPara
FinProcedimiento""",
        "traza_headers": ["Palabra", "Primer carácter", "¿Vocal?", "¿Se muestra?"],
        "traza_rows": [
            ["'El'", "'E'", "Sí", "Sí"],
            ["'aguila'", "'a'", "Sí", "Sí"],
            ["'vuela'", "'v'", "No", "No"],
            ["'sobre'", "'s'", "No", "No"],
            ["'arbol'", "'a'", "Sí", "Sí"],
            ["'azul'", "'a'", "Sí", "Sí"]
        ],
        "codigo_pascal": """// Ejercicio 28: Palabras que empiezan con vocal
procedure MostrarPalabrasEmpiezanVocal(frase: String; var resultado: String);
const
  voc: set of char = ['A','E','I','O','U'];
var
  norm, pal: String;
  i: Integer;
begin
  norm := NormalizarEspacios(frase);
  resultado := '';
  pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if (Length(pal) > 0) and (UpCase(pal[1]) in voc) then
        resultado := resultado + pal + ', ';
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and (UpCase(pal[1]) in voc) then
    resultado := resultado + pal;
end;""",
        "codigo_vcl": """procedure TForm1.MenuEmpiezanVocalClick(Sender: TObject);
var
  res: String;
begin
  MostrarPalabrasEmpiezanVocal(cad, res);
  Edit3.Text := 'Empiezan con vocal: ' + res;
end;""",
        "entrada_ejemplo": "El aguila vuela sobre el arbol azul",
        "salida_ejemplo": "El, aguila, el, arbol, azul",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 29,
        "titulo": "Mostrar las palabras que terminan en consonante.",
        "tipo": "Procedimiento",
        "categoria": "palabras",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Extraer palabras individuales. Comprobar si UpCase(palabra[Length(palabra)]) in cons. Agregar a la salida.<br>• Salida: Lista de palabras terminadas en consonante.",
        "pseudo": """Procedimiento MostrarPalabrasTerminanConsonante(frase: Cadena)
  cons <- ['A'..'Z'] - ['A','E','I','O','U']
  Para cada palabra en frase Hacer
    ult <- palabra[Longitud(palabra)]
    Si Mayuscula(ult) en cons Entonces
      Mostrar(palabra)
    FinSi
  FinPara
FinProcedimiento""",
        "traza_headers": ["Palabra", "Último carácter", "¿Consonante?", "¿Se muestra?"],
        "traza_rows": [
            ["'Juan'", "'n'", "Sí", "Sí"],
            ["'y'", "'y'", "Sí", "Sí"],
            ["'David'", "'d'", "Sí", "Sí"],
            ["'juegan'", "'n'", "Sí", "Sí"],
            ["'futbol'", "'l'", "Sí", "Sí"]
        ],
        "codigo_pascal": """// Ejercicio 29: Palabras terminadas en consonante
procedure MostrarPalabrasTerminanConsonante(frase: String; var resultado: String);
const
  cons: set of char = ['A'..'Z'] - ['A','E','I','O','U'];
var
  norm, pal: String;
  i: Integer;
begin
  norm := NormalizarEspacios(frase);
  resultado := '';
  pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if (Length(pal) > 0) and (UpCase(pal[Length(pal)]) in cons) then
        resultado := resultado + pal + ', ';
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and (UpCase(pal[Length(pal)]) in cons) then
    resultado := resultado + pal;
end;""",
        "codigo_vcl": """procedure TForm1.MenuTerminanConsonanteClick(Sender: TObject);
var
  res: String;
begin
  MostrarPalabrasTerminanConsonante(cad, res);
  Edit3.Text := 'Terminan en consonante: ' + res;
end;""",
        "entrada_ejemplo": "Juan y David juegan futbol",
        "salida_ejemplo": "Juan, y, David, juegan, futbol",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 30,
        "titulo": "Intercalar dos cadenas carácter por carácter (por ejemplo, “ABC” y “123” → “A1B2C3”).",
        "tipo": "Función",
        "categoria": "palabras",
        "analisis": "• Entrada: cad1, cad2 (String)<br>• Proceso: Recorrer de 1 hasta max(Length(cad1), Length(cad2)). Si i <= Length(cad1) anexar cad1[i]; si i <= Length(cad2) anexar cad2[i].<br>• Salida: String combinado intercalado.",
        "pseudo": """Funcion IntercalarCadenas(cad1, cad2: Cadena): Cadena
  res <- ""
  maxLen <- Mayor(Longitud(cad1), Longitud(cad2))
  Para i <- 1 Hasta maxLen Hacer
    Si i <= Longitud(cad1) Entonces res <- res + cad1[i] FinSi
    Si i <= Longitud(cad2) Entonces res <- res + cad2[i] FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad1[i]", "cad2[i]", "res acumulado"],
        "traza_rows": [
            ["1", "'A'", "'1'", "'A1'"],
            ["2", "'B'", "'2'", "'A1B2'"],
            ["3", "'C'", "'3'", "'A1B2C3'"]
        ],
        "codigo_pascal": """// Ejercicio 30: Intercalar dos cadenas
function IntercalarCadenas(cad1, cad2: String): String;
var
  i, maxLen: Integer;
  res: String;
begin
  res := '';
  maxLen := Length(cad1);
  if Length(cad2) > maxLen then maxLen := Length(cad2);
  for i := 1 to maxLen do
  begin
    if i <= Length(cad1) then res := res + cad1[i];
    if i <= Length(cad2) then res := res + cad2[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuIntercalarClick(Sender: TObject);
var
  cad2: String;
begin
  cad2 := InputBox('Intercalar', 'Segunda cadena:', '123');
  Edit3.Text := IntercalarCadenas(cad, cad2);
end;""",
        "entrada_ejemplo": "cad1='ABC', cad2='123'",
        "salida_ejemplo": "A1B2C3",
        "extra_req": True,
        "extra_label": "Segunda cadena a intercalar:",
        "extra_default": "123"
    },
    {
        "num": 31,
        "titulo": "Determinar cuántas palabras con más de 5 letras hay en una oración.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: oracion (String)<br>• Proceso: Extraer palabras individuales. Si Length(pal) > 5, incrementar contador c := c + 1.<br>• Salida: Cantidad de palabras largas (Integer).",
        "pseudo": """Funcion ContarPalabrasMasDe5Letras(oracion: Cadena): Entero
  c <- 0
  Para cada palabra en oracion Hacer
    Si Longitud(palabra) > 5 Entonces
      c <- c + 1
    FinSi
  FinPara
  Retornar c
FinFuncion""",
        "traza_headers": ["Palabra", "Longitud", "¿> 5?", "c"],
        "traza_rows": [
            ["'programacion'", "12", "Sí", "1"],
            ["'estructurada'", "12", "Sí", "2"],
            ["'ayuda'", "5", "No (no es > 5)", "2"],
            ["'desarrollo'", "10", "Sí", "3"]
        ],
        "codigo_pascal": """// Ejercicio 31: Palabras con más de 5 letras
function ContarPalabrasMasDe5Letras(oracion: String): Integer;
var
  norm, pal: String;
  i, c: Integer;
begin
  norm := NormalizarEspacios(oracion);
  c := 0; pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if Length(pal) > 5 then c := c + 1;
      pal := '';
    end;
  end;
  if Length(pal) > 5 then c := c + 1;
  Result := c;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPalabrasMas5Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarPalabrasMasDe5Letras(cad)) + ' palabras con mas de 5 letras';
end;""",
        "entrada_ejemplo": "La programacion estructurada ayuda al desarrollo",
        "salida_ejemplo": "3 (programacion, estructurada, desarrollo)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 32,
        "titulo": "Reemplazar todas las vocales por el carácter *.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Recorrer carácter a carácter. Si UpCase(cad[i]) in ['A','E','I','O','U'] concatenar '*' al resultado, sino concatenar cad[i].<br>• Salida: String con vocales censuradas.",
        "pseudo": """Funcion ReemplazarVocalesPorAsterisco(cad: Cadena): Cadena
  res <- ""
  voc <- ['A','E','I','O','U']
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si Mayuscula(cad[i]) en voc Entonces
      res <- res + '*'
    Sino
      res <- res + cad[i]
    FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿Vocal?", "res acumulado"],
        "traza_rows": [
            ["1", "'I'", "Sí -> '*'", "'*'"],
            ["2", "'n'", "No", "'*n'"],
            ["3", "'g'", "No", "'*ng'"],
            ["4", "'e'", "Sí -> '*'", "'*ng*'"]
        ],
        "codigo_pascal": """// Ejercicio 32: Reemplazar vocales por asterisco
function ReemplazarVocalesPorAsterisco(cad: String): String;
const
  voc: set of char = ['A','E','I','O','U'];
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if UpCase(cad[i]) in voc then
      res := res + '*'
    else
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuCensurarVocalesClick(Sender: TObject);
begin
  Edit3.Text := ReemplazarVocalesPorAsterisco(cad);
end;""",
        "entrada_ejemplo": "Ingenieria Informatica",
        "salida_ejemplo": "*ng*n**r** *nf*rm*t*c*",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 33,
        "titulo": "Crear una función que elimine acentos (á, é, í, ó, ú) de una cadena.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Reemplazar vocales acentuadas por sus equivalentes sin tilde mediante arreglos de correspondencia o StringReplace.<br>• Salida: String normalizado sin acentos.",
        "pseudo": """Funcion EliminarAcentos(cad: Cadena): Cadena
  Reemplazar 'á' por 'a', 'é' por 'e', 'í' por 'i', 'ó' por 'o', 'ú' por 'u'
  Reemplazar 'Á' por 'A', 'É' por 'E', 'Í' por 'I', 'Ó' por 'O', 'Ú' por 'U'
  Retornar cad
FinFuncion""",
        "traza_headers": ["Carácter con tilde", "Sustitución", "Ejemplo parcial"],
        "traza_rows": [
            ["'ó'", "'o'", "'canción' -> 'cancion'"],
            ["'é'", "'e'", "'café' -> 'cafe'"],
            ["'ú'", "'u'", "'música' -> 'musica'"],
            ["'á'", "'a'", "'árbol' -> 'arbol'"]
        ],
        "codigo_pascal": """// Ejercicio 33: Eliminar acentos
function EliminarAcentos(cad: String): String;
const
  CON_ACENTO: array[1..10] of String = ('á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú');
  SIN_ACENTO: array[1..10] of String = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
var
  k: Integer;
begin
  for k := 1 to 10 do
    cad := StringReplace(cad, CON_ACENTO[k], SIN_ACENTO[k], [rfReplaceAll]);
  Result := cad;
end;""",
        "codigo_vcl": """procedure TForm1.MenuQuitarAcentosClick(Sender: TObject);
begin
  Edit3.Text := EliminarAcentos(cad);
end;""",
        "entrada_ejemplo": "canción, café, música, árbol",
        "salida_ejemplo": "cancion, cafe, musica, arbol",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 34,
        "titulo": "Mostrar la palabra más larga de una frase.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Descomponer la frase en palabras. Mantener mayor = ''. Para cada palabra, si Length(pal) > Length(mayor), mayor := pal.<br>• Salida: String con la palabra de mayor longitud.",
        "pseudo": """Funcion PalabraMasLarga(frase: Cadena): Cadena
  mayor <- ""
  Para cada palabra en frase Hacer
    Si Longitud(palabra) > Longitud(mayor) Entonces
      mayor <- palabra
    FinSi
  FinPara
  Retornar mayor
FinFuncion""",
        "traza_headers": ["Palabra", "Longitud", "mayor anterior", "nuevo mayor"],
        "traza_rows": [
            ["'La'", "2", "''", "'La'"],
            ["'programacion'", "12", "'La'", "'programacion'"],
            ["'modular'", "7", "'programacion'", "'programacion'"],
            ["'simplifica'", "10", "'programacion'", "'programacion'"]
        ],
        "codigo_pascal": """// Ejercicio 34: Palabra más larga
function PalabraMasLarga(frase: String): String;
var
  norm, pal, mayor: String;
  i: Integer;
begin
  norm := NormalizarEspacios(frase);
  mayor := ''; pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if Length(pal) > Length(mayor) then mayor := pal;
      pal := '';
    end;
  end;
  if Length(pal) > Length(mayor) then mayor := pal;
  Result := mayor;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPalabraMasLargaClick(Sender: TObject);
begin
  Edit3.Text := 'Palabra mas larga: "' + PalabraMasLarga(cad) + '"';
end;""",
        "entrada_ejemplo": "La programacion modular simplifica problemas",
        "salida_ejemplo": "programacion (12 letras)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 35,
        "titulo": "Mostrar la palabra más corta de una frase.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: frase (String)<br>• Proceso: Extraer palabras. Mantener menor = ''. Si menor está vacío o Length(pal) < Length(menor), menor := pal.<br>• Salida: String con la palabra de menor longitud.",
        "pseudo": """Funcion PalabraMasCorta(frase: Cadena): Cadena
  menor <- ""
  Para cada palabra en frase Hacer
    Si (menor = "") O (Longitud(palabra) < Longitud(menor)) Entonces
      menor <- palabra
    FinSi
  FinPara
  Retornar menor
FinFuncion""",
        "traza_headers": ["Palabra", "Longitud", "menor anterior", "nuevo menor"],
        "traza_rows": [
            ["'Hoy'", "3", "''", "'Hoy'"],
            ["'vi'", "2", "'Hoy'", "'vi'"],
            ["'un'", "2", "'vi'", "'vi' (mantiene la primera)"],
            ["'gran'", "4", "'vi'", "'vi'"]
        ],
        "codigo_pascal": """// Ejercicio 35: Palabra más corta
function PalabraMasCorta(frase: String): String;
var
  norm, pal, menor: String;
  i: Integer;
begin
  norm := NormalizarEspacios(frase);
  menor := ''; pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if (Length(pal) > 0) and ((Length(menor) = 0) or (Length(pal) < Length(menor))) then
        menor := pal;
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and ((Length(menor) = 0) or (Length(pal) < Length(menor))) then
    menor := pal;
  Result := menor;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPalabraMasCortaClick(Sender: TObject);
begin
  Edit3.Text := 'Palabra mas corta: "' + PalabraMasCorta(cad) + '"';
end;""",
        "entrada_ejemplo": "Hoy vi un gran elefante",
        "salida_ejemplo": "vi (2 letras)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 36,
        "titulo": "Contar cuántas palabras repetidas hay en un texto.",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: texto (String)<br>• Proceso: Descomponer en palabras en un arreglo dinámico en minúsculas. Contar aquellas palabras que aparecen más de una vez sin contarlas doble.<br>• Salida: Cantidad de palabras repetidas (Integer).",
        "pseudo": """Funcion ContarPalabrasRepetidas(texto: Cadena): Entero
  palabras <- Descomponer(Minusculas(texto))
  repetidas <- 0
  Para i <- 1 Hasta Total(palabras) Hacer
    Si ApareceMasDeUnaVez(palabras[i]) Y NoFueContada(palabras[i]) Entonces
      repetidas <- repetidas + 1
    FinSi
  FinPara
  Retornar repetidas
FinFuncion""",
        "traza_headers": ["Palabra", "¿Aparece antes?", "¿Aparece después?", "¿Suma repetida?"],
        "traza_rows": [
            ["'el'", "No", "Sí (pos 4)", "Sí (+1)"],
            ["'gato'", "No", "Sí (pos 9)", "Sí (+1)"],
            ["'y'", "No", "No", "No"],
            ["'el'", "Sí (ya contada)", "No", "No"],
            ["Resultado", "-", "-", "2 ('el', 'gato')"]
        ],
        "codigo_pascal": """// Ejercicio 36: Palabras repetidas
function ContarPalabrasRepetidas(texto: String): Integer;
var
  norm, actual: String;
  palabras: array of String;
  i, j, n, repetidas: Integer;
  yaContada: Boolean;
begin
  norm := LowerCase(NormalizarEspacios(texto));
  SetLength(palabras, 0); actual := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then actual := actual + norm[i]
    else if Length(actual) > 0 then
    begin
      SetLength(palabras, Length(palabras) + 1);
      palabras[High(palabras)] := actual;
      actual := '';
    end;
  end;
  if Length(actual) > 0 then
  begin
    SetLength(palabras, Length(palabras) + 1);
    palabras[High(palabras)] := actual;
  end;
  n := Length(palabras); repetidas := 0;
  for i := 0 to n - 1 do
  begin
    yaContada := False;
    for j := 0 to i - 1 do
      if palabras[i] = palabras[j] then begin yaContada := True; Break; end;
    if not yaContada then
      for j := i + 1 to n - 1 do
        if palabras[i] = palabras[j] then begin repetidas := repetidas + 1; Break; end;
  end;
  Result := repetidas;
end;""",
        "codigo_vcl": """procedure TForm1.MenuPalabrasRepetidasClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarPalabrasRepetidas(cad)) + ' palabras repetidas';
end;""",
        "entrada_ejemplo": "el gato y el perro vieron a otro gato",
        "salida_ejemplo": "2 palabras repetidas (el, gato)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 37,
        "titulo": "Verificar si una cadena solo contiene letras (sin números ni símbolos).",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Si Length(cad) = 0 es False. Para cada carácter comprobar si está en ['A'..'Z', 'a'..'z']. Si alguno no pertenece, retornar False.<br>• Salida: Boolean (True si es 100% alfabética).",
        "pseudo": """Funcion SoloContieneLetras(cad: Cadena): Booleano
  Si Longitud(cad) = 0 Entonces Retornar Falso FinSi
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si No EsLetra(cad[i]) Entonces
      Retornar Falso
    FinSi
  FinPara
  Retornar Verdadero
FinFuncion""",
        "traza_headers": ["Carácter", "¿Es letra 'A'..'Z','a'..'z'?", "Continuar?"],
        "traza_rows": [
            ["'S'", "Sí", "Sí"],
            ["'o'", "Sí", "Sí"],
            ["'l'", "Sí", "Sí"],
            ["Resultado", "-", "Todos son letras -> TRUE"]
        ],
        "codigo_pascal": """// Ejercicio 37: Solo contiene letras
function SoloContieneLetras(cad: String): Boolean;
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
var
  i: Integer;
begin
  if Length(cad) = 0 then Exit(False);
  for i := 1 to Length(cad) do
  begin
    if not (cad[i] in letras) then
    begin
      Result := False;
      Exit;
    end;
  end;
  Result := True;
end;""",
        "codigo_vcl": """procedure TForm1.MenuSoloLetrasClick(Sender: TObject);
begin
  if SoloContieneLetras(cad) then
    Edit3.Text := 'SI: Solo contiene letras (Alfabetica)'
  else
    Edit3.Text := 'NO: Contiene numeros, espacios o simbolos';
end;""",
        "entrada_ejemplo": "SoloLetras",
        "salida_ejemplo": "TRUE (Solo letras)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 38,
        "titulo": "Generar una nueva cadena con los caracteres únicos (sin repetir).",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Acumular en res solo los caracteres donde Pos(cad[i], res) = 0 (es decir, que aún no hayan sido añadidos).<br>• Salida: String con caracteres sin duplicar.",
        "pseudo": """Funcion CaracteresUnicos(cad: Cadena): Cadena
  res <- ""
  Para i <- 1 Hasta Longitud(cad) Hacer
    Si Posicion(cad[i], res) = 0 Entonces
      res <- res + cad[i]
    FinSi
  FinPara
  Retornar res
FinFuncion""",
        "traza_headers": ["i", "cad[i]", "¿Pos(cad[i], res) = 0?", "res acumulado"],
        "traza_rows": [
            ["1", "'F'", "Sí (no está)", "'F'"],
            ["2", "'E'", "Sí", "'FE'"],
            ["3", "'R'", "Sí", "'FER'"],
            ["4", "'N'", "Sí", "'FERN'"],
            ["5", "'A'", "Sí", "'FERNA'"],
            ["6", "'N'", "No (ya está)", "'FERNA'"],
            ["...", "...", "...", "'FERNADO LVZ'"]
        ],
        "codigo_pascal": """// Ejercicio 38: Caracteres únicos
function CaracteresUnicos(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if Pos(cad[i], res) = 0 then
      res := res + cad[i];
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuCaracteresUnicosClick(Sender: TObject);
begin
  Edit3.Text := CaracteresUnicos(cad);
end;""",
        "entrada_ejemplo": "FERNANDO ALVAREZ",
        "salida_ejemplo": "FERNADO LVZ",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    },
    {
        "num": 39,
        "titulo": "Comprobar si dos cadenas son anagramas (contienen las mismas letras en distinto orden).",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: cad1, cad2 (String)<br>• Proceso: Limpiar solo letras en minúsculas. Si las longitudes difieren, False. Ordenar alfabéticamente ambas cadenas (Bubble sort de caracteres) y verificar si quedan idénticas.<br>• Salida: Boolean (True si son anagramas).",
        "pseudo": """Funcion SonAnagramas(cad1, cad2: Cadena): Booleano
  c1 <- OrdenarCaracteres(MinusculasSoloLetras(cad1))
  c2 <- OrdenarCaracteres(MinusculasSoloLetras(cad2))
  Retornar (c1 = c2)
FinFuncion""",
        "traza_headers": ["Cadena 1", "Cadena 2", "Ordenada 1", "Ordenada 2", "¿Iguales?"],
        "traza_rows": [
            ["'roma'", "'amor'", "'amor'", "'amor'", "TRUE (Son anagramas)"]
        ],
        "codigo_pascal": """// Ejercicio 39: Son anagramas
function SonAnagramas(cad1, cad2: String): Boolean;
var
  c1, c2: String;
  i, j: Integer;
  temp: Char;
begin
  c1 := ''; c2 := '';
  for i := 1 to Length(cad1) do
    if cad1[i] in ['A'..'Z', 'a'..'z'] then c1 := c1 + LowerCase(cad1[i]);
  for i := 1 to Length(cad2) do
    if cad2[i] in ['A'..'Z', 'a'..'z'] then c2 := c2 + LowerCase(cad2[i]);
  if Length(c1) <> Length(c2) then Exit(False);
  // Ordenar c1
  for i := 1 to Length(c1) - 1 do
    for j := i + 1 to Length(c1) do
      if c1[i] > c1[j] then begin temp := c1[i]; c1[i] := c1[j]; c1[j] := temp; end;
  // Ordenar c2
  for i := 1 to Length(c2) - 1 do
    for j := i + 1 to Length(c2) do
      if c2[i] > c2[j] then begin temp := c2[i]; c2[i] := c2[j]; c2[j] := temp; end;
  Result := (c1 = c2);
end;""",
        "codigo_vcl": """procedure TForm1.MenuAnagramasClick(Sender: TObject);
var
  cad2: String;
begin
  cad2 := InputBox('Anagramas', 'Segunda palabra:', 'amor');
  if SonAnagramas(cad, cad2) then
    Edit3.Text := 'SI: Son anagramas ("' + cad + '" y "' + cad2 + '")'
  else
    Edit3.Text := 'NO: No son anagramas';
end;""",
        "entrada_ejemplo": "cad1='roma', cad2='amor'",
        "salida_ejemplo": "TRUE (Son anagramas)",
        "extra_req": True,
        "extra_label": "Segunda palabra para comprobar anagrama:",
        "extra_default": "amor"
    },
    {
        "num": 40,
        "titulo": "Mostrar de la cadena solo los caracteres de índice impar (1, 3, 5...).",
        "tipo": "Función",
        "categoria": "avanzados",
        "analisis": "• Entrada: cad (String)<br>• Proceso: Iniciar i := 1. Mientras i <= Length(cad) concatenar cad[i] e incrementar i := i + 2.<br>• Salida: String con las letras en posiciones impares.",
        "pseudo": """Funcion CaracteresIndiceImpar(cad: Cadena): Cadena
  res <- ""
  i <- 1
  Mientras i <= Longitud(cad) Hacer
    res <- res + cad[i]
    i <- i + 2
  FinMientras
  Retornar res
FinFuncion""",
        "traza_headers": ["i (impar)", "cad[i]", "res acumulado"],
        "traza_rows": [
            ["1", "'U'", "'U'"],
            ["3", "'I'", "'UI'"],
            ["5", "'E'", "'UIE'"],
            ["7", "'S'", "'UIES'"],
            ["9", "'D'", "'UIESD'"],
            ["11", "'D'", "'UIESDD'"]
        ],
        "codigo_pascal": """// Ejercicio 40: Caracteres de índice impar
function CaracteresIndiceImpar(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  i := 1;
  while i <= Length(cad) do
  begin
    res := res + cad[i];
    i := i + 2;
  end;
  Result := res;
end;""",
        "codigo_vcl": """procedure TForm1.MenuIndiceImparClick(Sender: TObject);
begin
  Edit3.Text := CaracteresIndiceImpar(cad);
end;""",
        "entrada_ejemplo": "UNIVERSIDAD",
        "salida_ejemplo": "UIESDD (posiciones 1, 3, 5, 7, 9, 11)",
        "extra_req": False,
        "extra_label": "",
        "extra_default": ""
    }
]

print(f"Cargados {len(EJERCICIOS_DATA)} ejercicios para la integración.")
