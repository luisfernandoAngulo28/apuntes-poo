unit UnitClaseNumero;

interface

uses
  SysUtils;

type
  { Clase TNumero: Encapsula un número natural y provee métodos modulares }
  TNumero = class
  private
    FValor: Cardinal;
    function EsPrimoAux(d: Byte): Boolean;
  public
    // Constructores
    constructor Create; overload;
    constructor Create(AValor: Cardinal); overload;

    // Propiedad principal
    property Valor: Cardinal read FValor write FValor;

    // Métodos de carga y lectura
    procedure Cargar(AValor: Cardinal);
    function Descargar: Cardinal;

    // Métodos del Práctico #7 y Tarea de Clase
    function SumarDigitosPrimos: Cardinal;
    function FormarSoloPares: Cardinal;
    function SumarMultiplosDe3: Cardinal;
    function InvertirNumero: Cardinal;
    function EsCapicua: Boolean;
    function SumaImparesMayores3: Cardinal;
    function DigitoMayorIndicesImpares: Integer;
    function SumaDigitos: Cardinal;
    function PromedioDigitosMenores7: Double;
    procedure MayorYMenorDigito(var digMayor, digMenor: Byte);
    procedure SepararParesImpares(var numPares, numImpares: Cardinal);
    function MayorDigitoPar: Integer;
    function DigitosMultiplosDe3Str: String;
    procedure PrimerYUltimoDigito(var primero, ultimo: Byte);
    function EliminarPrimerYUltimoDigito: Cardinal;
    function ContarMultiplosDeCuatro: Cardinal;
    function MenorDigitoMultiploDeTres: Integer;
    function DecimalABinario: String;
    function DecimalAHexadecimal: String;
    function DecimalAOctal: String;
    function PromedioMultiplos3y5: Double;
    function PromedioDigitosPrimos: Double;
    function FormarNumeroPrimos: Cardinal;
    function CantidadDigitos: Cardinal;
  end;

implementation

{ TNumero }

constructor TNumero.Create;
begin
  inherited Create;
  FValor := 0;
end;

constructor TNumero.Create(AValor: Cardinal);
begin
  inherited Create;
  FValor := AValor;
end;

procedure TNumero.Cargar(AValor: Cardinal);
begin
  FValor := AValor;
end;

function TNumero.Descargar: Cardinal;
begin
  Result := FValor;
end;

function TNumero.EsPrimoAux(d: Byte): Boolean;
begin
  Result := (d = 2) or (d = 3) or (d = 5) or (d = 7);
end;

function TNumero.CantidadDigitos: Cardinal;
var
  n, c: Cardinal;
begin
  if FValor = 0 then Exit(1);
  n := FValor;
  c := 0;
  while n > 0 do
  begin
    Inc(c);
    n := n div 10;
  end;
  Result := c;
end;

function TNumero.SumarDigitosPrimos: Cardinal;
var
  n, d, suma: Cardinal;
begin
  n := FValor;
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimoAux(d) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;

function TNumero.FormarSoloPares: Cardinal;
var
  n, d, res, pot: Cardinal;
begin
  n := FValor;
  res := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  Result := res;
end;

function TNumero.SumarMultiplosDe3: Cardinal;
var
  n, d, suma: Cardinal;
begin
  n := FValor;
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 3 = 0 then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;

function TNumero.InvertirNumero: Cardinal;
var
  n, inv: Cardinal;
begin
  n := FValor;
  inv := 0;
  while n > 0 do
  begin
    inv := (inv * 10) + (n mod 10);
    n := n div 10;
  end;
  Result := inv;
end;

function TNumero.EsCapicua: Boolean;
begin
  Result := (FValor = InvertirNumero);
end;

function TNumero.SumaImparesMayores3: Cardinal;
var
  n, d, suma: Cardinal;
begin
  n := FValor;
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 <> 0) and (d > 3) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;

function TNumero.DigitoMayorIndicesImpares: Integer;
var
  s: String;
  i, maxD, valD: Integer;
begin
  s := IntToStr(FValor);
  maxD := -1;
  i := 1;
  while i <= Length(s) do
  begin
    valD := Ord(s[i]) - Ord('0');
    if valD > maxD then
      maxD := valD;
    i := i + 2;
  end;
  Result := maxD;
end;

function TNumero.SumaDigitos: Cardinal;
var
  n, suma: Cardinal;
begin
  n := FValor;
  suma := 0;
  while n > 0 do
  begin
    suma := suma + (n mod 10);
    n := n div 10;
  end;
  Result := suma;
end;

function TNumero.PromedioDigitosMenores7: Double;
var
  n, d, suma, cont: Cardinal;
