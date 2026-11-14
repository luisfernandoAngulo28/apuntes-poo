# -*- coding: utf-8 -*-
"""
Script para actualizar data_practico09.py con el estilo de la docente:
  function NombreFuncion(cad:String; n,i:Byte):TipoRetorno;
  i:=1; while i<=n do begin ... i:=i+1; end;
"""
import sys, ast, os
sys.stdout.reconfigure(encoding='utf-8')

# Leer el archivo actual
ruta = 'd:/Introz2/practico07/data_practico09.py'
with open(ruta, 'r', encoding='utf-8') as f:
    contenido = f.read()

# Extraer la lista ejecutando el módulo
ns = {}
exec(contenido, ns)
ejercicios = ns['EJERCICIOS_P9_DATA']

# Definir los nuevos codigo_pascal y codigo_vcl para cada ejercicio
# Usando el estilo exacto de la docente M.Sc. Angélica Garzón

nuevos_codigos = {}

nuevos_codigos[1] = {
    "codigo_pascal": r"""// Ejercicio 1: Contar cuantas veces aparece una palabra dentro de un texto
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
    "codigo_vcl": r"""// Evento OnClick - Llamada con cad, n, i globales
procedure TForm1.MenuContarPalabraClick(Sender: TObject);
var textoEntrada:String;
begin
  textoEntrada:=InputBox('Buscar','Ingrese la palabra a contar',' ');
  Edit3.Text:=IntToStr(ContarPalabra(cad,n,i,textoEntrada))+' veces';
end;"""
}

nuevos_codigos[2] = {
    "codigo_pascal": r"""// Ejercicio 2: Eliminar signos de puntuacion del texto
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
    "codigo_vcl": r"""procedure TForm1.MenuQuitarSignosClick(Sender: TObject);
begin
  Edit3.Text:=QuitarSignos(cad,n,i);
end;"""
}

nuevos_codigos[3] = {
    "codigo_pascal": r"""// Ejercicio 3: Repetir una cadena N veces
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
    "codigo_vcl": r"""procedure TForm1.MenuRepetirCadenaClick(Sender: TObject);
var nVeces:Byte;
begin
  nVeces:=StrToIntDef(InputBox('Repetir','Cuantas veces?','3'),3);
  Edit3.Text:=RepetirCadena(cad,n,i,nVeces);
end;"""
}

nuevos_codigos[4] = {
    "codigo_pascal": r"""// Ejercicio 4: Mayuscula inicial en cada palabra (Title Case)
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
    "codigo_vcl": r"""procedure TForm1.MenuMayusculaInicialClick(Sender: TObject);
begin
  Edit3.Text:=MayusculaInicial(cad,n,i);
end;"""
}

nuevos_codigos[5] = {
    "codigo_pascal": r"""// Ejercicio 5: Contar letras mayusculas y minusculas
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
    "codigo_vcl": r"""procedure TForm1.MenuContarMayusMinusClick(Sender: TObject);
begin
  Edit3.Text:=ContarMayusMinus(cad,n,i);
end;"""
}

nuevos_codigos[6] = {
    "codigo_pascal": r"""// Ejercicio 6: Comparar dos cadenas alfabeticamente
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
    "codigo_vcl": r"""procedure TForm1.MenuCompararCadenasClick(Sender: TObject);
var cad2:String;
begin
  cad2:=InputBox('Comparar','Ingrese la segunda cadena',' ');
  Edit3.Text:=CompararCadenas(cad,cad2);
end;"""
}

nuevos_codigos[7] = {
    "codigo_pascal": r"""// Ejercicio 7: Analisis completo de frase
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
    "codigo_vcl": r"""procedure TForm1.MenuAnalizarFraseClick(Sender: TObject);
begin
  Edit3.Text:=AnalizarFrase(cad,n,i);
end;"""
}

nuevos_codigos[8] = {
    "codigo_pascal": r"""// Ejercicio 8: Extraer dominio de un correo electronico
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
    "codigo_vcl": r"""procedure TForm1.MenuExtraerDominioClick(Sender: TObject);
begin
  Edit3.Text:=ExtraerDominio(cad,n,i);
end;"""
}

