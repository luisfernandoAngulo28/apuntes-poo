unit UnitCadenas;

{ ============================================================================
  UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO
  FACULTAD DE CIENCIAS DE LA COMPUTACION
  INGENIERIA INFORMATICA, SISTEMAS Y REDES
  MATERIA: INTRODUCCION A LA INFORMATICA (INF110) - Sem 2-2025
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
  PRACTICO # 8: CADENA DE CARACTERES
  PROGRAMACION MODULAR: PROCEDIMIENTOS Y FUNCIONES
  ============================================================================ }

interface

uses
  SysUtils;

// =============================================================================
//                             FUNCIONES AUXILIARES
// =============================================================================
function EsLetra(c: Char): Boolean;
function EsDigito(c: Char): Boolean;
function EsVocal(c: Char): Boolean;
function EsConsonante(c: Char): Boolean;
function A_Mayuscula(c: Char): Char;
function A_Minuscula(c: Char): Char;

// =============================================================================
//                     LOS 40 EJERCICIOS DEL PRÁCTICO # 8
// =============================================================================

// 1. Crear una función que cuente los caracteres de una cadena.
function ContarCaracteres(cad: String): Integer;

// 2. Diseñar un procedimiento que muestre la primera letra de una cadena.
procedure MostrarPrimeraLetra(cad: String);

// 3. Crear una función que retorne la última letra de una cadena.
function UltimaLetra(cad: String): Char;

// 4. Contar cuántas vocales tiene una palabra ingresada.
function ContarVocales(pal: String): Integer;

// 5. Contar cuántas consonantes tiene una palabra.
function ContarConsonantes(pal: String): Integer;

// 6. Mostrar la cadena en mayúsculas usando una función.
function CadenaMayusculas(cad: String): String;

// 7. Mostrar la cadena en minúsculas.
function CadenaMinusculas(cad: String): String;

// 8. Invertir una cadena carácter por carácter.
function InvertirCadena(cad: String): String;

// 9. Concatenar dos cadenas ingresadas por el usuario.
function ConcatenarCadenas(cad1, cad2: String): String;

// 10. Calcular cuántas veces aparece una letra específica dentro de una cadena.
function ContarOcurrenciasLetra(cad: String; letra: Char): Integer;

// 11. Crear una función que elimine espacios en blanco de una cadena.
function EliminarEspacios(cad: String): String;

// 12. Mostrar solo los n primeros caracteres de una cadena.
function PrimerosNCaracteres(cad: String; n: Integer): String;

// 13. Determinar si una cadena está vacía o contiene texto.
function EstaVacia(cad: String): Boolean;

// 14. Mostrar los códigos ASCII de cada carácter de una cadena.
procedure MostrarCodigosASCII(cad: String);

// 15. Contar cuántas letras mayúsculas hay en una cadena.
function ContarMayusculas(cad: String): Integer;

// 16. Determinar si una cadena es palíndroma (igual al derecho y al revés).
function EsPalindroma(cad: String): Boolean;

// 17. Contar cuántas palabras hay en una frase.
function ContarPalabras(frase: String): Integer;

// 18. Verificar si una palabra se encuentra dentro de una frase.
function ExistePalabra(frase, palabra: String): Boolean;

// 19. Reemplazar todas las apariciones de una letra por otra.
function ReemplazarLetra(cad: String; vieja, nueva: Char): String;

// 20. Eliminar todas las apariciones de una letra dentro de la cadena.
function EliminarLetra(cad: String; letra: Char): String;

// 21. Contar cuántas veces aparece una palabra en un texto.
function ContarOcurrenciasPalabra(texto, palabra: String): Integer;

// 22. Crear un procedimiento que muestre cada carácter de la cadena en una línea diferente.
procedure MostrarCaracteresPorLinea(cad: String);

// 23. Determinar si una cadena contiene números o solo letras.
function DeterminarContenido(cad: String): String;

// 24. Calcular cuántos dígitos numéricos hay en la cadena.
function ContarDigitos(cad: String): Integer;

// 25. Extraer la primera palabra de una frase.
function ExtraerPrimeraPalabra(frase: String): String;

// 26. Extraer la última palabra de una frase.
function ExtraerUltimaPalabra(frase: String): String;