begin
  n := FValor;
  suma := 0;
  cont := 0;
  if n = 0 then Exit(0.0);
  while n > 0 do
  begin
    d := n mod 10;
    if d < 7 then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then Result := suma / cont else Result := 0.0;
end;

procedure TNumero.MayorYMenorDigito(var digMayor, digMenor: Byte);
var
  n: Cardinal;
  d: Byte;
begin
  if FValor = 0 then
  begin
    digMayor := 0;
    digMenor := 0;
    Exit;
  end;
  n := FValor;
  digMayor := 0;
  digMenor := 9;
  while n > 0 do
  begin
    d := n mod 10;
    if d > digMayor then digMayor := d;
    if d < digMenor then digMenor := d;
    n := n div 10;
  end;
end;

procedure TNumero.SepararParesImpares(var numPares, numImpares: Cardinal);
var
  n, d, potPar, potImpar: Cardinal;
begin
  n := FValor;
  numPares := 0;
  numImpares := 0;
  potPar := 1;
  potImpar := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      numPares := numPares + (d * potPar);
      potPar := potPar * 10;
    end
    else
    begin
      numImpares := numImpares + (d * potImpar);
      potImpar := potImpar * 10;
    end;
    n := n div 10;
  end;
end;

function TNumero.MayorDigitoPar: Integer;
var
  n, d: Cardinal;
  mayor: Integer;
begin
  n := FValor;
  mayor := -1;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) and (Integer(d) > mayor) then
      mayor := d;
    n := n div 10;
  end;
  Result := mayor;
end;

function TNumero.DigitosMultiplosDe3Str: String;
var
  s, res: String;
  i, d: Integer;
begin
  s := IntToStr(FValor);
  res := '';
  for i := 1 to Length(s) do
  begin
    d := Ord(s[i]) - Ord('0');
    if d mod 3 = 0 then
    begin
      if res <> '' then res := res + ', ';
      res := res + s[i];
    end;
  end;
  if res = '' then Result := 'Ninguno' else Result := res;
end;

procedure TNumero.PrimerYUltimoDigito(var primero, ultimo: Byte);
var
  n: Cardinal;
begin
  n := FValor;
  ultimo := n mod 10;
  while n >= 10 do
    n := n div 10;
  primero := n;
end;

function TNumero.EliminarPrimerYUltimoDigito: Cardinal;
var
  n, pot: Cardinal;
begin
  n := FValor;
  if n < 100 then Exit(0);
  n := n div 10;
  pot := 1;
  while (n div pot) >= 10 do
    pot := pot * 10;
  n := n mod pot;
  Result := n;
end;

function TNumero.ContarMultiplosDeCuatro: Cardinal;
var
  n, d, c: Cardinal;
begin
  n := FValor;
  c := 0;
  if n = 0 then Exit(1);
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 4 = 0 then Inc(c);
    n := n div 10;
  end;
  Result := c;
end;

function TNumero.MenorDigitoMultiploDeTres: Integer;
var
  n, d: Cardinal;
  menor: Integer;
begin
  n := FValor;
  menor := 10;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) and (Integer(d) < menor) then
      menor := d;
    n := n div 10;
  end;
  if menor = 10 then Result := -1 else Result := menor;
end;

function TNumero.DecimalABinario: String;
var
  n: Cardinal;
  res: String;
begin
  if FValor = 0 then Exit('0');
  n := FValor;
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 2) + res;
    n := n div 2;
  end;
  Result := res;
end;

function TNumero.DecimalAHexadecimal: String;
const
  HexChars: array[0..15] of Char = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F');
var
  n: Cardinal;
  res: String;
begin
  if FValor = 0 then Exit('0');
  n := FValor;
  res := '';
  while n > 0 do
  begin
    res := HexChars[n mod 16] + res;
    n := n div 16;
  end;
  Result := res;
end;

function TNumero.DecimalAOctal: String;
var
  n: Cardinal;
  res: String;
begin
  if FValor = 0 then Exit('0');
  n := FValor;
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 8) + res;
    n := n div 8;
  end;
  Result := res;
end;

function TNumero.PromedioMultiplos3y5: Double;
var
  n, d, suma, cont: Cardinal;
begin
  n := FValor;
  suma := 0;
  cont := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) or (d mod 5 = 0) then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then Result := suma / cont else Result := 0.0;
end;

function TNumero.PromedioDigitosPrimos: Double;
var
  n, d, suma, cont: Cardinal;
begin
  n := FValor;
  suma := 0;
  cont := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimoAux(d) then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then Result := suma / cont else Result := 0.0;
end;

function TNumero.FormarNumeroPrimos: Cardinal;
var
  n, d, res, pot: Cardinal;
begin
  n := FValor;
  res := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimoAux(d) then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  Result := res;
end;

end.
