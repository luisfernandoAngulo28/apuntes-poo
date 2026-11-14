unit UFCadenasAtajos;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs,
  Vcl.StdCtrls, Vcl.Menus, UCCadena, UAtajosCadenas;

type
  TFormCadenas = class(TForm)
    LabelEntrada: TLabel;
    EditEntrada: TEdit;
    LabelResultado: TLabel;
    EditResultado: TEdit;
    LabelParametro: TLabel;
    EditParametro: TEdit;
    MemoSalida: TMemo;
    MainMenuPrincipal: TMainMenu;
    
    // Menús Principales
    MenuObjetoPOO: TMenuItem;
    ItemCrearObjeto: TMenuItem;
    ItemCargarObjeto: TMenuItem;
    ItemDescargarObjeto: TMenuItem;
    
    MenuBasicos: TMenuItem;
    ItemLongitud: TMenuItem;
    ItemPrimeraLetra: TMenuItem;
    ItemUltimaLetra: TMenuItem;
    ItemContarVocales: TMenuItem;
    ItemContarConsonantes: TMenuItem;
    ItemContarMayusculas: TMenuItem;
    ItemEsPalindromo: TMenuItem;
    
    MenuPalabras: TMenuItem;
    ItemContarPalabras: TMenuItem;
    ItemExtraerPalabra: TMenuItem;
    ItemInvertirSegundaPalabra: TMenuItem;
    ItemEliminarPalabra: TMenuItem;
    ItemDosVocalesJuntas: TMenuItem;
    
    MenuExamenes: TMenuItem;
    ItemInvertirPorMitades: TMenuItem;
    ItemOrdenarConsonante: TMenuItem;
    ItemOrdenarSegundaPalabra: TMenuItem;
    ItemFormatoTitulo: TMenuItem;
    ItemGenerarArbol: TMenuItem;
    ItemCifradoCesar: TMenuItem;
    ItemEliminarEspaciosRepetidos: TMenuItem;

    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure ItemCrearObjetoClick(Sender: TObject);
    procedure ItemCargarObjetoClick(Sender: TObject);
    procedure ItemDescargarObjetoClick(Sender: TObject);
    
    // Eventos Básicos
    procedure ItemLongitudClick(Sender: TObject);
    procedure ItemPrimeraLetraClick(Sender: TObject);
    procedure ItemUltimaLetraClick(Sender: TObject);
    procedure ItemContarVocalesClick(Sender: TObject);
    procedure ItemContarConsonantesClick(Sender: TObject);
    procedure ItemContarMayusculasClick(Sender: TObject);
    procedure ItemEsPalindromoClick(Sender: TObject);
    
    // Eventos Palabras
    procedure ItemContarPalabrasClick(Sender: TObject);
    procedure ItemExtraerPalabraClick(Sender: TObject);
    procedure ItemInvertirSegundaPalabraClick(Sender: TObject);
    procedure ItemEliminarPalabraClick(Sender: TObject);
    procedure ItemDosVocalesJuntasClick(Sender: TObject);
    
    // Eventos Exámenes
    procedure ItemInvertirPorMitadesClick(Sender: TObject);
    procedure ItemOrdenarConsonanteClick(Sender: TObject);
    procedure ItemOrdenarSegundaPalabraClick(Sender: TObject);
    procedure ItemFormatoTituloClick(Sender: TObject);
    procedure ItemGenerarArbolClick(Sender: TObject);
    procedure ItemCifradoCesarClick(Sender: TObject);
    procedure ItemEliminarEspaciosRepetidosClick(Sender: TObject);
  private
    ObjetoTexto: ClaseCadena; // Instancia POO encapsulada en el Form
    function ObtenerTextoEntrada: string;
    function ObtenerParametroEntero(out ValorEntero: Integer): Boolean;
  public
  end;

var
  FormCadenas: TFormCadenas;

implementation

{$R *.dfm}

{ TFormCadenas }

procedure TFormCadenas.FormCreate(Sender: TObject);
begin
  ObjetoTexto := ClaseCadena.Create;
end;

procedure TFormCadenas.FormDestroy(Sender: TObject);
begin
  ObjetoTexto.Free;
end;

function TFormCadenas.ObtenerTextoEntrada: string;
begin
  Result := EditEntrada.Text;
end;

function TFormCadenas.ObtenerParametroEntero(out ValorEntero: Integer): Boolean;
begin
  Result := TryStrToInt(Trim(EditParametro.Text), ValorEntero);
  if not Result then
    ShowMessage('Por favor, ingrese un número entero válido en el campo Parámetro.');
end;

procedure TFormCadenas.ItemCrearObjetoClick(Sender: TObject);
begin
  if Assigned(ObjetoTexto) then
    ObjetoTexto.Free;
  ObjetoTexto := ClaseCadena.Create;
  ShowMessage('Objeto ClaseCadena instanciado correctamente en memoria.');
