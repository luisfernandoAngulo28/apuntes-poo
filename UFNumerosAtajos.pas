unit UFNumerosAtajos;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs,
  Vcl.StdCtrls, Vcl.Menus, UCNatural, UAtajosNumeros;

type
  TFormNumeros = class(TForm)
    LabelNumero: TLabel;
    EditNumero: TEdit;
    LabelResultado: TLabel;
    EditResultado: TEdit;
    LabelParametro: TLabel;
    EditParametro: TEdit;
    MemoSalida: TMemo;
    MainMenuPrincipal: TMainMenu;
    
    // Menú POO
    MenuObjetoPOO: TMenuItem;
    ItemCrearObjeto: TMenuItem;
    ItemAsignarNumero: TMenuItem;
    ItemMostrarNumero: TMenuItem;
    
    // Menú Clásicos de Dígitos
    MenuMetodosClasicos: TMenuItem;
    ItemContarDigitos: TMenuItem;
    ItemInvertirNumero: TMenuItem;
    ItemEsCapicua: TMenuItem;
    ItemRaizDigital: TMenuItem;
    ItemMultiplicarDigitos: TMenuItem;
    ItemEliminarCeros: TMenuItem;
    ItemDigitosOrdenados: TMenuItem;
    ItemSumaParesEImpares: TMenuItem;
    
    // Menú Exámenes Finales
    MenuExamenesFinales: TMenuItem;
    ItemMitadDerechaCapicua: TMenuItem;
    ItemMitadIzquierdaCapicua: TMenuItem;
    ItemPrimeroYUltimoPrimos: TMenuItem;
    ItemEliminarRepetidos: TMenuItem;
    ItemSepararMenoresMayores: TMenuItem;
    
    // Menú Bases y Bits
    MenuBasesYBits: TMenuItem;
    ItemConvertirBinario: TMenuItem;
    ItemConvertirOctal: TMenuItem;
    ItemConvertirHexadecimal: TMenuItem;
    ItemPalindromoBinario: TMenuItem;
    ItemContarBitsUno: TMenuItem;

    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure ItemCrearObjetoClick(Sender: TObject);
    procedure ItemAsignarNumeroClick(Sender: TObject);
    procedure ItemMostrarNumeroClick(Sender: TObject);
    
    // Eventos Clásicos
    procedure ItemContarDigitosClick(Sender: TObject);
    procedure ItemInvertirNumeroClick(Sender: TObject);
    procedure ItemEsCapicuaClick(Sender: TObject);
    procedure ItemRaizDigitalClick(Sender: TObject);
    procedure ItemMultiplicarDigitosClick(Sender: TObject);
    procedure ItemEliminarCerosClick(Sender: TObject);
    procedure ItemDigitosOrdenadosClick(Sender: TObject);
    procedure ItemSumaParesEImparesClick(Sender: TObject);
    
    // Eventos Exámenes
    procedure ItemMitadDerechaCapicuaClick(Sender: TObject);
    procedure ItemMitadIzquierdaCapicuaClick(Sender: TObject);
    procedure ItemPrimeroYUltimoPrimosClick(Sender: TObject);
    procedure ItemEliminarRepetidosClick(Sender: TObject);
    procedure ItemSepararMenoresMayoresClick(Sender: TObject);
    
    // Eventos Bases
    procedure ItemConvertirBinarioClick(Sender: TObject);
    procedure ItemConvertirOctalClick(Sender: TObject);
    procedure ItemConvertirHexadecimalClick(Sender: TObject);
    procedure ItemPalindromoBinarioClick(Sender: TObject);
    procedure ItemContarBitsUnoClick(Sender: TObject);
  private
    ObjetoNumero: NumeroNatural; // Instancia POO encapsulada en el Formulario
    function ObtenerNumeroEntrada(out ValorNatural: Cardinal): Boolean;
    function ObtenerParametroByte(out ValorByte: Byte): Boolean;
  public
  end;

var
  FormNumeros: TFormNumeros;

implementation

{$R *.dfm}

{ TFormNumeros }

procedure TFormNumeros.FormCreate(Sender: TObject);
begin
  ObjetoNumero := NumeroNatural.Create;
end;

procedure TFormNumeros.FormDestroy(Sender: TObject);
begin
  ObjetoNumero.Free;
end;

function TFormNumeros.ObtenerNumeroEntrada(out ValorNatural: Cardinal): Boolean;
begin
  Result := TryStrToUInt(Trim(EditNumero.Text), ValorNatural);
  if not Result then
    ShowMessage('Por favor, ingrese un número natural entero positivo válido (0 .. 4.294.967.295).');
end;

function TFormNumeros.ObtenerParametroByte(out ValorByte: Byte): Boolean;
var
  ValEntero: Integer;
begin
  Result := TryStrToInt(Trim(EditParametro.Text), ValEntero) and (ValEntero >= 0) and (ValEntero <= 255);
  if Result then
    ValorByte := Byte(ValEntero)
  else
    ShowMessage('Por favor, ingrese un dígito o parámetro válido entre 0 y 255.');
end;

procedure TFormNumeros.ItemCrearObjetoClick(Sender: TObject);
begin
  if Assigned(ObjetoNumero) then
    ObjetoNumero.Free;
  ObjetoNumero := NumeroNatural.Create;
  ShowMessage('Objeto NumeroNatural instanciado exitosamente.');
end;

procedure TFormNumeros.ItemAsignarNumeroClick(Sender: TObject);
var
  N: Cardinal;
begin
  if ObtenerNumeroEntrada(N) then
  begin
    ObjetoNumero.CambiarValor(N);
    ShowMessage('Valor asignado correctamente al objeto.');
  end;