nuevos_codigos[9] = {
    "codigo_pascal": r"""// Ejercicio 9: Eliminar los primeros nDel caracteres
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
    "codigo_vcl": r"""procedure TForm1.MenuEliminarPrimerosNClick(Sender: TObject);
var nDel:Byte;
begin
  nDel:=StrToIntDef(InputBox('Eliminar','Cuantos caracteres eliminar?','5'),5);
  Edit3.Text:=EliminarPrimerosN(cad,n,i,nDel);
end;"""
}

nuevos_codigos[10] = {
    "codigo_pascal": r"""// Ejercicio 10: Insertar una subcadena en una posicion dada
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
    "codigo_vcl": r"""procedure TForm1.MenuInsertarSubcadenaClick(Sender: TObject);
var sub:String; posIndex:Byte;
begin
  sub:=InputBox('Insertar','Subcadena a insertar',' ');
  posIndex:=StrToIntDef(InputBox('Posicion','En que posicion?','5'),5);
  Edit3.Text:=InsertarSubcadena(cad,sub,n,i,posIndex);
end;"""
}

nuevos_codigos[11] = {
    "codigo_pascal": r"""// Ejercicio 11: Unir dos cadenas en una sola
// cad1='Hola', cad2='Mundo' -> 'Hola Mundo'
function UnirCadenas(cad1,cad2:String):String;
begin
  if (cad1<>'') and (cad2<>'') then
    Result:=cad1+' '+cad2
  else
    Result:=cad1+cad2;
end;""",
    "codigo_vcl": r"""procedure TForm1.MenuUnirCadenasClick(Sender: TObject);
var cad2:String;
begin
  cad2:=InputBox('Unir','Ingrese la segunda cadena',' ');
  Edit3.Text:=UnirCadenas(cad,cad2);
end;"""
}

nuevos_codigos[12] = {
    "codigo_pascal": r"""// Ejercicio 12: Eliminar la palabra numero k
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
    "codigo_vcl": r"""procedure TForm1.MenuEliminarPalabraKClick(Sender: TObject);
var k:Byte;
begin
  k:=StrToIntDef(InputBox('Eliminar','Numero de palabra a eliminar?','2'),2);
  Edit3.Text:=EliminarPalabraK(cad,n,i,k);
end;"""
}

nuevos_codigos[13] = {
    "codigo_pascal": r"""// Ejercicio 13: Eliminar palabras que tengan delante una palabra con 'c'
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
    "codigo_vcl": r"""procedure TForm1.MenuElimPalDelanteDeC(Sender: TObject);
begin
  Edit3.Text:=EliminarPalabrasDelanteDeC(cad,n,i);
end;"""
}

nuevos_codigos[14] = {
    "codigo_pascal": r"""// Ejercicio 14: Determinar cuantas palabras existen en una cadena
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
    "codigo_vcl": r"""procedure TForm1.MenuCantidadPalabrasClick(Sender: TObject);
begin
  Edit3.Text:=IntToStr(CantidadPalabras(cad,n,i))+' palabras';
end;"""
}

nuevos_codigos[15] = {
    "codigo_pascal": r"""// Ejercicio 15: Invertir una cadena de caracteres
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
    "codigo_vcl": r"""procedure TForm1.MenuInvertirCadenaClick(Sender: TObject);
begin
  Edit3.Text:=InvertirCadena(cad,n,i);
end;"""
}

nuevos_codigos[16] = {
    "codigo_pascal": r"""// Ejercicio 16: Invertir la segunda palabra de una cadena
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
    "codigo_vcl": r"""procedure TForm1.MenuInvertirSegundaPalClick(Sender: TObject);
begin
  Edit3.Text:=InvertirSegundaPalabra(cad,n,i);
end;"""
}

nuevos_codigos[17] = {
    "codigo_pascal": r"""// Ejercicio 17: Convertir a mayuscula palabras de longitud impar con consonante 'c'
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
    "codigo_vcl": r"""procedure TForm1.MenuMayusPalImparConCClick(Sender: TObject);
begin
  Edit3.Text:=MayusculaPalabrasImparConC(cad,n,i);
end;"""
}

nuevos_codigos[18] = {
    "codigo_pascal": r"""// Ejercicio 18: Mezclar dos cadenas
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
    "codigo_vcl": r"""procedure TForm1.MenuMezclarCadenasClick(Sender: TObject);
var cad2:String;
begin
  cad2:=InputBox('Mezclar','Ingrese la segunda cadena',' ');
  Edit3.Text:='Mezcla: '+MezclarCadenas(cad,cad2)+
              ' | Intercalar: '+IntercalarCaracteres(cad,cad2,n,i);
end;"""
}

nuevos_codigos[19] = {
    "codigo_pascal": r"""// Ejercicio 19: Insercion ordenada de caracteres en tiempo real (sin burbuja)
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
    "codigo_vcl": r"""procedure TForm1.MenuCaracteresOrdenadosClick(Sender: TObject);
begin
  Edit3.Text:=CadenaCaracteresOrdenados(cad,n,i);
end;"""
}

