# -*- coding: utf-8 -*-
"""
Genera la unidad Delphi Cadena.pas completa para Delphi 12 Community Edition,
respetando exactamente los nombres de componentes, variables y estilo de la docente
que el usuario mostró en su captura y código.
"""

def generate_cadena_pas():
    code = '''unit Cadena;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.Menus, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    BTNCargar: TButton;
    Button2: TButton;
    Button1: TButton;
    MainMenu1: TMainMenu;
    Cadenas1: TMenuItem;
    
    // Submenús del MainMenu organizados por categorías
    MenuBasicos: TMenuItem;
    MenuContarCaracteres: TMenuItem;
    MenuPrimeraLetra: TMenuItem;
    MenuUltimaLetra: TMenuItem;
    MenuMayusculas: TMenuItem;
    Minuscula1: TMenuItem;
    MenuInvertir: TMenuItem;
    MenuConcatenar: TMenuItem;
    BuscarCaracter1: TMenuItem;
    MenuAscii: TMenuItem;

    MenuVocalesConsonantes: TMenuItem;
    Vocales1: TMenuItem;
    MenuConsonantes: TMenuItem;
    MenuCensurarVocales: TMenuItem;
    MenuQuitarAcentos: TMenuItem;

    MenuEspaciosModif: TMenuItem;
    Cargar1: TMenuItem;
    MenuPrimerosN: TMenuItem;
    MenuEstaVacia: TMenuItem;
    Cargar2: TMenuItem;
    MenuPalindroma: TMenuItem;
    MenuReemplazarLetra: TMenuItem;
    MenuEliminarLetra: TMenuItem;
    MenuNormalizar: TMenuItem;

    MenuPalabrasFrases: TMenuItem;
    MenuContarPalabras: TMenuItem;
    BuscarPalabra: TMenuItem;
    MenuOcurrPalabra: TMenuItem;
    MenuLineas: TMenuItem;
    MenuTipoContenido: TMenuItem;
    MenuContarDigitos: TMenuItem;
    MenuPrimeraPalabra: TMenuItem;
    MenuUltimaPalabra: TMenuItem;
    MenuEmpiezanVocal: TMenuItem;
    MenuTerminanConsonante: TMenuItem;
    MenuPalabrasMas5: TMenuItem;
    MenuPalabraMasLarga: TMenuItem;
    MenuPalabraMasCorta: TMenuItem;
    MenuPalabrasRepetidas: TMenuItem;

    MenuAvanzados: TMenuItem;
    MenuIntercalar: TMenuItem;
    MenuSoloLetras: TMenuItem;
    MenuCaracteresUnicos: TMenuItem;
    MenuAnagramas: TMenuItem;
    MenuIndiceImpar: TMenuItem;

    // Eventos principales del Formulario
    procedure BTNCargarClick(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);

    // Eventos para los 40 Ejercicios de Cadenas
    procedure MenuContarCaracteresClick(Sender: TObject);
    procedure MenuPrimeraLetraClick(Sender: TObject);
    procedure MenuUltimaLetraClick(Sender: TObject);
    procedure Vocales1Click(Sender: TObject);
    procedure MenuConsonantesClick(Sender: TObject);
    procedure MenuMayusculasClick(Sender: TObject);
    procedure Minuscula1Click(Sender: TObject);
    procedure MenuInvertirClick(Sender: TObject);
    procedure MenuConcatenarClick(Sender: TObject);
    procedure BuscarCaracter1Click(Sender: TObject);
    procedure Cargar1Click(Sender: TObject);
    procedure MenuPrimerosNClick(Sender: TObject);
    procedure MenuEstaVaciaClick(Sender: TObject);
    procedure MenuAsciiClick(Sender: TObject);
    procedure Cargar2Click(Sender: TObject);
    procedure MenuPalindromaClick(Sender: TObject);
    procedure MenuContarPalabrasClick(Sender: TObject);
    procedure BuscarPalabraClick(Sender: TObject);
    procedure MenuReemplazarLetraClick(Sender: TObject);
    procedure MenuEliminarLetraClick(Sender: TObject);
    procedure MenuOcurrPalabraClick(Sender: TObject);
    procedure MenuLineasClick(Sender: TObject);
    procedure MenuTipoContenidoClick(Sender: TObject);
    procedure MenuContarDigitosClick(Sender: TObject);
    procedure MenuPrimeraPalabraClick(Sender: TObject);
    procedure MenuUltimaPalabraClick(Sender: TObject);
    procedure MenuNormalizarClick(Sender: TObject);
    procedure MenuEmpiezanVocalClick(Sender: TObject);
    procedure MenuTerminanConsonanteClick(Sender: TObject);
    procedure MenuIntercalarClick(Sender: TObject);
    procedure MenuPalabrasMas5Click(Sender: TObject);
    procedure MenuCensurarVocalesClick(Sender: TObject);
    procedure MenuQuitarAcentosClick(Sender: TObject);
    procedure MenuPalabraMasLargaClick(Sender: TObject);
    procedure MenuPalabraMasCortaClick(Sender: TObject);
    procedure MenuPalabrasRepetidasClick(Sender: TObject);
    procedure MenuSoloLetrasClick(Sender: TObject);
    procedure MenuCaracteresUnicosClick(Sender: TObject);
    procedure MenuAnagramasClick(Sender: TObject);
    procedure MenuIndiceImparClick(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  // Variables globales (Estilo de Pizarra INF110)
  cad: String;
  n, i: Byte;

// =============================================================================
//      DECLARACIÓN DE LAS FUNCIONES Y PROCEDIMIENTOS MODULARES (PRACTICO 8)
// =============================================================================
function espacioEnBlanco(cad: string; n, i: byte): byte;
function cantidadMayusculas(cad: string; n, i: byte): byte;
function contadorVocales(cad: string; n, i: byte): byte;
function contadorConsonantes(cad: string; n, i: byte): byte;
function cadenaAMayusculas(cad: string; n, i: byte): string;
function cadenaAMinusculas(cad: string; n, i: byte): string;
function invertirCadenaMod(cad: string; n, i: byte): string;
function contarOcurrenciasLetraMod(cad: string; letra: char; n, i: byte): byte;
function eliminarEspaciosMod(cad: string; n, i: byte): string;
function primerosNMod(cad: string; cant: integer): string;
function estaVaciaMod(cad: string): boolean;
function contarDigitosMod(cad: string; n, i: byte): byte;
function normalizarEspaciosMod(cad: string): string;
function censurarVocalesMod(cad: string; n, i: byte): string;
function caracteresIndiceImparMod(cad: string; n, i: byte): string;
function esPalindromaMod(cad: string): boolean;
function contarPalabrasMod(frase: string): integer;
function extraerPrimeraPalabraMod(frase: string): string;
function extraerUltimaPalabraMod(frase: string): string;
function palabraMasLargaMod(frase: string): string;
function palabraMasCortaMod(frase: string): string;
function soloLetrasMod(cad: string): boolean;
function caracteresUnicosMod(cad: string): string;
function sonAnagramasMod(cad1, cad2: string): boolean;
function intercalarCadenasMod(cad1, cad2: string): string;

implementation

{$R *.dfm}

// =============================================================================
//                  IMPLEMENTACIÓN DE MÓDULOS DE CADENAS
// =============================================================================

// Ejercicio 11: Espacios en blanco
function espacioEnBlanco(cad: string; n, i: byte): byte;
var
  espacios: byte;
begin
  espacios := 0;
  i := 1;
  while i <= n do
  begin
    if cad[i] = ' ' then
      espacios := espacios + 1;
    i := i + 1;
  end;
  Result := espacios;
end;

// Ejercicio 15: Cantidad de mayúsculas
function cantidadMayusculas(cad: string; n, i: byte): byte;
const
  may: set of char = ['A'..'Z'];
var
  contadorMay: byte;
begin
  contadorMay := 0;
  i := 1;
  while i <= n do
  begin
    if cad[i] in may then
      contadorMay := contadorMay + 1;
    i := i + 1;
  end;
  Result := contadorMay;
end;

// Ejercicio 4: Contador de vocales
function contadorVocales(cad: string; n, i: byte): byte;
const
  voc: set of char = ['A', 'E', 'I', 'O', 'U'];
var
  conteo: byte;
begin
  conteo := 0;
  i := 1;
  while i <= n do
  begin
    if UpCase(cad[i]) in voc then
      conteo := conteo + 1;
    i := i + 1;
  end;
  Result := conteo;
end;

// Ejercicio 5: Contador de consonantes
function contadorConsonantes(cad: string; n, i: byte): byte;
const
  cons: set of char = ['A'..'Z'] - ['A', 'E', 'I', 'O', 'U'];
var
  conteo: byte;
begin
  conteo := 0;
  i := 1;
  while i <= n do
  begin
    if UpCase(cad[i]) in cons then
      conteo := conteo + 1;
    i := i + 1;
  end;
  Result := conteo;
end;

// Ejercicio 6: Cadena a mayúsculas
function cadenaAMayusculas(cad: string; n, i: byte): string;
var
  res: string;
begin
  res := '';
  i := 1;
  while i <= n do
  begin
    if (cad[i] >= 'a') and (cad[i] <= 'z') then
      res := res + Chr(Ord(cad[i]) - 32)
    else
      res := res + cad[i];
    i := i + 1;
  end;
  Result := res;
end;

// Ejercicio 7: Cadena a minúsculas
function cadenaAMinusculas(cad: string; n, i: byte): string;
var
  res: string;
begin
  res := '';
  i := 1;
  while i <= n do
  begin
    if (cad[i] >= 'A') and (cad[i] <= 'Z') then
      res := res + Chr(Ord(cad[i]) + 32)
    else
      res := res + cad[i];
    i := i + 1;
  end;
  Result := res;
end;

// Ejercicio 8: Invertir cadena
function invertirCadenaMod(cad: string; n, i: byte): string;
var
  res: string;
begin
  res := '';
  i := n;
  while i >= 1 do
  begin
    res := res + cad[i];
    i := i - 1;
  end;
  Result := res;
end;

// Ejercicio 10: Ocurrencias de una letra
function contarOcurrenciasLetraMod(cad: string; letra: char; n, i: byte): byte;
var
  c: byte;
begin
  c := 0;
  i := 1;
  while i <= n do
  begin
    if UpCase(cad[i]) = UpCase(letra) then
      c := c + 1;
    i := i + 1;
  end;
  Result := c;
end;

// Ejercicio 11 bis: Eliminar espacios
function eliminarEspaciosMod(cad: string; n, i: byte): string;
var
  res: string;
begin
  res := '';
  i := 1;
  while i <= n do
  begin
    if cad[i] <> ' ' then
      res := res + cad[i];
    i := i + 1;
  end;
  Result := res;
end;

// Ejercicio 12: Primeros n caracteres
function primerosNMod(cad: string; cant: integer): string;
var
  idx, limite: integer;
  res: string;
begin
  res := '';
  limite := cant;
  if limite > Length(cad) then
    limite := Length(cad);
  for idx := 1 to limite do
    res := res + cad[idx];
  Result := res;
end;

// Ejercicio 13: Determinar si está vacía
function estaVaciaMod(cad: string): boolean;
begin
  Result := (Length(Trim(cad)) = 0);
end;

// Ejercicio 16: Es palíndroma
function esPalindromaMod(cad: string): boolean;
var
  limpia: string;
  idx, j: integer;
begin
  limpia := '';
  for idx := 1 to Length(cad) do
    if cad[idx] <> ' ' then
      limpia := limpia + UpCase(cad[idx]);
  idx := 1;
  j := Length(limpia);
  Result := True;
  while idx < j do
  begin
    if limpia[idx] <> limpia[j] then
    begin
      Result := False;
      Exit;
    end;
    idx := idx + 1;
    j := j - 1;
  end;
end;

// Ejercicio 17: Contar palabras
function contarPalabrasMod(frase: string): integer;
var
  idx, c: integer;
  enPalabra: boolean;
begin
  c := 0;
  enPalabra := False;
  for idx := 1 to Length(frase) do
  begin
    if frase[idx] <> ' ' then
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
end;

// Ejercicio 24: Contar dígitos numéricos
function contarDigitosMod(cad: string; n, i: byte): byte;
const
  dig: set of char = ['0'..'9'];
var
  c: byte;
begin
  c := 0;
  i := 1;
  while i <= n do
  begin
    if cad[i] in dig then
      c := c + 1;
    i := i + 1;
  end;
  Result := c;
end;

// Ejercicio 25: Extraer primera palabra
function extraerPrimeraPalabraMod(frase: string): string;
var
  inicio, finP: integer;
begin
  inicio := 1;
  while (inicio <= Length(frase)) and (frase[inicio] = ' ') do
    inicio := inicio + 1;
  if inicio > Length(frase) then Exit('');
  finP := inicio;
  while (finP <= Length(frase)) and (frase[finP] <> ' ') do
    finP := finP + 1;
  Result := Copy(frase, inicio, finP - inicio);
end;

// Ejercicio 26: Extraer última palabra
function extraerUltimaPalabraMod(frase: string): string;
var
  finP, inicio: integer;
begin
  finP := Length(frase);
  while (finP >= 1) and (frase[finP] = ' ') do
    finP := finP - 1;
  if finP < 1 then Exit('');
  inicio := finP;
  while (inicio >= 1) and (frase[inicio] <> ' ') do
    inicio := inicio - 1;
  Result := Copy(frase, inicio + 1, finP - inicio);
end;

// Ejercicio 27: Normalizar espacios múltiples
function normalizarEspaciosMod(cad: string): string;
var
  idx: integer;
  res: string;
  espacioAnt: boolean;
begin
  res := '';
  espacioAnt := True;
  for idx := 1 to Length(cad) do
  begin
    if cad[idx] <> ' ' then
    begin
      res := res + cad[idx];
      espacioAnt := False;
    end
    else if not espacioAnt then
    begin
      res := res + ' ';
      espacioAnt := True;
    end;
  end;
  if (Length(res) > 0) and (res[Length(res)] = ' ') then
    Delete(res, Length(res), 1);
  Result := res;
end;

// Ejercicio 30: Intercalar dos cadenas
function intercalarCadenasMod(cad1, cad2: string): string;
var
  idx, maxLen: integer;
  res: string;
begin
  res := '';
  maxLen := Length(cad1);
  if Length(cad2) > maxLen then maxLen := Length(cad2);
  for idx := 1 to maxLen do
  begin
    if idx <= Length(cad1) then res := res + cad1[idx];
    if idx <= Length(cad2) then res := res + cad2[idx];
  end;
  Result := res;
end;

// Ejercicio 32: Censurar vocales con *
function censurarVocalesMod(cad: string; n, i: byte): string;
const
  voc: set of char = ['A', 'E', 'I', 'O', 'U'];
var
  res: string;
begin
  res := '';
  i := 1;
  while i <= n do
  begin
    if UpCase(cad[i]) in voc then
      res := res + '*'
    else
      res := res + cad[i];
    i := i + 1;
  end;
  Result := res;
end;

// Ejercicio 34: Palabra más larga
function palabraMasLargaMod(frase: string): string;
var
  norm, pal, mayor: string;
  idx: integer;
begin
  norm := normalizarEspaciosMod(frase);
  mayor := ''; pal := '';
  for idx := 1 to Length(norm) do
  begin
    if norm[idx] <> ' ' then
      pal := pal + norm[idx]
    else
    begin
      if Length(pal) > Length(mayor) then mayor := pal;
      pal := '';
    end;
  end;
  if Length(pal) > Length(mayor) then mayor := pal;
  Result := mayor;
end;

// Ejercicio 35: Palabra más corta
function palabraMasCortaMod(frase: string): string;
var
  norm, pal, menor: string;
  idx: integer;
begin
  norm := normalizarEspaciosMod(frase);
  menor := ''; pal := '';
  for idx := 1 to Length(norm) do
  begin
    if norm[idx] <> ' ' then
      pal := pal + norm[idx]
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
end;

// Ejercicio 37: Solo contiene letras
function soloLetrasMod(cad: string): boolean;
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
var
  idx: integer;
begin
  if Length(cad) = 0 then Exit(False);
  for idx := 1 to Length(cad) do
  begin
    if not (cad[idx] in letras) then
    begin
      Result := False;
      Exit;
    end;
  end;
  Result := True;
end;

// Ejercicio 38: Caracteres únicos
function caracteresUnicosMod(cad: string): string;
var
  idx: integer;
  res: string;
begin
  res := '';
  for idx := 1 to Length(cad) do
  begin
    if Pos(cad[idx], res) = 0 then
      res := res + cad[idx];
  end;
  Result := res;
end;

// Ejercicio 39: Son anagramas
function sonAnagramasMod(cad1, cad2: string): boolean;
var
  c1, c2: string;
  idx, j: integer;
  temp: char;
begin
  c1 := ''; c2 := '';
  for idx := 1 to Length(cad1) do
    if cad1[idx] in ['A'..'Z', 'a'..'z'] then c1 := c1 + LowerCase(cad1[idx]);
  for idx := 1 to Length(cad2) do
    if cad2[idx] in ['A'..'Z', 'a'..'z'] then c2 := c2 + LowerCase(cad2[idx]);
  if Length(c1) <> Length(c2) then Exit(False);
  for idx := 1 to Length(c1) - 1 do
    for j := idx + 1 to Length(c1) do
      if c1[idx] > c1[j] then begin temp := c1[idx]; c1[idx] := c1[j]; c1[j] := temp; end;
  for idx := 1 to Length(c2) - 1 do
    for j := idx + 1 to Length(c2) do
      if c2[idx] > c2[j] then begin temp := c2[idx]; c2[idx] := c2[j]; c2[j] := temp; end;
  Result := (c1 = c2);
end;

// Ejercicio 40: Caracteres de índice impar
function caracteresIndiceImparMod(cad: string; n, i: byte): string;
var
  res: string;
begin
  res := '';
  i := 1;
  while i <= n do
  begin
    res := res + cad[i];
    i := i + 2;
  end;
  Result := res;
end;

// =============================================================================
//                    EVENTOS DEL FORMULARIO TForm1
// =============================================================================

procedure TForm1.BTNCargarClick(Sender: TObject);
begin
  cad := Edit1.Text;
  ShowMessage('cadena de caracter registrado');
  Label5.Caption := 'cad=' + cad;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  n := Length(cad);
  Edit2.Text := IntToStr(n) + ' caracteres';
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  Close;
end;

// Ejercicio 1: Contar caracteres
procedure TForm1.MenuContarCaracteresClick(Sender: TObject);
begin
  n := Length(cad);
  Edit2.Text := IntToStr(n) + ' caracteres';
  Edit3.Text := 'Total: ' + IntToStr(n) + ' caracteres';
end;

// Ejercicio 2: Primera letra
procedure TForm1.MenuPrimeraLetraClick(Sender: TObject);
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
var
  idx: integer;
begin
  n := Length(cad);
  for idx := 1 to n do
  begin
    if cad[idx] in letras then
    begin
      Edit3.Text := 'Primera letra: ' + cad[idx];
      Exit;
    end;
  end;
  Edit3.Text := 'No contiene letras';
end;

// Ejercicio 3: Última letra
procedure TForm1.MenuUltimaLetraClick(Sender: TObject);
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
var
  idx: integer;
begin
  n := Length(cad);
  for idx := n downto 1 do
  begin
    if cad[idx] in letras then
    begin
      Edit3.Text := 'Ultima letra: ' + cad[idx];
      Exit;
    end;
  end;
  Edit3.Text := 'No contiene letras';
end;

// Ejercicio 4: Vocales
procedure TForm1.Vocales1Click(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := IntToStr(contadorVocales(cad, n, i)) + ' vocales';
end;

// Ejercicio 5: Consonantes
procedure TForm1.MenuConsonantesClick(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := IntToStr(contadorConsonantes(cad, n, i)) + ' consonantes';
end;

// Ejercicio 6: Mayúsculas
procedure TForm1.MenuMayusculasClick(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := cadenaAMayusculas(cad, n, i);
end;

// Ejercicio 7: Minúsculas
procedure TForm1.Minuscula1Click(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := cadenaAMinusculas(cad, n, i);
end;

// Ejercicio 8: Invertir
procedure TForm1.MenuInvertirClick(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := invertirCadenaMod(cad, n, i);
end;

// Ejercicio 9: Concatenar
procedure TForm1.MenuConcatenarClick(Sender: TObject);
var
  cad2: string;
begin
  cad2 := InputBox('Concatenar', 'Ingrese segunda cadena:', 'UAGRM');
  Edit3.Text := cad + ' ' + cad2;
end;

// Ejercicio 10: Ocurrencias de letra
procedure TForm1.BuscarCaracter1Click(Sender: TObject);
var
  letraStr: string;
begin
  letraStr := InputBox('Buscar Caracter', 'Caracter a contar:', 'a');
  if Length(letraStr) > 0 then
  begin
    n := Length(cad);
    Edit3.Text := 'La letra ' + letraStr[1] + ' aparece ' +
                  IntToStr(contarOcurrenciasLetraMod(cad, letraStr[1], n, i)) + ' veces';
  end;
end;

// Ejercicio 11: Espacios en blanco
procedure TForm1.Cargar1Click(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := IntToStr(espacioEnBlanco(cad, n, i)) + ' Espacio Blanco';
end;

// Ejercicio 12: Primeros N caracteres
procedure TForm1.MenuPrimerosNClick(Sender: TObject);
var
  cant: integer;
begin
  cant := StrToIntDef(InputBox('Primeros N', 'Cantidad de caracteres:', '5'), 0);
  Edit3.Text := primerosNMod(cad, cant);
end;

// Ejercicio 13: ¿Está vacía?
procedure TForm1.MenuEstaVaciaClick(Sender: TObject);
begin
  if estaVaciaMod(cad) then
    Edit3.Text := 'La cadena esta VACIA'
  else
    Edit3.Text := 'La cadena CONTIENE TEXTO';
end;

// Ejercicio 14: Códigos ASCII
procedure TForm1.MenuAsciiClick(Sender: TObject);
var
  idx: integer;
  info: string;
begin
  n := Length(cad);
  info := '';
  for idx := 1 to n do
    info := info + cad[idx] + '->' + IntToStr(Ord(cad[idx])) + '  ';
  Edit3.Text := info;
  ShowMessage('Codigos ASCII:' + #13#10 + info);
end;

// Ejercicio 15: Cantidad Mayúsculas
procedure TForm1.Cargar2Click(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := IntToStr(cantidadMayusculas(cad, n, i)) + ' Mayusculas';
end;

// Ejercicio 16: Palíndroma
procedure TForm1.MenuPalindromaClick(Sender: TObject);
begin
  if esPalindromaMod(cad) then
    Edit3.Text := 'SI es Palindroma'
  else
    Edit3.Text := 'NO es Palindroma';
end;

// Ejercicio 17: Contar palabras
procedure TForm1.MenuContarPalabrasClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(contarPalabrasMod(cad)) + ' palabras';
end;

// Ejercicio 18: Buscar palabra
procedure TForm1.BuscarPalabraClick(Sender: TObject);
var
  pal: string;
begin
  pal := InputBox('Buscar Palabra', 'Palabra a buscar:', 'Delphi');
  if Pos(UpperCase(pal), UpperCase(cad)) > 0 then
    Edit3.Text := 'SI existe la palabra "' + pal + '"'
  else
    Edit3.Text := 'NO existe la palabra "' + pal + '"';
end;

// Ejercicio 19: Reemplazar letra
procedure TForm1.MenuReemplazarLetraClick(Sender: TObject);
var
  vieja, nueva: string;
  idx: integer;
  res: string;
begin
  vieja := InputBox('Reemplazar', 'Letra a reemplazar:', 'a');
  nueva := InputBox('Reemplazar', 'Nueva letra:', 'o');
  if (Length(vieja) > 0) and (Length(nueva) > 0) then
  begin
    res := '';
    for idx := 1 to Length(cad) do
      if cad[idx] = vieja[1] then res := res + nueva[1] else res := res + cad[idx];
    Edit3.Text := res;
  end;
end;

// Ejercicio 20: Eliminar letra
procedure TForm1.MenuEliminarLetraClick(Sender: TObject);
var
  letraStr: string;
  idx: integer;
  res: string;
begin
  letraStr := InputBox('Eliminar Letra', 'Letra a eliminar:', 'e');
  if Length(letraStr) > 0 then
  begin
    res := '';
    for idx := 1 to Length(cad) do
      if UpCase(cad[idx]) <> UpCase(letraStr[1]) then res := res + cad[idx];
    Edit3.Text := res;
  end;
end;

// Ejercicio 21: Ocurrencias de palabra
procedure TForm1.MenuOcurrPalabraClick(Sender: TObject);
var
  pal, tMay, pMay: string;
  p, c: integer;
begin
  pal := InputBox('Ocurrencias Palabra', 'Palabra a contar:', 'Mundo');
  c := 0;
  tMay := UpperCase(cad);
  pMay := UpperCase(pal);
  p := Pos(pMay, tMay);
  while p > 0 do
  begin
    c := c + 1;
    Delete(tMay, 1, p + Length(pMay) - 1);
    p := Pos(pMay, tMay);
  end;
  Edit3.Text := 'La palabra "' + pal + '" aparece ' + IntToStr(c) + ' veces';
end;

// Ejercicio 22: Mostrar por línea
procedure TForm1.MenuLineasClick(Sender: TObject);
var
  idx: integer;
  res: string;
begin
  res := '';
  for idx := 1 to Length(cad) do
    res := res + '[' + IntToStr(idx) + ']: ' + cad[idx] + #13#10;
  ShowMessage('Caracteres por linea:' + #13#10 + res);
  Edit3.Text := 'Mostrado en mensaje emergente';
end;

// Ejercicio 23: Números o solo letras
procedure TForm1.MenuTipoContenidoClick(Sender: TObject);
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
  digitos: set of char = ['0'..'9'];
var
  idx: integer;
  tL, tD: boolean;
begin
  tL := False; tD := False;
  for idx := 1 to Length(cad) do
  begin
    if cad[idx] in letras then tL := True;
    if cad[idx] in digitos then tD := True;
  end;
  if tL and not tD then Edit3.Text := 'Solo letras'
  else if tD and not tL then Edit3.Text := 'Solo digitos'
  else if tL and tD then Edit3.Text := 'Alfanumerica (letras y numeros)'
  else Edit3.Text := 'Simbolos / Espacios';
end;

// Ejercicio 24: Contar dígitos
procedure TForm1.MenuContarDigitosClick(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := IntToStr(contarDigitosMod(cad, n, i)) + ' digitos numericos';
end;

// Ejercicio 25: Extraer primera palabra
procedure TForm1.MenuPrimeraPalabraClick(Sender: TObject);
begin
  Edit3.Text := 'Primera palabra: "' + extraerPrimeraPalabraMod(cad) + '"';
end;

// Ejercicio 26: Extraer última palabra
procedure TForm1.MenuUltimaPalabraClick(Sender: TObject);
begin
  Edit3.Text := 'Ultima palabra: "' + extraerUltimaPalabraMod(cad) + '"';
end;

// Ejercicio 27: Normalizar espacios
procedure TForm1.MenuNormalizarClick(Sender: TObject);
begin
  Edit3.Text := normalizarEspaciosMod(cad);
end;

// Ejercicio 28: Palabras que empiezan con vocal
procedure TForm1.MenuEmpiezanVocalClick(Sender: TObject);
const
  voc: set of char = ['A', 'E', 'I', 'O', 'U'];
var
  norm, pal, res: string;
  idx: integer;
begin
  norm := normalizarEspaciosMod(cad);
  pal := ''; res := '';
  for idx := 1 to Length(norm) do
  begin
    if norm[idx] <> ' ' then pal := pal + norm[idx]
    else
    begin
      if (Length(pal) > 0) and (UpCase(pal[1]) in voc) then res := res + pal + ', ';
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and (UpCase(pal[1]) in voc) then res := res + pal;
  Edit3.Text := 'Empiezan con vocal: ' + res;
end;

// Ejercicio 29: Palabras que terminan en consonante
procedure TForm1.MenuTerminanConsonanteClick(Sender: TObject);
const
  cons: set of char = ['A'..'Z'] - ['A', 'E', 'I', 'O', 'U'];
var
  norm, pal, res: string;
  idx: integer;
begin
  norm := normalizarEspaciosMod(cad);
  pal := ''; res := '';
  for idx := 1 to Length(norm) do
  begin
    if norm[idx] <> ' ' then pal := pal + norm[idx]
    else
    begin
      if (Length(pal) > 0) and (UpCase(pal[Length(pal)]) in cons) then res := res + pal + ', ';
      pal := '';
    end;
  end;
  if (Length(pal) > 0) and (UpCase(pal[Length(pal)]) in cons) then res := res + pal;
  Edit3.Text := 'Terminan en consonante: ' + res;
end;

// Ejercicio 30: Intercalar dos cadenas
procedure TForm1.MenuIntercalarClick(Sender: TObject);
var
  cad2: string;
begin
  cad2 := InputBox('Intercalar', 'Segunda cadena:', '12345');
  Edit3.Text := intercalarCadenasMod(cad, cad2);
end;

// Ejercicio 31: Palabras con más de 5 letras
procedure TForm1.MenuPalabrasMas5Click(Sender: TObject);
var
  norm, pal: string;
  idx, c: integer;
begin
  norm := normalizarEspaciosMod(cad);
  pal := ''; c := 0;
  for idx := 1 to Length(norm) do
  begin
    if norm[idx] <> ' ' then pal := pal + norm[idx]
    else
    begin
      if Length(pal) > 5 then c := c + 1;
      pal := '';
    end;
  end;
  if Length(pal) > 5 then c := c + 1;
  Edit3.Text := IntToStr(c) + ' palabras con mas de 5 letras';
end;

// Ejercicio 32: Reemplazar vocales por asterisco
procedure TForm1.MenuCensurarVocalesClick(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := censurarVocalesMod(cad, n, i);
end;

// Ejercicio 33: Eliminar acentos
procedure TForm1.MenuQuitarAcentosClick(Sender: TObject);
const
  CON_ACENTO: array[1..10] of String = ('á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú');
  SIN_ACENTO: array[1..10] of String = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
var
  k: integer;
  temp: string;
begin
  temp := cad;
  for k := 1 to 10 do
    temp := StringReplace(temp, CON_ACENTO[k], SIN_ACENTO[k], [rfReplaceAll]);
  Edit3.Text := temp;
end;

// Ejercicio 34: Palabra más larga
procedure TForm1.MenuPalabraMasLargaClick(Sender: TObject);
begin
  Edit3.Text := 'Palabra mas larga: "' + palabraMasLargaMod(cad) + '"';
end;

// Ejercicio 35: Palabra más corta
procedure TForm1.MenuPalabraMasCortaClick(Sender: TObject);
begin
  Edit3.Text := 'Palabra mas corta: "' + palabraMasCortaMod(cad) + '"';
end;

// Ejercicio 36: Palabras repetidas
procedure TForm1.MenuPalabrasRepetidasClick(Sender: TObject);
var
  norm, actual: string;
  palabras: array of string;
  idx, j, lenP, repetidas: integer;
  yaContada: boolean;
begin
  norm := LowerCase(normalizarEspaciosMod(cad));
  SetLength(palabras, 0);
  actual := '';
  for idx := 1 to Length(norm) do
  begin
    if norm[idx] <> ' ' then actual := actual + norm[idx]
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
  lenP := Length(palabras); repetidas := 0;
  for idx := 0 to lenP - 1 do
  begin
    yaContada := False;
    for j := 0 to idx - 1 do
      if palabras[idx] = palabras[j] then begin yaContada := True; Break; end;
    if not yaContada then
      for j := idx + 1 to lenP - 1 do
        if palabras[idx] = palabras[j] then begin repetidas := repetidas + 1; Break; end;
  end;
  Edit3.Text := IntToStr(repetidas) + ' palabras repetidas';
end;

// Ejercicio 37: Solo letras
procedure TForm1.MenuSoloLetrasClick(Sender: TObject);
begin
  if soloLetrasMod(cad) then
    Edit3.Text := 'SI: Solo contiene letras'
  else
    Edit3.Text := 'NO: Contiene otros caracteres';
end;

// Ejercicio 38: Caracteres únicos
procedure TForm1.MenuCaracteresUnicosClick(Sender: TObject);
begin
  Edit3.Text := caracteresUnicosMod(cad);
end;

// Ejercicio 39: Anagramas
procedure TForm1.MenuAnagramasClick(Sender: TObject);
var
  cad2: string;
begin
  cad2 := InputBox('Anagramas', 'Segunda palabra para comparar:', 'amor');
  if sonAnagramasMod(cad, cad2) then
    Edit3.Text := 'SI: Son anagramas'
  else
    Edit3.Text := 'NO: No son anagramas';
end;

// Ejercicio 40: Caracteres de índice impar
procedure TForm1.MenuIndiceImparClick(Sender: TObject);
begin
  n := Length(cad);
  Edit3.Text := caracteresIndiceImparMod(cad, n, i);
end;

end.
'''
    with open('Cadena.pas', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Cadena.pas generado exitosamente.")

if __name__ == '__main__':
    generate_cadena_pas()
