unit UnitPractico09;

{ ============================================================================
  UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO
  FACULTAD DE CIENCIAS DE LA COMPUTACION
  INGENIERIA INFORMATICA, SISTEMAS Y REDES
  MATERIA: INTRODUCCION A LA INFORMATICA (INF110) - Sem 2-2025
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
  PRACTICO # 9: CADENAS, FUNCIONES Y PROCEDIMIENTOS (31 EJERCICIOS)
  METODOLOGIA: cad:String; n,i:Byte  (n=longitud, i=indice)
  ============================================================================ }

{$mode objfpc}{$H+}

interface

uses
  SysUtils;

// =============================================================================
//                    DECLARACIÓN DE LAS 31 FUNCIONES/PROCEDIMIENTOS
//                    Metodología: (cad:String; n,i:Byte)
// =============================================================================

// 1. Contar cuántas veces aparece una palabra dentro de un texto
function ContarPalabra(cad:String; n,i:Byte; palBuscada:String):Byte;

// 2. Eliminar signos de puntuación del texto
function QuitarSignos(cad:String; n,i:Byte):String;

// 3. Repetir una cadena N veces
function RepetirCadena(cad:String; n,i,nVeces:Byte):String;

// 4. Mayúscula inicial en cada palabra
function MayusculaInicial(cad:String; n,i:Byte):String;

// 5. Contar letras mayúsculas y minúsculas
function ContarMayusMinus(cad:String; n,i:Byte):String;
procedure ContarMayusMinusProc(cad:String; n,i:Byte; var may,min:Byte);

// 6. Comparar dos cadenas alfabéticamente
function CompararCadenas(cad1,cad2:String):String;

// 7. Análisis completo de frase (palabras, letras, vocales, consonantes, may, min)
function ContarPalabras(cad:String; n,i:Byte):Byte;
function ContarLetrasTotales(cad:String; n,i:Byte):Byte;
function ContarVocalesP9(cad:String; n,i:Byte):Byte;
function ContarConsonantesP9(cad:String; n,i:Byte):Byte;
function ContarMayusculas(cad:String; n,i:Byte):Byte;
function ContarMinusculas(cad:String; n,i:Byte):Byte;
function AnalizarFrase(cad:String; n,i:Byte):String;

// 8. Extraer dominio de un correo electrónico
function ExtraerDominio(cad:String; n,i:Byte):String;

// 9. Eliminar los primeros nDel caracteres
function EliminarPrimerosN(cad:String; n,i,nDel:Byte):String;

// 10. Insertar una subcadena en una posición dada
function InsertarSubcadena(cad,sub:String; n,i,posIndex:Byte):String;

// 11. Unir dos cadenas en una sola
function UnirCadenas(cad1,cad2:String):String;

// 12. Eliminar la palabra número k
function EliminarPalabraK(cad:String; n,i,k:Byte):String;

// 13. Eliminar palabras que tengan delante una palabra con la consonante 'c'
function EliminarPalabrasDelanteDeC(cad:String; n,i:Byte):String;

// 14. Determinar cuántas palabras existen en una cadena
function CantidadPalabras(cad:String; n,i:Byte):Byte;

// 15. Invertir una cadena de caracteres
function InvertirCadena(cad:String; n,i:Byte):String;

// 16. Invertir la segunda palabra de una cadena
function InvertirSegundaPalabra(cad:String; n,i:Byte):String;

// 17. Convertir a mayúscula palabras de longitud impar con consonante 'c'
function MayusculaPalabrasImparConC(cad:String; n,i:Byte):String;

// 18. Mezclar dos cadenas (cad1=ana, cad2=jose -> anajose)
function MezclarCadenas(cad1,cad2:String):String;
function IntercalarCaracteres(cad1,cad2:String; n,i:Byte):String;

// 19. Inserción ordenada de caracteres en tiempo real
function CadenaCaracteresOrdenados(cad:String; n,i:Byte):String;