nuevos_codigos[20] = {
    "codigo_pascal": r"""// Ejercicio 20: Insercion ordenada de palabras en tiempo real
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
    "codigo_vcl": r"""procedure TForm1.MenuOrdenarPalabrasClick(Sender: TObject);
begin
  Edit3.Text:=OrdenarPalabrasAlfabeticamente(cad,n,i);
end;"""
}

nuevos_codigos[21] = {
    "codigo_pascal": r"""// Ejercicio 21: Interseccion de dos conjuntos de caracteres (C = A inter B)
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
    "codigo_vcl": r"""procedure TForm1.MenuInterseccionConjuntosClick(Sender: TObject);
var cadB:String;
begin
  cadB:=InputBox('Interseccion','Ingrese el conjunto B',' ');
  Edit3.Text:=InterseccionConjuntos(cad,cadB,n,i);
end;"""
}

nuevos_codigos[22] = {
    "codigo_pascal": r"""// Ejercicio 22: Convertir un numero decimal a binario usando cadenas
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
    "codigo_vcl": r"""procedure TForm1.MenuDecimalABinarioClick(Sender: TObject);
var num:Integer;
begin
  num:=StrToIntDef(InputBox('Decimal a Binario','Ingrese el numero','10'),10);
  Edit3.Text:=IntToStr(num)+' en binario = '+DecimalABinario(num);
end;"""
}

nuevos_codigos[23] = {
    "codigo_pascal": r"""// Ejercicio 23: Contar la cantidad de veces que existen 2 vocales juntas
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
    "codigo_vcl": r"""procedure TForm1.MenuContarVocalesJuntasClick(Sender: TObject);
begin
  Edit3.Text:=IntToStr(ContarDosVocalesJuntas(cad,n,i))+' pares de vocales juntas';
end;"""
}

nuevos_codigos[24] = {
    "codigo_pascal": r"""// Ejercicio 24: Procedimiento para invertir una cadena
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
    "codigo_vcl": r"""procedure TForm1.MenuInvertirCadenaProcClick(Sender: TObject);
var invertida:String;
begin
  InvertirCadenaProc(cad,n,i,invertida);
  Edit3.Text:=invertida;
end;"""
}

nuevos_codigos[25] = {
    "codigo_pascal": r"""// Ejercicio 25: Ordenar conjunto de caracteres con metodo de burbuja
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
    "codigo_vcl": r"""procedure TForm1.MenuOrdenarBurbujaClick(Sender: TObject);
var cadTemp:String;
begin
  cadTemp:=cad;
  OrdenarBurbuja(cadTemp,n,i);
  Edit3.Text:=cadTemp;
end;"""
}

nuevos_codigos[26] = {
    "codigo_pascal": r"""// Ejercicio 26: Contar palabras que comienzan y terminan en vocal
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
    "codigo_vcl": r"""procedure TForm1.MenuPalabrasVocExtremosClick(Sender: TObject);
begin
  Edit3.Text:=IntToStr(ContarPalabrasVocalesExtremos(cad,n,i))+' palabras';
end;"""
}

nuevos_codigos[27] = {
    "codigo_pascal": r"""// Ejercicio 27: Eliminar consonantes de la ultima palabra
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
    "codigo_vcl": r"""procedure TForm1.MenuElimConsUltimaPalClick(Sender: TObject);
begin
  Edit3.Text:=EliminarConsonantesUltimaPal(cad,n,i);
end;"""
}

nuevos_codigos[28] = {
    "codigo_pascal": r"""// Ejercicio 28: Insertar una palabra a partir de la segunda palabra
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
    "codigo_vcl": r"""procedure TForm1.MenuInsertarTrasSegundaClick(Sender: TObject);
var palNueva:String;
begin
  palNueva:=InputBox('Insertar','Palabra a insertar despues de la 2da',' ');
  Edit3.Text:=InsertarTrasSegunda(cad,palNueva,n,i);
end;"""
}

nuevos_codigos[29] = {
    "codigo_pascal": r"""// Ejercicio 29: Mostrar caracteres en los indices pares
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
    "codigo_vcl": r"""procedure TForm1.MenuCaracteresParesClick(Sender: TObject);
begin
  Edit3.Text:=CaracteresIndicesPares(cad,n,i);
end;"""
}