end;

procedure TFormNumeros.ItemMostrarNumeroClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoNumero.ObtenerValor);
end;

// ============================================================================
// EVENTOS CLÁSICOS DE DÍGITOS
// ============================================================================

procedure TFormNumeros.ItemContarDigitosClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoNumero.ContarDigitos) + ' dígitos';
end;

procedure TFormNumeros.ItemInvertirNumeroClick(Sender: TObject);
var
  N: Cardinal;
begin
  if ObtenerNumeroEntrada(N) then
    EditResultado.Text := IntToStr(UAtajosNumeros.InvertirNumero(N));
end;

procedure TFormNumeros.ItemEsCapicuaClick(Sender: TObject);
var
  N: Cardinal;
begin
  if ObtenerNumeroEntrada(N) then
  begin
    if UAtajosNumeros.EsCapicua(N) then
      EditResultado.Text := 'VERDADERO: Es Capicúa'
    else
      EditResultado.Text := 'FALSO: No es Capicúa';
  end;
end;

procedure TFormNumeros.ItemRaizDigitalClick(Sender: TObject);
begin
  EditResultado.Text := 'Raíz Digital: ' + IntToStr(ObjetoNumero.SumarDigitosHastaMenor10);
end;

procedure TFormNumeros.ItemMultiplicarDigitosClick(Sender: TObject);
begin
  EditResultado.Text := 'Producto: ' + IntToStr(ObjetoNumero.MultiplicarDigitos);
end;

procedure TFormNumeros.ItemEliminarCerosClick(Sender: TObject);
begin
  EditResultado.Text := 'Sin Ceros: ' + IntToStr(ObjetoNumero.EliminarCeros);
end;

procedure TFormNumeros.ItemDigitosOrdenadosClick(Sender: TObject);
begin
  if ObjetoNumero.DigitosOrdenadosAsc then
    EditResultado.Text := 'VERDADERO: Ordenados Ascendentemente'
  else
    EditResultado.Text := 'FALSO: No están ordenados';
end;

procedure TFormNumeros.ItemSumaParesEImparesClick(Sender: TObject);
var
  SumaP, SumaI: Cardinal;
begin
  ObjetoNumero.SumaParesEImpares(SumaP, SumaI);
  EditResultado.Text := 'Pares: ' + IntToStr(SumaP) + ' | Impares: ' + IntToStr(SumaI);
end;

// ============================================================================
// EVENTOS EXÁMENES FINALES
// ============================================================================

procedure TFormNumeros.ItemMitadDerechaCapicuaClick(Sender: TObject);
begin
  EditResultado.Text := ObjetoNumero.MitadDerechaCapicua;
end;

procedure TFormNumeros.ItemMitadIzquierdaCapicuaClick(Sender: TObject);
begin
  EditResultado.Text := ObjetoNumero.MitadIzquierdaCapicua;
end;

procedure TFormNumeros.ItemPrimeroYUltimoPrimosClick(Sender: TObject);
begin
  if ObjetoNumero.PrimeroYUltimoDigitoPrimos then
    EditResultado.Text := 'VÁLIDO: Primer y Último Dígito son Primos'
  else
    EditResultado.Text := 'NO CUMPLE: Uno o ambos no son primos';
end;

procedure TFormNumeros.ItemEliminarRepetidosClick(Sender: TObject);
begin
  EditResultado.Text := 'Dígitos Únicos: ' + IntToStr(ObjetoNumero.EliminarDigitosRepetidos);
end;

procedure TFormNumeros.ItemSepararMenoresMayoresClick(Sender: TObject);
var
  Crit: Byte;
  Men, May: Cardinal;
begin
  if ObtenerParametroByte(Crit) then
  begin
    ObjetoNumero.SepararDigitosMenoresYMayores(Crit, Men, May);
    EditResultado.Text := 'Menores a ' + IntToStr(Crit) + ': ' + IntToStr(Men) + 
                          ' | Mayores o iguales: ' + IntToStr(May);
  end;
end;

// ============================================================================
// EVENTOS BASES Y BITS
// ============================================================================

procedure TFormNumeros.ItemConvertirBinarioClick(Sender: TObject);
begin
  EditResultado.Text := 'Binario: ' + UAtajosNumeros.ConvertirABinario(ObjetoNumero.ObtenerValor);
end;

procedure TFormNumeros.ItemConvertirOctalClick(Sender: TObject);
begin
  EditResultado.Text := 'Octal: ' + UAtajosNumeros.ConvertirAOctal(ObjetoNumero.ObtenerValor);
end;

procedure TFormNumeros.ItemConvertirHexadecimalClick(Sender: TObject);
begin
  EditResultado.Text := 'Hexadecimal: ' + UAtajosNumeros.ConvertirAHexadecimal(ObjetoNumero.ObtenerValor);
end;

procedure TFormNumeros.ItemPalindromoBinarioClick(Sender: TObject);
var
  Bin: string;
begin
  Bin := UAtajosNumeros.ConvertirABinario(ObjetoNumero.ObtenerValor);
  if UAtajosNumeros.EsPalindromoBinario(ObjetoNumero.ObtenerValor) then
    EditResultado.Text := 'Sí es palíndromo en binario (' + Bin + ')'
  else
    EditResultado.Text := 'No es palíndromo en binario (' + Bin + ')';
end;

procedure TFormNumeros.ItemContarBitsUnoClick(Sender: TObject);
begin
  EditResultado.Text := 'Bits 1: ' + IntToStr(UAtajosNumeros.ContarBitsUno(ObjetoNumero.ObtenerValor));
end;

end.

