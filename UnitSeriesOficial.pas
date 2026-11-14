unit UnitSeriesOficial;
{==============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE INGENIERÍA EN CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES
  INF110 - GRUPO Z2 | SEMESTRE 2-2026
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar

  UNIDAD OFICIAL: Funciones y Procedimiento Series
  TEMA: Programación Modular aplicada a Series Numéricas con Formulario VCL.
==============================================================================}

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Button1: TButton;
    Edit2: TEdit;
    Label3: TLabel;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    Button6: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure Button6Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  // Variables Globales
  numero, contador: Integer;

// Declaración modular de las funciones
function sumaDoble(numero, contador: integer): integer;
function sumafactorial(numero, contador: integer): integer;
function sumaCuadratica(numero, contador: integer): integer;
function sumaParImpar(numero, contador: integer): integer;

implementation

{$R *.dfm}

// =============================================================================
// 1. FUNCIÓN SUMA DOBLE: 1 + 2 + 4 + 8 + 16 + ... (Potencias sucesivas de 2)
// =============================================================================
function sumaDoble(numero, contador: integer): integer;
var
  doble, sumadordoble: integer;
begin
  sumadordoble := 0;
  contador := 1;
  doble := 1;
  while numero >= contador do
  begin
    // ShowMessage(IntToStr(sumadordoble));
    sumadordoble := sumadordoble + doble;
    doble := doble * 2;
    contador := contador + 1;
  end;
  Result := sumadordoble;
end;

// =============================================================================
// 2. FUNCIÓN SUMA FACTORIAL: 1! + 2! + 3! + 4! + 5! + ...
//    Ejemplo N = 5: 1 + 2 + 6 + 24 + 120 = 153
// =============================================================================
function sumafactorial(numero, contador: integer): integer;
var
  factorial, sumadorfactorial: integer;
begin
  sumadorfactorial := 0;
  contador := 1;
  factorial := 1;
  while numero >= contador do
  begin
    // ShowMessage(IntToStr(sumadordoble));
    factorial := factorial * contador;
    sumadorfactorial := sumadorfactorial + factorial;
    contador := contador + 1;
  end;
  Result := sumadorfactorial;
end;

// =============================================================================
// 3. FUNCIÓN SUMA CUADRÁTICA: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + ...
//    Ejemplo N = 5: 1 + 4 + 9 + 16 + 25 = 55
// =============================================================================
function sumaCuadratica(numero, contador: integer): integer;
var
  cuadratica, sumadorCuadratica: integer;
begin
  sumadorCuadratica := 0;
  contador := 1;
  cuadratica := 1;
  while numero >= contador do
  begin
    cuadratica := contador * contador;
    sumadorCuadratica := sumadorCuadratica + cuadratica;
    contador := contador + 1;
  end;
  Result := sumadorCuadratica;
end;

// =============================================================================
// 4. FUNCIÓN SUMA PAR IMPAR: Dos secuencias concurrentes (Par -= 2, Impar += 2)
//    Par inicia en 20 (y se decrementa antes de sumar: 18, 16, 14, 12, 10...)
//    Impar inicia en 1 (y avanza de 2 en 2: 3, 5, 7, 9...)
// =============================================================================
function sumaParImpar(numero, contador: integer): integer;
var
  Par, Impar, sumadorParImpar: integer;
begin
  sumadorParImpar := 0;
  contador := 1;
  Par := 20;
  Impar := 1;
  while numero >= contador do
  begin
    Par := Par - 2;
    Impar := Impar + 2;
    sumadorParImpar := sumadorParImpar + Par;
    contador := contador + 1;
  end;
  Result := sumadorParImpar;
end;

// =============================================================================
// PROCEDIMIENTOS DE EVENTO (CONEXIÓN DE BOTONES CON FORMULARIO VCL)
// =============================================================================

procedure TForm1.Button1Click(Sender: TObject);
begin
  numero := StrToInt(Edit1.Text);
  ShowMessage('Registrado con exito n=' + IntToStr(numero));
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumaDoble(numero, contador));
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumafactorial(numero, contador));
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumaCuadratica(numero, contador));
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
  Close;
end;

procedure TForm1.Button6Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumaParImpar(numero, contador));
end;

end.