nuevos_codigos[30] = {
    "codigo_pascal": r"""// Ejercicio 30: Eliminar la ultima palabra de la cadena
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
    "codigo_vcl": r"""procedure TForm1.MenuEliminarUltimaPalClick(Sender: TObject);
begin
  Edit3.Text:=EliminarUltimaPalabra(cad,n,i);
end;"""
}

nuevos_codigos[31] = {
    "codigo_pascal": r"""// Ejercicio 31: Verificar si la cadena es capicua / palindroma
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
    "codigo_vcl": r"""procedure TForm1.MenuEsCapicuaClick(Sender: TObject);
begin
  Edit3.Text:=MensajeCapicua(cad,n,i);
end;"""
}

# Ahora aplicar los cambios
for ej in ejercicios:
    num = ej["num"]
    if num in nuevos_codigos:
        ej["codigo_pascal"] = nuevos_codigos[num]["codigo_pascal"]
        ej["codigo_vcl"] = nuevos_codigos[num]["codigo_vcl"]

# Escribir el archivo actualizado
output_lines = []
output_lines.append('# -*- coding: utf-8 -*-')
output_lines.append('"""')
output_lines.append('Datos completos de los 31 ejercicios del Práctico #9 (Cadenas, Funciones y Procedimientos)')
output_lines.append('Materia: INF110 - Introducción a la Informática')
output_lines.append('Docente: M.Sc. Angélica Garzón Cuéllar - UAGRM')
output_lines.append('ESTILO: function NombreFuncion(cad:String; n,i:Byte):TipoRetorno;')
output_lines.append('"""')
output_lines.append('')
output_lines.append('EJERCICIOS_P9_DATA = [')

for idx, ej in enumerate(ejercicios):
    output_lines.append('    {')
    # Fields in order
    for key in ["num", "titulo", "tipo", "categoria", "analisis", "pseudo",
                "traza_headers", "traza_rows", "codigo_pascal", "codigo_vcl",
                "entrada_ejemplo", "salida_ejemplo", "extra_req", "extra_label", "extra_default"]:
        if key not in ej:
            continue
        val = ej[key]
        if key in ("pseudo", "codigo_pascal", "codigo_vcl", "analisis") and isinstance(val, str) and '\n' in val:
            # Use triple-quoted string
            output_lines.append(f'        "{key}": """{val}""",')
        elif isinstance(val, str):
            # Escape for repr
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            output_lines.append(f'        "{key}": "{escaped}",')
        elif isinstance(val, bool):
            output_lines.append(f'        "{key}": {str(val)},')
        elif isinstance(val, (int, float)):
            output_lines.append(f'        "{key}": {val},')
        elif isinstance(val, list):
            # Format list
            list_repr = repr(val)
            if len(list_repr) < 100:
                output_lines.append(f'        "{key}": {list_repr},')
            else:
                output_lines.append(f'        "{key}": [')
                for item in val:
                    output_lines.append(f'            {repr(item)},')
                output_lines.append(f'        ],')
    
    if idx < len(ejercicios) - 1:
        output_lines.append('    },')
    else:
        output_lines.append('    }')

output_lines.append(']')
output_lines.append('')

output_text = '\n'.join(output_lines)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(output_text)

print(f"Archivo actualizado exitosamente: {ruta}")
print(f"Total ejercicios: {len(ejercicios)}")
print(f"Tamaño: {len(output_text)} bytes")

# Verificar que todos tienen el estilo correcto
for ej in ejercicios:
    cod = ej.get("codigo_pascal", "")
    num = ej["num"]
    if "n,i:Byte" in cod or "n,i,k:Byte" in cod or "n,i,nVeces:Byte" in cod or "n,i,nDel:Byte" in cod or "n,i,posIndex:Byte" in cod or num in (6, 11, 22):
        print(f"  [OK] Ejercicio {num}: estilo docente")
    elif "var cad:String" in cod:
        print(f"  [OK] Ejercicio {num}: procedimiento con var")
    else:
        print(f"  [!!] Ejercicio {num}: REVISAR estilo")