// 20. Inserción ordenada de palabras en tiempo real
function OrdenarPalabrasAlfabeticamente(cad:String; n,i:Byte):String;

// 21. Intersección de dos conjuntos de caracteres (C = A ∩ B)
function InterseccionConjuntos(cadA,cadB:String; n,i:Byte):String;

// 22. Convertir un número decimal a binario usando cadenas
function DecimalABinario(num:Integer):String;

// 23. Contar la cantidad de veces que existen 2 vocales juntas
function ContarDosVocalesJuntas(cad:String; n,i:Byte):Byte;

// 24. Procedimiento para invertir una cadena
procedure InvertirCadenaProc(cad:String; n,i:Byte; var invertida:String);

// 25. Ordenar conjunto de caracteres con método de burbuja
procedure OrdenarBurbuja(var cad:String; n,i:Byte);

// 26. Contar palabras que comienzan y terminan en vocal
function ContarPalabrasVocalesExtremos(cad:String; n,i:Byte):Byte;

// 27. Eliminar consonantes de la última palabra
function EliminarConsonantesUltimaPal(cad:String; n,i:Byte):String;

// 28. Insertar una palabra a partir de la segunda palabra
function InsertarTrasSegunda(cad,palNueva:String; n,i:Byte):String;

// 29. Mostrar caracteres en los índices pares
function CaracteresIndicesPares(cad:String; n,i:Byte):String;

// 30. Eliminar la última palabra de la cadena
function EliminarUltimaPalabra(cad:String; n,i:Byte):String;

// 31. Verificar si la cadena es capicúa / palíndroma
function EsCapicua(cad:String; n,i:Byte):Boolean;
function MensajeCapicua(cad:String; n,i:Byte):String;

implementation

// =============================================================================
//                   IMPLEMENTACIÓN DE LAS 31 FUNCIONES
//                   Estilo: (cad:String; n,i:Byte)
//                   while i<=n do begin ... i:=i+1; end;
// =============================================================================

// -----------------------------------------------------------------------------
// 1. Contar cuántas veces aparece una palabra dentro de un texto
// Ejemplo: cad='hola mundo hola', palBuscada='hola' -> 2
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 2. Eliminar signos de puntuación del texto
// Ejemplo: cad='Hola, mundo!' -> 'Hola mundo'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 3. Repetir una cadena N veces
// Ejemplo: cad='Hola', nVeces=3 -> 'HolaHolaHola'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 4. Mayúscula inicial en cada palabra (Title Case)
// Ejemplo: cad='hola mundo' -> 'Hola Mundo'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 5. Contar letras mayúsculas y minúsculas
// Ejemplo: cad='Hola Mundo' -> 'Mayusculas: 2, Minusculas: 8'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 6. Comparar dos cadenas alfabéticamente
// Ejemplo: cad1='Ana', cad2='Pedro' -> '"Ana" va antes que "Pedro"'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 7. Análisis completo de frase
// Sub-funciones individuales con (cad:String; n,i:Byte)
// -----------------------------------------------------------------------------
function ContarPalabras(cad:String; n,i:Byte):Byte;
var
  cantPal:Byte;
  enPalabra:Boolean;
begin
  cantPal:=0;
  enPalabra:=false;
  i:=1;
  while i<=n do begin
    if cad[i]<>' ' then begin
      if enPalabra=false then begin
        cantPal:=cantPal+1;
        enPalabra:=true;
      end;
    end else begin
      enPalabra:=false;
    end;
    i:=i+1;
  end;
  Result:=cantPal;
end;

function ContarLetrasTotales(cad:String; n,i:Byte):Byte;
const letras:set of char=['A'..'Z','a'..'z'];
var contador:Byte;
begin
  contador:=0;
  i:=1;
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
  contador:=0;
  i:=1;
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
  contador:=0;
  i:=1;
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
  contador:=0;
  i:=1;
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
  contador:=0;
  i:=1;
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
end;