// 27. Convertir una cadena con espacios múltiples a una con un solo espacio entre palabras.
function NormalizarEspacios(cad: String): String;

// 28. Mostrar las palabras que empiezan con vocal de una frase.
procedure MostrarPalabrasEmpiezanVocal(frase: String);

// 29. Mostrar las palabras que terminan en consonante.
procedure MostrarPalabrasTerminanConsonante(frase: String);

// 30. Intercalar dos cadenas carácter por carácter (ejemplo: 'ABC' y '123' -> 'A1B2C3').
function IntercalarCadenas(cad1, cad2: String): String;

// 31. Determinar cuántas palabras con más de 5 letras hay en una oración.
function ContarPalabrasMasDe5Letras(oracion: String): Integer;

// 32. Reemplazar todas las vocales por el carácter '*'.
function ReemplazarVocalesPorAsterisco(cad: String): String;

// 33. Crear una función que elimine acentos (á, é, í, ó, ú) de una cadena.
function EliminarAcentos(cad: String): String;

// 34. Mostrar la palabra más larga de una frase.
function PalabraMasLarga(frase: String): String;

// 35. Mostrar la palabra más corta de una frase.
function PalabraMasCorta(frase: String): String;

// 36. Contar cuántas palabras repetidas hay en un texto.
function ContarPalabrasRepetidas(texto: String): Integer;

// 37. Verificar si una cadena solo contiene letras (sin números ni símbolos).
function SoloContieneLetras(cad: String): Boolean;

// 38. Generar una nueva cadena con los caracteres únicos (sin repetir).
function CaracteresUnicos(cad: String): String;

// 39. Comprobar si dos cadenas son anagramas (mismas letras en distinto orden).
function SonAnagramas(cad1, cad2: String): Boolean;

// 40. Mostrar de la cadena solo los caracteres de índice impar (1, 3, 5...).
function CaracteresIndiceImpar(cad: String): String;

implementation

// =============================================================================
//                     IMPLEMENTACIÓN DE FUNCIONES AUXILIARES
// =============================================================================

function A_Mayuscula(c: Char): Char;
begin
  if (c >= 'a') and (c <= 'z') then
    A_Mayuscula := Chr(Ord(c) - 32)
  else
    A_Mayuscula := c;
end;

function A_Minuscula(c: Char): Char;
begin
  if (c >= 'A') and (c <= 'Z') then
    A_Minuscula := Chr(Ord(c) + 32)
  else
    A_Minuscula := c;
end;

function EsLetra(c: Char): Boolean;
var
  m: Char;
begin
  m := A_Mayuscula(c);
  EsLetra := (m >= 'A') and (m <= 'Z');
end;

function EsDigito(c: Char): Boolean;
begin
  EsDigito := (c >= '0') and (c <= '9');
end;

function EsVocal(c: Char): Boolean;
var
  m: Char;
begin
  m := A_Mayuscula(c);
  EsVocal := (m = 'A') or (m = 'E') or (m = 'I') or (m = 'O') or (m = 'U');
end;

function EsConsonante(c: Char): Boolean;
begin
  EsConsonante := EsLetra(c) and not EsVocal(c);
end;

// =============================================================================
//                 IMPLEMENTACIÓN DE LOS 40 EJERCICIOS
// =============================================================================

// 1. Contar los caracteres de una cadena
function ContarCaracteres(cad: String): Integer;
var
  i, total: Integer;
begin
  total := 0;
  for i := 1 to Length(cad) do
    total := total + 1;
  ContarCaracteres := total;
end;

// 2. Procedimiento que muestre la primera letra de una cadena
procedure MostrarPrimeraLetra(cad: String);
var
  i: Integer;
begin
  for i := 1 to Length(cad) do
  begin
    if EsLetra(cad[i]) then
    begin
      WriteLn('Primera letra: ', cad[i]);
      Exit;
    end;
  end;
  if Length(cad) > 0 then
    WriteLn('Primer caracter: ', cad[1])
  else
    WriteLn('La cadena esta vacia.');
end;

// 3. Función que retorne la última letra de una cadena
function UltimaLetra(cad: String): Char;
var
  i: Integer;