end;

procedure TFormCadenas.ItemCargarObjetoClick(Sender: TObject);
begin
  ObjetoTexto.Cargar(ObtenerTextoEntrada);
  ShowMessage('Texto cargado exitosamente en el atributo privado del objeto.');
end;

procedure TFormCadenas.ItemDescargarObjetoClick(Sender: TObject);
begin
  EditResultado.Text := ObjetoTexto.Descargar;
end;

// ============================================================================
// EVENTOS BÁSICOS
// ============================================================================

procedure TFormCadenas.ItemLongitudClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoTexto.Longitud) + ' caracteres';
end;

procedure TFormCadenas.ItemPrimeraLetraClick(Sender: TObject);
begin
  EditResultado.Text := ObjetoTexto.PrimeraLetra;
end;

procedure TFormCadenas.ItemUltimaLetraClick(Sender: TObject);
begin
  EditResultado.Text := ObjetoTexto.UltimaLetra;
end;

procedure TFormCadenas.ItemContarVocalesClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoTexto.ContarVocales) + ' vocales';
end;

procedure TFormCadenas.ItemContarConsonantesClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoTexto.ContarConsonantes) + ' consonantes';
end;

procedure TFormCadenas.ItemContarMayusculasClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoTexto.ContarMayusculas) + ' mayúsculas';
end;

procedure TFormCadenas.ItemEsPalindromoClick(Sender: TObject);
begin
  if ObjetoTexto.EsPalindromo then
    EditResultado.Text := 'VERDADERO: Es palíndroma'
  else
    EditResultado.Text := 'FALSO: No es palíndroma';
end;

// ============================================================================
// EVENTOS MANIPULACIÓN DE PALABRAS
// ============================================================================

procedure TFormCadenas.ItemContarPalabrasClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoTexto.ContarPalabras) + ' palabras';
end;

procedure TFormCadenas.ItemExtraerPalabraClick(Sender: TObject);
var
  K: Integer;
begin
  if ObtenerParametroEntero(K) then
    EditResultado.Text := ObjetoTexto.ExtraerPalabra(K);
end;

procedure TFormCadenas.ItemInvertirSegundaPalabraClick(Sender: TObject);
begin
  ObjetoTexto.InvertirSegundaPalabra;
  EditResultado.Text := ObjetoTexto.Descargar;
end;

procedure TFormCadenas.ItemEliminarPalabraClick(Sender: TObject);
var
  K: Integer;
begin
  if ObtenerParametroEntero(K) then
  begin
    ObjetoTexto.EliminarPalabra(K);
    EditResultado.Text := ObjetoTexto.Descargar;
  end;
end;

procedure TFormCadenas.ItemDosVocalesJuntasClick(Sender: TObject);
begin
  EditResultado.Text := IntToStr(ObjetoTexto.ContarPalabrasDosVocalesJuntas) + ' palabras con 2 vocales juntas';
end;

// ============================================================================
// EVENTOS EXÁMENES Y TRANSFORMACIONES
// ============================================================================

procedure TFormCadenas.ItemInvertirPorMitadesClick(Sender: TObject);
begin
  ObjetoTexto.InvertirPorMitades;
  EditResultado.Text := ObjetoTexto.Descargar;
end;

procedure TFormCadenas.ItemOrdenarConsonanteClick(Sender: TObject);
begin
  // Algoritmo Examen 2024-1 Z2: Ordenar la palabra que comienza en consonante
  EditResultado.Text := UAtajosCadenas.OrdenarPalabraQueComienzaEnConsonante(ObtenerTextoEntrada);
end;

procedure TFormCadenas.ItemOrdenarSegundaPalabraClick(Sender: TObject);
begin
  ObjetoTexto.OrdenarSegundaPalabra;
  EditResultado.Text := ObjetoTexto.Descargar;
end;

procedure TFormCadenas.ItemFormatoTituloClick(Sender: TObject);
begin
  ObjetoTexto.FormatoTitulo;
  EditResultado.Text := ObjetoTexto.Descargar;
end;

procedure TFormCadenas.ItemGenerarArbolClick(Sender: TObject);
begin
  MemoSalida.Text := ObjetoTexto.GenerarArbol;
end;

procedure TFormCadenas.ItemCifradoCesarClick(Sender: TObject);
var
  Clave: Integer;
begin
  if ObtenerParametroEntero(Clave) then
  begin
    ObjetoTexto.CifrarCesar(Clave);
    EditResultado.Text := ObjetoTexto.Descargar;
  end;
end;

procedure TFormCadenas.ItemEliminarEspaciosRepetidosClick(Sender: TObject);
begin
  ObjetoTexto.EliminarEspaciosRepetidos;
  EditResultado.Text := ObjetoTexto.Descargar;
end;

end.