// -----------------------------------------------------------------------------
// 8. Extraer dominio de un correo electrónico
// Ejemplo: cad='alumno@uagrm.edu.bo' -> 'uagrm.edu.bo'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 9. Eliminar los primeros nDel caracteres
// Ejemplo: cad='Hola Mundo', nDel=5 -> 'Mundo'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 10. Insertar una subcadena en una posición dada
// Ejemplo: cad='Hola Mundo', sub=' Cruel', posIndex=5 -> 'Hola Cruel Mundo'
// -----------------------------------------------------------------------------
function InsertarSubcadena(cad,sub:String; n,i,posIndex:Byte):String;
var
  res:String;
  j,nSub:Byte;
begin
  res:='';
  nSub:=Length(sub);
  if posIndex<=1 then begin
    // Insertar al inicio
    j:=1;
    while j<=nSub do begin
      res:=res+sub[j];
      j:=j+1;
    end;
    i:=1;
    while i<=n do begin
      res:=res+cad[i];
      i:=i+1;
    end;
  end else if posIndex>n then begin
    // Insertar al final
    i:=1;
    while i<=n do begin
      res:=res+cad[i];
      i:=i+1;
    end;
    j:=1;
    while j<=nSub do begin
      res:=res+sub[j];
      j:=j+1;
    end;
  end else begin
    // Insertar en la posición indicada
    i:=1;
    while i<posIndex do begin
      res:=res+cad[i];
      i:=i+1;
    end;
    j:=1;
    while j<=nSub do begin
      res:=res+sub[j];
      j:=j+1;
    end;
    while i<=n do begin
      res:=res+cad[i];
      i:=i+1;
    end;
  end;
  Result:=res;
end;

// -----------------------------------------------------------------------------
// 11. Unir dos cadenas en una sola
// Ejemplo: cad1='Hola', cad2='Mundo' -> 'Hola Mundo'
// -----------------------------------------------------------------------------
function UnirCadenas(cad1,cad2:String):String;
begin
  if (cad1<>'') and (cad2<>'') then
    Result:=cad1+' '+cad2
  else
    Result:=cad1+cad2;
end;

// -----------------------------------------------------------------------------
// 12. Eliminar la palabra número k
// Ejemplo: cad='Hola mundo cruel', k=2 -> 'Hola cruel'
// -----------------------------------------------------------------------------
function EliminarPalabraK(cad:String; n,i,k:Byte):String;
var
  pal,res:String;
  numPal:Byte;
begin
  i:=1;
  numPal:=0;
  res:='';
  while i<=n do begin
    // Saltar espacios
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    // Extraer palabra
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
end;

// -----------------------------------------------------------------------------
// 13. Eliminar palabras que tengan delante una palabra con la consonante 'c'
// Ejemplo: cad='la casa bonita' -> 'la casa' (bonita se elimina, va despues de casa)
// -----------------------------------------------------------------------------
function EliminarPalabrasDelanteDeC(cad:String; n,i:Byte):String;
const
  letras:set of char=['A'..'Z','a'..'z'];
  voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
  teniaCAnterior:Boolean;
  tieneC:Boolean;
begin
  // Extraer todas las palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;

  // Reconstruir sin las palabras que van despues de una con 'c'
  res:='';
  j:=1;
  while j<=totalP do begin
    teniaCAnterior:=false;
    if j>1 then begin
      // Verificar si la palabra anterior contiene 'c' o 'C'
      tieneC:=false;
      k:=1;
      while k<=Length(palabras[j-1]) do begin
        if (UpCase(palabras[j-1][k])='C') and (palabras[j-1][k] in letras) and not (palabras[j-1][k] in voc) then begin
          tieneC:=true;
        end;
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
end;

// -----------------------------------------------------------------------------
// 14. Determinar cuántas palabras existen en una cadena
// Ejemplo: cad='Hola mundo cruel' -> 3
// -----------------------------------------------------------------------------
function CantidadPalabras(cad:String; n,i:Byte):Byte;
var
  cantPal:Byte;
  enPalabra:Boolean;