begin
  UltimaLetra := #0;
  for i := Length(cad) downto 1 do
  begin
    if EsLetra(cad[i]) then
    begin
      UltimaLetra := cad[i];
      Exit;
    end;
  end;
  if Length(cad) > 0 then
    UltimaLetra := cad[Length(cad)];
end;

// 4. Contar cuántas vocales tiene una palabra ingresada
function ContarVocales(pal: String): Integer;
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(pal) do
  begin
    if EsVocal(pal[i]) then
      c := c + 1;
  end;
  ContarVocales := c;
end;

// 5. Contar cuántas consonantes tiene una palabra
function ContarConsonantes(pal: String): Integer;
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(pal) do
  begin
    if EsConsonante(pal[i]) then
      c := c + 1;
  end;
  ContarConsonantes := c;
end;

// 6. Mostrar la cadena en mayúsculas usando una función
function CadenaMayusculas(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
    res := res + A_Mayuscula(cad[i]);
  CadenaMayusculas := res;
end;

// 7. Mostrar la cadena en minúsculas
function CadenaMinusculas(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
    res := res + A_Minuscula(cad[i]);
  CadenaMinusculas := res;
end;

// 8. Invertir una cadena carácter por carácter
function InvertirCadena(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := Length(cad) downto 1 do
    res := res + cad[i];
  InvertirCadena := res;
end;

// 9. Concatenar dos cadenas ingresadas por el usuario
function ConcatenarCadenas(cad1, cad2: String): String;
begin
  ConcatenarCadenas := cad1 + cad2;
end;

// 10. Calcular cuántas veces aparece una letra específica dentro de una cadena
function ContarOcurrenciasLetra(cad: String; letra: Char): Integer;
var
  i, c: Integer;
  letraMayus: Char;
begin
  c := 0;
  letraMayus := A_Mayuscula(letra);
  for i := 1 to Length(cad) do
  begin
    if A_Mayuscula(cad[i]) = letraMayus then
      c := c + 1;
  end;
  ContarOcurrenciasLetra := c;
end;

// 11. Eliminar espacios en blanco de una cadena
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
  EliminarEspacios := res;
end;

// 12. Mostrar solo los n primeros caracteres de una cadena
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
  PrimerosNCaracteres := res;
end;

// 13. Determinar si una cadena está vacía o contiene texto
function EstaVacia(cad: String): Boolean;
begin
  EstaVacia := (Length(Trim(cad)) = 0);
end;

// 14. Mostrar los códigos ASCII de cada carácter de una cadena
procedure MostrarCodigosASCII(cad: String);
var
  i: Integer;
begin
  WriteLn('Codigos ASCII de cada caracter:');
  for i := 1 to Length(cad) do
    WriteLn('  ''', cad[i], ''' -> ASCII: ', Ord(cad[i]));
end;

// 15. Contar cuántas letras mayúsculas hay en una cadena
function ContarMayusculas(cad: String): Integer;
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(cad) do
  begin
    if (cad[i] >= 'A') and (cad[i] <= 'Z') then
      c := c + 1;
  end;
  ContarMayusculas := c;
end;

// 16. Determinar si una cadena es palíndroma (igual al derecho y al revés)
function EsPalindroma(cad: String): Boolean;
var
  limpia: String;
  i, j: Integer;
begin
  limpia := '';
  // Limpiamos espacios y pasamos a mayúsculas
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
      limpia := limpia + A_Mayuscula(cad[i]);
  end;

  i := 1;
  j := Length(limpia);
  EsPalindroma := True;
  while i < j do
  begin
    if limpia[i] <> limpia[j] then
    begin
      EsPalindroma := False;
      Exit;
    end;
    i := i + 1;
    j := j - 1;
  end;
end;

// 17. Contar cuántas palabras hay en una frase
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
  ContarPalabras := c;
end;

// 18. Verificar si una palabra se encuentra dentro de una frase
function ExistePalabra(frase, palabra: String): Boolean;
var
  fMayus, pMayus: String;
begin
  fMayus := CadenaMayusculas(frase);
  pMayus := CadenaMayusculas(palabra);
  ExistePalabra := (Pos(pMayus, fMayus) > 0);
end;

// 19. Reemplazar todas las apariciones de una letra por otra
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
  ReemplazarLetra := res;
end;

// 20. Eliminar todas las apariciones de una letra dentro de la cadena
function EliminarLetra(cad: String; letra: Char): String;
var
  i: Integer;
  res: String;
  letraMayus: Char;
begin
  res := '';
  letraMayus := A_Mayuscula(letra);
  for i := 1 to Length(cad) do
  begin
    if A_Mayuscula(cad[i]) <> letraMayus then
      res := res + cad[i];
  end;
  EliminarLetra := res;
end;

// 21. Contar cuántas veces aparece una palabra en un texto
function ContarOcurrenciasPalabra(texto, palabra: String): Integer;
var
  p, c: Integer;
  tMayus, pMayus: String;
begin
  c := 0;
  tMayus := CadenaMayusculas(texto);
  pMayus := CadenaMayusculas(palabra);
  if (Length(pMayus) = 0) or (Length(tMayus) = 0) then
  begin
    ContarOcurrenciasPalabra := 0;
    Exit;
  end;

  p := Pos(pMayus, tMayus);
  while p > 0 do
  begin
    c := c + 1;
    Delete(tMayus, 1, p + Length(pMayus) - 1);
    p := Pos(pMayus, tMayus);
  end;
  ContarOcurrenciasPalabra := c;
end;

// 22. Procedimiento que muestre cada carácter de la cadena en una línea diferente
procedure MostrarCaracteresPorLinea(cad: String);
var
  i: Integer;
begin
  for i := 1 to Length(cad) do
    WriteLn('[', i, ']: ', cad[i]);
end;

// 23. Determinar si una cadena contiene números o solo letras
function DeterminarContenido(cad: String): String;
var
  i: Integer;
  tieneLetras, tieneDigitos, otros: Boolean;
begin
  tieneLetras := False;
  tieneDigitos := False;
  otros := False;

  for i := 1 to Length(cad) do
  begin
    if EsLetra(cad[i]) then
      tieneLetras := True
    else if EsDigito(cad[i]) then
      tieneDigitos := True
    else if cad[i] <> ' ' then
      otros := True;
  end;

  if tieneDigitos and not tieneLetras and not otros then
    DeterminarContenido := 'Solo digitos numericos'
  else if tieneLetras and not tieneDigitos and not otros then
    DeterminarContenido := 'Solo letras'
  else if tieneLetras and tieneDigitos then
    DeterminarContenido := 'Contiene numeros y letras (Alfanumerica)'
  else
    DeterminarContenido := 'Contiene caracteres especiales o espacios';
end;

// 24. Calcular cuántos dígitos numéricos hay en la cadena
function ContarDigitos(cad: String): Integer;
var
  i, c: Integer;
begin
  c := 0;
  for i := 1 to Length(cad) do
  begin
    if EsDigito(cad[i]) then
      c := c + 1;
  end;
  ContarDigitos := c;
end;

// 25. Extraer la primera palabra de una frase
function ExtraerPrimeraPalabra(frase: String): String;
var
  inicio, fin: Integer;
begin
  inicio := 1;
  while (inicio <= Length(frase)) and (frase[inicio] = ' ') do
    inicio := inicio + 1;

  if inicio > Length(frase) then
  begin
    ExtraerPrimeraPalabra := '';
    Exit;
  end;

  fin := inicio;
  while (fin <= Length(frase)) and (frase[fin] <> ' ') do
    fin := fin + 1;

  ExtraerPrimeraPalabra := Copy(frase, inicio, fin - inicio);
end;

// 26. Extraer la última palabra de una frase
function ExtraerUltimaPalabra(frase: String): String;
var
  fin, inicio: Integer;
begin
  fin := Length(frase);
  while (fin >= 1) and (frase[fin] = ' ') do
    fin := fin - 1;

  if fin < 1 then
  begin
    ExtraerUltimaPalabra := '';
    Exit;
  end;

  inicio := fin;
  while (inicio >= 1) and (frase[inicio] <> ' ') do
    inicio := inicio - 1;

  ExtraerUltimaPalabra := Copy(frase, inicio + 1, fin - inicio);
end;

// 27. Convertir espacios múltiples a uno solo entre palabras
function NormalizarEspacios(cad: String): String;
var
  i: Integer;
  res: String;
  espacioAnterior: Boolean;
begin
  res := '';
  espacioAnterior := True; // Evita espacios iniciales
  for i := 1 to Length(cad) do
  begin
    if cad[i] <> ' ' then
    begin
      res := res + cad[i];
      espacioAnterior := False;
    end
    else
    begin
      if not espacioAnterior then
      begin
        res := res + ' ';
        espacioAnterior := True;
      end;
    end;
  end;

  // Si terminó en espacio, lo quitamos
  if (Length(res) > 0) and (res[Length(res)] = ' ') then
    Delete(res, Length(res), 1);

  NormalizarEspacios := res;
end;

// 28. Mostrar las palabras que empiezan con vocal de una frase
procedure MostrarPalabrasEmpiezanVocal(frase: String);
var
  pal: String;
  i: Integer;
  norm: String;
begin
  norm := NormalizarEspacios(frase);
  if Length(norm) = 0 then
    Exit;

  WriteLn('Palabras que empiezan con vocal:');
  pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if (Length(pal) > 0) and EsVocal(pal[1]) then
        WriteLn('  - ', pal);
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and EsVocal(pal[1]) then
    WriteLn('  - ', pal);
end;

// 29. Mostrar las palabras que terminan en consonante
procedure MostrarPalabrasTerminanConsonante(frase: String);
var
  pal: String;
  i: Integer;
  norm: String;
begin
  norm := NormalizarEspacios(frase);
  if Length(norm) = 0 then
    Exit;

  WriteLn('Palabras que terminan en consonante:');
  pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if (Length(pal) > 0) and EsConsonante(pal[Length(pal)]) then
        WriteLn('  - ', pal);
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and EsConsonante(pal[Length(pal)]) then
    WriteLn('  - ', pal);
end;

// 30. Intercalar dos cadenas carácter por carácter
function IntercalarCadenas(cad1, cad2: String): String;
var
  i, maxLen: Integer;
  res: String;
begin
  res := '';
  maxLen := Length(cad1);
  if Length(cad2) > maxLen then
    maxLen := Length(cad2);

  for i := 1 to maxLen do
  begin
    if i <= Length(cad1) then
      res := res + cad1[i];
    if i <= Length(cad2) then
      res := res + cad2[i];
  end;
  IntercalarCadenas := res;
end;

// 31. Determinar cuántas palabras con más de 5 letras hay en una oración
function ContarPalabrasMasDe5Letras(oracion: String): Integer;
var
  norm, pal: String;
  i, c: Integer;
begin
  norm := NormalizarEspacios(oracion);
  c := 0;
  pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if Length(pal) > 5 then
        c := c + 1;
      pal := '';
    end;
  end;
  if Length(pal) > 5 then
    c := c + 1;

  ContarPalabrasMasDe5Letras := c;
end;

// 32. Reemplazar todas las vocales por el carácter '*'
function ReemplazarVocalesPorAsterisco(cad: String): String;
var
  i: Integer;
  res: String;
begin
  res := '';
  for i := 1 to Length(cad) do
  begin
    if EsVocal(cad[i]) then
      res := res + '*'
    else
      res := res + cad[i];
  end;
  ReemplazarVocalesPorAsterisco := res;
end;

// 33. Crear una función que elimine acentos (á, é, í, ó, ú) de una cadena
function EliminarAcentos(cad: String): String;
const
  CON_ACENTO: array[1..10] of String = ('á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú');
  SIN_ACENTO: array[1..10] of String = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
var
  k: Integer;
begin
  for k := 1 to 10 do
    cad := StringReplace(cad, CON_ACENTO[k], SIN_ACENTO[k], [rfReplaceAll]);
  EliminarAcentos := cad;
end;

// 34. Mostrar la palabra más larga de una frase
function PalabraMasLarga(frase: String): String;
var
  norm, pal, mayor: String;
  i: Integer;
begin
  norm := NormalizarEspacios(frase);
  mayor := '';
  pal := '';
  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      pal := pal + norm[i]
    else
    begin
      if Length(pal) > Length(mayor) then
        mayor := pal;
      pal := '';
    end;
  end;
  if Length(pal) > Length(mayor) then
    mayor := pal;

  PalabraMasLarga := mayor;
end;

// 35. Mostrar la palabra más corta de una frase
function PalabraMasCorta(frase: String): String;
var
  norm, pal, menor: String;
  i: Integer;
begin
  norm := NormalizarEspacios(frase);
  menor := '';
  pal := '';
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

  PalabraMasCorta := menor;
end;

// 36. Contar cuántas palabras repetidas hay en un texto
function ContarPalabrasRepetidas(texto: String): Integer;
var
  norm, actual: String;
  palabras: array of String;
  i, j, n, repetidas: Integer;
  yaContada: Boolean;
begin
  norm := CadenaMinusculas(NormalizarEspacios(texto));
  SetLength(palabras, 0);
  actual := '';

  for i := 1 to Length(norm) do
  begin
    if norm[i] <> ' ' then
      actual := actual + norm[i]
    else
    begin
      if Length(actual) > 0 then
      begin
        SetLength(palabras, Length(palabras) + 1);
        palabras[High(palabras)] := actual;
        actual := '';
      end;
    end;
  end;
  if Length(actual) > 0 then
  begin
    SetLength(palabras, Length(palabras) + 1);
    palabras[High(palabras)] := actual;
  end;

  n := Length(palabras);
  repetidas := 0;

  for i := 0 to n - 1 do
  begin
    // Verificamos si ya apareció antes
    yaContada := False;
    for j := 0 to i - 1 do
    begin
      if palabras[i] = palabras[j] then
      begin
        yaContada := True;
        Break;
      end;
    end;

    // Si es la primera vez que la vemos, verificamos si se repite más adelante
    if not yaContada then
    begin
      for j := i + 1 to n - 1 do
      begin
        if palabras[i] = palabras[j] then
        begin
          repetidas := repetidas + 1;
          Break;
        end;
      end;
    end;
  end;

  ContarPalabrasRepetidas := repetidas;
end;

// 37. Verificar si una cadena solo contiene letras (sin números ni símbolos)
function SoloContieneLetras(cad: String): Boolean;
var
  i: Integer;
begin
  if Length(cad) = 0 then
  begin
    SoloContieneLetras := False;
    Exit;
  end;

  SoloContieneLetras := True;
  for i := 1 to Length(cad) do
  begin
    if not EsLetra(cad[i]) then
    begin
      SoloContieneLetras := False;
      Exit;
    end;
  end;
end;

// 38. Generar una nueva cadena con los caracteres únicos (sin repetir)
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
  CaracteresUnicos := res;
end;

// 39. Comprobar si dos cadenas son anagramas (mismas letras en distinto orden)
function SonAnagramas(cad1, cad2: String): Boolean;
var
  c1, c2: String;
  i, j: Integer;
  temp: Char;
begin
  c1 := '';
  c2 := '';

  // Extraemos solo letras en minúscula
  for i := 1 to Length(cad1) do
    if EsLetra(cad1[i]) then
      c1 := c1 + A_Minuscula(cad1[i]);

  for i := 1 to Length(cad2) do
    if EsLetra(cad2[i]) then
      c2 := c2 + A_Minuscula(cad2[i]);

  if Length(c1) <> Length(c2) then
  begin
    SonAnagramas := False;
    Exit;
  end;

  // Ordenamos ambas cadenas (Bubble sort)
  for i := 1 to Length(c1) - 1 do
    for j := i + 1 to Length(c1) do
      if c1[i] > c1[j] then
      begin
        temp := c1[i];
        c1[i] := c1[j];
        c1[j] := temp;
      end;

  for i := 1 to Length(c2) - 1 do
    for j := i + 1 to Length(c2) do
      if c2[i] > c2[j] then
      begin
        temp := c2[i];
        c2[i] := c2[j];
        c2[j] := temp;
      end;

  SonAnagramas := (c1 = c2);
end;

// 40. Mostrar de la cadena solo los caracteres de índice impar (1, 3, 5...)
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
  CaracteresIndiceImpar := res;
end;

end.
