unit UFSeriesAtajos;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs,
  Vcl.StdCtrls, Vcl.Menus, UAtajosExamen;

type
  TFormSeriesAtajos = class(TForm)
    EditEntradaN: TEdit;
    LabelEntrada: TLabel;
    LabelResultado: TLabel;
    EditResultado: TEdit;
    ButtonCalcular: TButton;
    ButtonLimpiar: TButton;
    ButtonCerrar: TButton;
    MainMenuPrincipal: TMainMenu;
    MenuSeriesCompuestas: TMenuItem;
    ItemFactorialDoble: TMenuItem;
    ItemCuadradoFibonacci: TMenuItem;
    ItemPotenciaMultiplo5: TMenuItem;
    ItemImparesCuadrados: TMenuItem;
    MenuSeriesSimples: TMenuItem;
    ItemSumaDobles: TMenuItem;
    ItemSumaFactoriales: TMenuItem;
    ItemSumaCuadratica: TMenuItem;
    
    // Eventos de botones
    procedure ButtonCerrarClick(Sender: TObject);
    procedure ButtonLimpiarClick(Sender: TObject);
    
    // Eventos de menú (Series clásicas de examen)
    procedure ItemFactorialDobleClick(Sender: TObject);
    procedure ItemCuadradoFibonacciClick(Sender: TObject);
    procedure ItemPotenciaMultiplo5Click(Sender: TObject);
    procedure ItemImparesCuadradosClick(Sender: TObject);
    procedure ItemSumaDoblesClick(Sender: TObject);
    procedure ItemSumaFactorialesClick(Sender: TObject);
    procedure ItemSumaCuadraticaClick(Sender: TObject);
  private
    function ObtenerValorN(out n: Integer): Boolean;
    procedure MostrarResultado(const nombreSerie: string; valor: Double);
  public
    { Public declarations }
  end;

var
  FormSeriesAtajos: TFormSeriesAtajos;

implementation

{$R *.dfm}

function TFormSeriesAtajos.ObtenerValorN(out n: Integer): Boolean;
begin
  Result := TryStrToInt(Trim(EditEntradaN.Text), n) and (n > 0);
  if not Result then
  begin
    ShowMessage('Por favor, ingrese un número entero positivo (N > 0).');
    EditEntradaN.SetFocus;
  end;
end;

procedure TFormSeriesAtajos.MostrarResultado(const nombreSerie: string; valor: Double);
begin
  EditResultado.Text := FloatToStrF(valor, ffFixed, 10, 4);
  ShowMessage(nombreSerie + ' para N = ' + EditEntradaN.Text + #13#10 +
              'Resultado = ' + EditResultado.Text);
end;

procedure TFormSeriesAtajos.ButtonLimpiarClick(Sender: TObject);
begin
  EditEntradaN.Clear;
  EditResultado.Clear;
  EditEntradaN.SetFocus;
end;

procedure TFormSeriesAtajos.ButtonCerrarClick(Sender: TObject);
begin
  Close;
end;

// =============================================================================
// HANDLERS DEL MENÚ: DIVIDE Y VENCERÁS EN ACCIÓN
// =============================================================================

// 1. Factorial / Doble = 1/2 + 2/4 + 6/8 + 24/16 + 120/32 + ...
procedure TFormSeriesAtajos.ItemFactorialDobleClick(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Factorial / Doble', SumaFactorialDoble(n));
end;

// 2. Cuadrado / Fibonacci = 3/1 + 6/1 + 12/2 + 24/3 + 48/5 + ...
procedure TFormSeriesAtajos.ItemCuadradoFibonacciClick(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Cuadrado / Fibonacci', SumaCuadradoFibonacci(n));
end;

// 3. Potencia / Múltiplo de 5 = 1^1/5 + 2^2/10 + 3^3/15 + 4^4/20 + ...
procedure TFormSeriesAtajos.ItemPotenciaMultiplo5Click(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Potencia / Múltiplo de 5', SumaPotenciaMultiplo5(n));
end;

// 4. Impares / Cuadrados = 1/1 - 3/4 + 5/9 - 7/16 + 9/25 - ...
procedure TFormSeriesAtajos.ItemImparesCuadradosClick(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Impares / Cuadrados (Alternada)', SumaImparesCuadrados(n));
end;

// 5. Sumatoria de Dobles = 1 + 2 + 4 + 8 + ...
procedure TFormSeriesAtajos.ItemSumaDoblesClick(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Suma de Dobles (2^k)', SumaDobleSimple(n));
end;

// 6. Sumatoria de Factoriales = 1! + 2! + 3! + ...
procedure TFormSeriesAtajos.ItemSumaFactorialesClick(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Suma de Factoriales (k!)', SumaFactorialSimple(n));
end;

// 7. Sumatoria Cuadrática = 1^2 + 2^2 + 3^2 + ...
procedure TFormSeriesAtajos.ItemSumaCuadraticaClick(Sender: TObject);
var
  n: Integer;
begin
  if ObtenerValorN(n) then
    MostrarResultado('Serie: Suma Cuadrática (k^2)', SumaCuadraticaSimple(n));
end;

end.

