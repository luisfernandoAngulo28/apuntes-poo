unit Series;

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
  //variables Globales
  numero,contador:Integer;

// Declaraciones de funciones modulares (Metodología Oficial Ing. Angélica Garzón)
function sumaDoble(numero,contador:integer):integer;
function sumafactorial(numero,contador:integer):integer;
function sumaCuadratica(numero,contador:integer):integer;
function sumaParImpar(numero,contador:integer):integer;

implementation

{$R *.dfm}

// =============================================================================
// FUNCIONES DE SERIES (ESTILO OFICIAL DE CÁTEDRA)
// =============================================================================

// 1. Suma Doble: 1 + 2 + 4 + 8 + 16 + ... (Geométrica razón 2)
function sumaDoble(numero,contador:integer):integer;
var doble,sumadordoble:integer;
begin
  sumadordoble:=0; contador:=1; doble:=1;
  while numero >=contador do
  begin
    // ShowMessage(IntToStr(sumadordoble));
    sumadordoble:=sumadordoble+doble;
    doble:=doble*2;
    contador:=contador+1;
  end;
   Result:=sumadordoble;
end;

// 2. Suma Factorial: 1 + 2 + 6 + 24 + 120 = 153 (para n=5)
function sumafactorial(numero,contador:integer):integer;
var factorial,sumadorfactorial:integer;      //n=5 -> 1+2+6+24+120=153
begin
  sumadorfactorial:=0; contador:=1; factorial:=1;
  while numero >=contador do
  begin
    // ShowMessage(IntToStr(sumadordoble));
    factorial:=factorial*contador;
    sumadorfactorial:=sumadorfactorial+factorial;
    contador:=contador+1;
  end;
   Result:=sumadorfactorial;
end;

// 3. Suma Cuadrática: 1 + 4 + 9 + 16 + 25 = 55 (para n=5)
function sumaCuadratica(numero,contador:integer):integer;
var cuadratica,sumadorCuadratica:integer;    //1+4+9+16+25=55
begin
  sumadorCuadratica:=0; contador:=1; cuadratica:=1;
  while numero >=contador do
  begin
    //ShowMessage(IntToStr(cuadratica));
    cuadratica:=contador*contador;
    sumadorCuadratica:=sumadorCuadratica+cuadratica;
    contador:=contador+1;
  end;
   Result:=sumadorCuadratica;
end;

// 4. Suma Par Impar: Manejo de dos secuencias simultáneas (Par decrementa de 20, Impar incrementa de 1)
function sumaParImpar(numero,contador:integer):integer;
var Par,Impar,sumadorParImpar:integer;
begin
  sumadorParImpar:=0; contador:=1; Par:=20; Impar:=1;
  while numero >=contador do
  begin
    //ShowMessage(IntToStr(cuadratica));
    Par:=Par-2;
    Impar:=Impar+2;
    sumadorParImpar:=sumadorParImpar+Par;
    contador:=contador+1;
  end;
   Result:=sumadorParImpar;
end;

// =============================================================================
// PROCEDIMIENTOS DE EVENTO (BOTONES DEL FORMULARIO)
// =============================================================================

procedure TForm1.Button1Click(Sender: TObject);
begin
  numero:=StrToInt(Edit1.Text);
  ShowMessage('Registrado con exito n='+IntToStr(numero));
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Edit2.Text:=IntToStr(sumaDoble(numero,contador));
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Edit2.Text:=IntToStr(sumafactorial(numero,contador));
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Edit2.Text:=IntToStr(sumaCuadratica(numero,contador));
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
  Close;
end;

procedure TForm1.Button6Click(Sender: TObject);
begin
  Edit2.Text:=IntToStr(sumaParImpar(numero,contador));
end;

end.
