unit Cadena;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.Menus, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    BTNCargar: TButton;
    Edit1: TEdit;
    Button2: TButton;
    Edit2: TEdit;
    MainMenu1: TMainMenu;
    Cadenas1: TMenuItem;
    Cargar1: TMenuItem;
    Cargar2: TMenuItem;
    Button1: TButton;
    Edit3: TEdit;
    Minuscula1: TMenuItem;
    Vocales1: TMenuItem;
    BuscarCaracter1: TMenuItem;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    PracticoCadena1al101: TMenuItem;
    N1ContarCaracteres1: TMenuItem;
    Label7: TLabel;
    N2MostrarPrimeraLetra1: TMenuItem;
    ultimaLtr1: TMenuItem;
    contarvc2: TMenuItem;
    buscarunaletraylasnveces1: TMenuItem;
    BuscarCaracterNseRepite1: TMenuItem;
    EspaciosModificacin11201: TMenuItem;
    N11Eliminarespaciosenblanco1: TMenuItem;
    N12Primerosncaracteres1: TMenuItem;
    N13Determinarsiestvaca1: TMenuItem;
    N14MostrarcdigosASCII1: TMenuItem;
    N15Contarmaysculas1: TMenuItem;
    N16Espalndroma1: TMenuItem;
    ContarVocalesJuntas1: TMenuItem;
    
    // Opciones del Menú para los ejercicios de clase y tarea
    MenuEjerciciosClase1: TMenuItem;
    N1ContarPalabrasCadena1: TMenuItem;
    N2ContarPalabras2VocalesJuntas1: TMenuItem;
    N3MostrarIndicesImpares1: TMenuItem;
    N4ContarConsonantes1: TMenuItem;
    MenuTareaViernes1: TMenuItem;
    T1BuscarCaracterPosiciones1: TMenuItem;
    T2ContarRepeticiones1: TMenuItem;

    procedure BTNCargarClick(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Cargar1Click(Sender: TObject);
    procedure Cargar2Click(Sender: TObject);
    procedure Vocales1Click(Sender: TObject);
    procedure N1ContarCaracteres1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure N2MostrarPrimeraLetra1Click(Sender: TObject);
    procedure ultimaLtr1Click(Sender: TObject);
    procedure contarvc2Click(Sender: TObject);
    procedure BuscarCaracter1Click(Sender: TObject);
    procedure buscarunaletraylasnveces1Click(Sender: TObject);
    procedure BuscarCaracterNseRepite1Click(Sender: TObject);
    procedure N11Eliminarespaciosenblanco1Click(Sender: TObject);
    procedure N12Primerosncaracteres1Click(Sender: TObject);
    procedure N13Determinarsiestvaca1Click(Sender: TObject);
    procedure N14MostrarcdigosASCII1Click(Sender: TObject);
    procedure N15Contarmaysculas1Click(Sender: TObject);
    procedure N16Espalndroma1Click(Sender: TObject);
    procedure ContarVocalesJuntas1Click(Sender: TObject);
    
    // Procedimientos de los nuevos ejercicios
    procedure N1ContarPalabrasCadena1Click(Sender: TObject);
    procedure N2ContarPalabras2VocalesJuntas1Click(Sender: TObject);
    procedure N3MostrarIndicesImpares1Click(Sender: TObject);
    procedure N4ContarConsonantes1Click(Sender: TObject);
    procedure T1BuscarCaracterPosiciones1Click(Sender: TObject);
    procedure T2ContarRepeticiones1Click(Sender: TObject);
    // Menú de Ordenamiento (Avanzado esta semana - Ing. Angélica Garzón)
    Ordenamiento1: TMenuItem;
    Ascendente1: TMenuItem;
    Descendente1: TMenuItem;
    OrdenarUltimaPalabra1: TMenuItem;
    InvertirSegundaPalabra1: TMenuItem;
    OrdenarSegundaPalabra1: TMenuItem;

    procedure Ascendente1Click(Sender: TObject);
    procedure Descendente1Click(Sender: TObject);
    procedure OrdenarUltimaPalabra1Click(Sender: TObject);
    procedure InvertirSegundaPalabra1Click(Sender: TObject);
    procedure OrdenarSegundaPalabra1Click(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  // Variables globales: metodología de la Ing. Angélica Garzón
  // cad : cadena de entrada registrada
  // n   : longitud de la cadena calculada con Length(cad)
  // i   : índice / posición para recorrer desde 1 hasta n
  cad: String;
  n, i: Byte;

// =============================================================================
//      DECLARACIÓN DE LAS FUNCIONES DE CADENA (METODOLOGÍA DE LA DOCENTE)
// =============================================================================

function espacioEnBlanco(cad: string; n, i: byte): byte;
function cantidadMayusculas(cad: string; n, i: byte): byte;
function BuscarCaracterPosicion(cad: String; i, n: Byte; buscarcar: Char): Byte;
function BuscarCaracterNPosicion(cad: String; i, n: Byte; buscarcar: Char): String;
function BuscarCaracterNRepite(cad: String; i, n: Byte; buscarcar: Char): byte;

// Los 4 Ejercicios de Clase (21 de Octubre)
function contarPalabras(cad: string; n, i: byte): byte;
function contarVocalesJuntas(Cad: string; n, i: Byte): Byte;
function contarPalabras2VocalesJuntas(cad: string; n, i: byte): byte;
function mostrarCaracteresIndicesImpares(cad: string; n, i: byte): string;
function contarConsonantes(cad: string; n, i: byte): byte;

// Práctico #8 de la materia
function contarCaracteres(cad: string; n, i: Byte): byte;
procedure MostrarPrimeraLetra(cad: string; var letra: Char);
function mostrarPrimerCaracterF(cad: string; n, i: byte): Char;
function mostrarprimercaracter(cad: string; n, i: byte): Char;
function ultimaletra(cad: string; n, i: byte): char;
function contarvocal(cad: string; n, i: byte): integer;
function EliminarEspacios(cad: String; n, i: Byte): String;
function PrimerosNCaracteres(cad: string; nCant: Cardinal; n, i: Byte): string;
function EstaVacia(cad: String): Boolean;
procedure MostrarCodigosASCII(cad: String; var salida: String; n, i: Byte);
function ContarMayusculas(cad: string; n, i: Byte): Integer;
function EsPalindroma(cad: string; n, i: byte): Boolean;
function contadorVocales(cad: string; n, i: Byte): byte;

implementation

{$R *.dfm}

// =============================================================================
//                   IMPLEMENTACIÓN DE FUNCIONES DE CADENA
// =============================================================================

// Espacios en blanco: n entra con el valor de la longitud
function espacioEnBlanco(cad: string; n, i: byte): byte;
var espacioEnBlancoCont: byte;
begin
  espacioEnBlancoCont := 0; 
  i := 1;
  while i <= n do begin
    if cad[i] = ' ' then
      espacioEnBlancoCont := espacioEnBlancoCont + 1;
    i := i + 1;
  end;
  Result := espacioEnBlancoCont;
end;

// Cantidad de mayúsculas usando conjunto may: set of char
function cantidadMayusculas(cad: string; n, i: byte): byte;
const may: set of char = ['A'..'Z'];
var contadorMayusculas: byte;
begin
  contadorMayusculas := 0; 
  i := 1;
  while i <= n do begin
    if cad[i] in may then
      contadorMayusculas := contadorMayusculas + 1;
    i := i + 1;
  end;
  Result := contadorMayusculas;
end;

// Buscar Caracter y retornar la primera posición
function BuscarCaracterPosicion(cad: String; i, n: Byte; buscarcar: Char): Byte;
var posicion: Byte;
    encontrado: Boolean;
begin
  posicion := 0; 
  encontrado := false; 
  i := 1;
  while (i <= n) and (encontrado = false) do begin
    if UpCase(cad[i]) = UpCase(buscarcar) then begin
      posicion := i;
      encontrado := True;
    end;
    i := i + 1;
  end;
  Result := posicion;
end;

// Tarea 1 para el Viernes: Buscar Carácter y mostrar todas las posiciones
// Ejemplo: 'Hola cadena de texto', 'a' -> ' 4,7,11,'
function BuscarCaracterNPosicion(cad: String; i, n: Byte; buscarcar: Char): String;
var posicion: String;
begin
  posicion := ' ';  
  i := 1;
  while (i <= n) do begin
    if UpCase(cad[i]) = UpCase(buscarcar) then begin
      posicion := posicion + IntToStr(i) + ',';
    end;
    i := i + 1;
  end;
  Result := posicion;
end;

// Tarea 2 para el Viernes: Contar las veces que se repite un carácter buscado
// Ejemplo: 'Hola cadena de texto', 'a' -> 3
function BuscarCaracterNRepite(cad: String; i, n: Byte; buscarcar: Char): byte;
var repite: byte;
begin
  repite := 0;  
  i := 1;
  while (i <= n) do begin
    if UpCase(cad[i]) = UpCase(buscarcar) then begin
      repite := repite + 1;
    end;
    i := i + 1;
  end;
  Result := repite;
end;

// =============================================================================
//                   LOS 4 EJERCICIOS DE LA CLASE DE HOY
// =============================================================================

// Ejercicio 1: Contar las palabras de una cadena
// cad = 'Hola cadena de texto' -> cantpal = 4
function contarPalabras(cad: string; n, i: byte): byte;
var
  cantPal: byte;
  enPalabra: boolean;
begin
  cantPal := 0;
  enPalabra := false;
  i := 1;
  while i <= n do begin
    if cad[i] <> ' ' then begin
      if enPalabra = false then begin
        cantPal := cantPal + 1;
        enPalabra := true;
      end;
    end else begin
      enPalabra := false;
    end;
    i := i + 1;
  end;
  Result := cantPal;
end;

// Ejercicio 2 (Auxiliar): Verifica si en una palabra hay vocales juntas
// hola       4  0
function contarVocalesJuntas(Cad: string; n, i: Byte): Byte;
const voc: set of char = ['A', 'E', 'I', 'O', 'U'];
var contador, ayudante: Byte;
begin
  contador := 0;
  for i := 1 to n do begin
    ayudante := i + 1;
    if (ayudante <= n) then begin
      if (UpCase(cad[i]) in voc) and (UpCase(cad[i + 1]) in voc) then
        contador := contador + 1;
    end;
  end;
  Result := contador;
end;

// Ejercicio 2: Contar palabras donde exista 2 vocales juntas
// Cad = 'eleccion superior de bolivia' -> salida cantidadvoc = 3
function contarPalabras2VocalesJuntas(cad: string; n, i: byte): byte;
var
  palabra: string;
  cantPalVoc: byte;
begin
  cad := cad + ' '; // centinela para evaluar la última palabra
  n := Length(cad);
  cantPalVoc := 0;
  palabra := '';
  i := 1;
  while i <= n do begin
    if cad[i] <> ' ' then begin
      palabra := palabra + cad[i];
    end else begin
      if palabra <> '' then begin
        if contarVocalesJuntas(palabra, Length(palabra), 1) > 0 then begin
          cantPalVoc := cantPalVoc + 1;
        end;
        palabra := '';
      end;
    end;
    i := i + 1;
  end;
  Result := cantPalVoc;
end;

// Ejercicio 3: Mostrar los caracteres de los indices impares
// cad = |H|o|l|a| |M|u|n|d|o| (1..10) -> salida 'hlud'
function mostrarCaracteresIndicesImpares(cad: string; n, i: byte): string;
var
  salida: string;
begin
  salida := '';
  i := 1;
  while i <= n do begin
    // si el índice i es impar (1, 3, 5, 7, 9) y el caracter no es un espacio
    if (i mod 2 <> 0) and (cad[i] <> ' ') then begin
      salida := salida + LowerCase(cad[i]);
    end;
    i := i + 1;
  end;
  Result := salida;
end;

// Ejercicio 4: Contar las consonantes que tiene una cadena
// entrada 'cadena de texto' -> salida 7
function contarConsonantes(cad: string; n, i: byte): byte;
const
  letras: set of char = ['A'..'Z', 'a'..'z'];
  voc: set of char = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'];
var
  contadorConsonantes: byte;
begin
  contadorConsonantes := 0;
  i := 1;
  while i <= n do begin
    // Es una letra del abecedario y NO es vocal
    if (cad[i] in letras) and not (cad[i] in voc) then begin
      contadorConsonantes := contadorConsonantes + 1;
    end;
    i := i + 1;
  end;
  Result := contadorConsonantes;
end;

// =============================================================================
//                   FUNCIONES DEL PRÁCTICO #8
// =============================================================================

function contarCaracteres(cad: string; n, i: Byte): byte;
var contador: Byte;
begin
  contador := 0; 
  for i := 1 to n do begin
    contador := contador + 1;
  end;
  Result := contador;
end;

procedure MostrarPrimeraLetra(cad: string; var letra: Char);
const letras: set of Char = ['A'..'Z', 'a'..'z'];
begin
  letra := #0;
  for i := 1 to n do begin
    if cad[i] in letras then begin
      letra := cad[i];
      Exit;
    end;
  end;
end;

function mostrarPrimerCaracterF(cad: string; n, i: byte): Char;
const letras: set of Char = ['A'..'Z', 'a'..'z'];
var encontrado: Boolean;
    letra: Char;
begin
  letra := ' '; 
  encontrado := false; 
  i := 1;
  while (i <= n) and (encontrado = false) do begin
    if cad[i] in letras then begin
      letra := cad[i];
      encontrado := True;
    end;
    i := i + 1;
  end;
  Result := letra;
end;

function mostrarprimercaracter(cad: string; n, i: byte): Char;
begin
  Result := cad[1];
end;

function ultimaletra(cad: string; n, i: byte): char;
const letras: set of char = ['A'..'Z', 'a'..'z'];
begin
  Result := #0;
  for i := Length(cad) downto 1 do begin
    if cad[i] in letras then begin
      Result := cad[i];
      Exit;
    end;
  end;
end;

function contarvocal(cad: string; n, i: byte): integer;
const voc: set of char = ['A', 'E', 'I', 'O', 'U'];
var c: integer;
begin
  c := 0;
  for i := 1 to Length(cad) do begin
    if UpCase(cad[i]) in voc then
      c := c + 1;
  end;
  Result := c;
end;

function EliminarEspacios(cad: String; n, i: Byte): String;
var res: String;
begin
  res := '';
  for i := 1 to n do begin
    if cad[i] <> ' ' then
      res := res + cad[i];
  end;
  Result := res;
end;

function PrimerosNCaracteres(cad: string; nCant: Cardinal; n, i: Byte): string;
var res: string;
    limite: Integer;
begin
  res := '';
  limite := nCant;
  if limite > n then limite := n;
  for i := 1 to limite do begin
    res := res + cad[i];
  end;
  Result := res;
end;

function EstaVacia(cad: String): Boolean;
begin
  Result := (Length(Trim(cad)) = 0);
end;

procedure MostrarCodigosASCII(cad: String; var salida: String; n, i: Byte);
begin
  salida := '';
  for i := 1 to n do begin
    salida := salida + cad[i] + '->' + IntToStr(Ord(cad[i])) + '  ';
  end;
end;

function ContarMayusculas(cad: string; n, i: Byte): Integer;
const may: set of Char = ['A'..'Z'];
var contador: Integer;
begin
  contador := 0;
  for i := 1 to n do begin
    if cad[i] in may then
      contador := contador + 1;
  end;
  Result := contador;
end;

function EsPalindroma(cad: string; n, i: byte): Boolean;
var
  limpia: string;
  j: Cardinal;
begin
  limpia := '';
  for i := 1 to n do begin
    if cad[i] <> ' ' then
      limpia := limpia + UpCase(cad[i]);
  end;

  i := 1;
  j := Length(limpia);
  Result := True;

  while i < j do begin
    if limpia[i] <> limpia[j] then begin
      Result := False;
      Exit;
    end;
    i := i + 1;
    j := j - 1;
  end;
end;

function contadorVocales(cad: string; n, i: Byte): byte;
const voc: set of char = ['A', 'E', 'I', 'O', 'U'];
var contadoDeVocales: byte;
begin
  contadoDeVocales := 0; 
  i := 1;
  while i <= n do begin
    if UpCase(cad[i]) in voc then
      contadoDeVocales := contadoDeVocales + 1;
    i := i + 1;
  end;
  Result := contadoDeVocales;
end;

// =============================================================================
//                   EVENTOS DEL FORMULARIO TForm1
// =============================================================================

procedure TForm1.FormCreate(Sender: TObject);
begin
  Label5.Caption := 'cad=' + cad;
  Label6.Caption := 'n=' + IntToStr(n);
end;

// BOTÓN REGISTRAR: Guarda la cadena de Edit1 en la variable global cad
procedure TForm1.BTNCargarClick(Sender: TObject);
begin
  cad := Edit1.Text;
  ShowMessage('cadena de caracter registrado: cad=' + cad);
  Label5.Caption := 'cad=' + cad;
end;

// BOTÓN LONGITUD: Calcula n := Length(cad) y muestra en Edit2
procedure TForm1.Button2Click(Sender: TObject);
begin
  n := Length(cad); // calcular longitud n
  Edit2.Text := IntToStr(n) + ' caracteres';
  Label6.Caption := 'n=' + IntToStr(n);
end;

// BOTÓN CLOSE: Cierra el formulario
procedure TForm1.Button1Click(Sender: TObject);
begin
  Close;
end;

// EVENTOS DE LOS EJERCICIOS DE CLASE
procedure TForm1.N1ContarPalabrasCadena1Click(Sender: TObject);
begin
  Edit3.Text := 'Cantidad de palabras = ' + IntToStr(contarPalabras(cad, n, i));
end;

procedure TForm1.ContarVocalesJuntas1Click(Sender: TObject);
begin
  Edit3.Text := 'Vocales juntas en cadena = ' + IntToStr(contarVocalesJuntas(cad, n, i));
end;

procedure TForm1.N2ContarPalabras2VocalesJuntas1Click(Sender: TObject);
begin
  Edit3.Text := 'Palabras con 2 vocales juntas = ' + IntToStr(contarPalabras2VocalesJuntas(cad, n, i));
end;

procedure TForm1.N3MostrarIndicesImpares1Click(Sender: TObject);
begin
  Edit3.Text := 'Indices impares: ' + mostrarCaracteresIndicesImpares(cad, n, i);
end;

procedure TForm1.N4ContarConsonantes1Click(Sender: TObject);
begin
  Edit3.Text := 'Cantidad de consonantes = ' + IntToStr(contarConsonantes(cad, n, i));
end;

// EVENTOS DE LA TAREA PARA EL VIERNES
procedure TForm1.buscarunaletraylasnveces1Click(Sender: TObject);
var buscarcar: Char;
    textoEntrada: String;
begin
  textoEntrada := InputBox('Buscar', 'Ingrese un caracter a buscar:', 'a');
  if Length(textoEntrada) > 0 then
    buscarcar := textoEntrada[1]
  else
    buscarcar := ' ';

  Edit3.Text := 'Posiciones:' + BuscarCaracterNPosicion(cad, i, n, buscarcar);
end;

procedure TForm1.T1BuscarCaracterPosiciones1Click(Sender: TObject);
begin
  buscarunaletraylasnveces1Click(Sender);
end;

procedure TForm1.BuscarCaracterNseRepite1Click(Sender: TObject);
var buscarcar: Char;
    textoEntrada: String;
begin
  textoEntrada := InputBox('Buscar', 'Ingrese un caracter a buscar:', 'a');
  if Length(textoEntrada) > 0 then
    buscarcar := textoEntrada[1]
  else
    buscarcar := ' ';

  Edit3.Text := 'Se repite: ' + IntToStr(BuscarCaracterNRepite(cad, i, n, buscarcar)) + ' veces';
end;

procedure TForm1.T2ContarRepeticiones1Click(Sender: TObject);
begin
  BuscarCaracterNseRepite1Click(Sender);
end;

// EVENTOS DEL MENÚ PRÁCTICO 8
procedure TForm1.N1ContarCaracteres1Click(Sender: TObject);
begin
  Edit3.Text := 'la cantidad es ' + IntToStr(contarCaracteres(cad, n, i)) + ' caracteres';
end;

procedure TForm1.N2MostrarPrimeraLetra1Click(Sender: TObject);
begin
  Edit3.Text := mostrarPrimerCaracterF(cad, n, i);
end;

procedure TForm1.ultimaLtr1Click(Sender: TObject);
begin
  Edit3.Text := ultimaletra(cad, n, i);
end;

procedure TForm1.contarvc2Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(contarvocal(cad, n, i)) + ' vocales';
end;

procedure TForm1.Vocales1Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(contadorVocales(cad, n, i)) + ' vocales';
end;

procedure TForm1.BuscarCaracter1Click(Sender: TObject);
var buscarcar: Char;
    textoEntrada: String;
begin
  textoEntrada := InputBox('Buscar', 'Ingrese un caracter a buscar', ' ');
  if Length(textoEntrada) > 0 then
    buscarcar := textoEntrada[1]
  else
    buscarcar := ' ';

  Edit3.Text := 'Primera posicion: ' + IntToStr(BuscarCaracterPosicion(cad, i, n, buscarcar));
end;

procedure TForm1.Cargar1Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(espacioEnBlanco(cad, n, i)) + ' Espacio Blanco';
end;

procedure TForm1.Cargar2Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(cantidadMayusculas(cad, n, i)) + ' Mayusculas';
end;

procedure TForm1.N11Eliminarespaciosenblanco1Click(Sender: TObject);
begin
  Edit3.Text := EliminarEspacios(cad, n, i);
end;

procedure TForm1.N12Primerosncaracteres1Click(Sender: TObject);
var nCant: Cardinal;
begin
  nCant := StrToIntDef(InputBox('Primeros N', 'Cantidad de caracteres:', '8'), 0);
  Edit3.Text := PrimerosNCaracteres(cad, nCant, n, i);
end;

procedure TForm1.N13Determinarsiestvaca1Click(Sender: TObject);
begin
  if EstaVacia(cad) then
    Edit3.Text := 'La cadena esta VACIA'
  else
    Edit3.Text := 'La cadena CONTIENE TEXTO';
end;

procedure TForm1.N14MostrarcdigosASCII1Click(Sender: TObject);
var info: String;
begin
  MostrarCodigosASCII(cad, info, n, i);
  Edit3.Text := info;
  ShowMessage('Codigos ASCII:' + #13#10 + info);
end;

procedure TForm1.N15Contarmaysculas1Click(Sender: TObject);
begin
  Edit3.Text := IntToStr(ContarMayusculas(cad, n, i)) + ' Mayusculas';
end;

procedure TForm1.N16Espalndroma1Click(Sender: TObject);
begin
  if EsPalindroma(cad, n, i) then
    Edit3.Text := 'Es Palindroma (SI)'
  else
    Edit3.Text := 'No es Palindroma (NO)';
end;


// =============================================================================
// MÉTODOS DE ORDENAMIENTO EN CADENAS (METODOLOGÍA ING. ANGÉLICA GARZÓN)
// =============================================================================

// 1. Ordenar Cadena Completa Ascendente ('A'..'Z') - Algoritmo Burbuja
function OrdenarCadenaAscendente(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  for i := 1 to n - 1 do
  begin
    for j := i + 1 to n do
    begin
      if cad[i] > cad[j] then
      begin
        // Intercambio en 3 fases (Swap de la pizarra)
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
    end;
  end;
  Result := cad;
end;

// 2. Ordenar Cadena Completa Descendente ('Z'..'A')
function OrdenarCadenaDescendente(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  for i := 1 to n - 1 do
  begin
    for j := i + 1 to n do
    begin
      if cad[i] < cad[j] then
      begin
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
    end;
  end;
  Result := cad;
end;

// Invertir una cadena / palabra auxiliar
function InvertirTexto(cad: String; n: Byte): String;
var
  i: Byte;
  res: String;
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

// Obtener límites [ini, fin] de la k-ésima palabra
procedure ObtenerLimitesPalabra(cad: String; n, k: Byte; var pIni, pFin: Byte);
var
  i, numPalabra: Byte;
  enPalabra: Boolean;
begin
  pIni := 0;
  pFin := 0;
  numPalabra := 0;
  enPalabra := false;
  i := 1;
  while i <= n do
  begin
    if cad[i] <> ' ' then
    begin
      if not enPalabra then
      begin
        enPalabra := true;
        numPalabra := numPalabra + 1;
        if numPalabra = k then
          pIni := i;
      end;
    end
    else
    begin
      if enPalabra then
      begin
        if numPalabra = k then
        begin
          pFin := i - 1;
          Exit;
        end;
        enPalabra := false;
      end;
    end;
    i := i + 1;
  end;
  if enPalabra and (numPalabra = k) then
    pFin := n;
end;

// Obtener límites [ini, fin] de la última palabra
procedure ObtenerLimitesUltimaPalabra(cad: String; n: Byte; var pIni, pFin: Byte);
var
  i: Byte;
begin
  pIni := 0;
  pFin := 0;
  if n = 0 then Exit;
  i := n;
  while (i >= 1) and (cad[i] = ' ') do
    i := i - 1;
  if i = 0 then Exit;
  pFin := i;
  while (i >= 1) and (cad[i] <> ' ') do
    i := i - 1;
  pIni := i + 1;
end;

// 3. Ordenar la Última Palabra de la Cadena (Pizarra Ej. 3)
// Entrada: 'Casa de aña' -> Salida: 'Casa de aan'
function OrdenarUltimaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palOrd, res: String;
begin
  ObtenerLimitesUltimaPalabra(cad, n, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;
  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palOrd := OrdenarCadenaAscendente(pal, lenPal);
  res := Copy(cad, 1, pIni - 1) + palOrd + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;

// 4. Invertir la Segunda Palabra de la Cadena (Pizarra Ej. 4)
// Entrada: 'Hola mundo de Cadena' -> Salida: 'Hola odnum de Cadena'
function InvertirSegundaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palInv, res: String;
begin
  ObtenerLimitesPalabra(cad, n, 2, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;
  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palInv := InvertirTexto(pal, lenPal);
  res := Copy(cad, 1, pIni - 1) + palInv + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;

// 5. Ordenar la Segunda Palabra de la Cadena (Pizarra Ej. 5)
// Entrada: 'Hola mundo de Cadena' -> Salida: 'Hola dmnou de Cadena'
function OrdenarSegundaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palOrd, res: String;
begin
  ObtenerLimitesPalabra(cad, n, 2, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;
  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palOrd := OrdenarCadenaAscendente(pal, lenPal);
  res := Copy(cad, 1, pIni - 1) + palOrd + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;

// =============================================================================
// EVENTOS DE BOTONES Y MENÚS DEL FORMULARIO DELPHI
// =============================================================================

procedure TForm1.Ascendente1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarCadenaAscendente(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Cadena ordenada ascendentemente: ' + cad);
end;

procedure TForm1.Descendente1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarCadenaDescendente(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Cadena ordenada descendentemente: ' + cad);
end;

procedure TForm1.OrdenarUltimaPalabra1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarUltimaPalabra(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Ultima palabra ordenada: ' + cad);
end;

procedure TForm1.InvertirSegundaPalabra1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := InvertirSegundaPalabra(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Segunda palabra invertida: ' + cad);
end;

procedure TForm1.OrdenarSegundaPalabra1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarSegundaPalabra(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Segunda palabra ordenada: ' + cad);
end;

end.