begin
  cantPal:=0;
  enPalabra:=false;
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

// -----------------------------------------------------------------------------
// 15. Invertir una cadena de caracteres
// Ejemplo: cad='Hola' -> 'aloH'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 16. Invertir la segunda palabra de una cadena
// Ejemplo: cad='Hola Mundo cruel' -> 'Hola odnuM cruel'
// -----------------------------------------------------------------------------
function InvertirSegundaPalabra(cad:String; n,i:Byte):String;
var
  pal,res,invertida:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  // Extraer palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;

  // Invertir la segunda palabra
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
end;

// -----------------------------------------------------------------------------
// 17. Convertir a mayúscula palabras de longitud impar con consonante 'c'
// Ejemplo: cad='casa color bonita' -> 'CASA color bonita' (casa=4 par, NO; color=5 impar y tiene c -> MAYUS)
// -----------------------------------------------------------------------------
function MayusculaPalabrasImparConC(cad:String; n,i:Byte):String;
const
  letras:set of char=['A'..'Z','a'..'z'];
  voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
  esImpar,tieneCFlag:Boolean;
begin
  // Extraer palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;

  // Procesar cada palabra
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
end;

// -----------------------------------------------------------------------------
// 18. Mezclar dos cadenas
// MezclarCadenas: cad1+cad2 concatenado
// IntercalarCaracteres: intercalar caracter a caracter
// Ejemplo: cad1='abc', cad2='123' -> 'a1b2c3'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 19. Inserción ordenada de caracteres en tiempo real (sin burbuja)
// Ejemplo: cad='dcba' -> 'abcd'
// -----------------------------------------------------------------------------
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
      // Insertar c en la posición correcta dentro de res
      insertado:=false;
      nRes:=Length(res);
      j:=1;
      while (j<=nRes) and (insertado=false) do begin
        if c<res[j] then begin
          // Insertar antes de j
          temp:='';
          // copiar 1..j-1
          if j>1 then begin
            temp:=Copy(res,1,j-1);
          end;
          temp:=temp+c;
          temp:=temp+Copy(res,j,nRes-j+1);
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
end;

