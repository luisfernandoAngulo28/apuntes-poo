unit UFNatural;  // FORMULARIO PRINCIPAL VCL - INF110-Z2

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs,
  UCNatural, Vcl.StdCtrls, Vcl.Buttons, Vcl.Menus;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Crear: TButton;
    AsignarNumrero: TButton;
    Mostrar: TButton;
    CDigitos1: TButton;
    procedure CrearClick(Sender: TObject);
    procedure AsignarNumreroClick(Sender: TObject);
    procedure MostrarClick(Sender: TObject);
    procedure CDigitos1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  Numero: NumeroNatural;

implementation

{$R *.dfm}

// 1. CREAR LA CLASE
procedure TForm1.CrearClick(Sender: TObject);
begin
  Numero := NumeroNatural.Create;
  ShowMessage('Numero Creado create');
end;

// 2. ASIGNAR EL NUMERO
procedure TForm1.AsignarNumreroClick(Sender: TObject);
begin
  Numero.CambiarValor(StrToInt(Edit1.Text));
  ShowMessage('Valor asignado');
end;

// 3. MOSTRAR NUMERO
procedure TForm1.MostrarClick(Sender: TObject);
begin
  Edit2.Text := IntToStr(Numero.ObtenerValor);
end;

// 4. CONTAR DIGITOS
procedure TForm1.CDigitos1Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(Numero.ContarDigitos) + ' digitos';
end;

end.

