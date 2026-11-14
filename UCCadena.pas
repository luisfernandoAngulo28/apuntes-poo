unit UCCadena;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

{ ============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE CIENCIAS DE LA COMPUTACIÓN Y TECNOLOGÍA
  MATERIA: INTRODUCCIÓN A LA INFORMÁTICA (INF-110)
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
  
  CLASE ORIENTADA A OBJETOS: ClaseCadena
  Encapsulamiento del atributo Valor: string con métodos canónicos de examen.
  ============================================================================ }

interface

uses
  SysUtils, UAtajosCadenas;

type
  ClaseCadena = class
  private
    Valor: string; // Atributo encapsulado privado
  public
    // Métodos Canónicos de la Clase
    constructor Create;
    procedure Cargar(const NuevoTexto: string);
    function Descargar: string;
    
    // Métodos de Inspección y Conteo
    function Longitud: Integer;
    function PrimeraLetra: Char;
    function UltimaLetra: Char;
    function ContarVocales: Integer;
    function ContarConsonantes: Integer;
    function ContarMayusculas: Integer;
    function ContarMinusculas: Integer;
    function ContarPalabras: Integer;
    function ExtraerPalabra(PosicionPalabra: Integer): string;
    function ContarPalabrasDosVocalesJuntas: Integer;
    function EsPalindromo: Boolean;
    function BuscarPosiciones(CaracterBuscado: Char): string;

    // Métodos de Mutación y Transformación
    procedure Invertir;
    procedure InvertirPorMitades;
    procedure InvertirSegundaPalabra;
    procedure InvertirPalabraK(PosicionPalabra: Integer);
    procedure OrdenarCaracteres;
    procedure OrdenarSegundaPalabra;
    procedure OrdenarUltimaPalabra;
    procedure EliminarPalabra(PosicionPalabra: Integer);
    procedure FormatoTitulo;
    procedure EliminarEspaciosRepetidos;
    procedure CifrarCesar(Desplazamiento: Integer);
    
    // Patrones de examen
    function GenerarArbol: string;
    function IntercalarCon(const OtraCadena: string): string;
  end;

implementation

constructor ClaseCadena.Create;
begin
  Valor := '';
end;

procedure ClaseCadena.Cargar(const NuevoTexto: string);
begin
  Valor := NuevoTexto;
end;

function ClaseCadena.Descargar: string;
begin
  Result := Valor;
end;

function ClaseCadena.Longitud: Integer;
begin
  Result := Length(Valor);
end;

function ClaseCadena.PrimeraLetra: Char;
begin
  Result := UAtajosCadenas.PrimeraLetra(Valor);
end;

function ClaseCadena.UltimaLetra: Char;
begin
  Result := UAtajosCadenas.UltimaLetra(Valor);
end;

function ClaseCadena.ContarVocales: Integer;
begin
  Result := UAtajosCadenas.ContarVocales(Valor);
end;

function ClaseCadena.ContarConsonantes: Integer;
begin
  Result := UAtajosCadenas.ContarConsonantes(Valor);
end;

function ClaseCadena.ContarMayusculas: Integer;
begin
  Result := UAtajosCadenas.ContarMayusculas(Valor);
end;

function ClaseCadena.ContarMinusculas: Integer;
begin
  Result := UAtajosCadenas.ContarMinusculas(Valor);
end;

function ClaseCadena.ContarPalabras: Integer;
begin
  Result := UAtajosCadenas.ContarPalabras(Valor);
end;

function ClaseCadena.ExtraerPalabra(PosicionPalabra: Integer): string;
begin
  Result := UAtajosCadenas.ExtraerPalabra(Valor, PosicionPalabra);
end;

function ClaseCadena.ContarPalabrasDosVocalesJuntas: Integer;
begin
  Result := UAtajosCadenas.ContarPalabrasDosVocalesJuntas(Valor);
end;

function ClaseCadena.EsPalindromo: Boolean;
begin
  Result := UAtajosCadenas.EsPalindromo(Valor);
end;

function ClaseCadena.BuscarPosiciones(CaracterBuscado: Char): string;
begin
  Result := UAtajosCadenas.BuscarPosicionesCaracter(Valor, CaracterBuscado);
end;

procedure ClaseCadena.Invertir;
begin
  Valor := UAtajosCadenas.InvertirCadena(Valor);
end;

procedure ClaseCadena.InvertirPorMitades;
begin
  Valor := UAtajosCadenas.InvertirPorMitades(Valor);
end;

procedure ClaseCadena.InvertirSegundaPalabra;
begin
  Valor := UAtajosCadenas.InvertirSegundaPalabra(Valor);
end;

procedure ClaseCadena.InvertirPalabraK(PosicionPalabra: Integer);
begin
  Valor := UAtajosCadenas.InvertirPalabraK(Valor, PosicionPalabra);
end;

procedure ClaseCadena.OrdenarCaracteres;
begin
  Valor := UAtajosCadenas.OrdenarCaracteresAscendente(Valor);
end;

procedure ClaseCadena.OrdenarSegundaPalabra;
begin
  Valor := UAtajosCadenas.OrdenarSegundaPalabra(Valor);
end;

procedure ClaseCadena.OrdenarUltimaPalabra;
begin
  Valor := UAtajosCadenas.OrdenarUltimaPalabra(Valor);
end;

procedure ClaseCadena.EliminarPalabra(PosicionPalabra: Integer);
begin
  Valor := UAtajosCadenas.EliminarPalabraK(Valor, PosicionPalabra);
end;

procedure ClaseCadena.FormatoTitulo;
begin
  Valor := UAtajosCadenas.FormatoTitulo(Valor);
end;

procedure ClaseCadena.EliminarEspaciosRepetidos;
begin
  Valor := UAtajosCadenas.EliminarEspaciosRepetidos(Valor);
end;

procedure ClaseCadena.CifrarCesar(Desplazamiento: Integer);
begin
  Valor := UAtajosCadenas.CifradoCesar(Valor, Desplazamiento);
end;

function ClaseCadena.GenerarArbol: string;
begin
  Result := UAtajosCadenas.GenerarCadenaArbol(Valor);
end;

function ClaseCadena.IntercalarCon(const OtraCadena: string): string;
begin
  Result := UAtajosCadenas.IntercalarCadenas(Valor, OtraCadena);
end;

end.