// -----------------------------------------------------------------------------
// 20. Inserción ordenada de palabras en tiempo real
// Ejemplo: cad='banana apple cherry' -> 'apple banana cherry'
// -----------------------------------------------------------------------------
function OrdenarPalabrasAlfabeticamente(cad:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  // Extraer palabras e insertar en orden
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      // Inserción ordenada
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

  // Reconstruir
  res:='';
  j:=1;
  while j<=totalP do begin
    if res<>'' then res:=res+' ';
    res:=res+palabras[j];
    j:=j+1;
  end;
  Result:=res;
end;

// -----------------------------------------------------------------------------
// 21. Intersección de dos conjuntos de caracteres (C = A ∩ B)
// Ejemplo: cadA='abcde', cadB='cdefg' -> '{c, d, e}'
// -----------------------------------------------------------------------------
function InterseccionConjuntos(cadA,cadB:String; n,i:Byte):String;
var
  setA,setB,setC:set of Char;
  ch:Char;
  res:String;
  nA,nB:Byte;
begin
  setA:=[];
  setB:=[];
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
end;

// -----------------------------------------------------------------------------
// 22. Convertir un número decimal a binario usando cadenas
// Ejemplo: num=10 -> '1010'
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 23. Contar la cantidad de veces que existen 2 vocales juntas
// Ejemplo: cad='bueno aeiou' -> 5
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 24. Procedimiento para invertir una cadena
// Ejemplo: cad='Hola' -> invertida='aloH'
// -----------------------------------------------------------------------------
procedure InvertirCadenaProc(cad:String; n,i:Byte; var invertida:String);
begin
  invertida:='';
  i:=n;
  while i>=1 do begin
    invertida:=invertida+cad[i];
    if i=0 then Break;
    i:=i-1;
  end;
end;

// -----------------------------------------------------------------------------
// 25. Ordenar conjunto de caracteres con método de burbuja
// Ejemplo: cad='dcba' -> cad='abcd'
// -----------------------------------------------------------------------------
procedure OrdenarBurbuja(var cad:String; n,i:Byte);
var
  j:Byte;
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
end;

// -----------------------------------------------------------------------------
// 26. Contar palabras que comienzan y terminan en vocal
// Ejemplo: cad='ala este gol uno' -> 3 (ala, este, uno)
// -----------------------------------------------------------------------------
function ContarPalabrasVocalesExtremos(cad:String; n,i:Byte):Byte;
const voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal:String;
  contador:Byte;
  nPal:Byte;
begin
  contador:=0;
  i:=1;
  while i<=n do begin
    // Saltar espacios
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    // Extraer palabra
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
end;

// -----------------------------------------------------------------------------
// 27. Eliminar consonantes de la última palabra
// Ejemplo: cad='Hola Mundo' -> 'Hola uo'
// -----------------------------------------------------------------------------
function EliminarConsonantesUltimaPal(cad:String; n,i:Byte):String;
const
  letras:set of char=['A'..'Z','a'..'z'];
  voc:set of char=['A','E','I','O','U','a','e','i','o','u'];
var
  pal,res,ultLimpia:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  // Extraer palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;

  // Eliminar consonantes de la última palabra
  if totalP>=1 then begin
    ultLimpia:='';
    j:=1;
    while j<=Length(palabras[totalP]) do begin
      if not ((palabras[totalP][j] in letras) and not (palabras[totalP][j] in voc)) then
        ultLimpia:=ultLimpia+palabras[totalP][j];
      j:=j+1;
    end;
    palabras[totalP]:=ultLimpia;
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
end;

// -----------------------------------------------------------------------------
// 28. Insertar una palabra a partir de la segunda palabra
// Ejemplo: cad='Hola Mundo Cruel', palNueva='Bello' -> 'Hola Mundo Bello Cruel'
// -----------------------------------------------------------------------------
function InsertarTrasSegunda(cad,palNueva:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j,k:Byte;
  palabras:array[1..100] of String;
begin
  // Extraer palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;

  // Insertar palNueva despues de la segunda
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

  // Reconstruir
  res:='';
  j:=1;
  while j<=totalP do begin
    if res<>'' then res:=res+' ';
    res:=res+palabras[j];
    j:=j+1;
  end;
  Result:=res;
end;

// -----------------------------------------------------------------------------
// 29. Mostrar caracteres en los índices pares
// Ejemplo: cad='Hola Mundo' -> 'oaMno' (pos 2,4,6,8,10)
// -----------------------------------------------------------------------------
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
end;

// -----------------------------------------------------------------------------
// 30. Eliminar la última palabra de la cadena
// Ejemplo: cad='Hola Mundo Cruel' -> 'Hola Mundo'
// -----------------------------------------------------------------------------
function EliminarUltimaPalabra(cad:String; n,i:Byte):String;
var
  pal,res:String;
  totalP,j:Byte;
  palabras:array[1..100] of String;
begin
  // Extraer palabras
  i:=1; totalP:=0;
  while i<=n do begin
    while (i<=n) and (cad[i]=' ') do
      i:=i+1;
    pal:='';
    while (i<=n) and (cad[i]<>' ') do begin
      pal:=pal+cad[i];
      i:=i+1;
    end;
    if pal<>'' then begin
      totalP:=totalP+1;
      palabras[totalP]:=pal;
    end;
  end;

  // Reconstruir sin la última
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
end;

// -----------------------------------------------------------------------------
// 31. Verificar si la cadena es capicúa / palíndroma
// Ejemplo: cad='anilina' -> True
// -----------------------------------------------------------------------------
function EsCapicua(cad:String; n,i:Byte):Boolean;
var
  limpia:String;
  j:Byte;
  nLimpia:Byte;
begin
  // Limpiar: quitar espacios, pasar a mayúsculas
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
end;

end.
