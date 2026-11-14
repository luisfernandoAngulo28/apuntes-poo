unit UnitExamenParcial2;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes,
  Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls,
  UnitModelosSegundoParcial;

type
  TFormExamenParcial2 = class(TForm)
    LabelTitulo: TLabel;
    LabelEntrada1: TLabel;
    EditEntrada1: TEdit;
    LabelEntrada2: TLabel;
    EditEntrada2: TEdit;
    LabelResultado: TLabel;
    EditResultado: TEdit;
    
    // Botones de Examen 2024-1 Z2
    Button2024_P1: TButton;
    Button2024_P2: TButton;
    Button2024_P3a: TButton;
    Button2024_P3b: TButton;
    
    // Botones de Examen 2024-1 Z2-R
    Button2024R_P1: TButton;
    Button2024R_P2: TButton;
    
    // Botones de Examen 2024-1 SF
    Button2024SF_P1: TButton;
    Button2024SF_P2: TButton;
    Button2024SF_P3: TButton;
    
    // Botones de Examen 2023-2 Z2
    Button2023_2_P2: TButton;
    Button2023_2_P3: TButton;
    
    // Botones de Examen 2023-1 Z2
    Button2023_1_P1: TButton;
    Button2023_1_P3: TButton;
    
    // Botones de Clase Ordenación (Burbuja)
    ButtonBurbuja_Ultima: TButton;
    ButtonBurbuja_2daInv: TButton;
    ButtonBurbuja_2daOrd: TButton;
    
    ButtonSalir: TButton;

    procedure Button2024_P1Click(Sender: TObject);
    procedure Button2024_P2Click(Sender: TObject);
    procedure Button2024_P3aClick(Sender: TObject);
    procedure Button2024_P3bClick(Sender: TObject);
    
    procedure Button2024R_P1Click(Sender: TObject);
    procedure Button2024R_P2Click(Sender: TObject);
    
    procedure Button2024SF_P1Click(Sender: TObject);
    procedure Button2024SF_P2Click(Sender: TObject);
    procedure Button2024SF_P3Click(Sender: TObject);
    
    procedure Button2023_2_P2Click(Sender: TObject);
    procedure Button2023_2_P3Click(Sender: TObject);
    
    procedure Button2023_1_P1Click(Sender: TObject);
    procedure Button2023_1_P3Click(Sender: TObject);
    
    procedure ButtonBurbuja_UltimaClick(Sender: TObject);
    procedure ButtonBurbuja_2daInvClick(Sender: TObject);
    procedure ButtonBurbuja_2daOrdClick(Sender: TObject);
    
    procedure ButtonSalirClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FormExamenParcial2: TFormExamenParcial2;

implementation

{$R *.dfm}

{ --- 2024-1 Z2 --- }
procedure TFormExamenParcial2.Button2024_P1Click(Sender: TObject);
var n: Integer;
begin
  n := StrToIntDef(EditEntrada1.Text, 4);
  EditResultado.Text := FloatToStrF(SumaSerie_2024_1_Z2(n), ffFixed, 8, 4);
end;

procedure TFormExamenParcial2.Button2024_P2Click(Sender: TObject);
var n: LongWord;
begin
  n := StrToIntDef(EditEntrada1.Text, 85239);
  EditResultado.Text := IntToStr(MenorImparMayorPar(n));
end;

procedure TFormExamenParcial2.Button2024_P3aClick(Sender: TObject);
begin
  EditResultado.Text := InvertirUltimaPalabra(EditEntrada1.Text);
end;

procedure TFormExamenParcial2.Button2024_P3bClick(Sender: TObject);
begin
  EditResultado.Text := EliminarConsonantes(EditEntrada1.Text);
end;

{ --- 2024-1 Z2-R --- }
procedure TFormExamenParcial2.Button2024R_P1Click(Sender: TObject);
var x, n: Integer;
begin
  x := StrToIntDef(EditEntrada1.Text, 2);
  n := StrToIntDef(EditEntrada2.Text, 3);
  EditResultado.Text := IntToStr(SumaPotenciasX(x, n));
end;

procedure TFormExamenParcial2.Button2024R_P2Click(Sender: TObject);
begin
  EditResultado.Text := MayusculasPalabrasInicianVocal(EditEntrada1.Text);
end;

{ --- 2024-1 SF --- }
procedure TFormExamenParcial2.Button2024SF_P1Click(Sender: TObject);
var n: Integer;
begin
  n := StrToIntDef(EditEntrada1.Text, 4);
  EditResultado.Text := FloatToStrF(SumaSerie_2024_1_SF(n), ffFixed, 8, 2);
end;

procedure TFormExamenParcial2.Button2024SF_P2Click(Sender: TObject);
var n: LongWord; k: Byte;
begin
  n := StrToIntDef(EditEntrada1.Text, 78143);
  k := StrToIntDef(EditEntrada2.Text, 3);
  EditResultado.Text := IntToStr(EliminarDesdePosicionK(n, k));
end;

procedure TFormExamenParcial2.Button2024SF_P3Click(Sender: TObject);
begin
  EditResultado.Text := PrimerLetraCadaPalabraMayuscula(EditEntrada1.Text);
end;

{ --- 2023-2 Z2 --- }
procedure TFormExamenParcial2.Button2023_2_P2Click(Sender: TObject);
var n: LongWord; k: Byte;
begin
  n := StrToIntDef(EditEntrada1.Text, 78143);
  k := StrToIntDef(EditEntrada2.Text, 2);
  EditResultado.Text := IntToStr(EliminarDigitoPosicionK(n, k));
end;

procedure TFormExamenParcial2.Button2023_2_P3Click(Sender: TObject);
begin
  EditResultado.Text := CantidadVocalesPorPalabra(EditEntrada1.Text);
end;

{ --- 2023-1 Z2 --- }
procedure TFormExamenParcial2.Button2023_1_P1Click(Sender: TObject);
var n: Integer;
begin
  n := StrToIntDef(EditEntrada1.Text, 4);
  EditResultado.Text := FloatToStrF(SumaSerie_2023_1_Z2(n), ffFixed, 8, 4);
end;

procedure TFormExamenParcial2.Button2023_1_P3Click(Sender: TObject);
begin
  EditResultado.Text := InvertirCadaPalabra(EditEntrada1.Text);
end;

{ --- BURBUJA DE PIZARRA --- }
procedure TFormExamenParcial2.ButtonBurbuja_UltimaClick(Sender: TObject);
begin
  EditResultado.Text := OrdenarUltimaPalabra(EditEntrada1.Text);
end;

procedure TFormExamenParcial2.ButtonBurbuja_2daInvClick(Sender: TObject);
begin
  EditResultado.Text := InvertirSegundaPalabra(EditEntrada1.Text);
end;

procedure TFormExamenParcial2.ButtonBurbuja_2daOrdClick(Sender: TObject);
begin
  EditResultado.Text := OrdenarSegundaPalabra(EditEntrada1.Text);
end;

procedure TFormExamenParcial2.ButtonSalirClick(Sender: TObject);
begin
  Close;
end;

end.

