unit UAtajosCadenas;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

{ ============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE CIENCIAS DE LA COMPUTACIÓN Y TECNOLOGÍA
  MATERIA: INTRODUCCIÓN A LA INFORMÁTICA (INF-110)
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
  
  LIBRERÍA MODULAR ATÓMICA: HOJA DE ATAJOS MAESTRA PARA CADENAS (STRINGS)
  Filosofía: "Divide y Vencerás" · Clean Code · Programación Modular
  ============================================================================ }

interface

uses
  SysUtils;

// ============================================================================
// BLOQUE 0: FUNCIONES AUXILIARES ATÓMICAS (BASE INDISPENSABLE)
// ============================================================================
function EsVocal(C: Char): Boolean;
function EsConsonante(C: Char): Boolean;
function EsLetra(C: Char): Boolean;
function EsDigito(C: Char): Boolean;
function UpCaseChar(C: Char): Char;
function LowerCaseChar(C: Char): Char;

// Reemplazos canónicos manuales (sin depender de librerías del sistema)
function LongitudManual(const Cadena: string): Integer;
function CopiarManual(const Cadena: string; Desde, Cantidad: Integer): string;
function PosicionManual(const Subcadena, Cadena: string): Integer;
function TrimManual(const Cadena: string): string;

// ============================================================================
// BLOQUE 1: MÉTODOS BÁSICOS Y ESTADÍSTICAS DE CARACTERES
// ============================================================================
function PrimeraLetra(const Cadena: string): Char;
function UltimaLetra(const Cadena: string): Char;
function ContarVocales(const Cadena: string): Integer;
function ContarConsonantes(const Cadena: string): Integer;
function ContarMayusculas(const Cadena: string): Integer;
function ContarMinusculas(const Cadena: string): Integer;
function ContarOcurrenciasCaracter(const Cadena: string; CaracterBuscado: Char): Integer;
function BuscarPosicionesCaracter(const Cadena: string; CaracterBuscado: Char): string;

// ============================================================================
// BLOQUE 2: INVERSIÓN Y PALÍNDROMOS (ALGORITMOS ESTRELLA DE EXAMEN)
// ============================================================================
function InvertirCadena(const Cadena: string): string;
function EsPalindromo(const Cadena: string): Boolean;
// Examen 2023-2 SF: Invertir por mitades manteniendo el carácter central impar
// Ej: 'cadenas' -> mitad 1 'cad' -> 'dac', centro 'e', mitad 2 'nas' -> 'san' => 'dacesan'
function InvertirPorMitades(const Cadena: string): string;

// ============================================================================
// BLOQUE 3: MANIPULACIÓN DE PALABRAS (CONTEO, EXTRACCIÓN Y MODIFICACIÓN)
// ============================================================================
function ContarPalabras(const Cadena: string): Integer;
function ExtraerPalabra(const Cadena: string; PosicionPalabra: Integer): string;
function ReemplazarPalabra(const Cadena: string; PosicionPalabra: Integer; const NuevaPalabra: string): string;
function InvertirPalabraK(const Cadena: string; K: Integer): string;
function InvertirSegundaPalabra(const Cadena: string): string;
function EliminarPalabraK(const Cadena: string; K: Integer): string;
function TieneDosVocalesJuntas(const Palabra: string): Boolean;
function ContarPalabrasDosVocalesJuntas(const Cadena: string): Integer;

// ============================================================================
// BLOQUE 4: ORDENAMIENTO DE CARACTERES Y PALABRAS
// ============================================================================
function OrdenarCaracteresAscendente(const Cadena: string): string;
function OrdenarCaracteresDescendente(const Cadena: string): string;
function OrdenarSegundaPalabra(const Cadena: string): string;
function OrdenarUltimaPalabra(const Cadena: string): string;
// Examen 2024-1 Z2 Pregunta 3: Ordenar la palabra que comienza en una consonante
// Ej: 'Ana estudia lenguaje' -> la palabra 'lenguaje' empieza con 'l' -> 'aeegjlnu'
function OrdenarPalabraQueComienzaEnConsonante(const Frase: string): string;

// ============================================================================
// BLOQUE 5: TRANSFORMACIONES, CIFRADO Y PATRONES VISUALES
// ============================================================================
function FormatoTitulo(const Cadena: string): string;
function EliminarEspaciosRepetidos(const Cadena: string): string;
function EliminarCaracteresRepetidos(const Cadena: string): string;
function IntercalarCadenas(const Cadena1, Cadena2: string): string;
function CifradoCesar(const Cadena: string; Desplazamiento: Integer): string;
// Tarea #8 Presencial: Generar visualización en forma de árbol
// 'Cadena' -> 'Cadena\nCaden\nCade\nCad\nCa\nC'
function GenerarCadenaArbol(const Cadena: string): string;

implementation

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 0: FUNCIONES AUXILIARES ATÓMICAS
// ============================================================================

function EsVocal(C: Char): Boolean;
var
  Mayus: Char;
begin
  Mayus := UpCaseChar(C);
  Result := Mayus in ['A', 'E', 'I', 'O', 'U'];
end;

function EsConsonante(C: Char): Boolean;
var
  Mayus: Char;
begin
  Mayus := UpCaseChar(C);
  Result := (Mayus in ['A'..'Z']) and not (Mayus in ['A', 'E', 'I', 'O', 'U']);
end;

function EsLetra(C: Char): Boolean;
var
  Mayus: Char;
begin
  Mayus := UpCaseChar(C);
  Result := (Mayus in ['A'..'Z']);
end;

function EsDigito(C: Char): Boolean;
begin
  Result := C in ['0'..'9'];
end;

function UpCaseChar(C: Char): Char;
begin
  if (C >= 'a') and (C <= 'z') then
    Result := Chr(Ord(C) - 32)
  else
    Result := C;
end;

function LowerCaseChar(C: Char): Char;
begin
  if (C >= 'A') and (C <= 'Z') then
    Result := Chr(Ord(C) + 32)
  else
    Result := C;
end;

function LongitudManual(const Cadena: string): Integer;
begin
  Result := Length(Cadena);
end;

function CopiarManual(const Cadena: string; Desde, Cantidad: Integer): string;
var
  i, Limite, LongitudCadena: Integer;
  ResultadoTexto: string;
begin
  ResultadoTexto := '';
  LongitudCadena := Length(Cadena);
  if (Desde >= 1) and (Desde <= LongitudCadena) and (Cantidad > 0) then
  begin
    Limite := Desde + Cantidad - 1;
    if Limite > LongitudCadena then
      Limite := LongitudCadena;
    for i := Desde to Limite do
      ResultadoTexto := ResultadoTexto + Cadena[i];
  end;
  Result := ResultadoTexto;
end;

function PosicionManual(const Subcadena, Cadena: string): Integer;
var
  i, j, LongSub, LongCad: Integer;
  Coincide: Boolean;
begin
  LongSub := Length(Subcadena);
  LongCad := Length(Cadena);
  if (LongSub = 0) or (LongSub > LongCad) then
    Exit(0);

  for i := 1 to (LongCad - LongSub + 1) do
  begin
    Coincide := True;
    for j := 1 to LongSub do
    begin
      if Cadena[i + j - 1] <> Subcadena[j] then
      begin
        Coincide := False;
        Break;
      end;
    end;
    if Coincide then
      Exit(i);
  end;
  Result := 0;
end;

function TrimManual(const Cadena: string): string;
var
  InicioIndice, FinIndice: Integer;
begin
  InicioIndice := 1;
  FinIndice := Length(Cadena);

  while (InicioIndice <= FinIndice) and (Cadena[InicioIndice] = ' ') do
    Inc(InicioIndice);

  while (FinIndice >= InicioIndice) and (Cadena[FinIndice] = ' ') do
    Dec(FinIndice);

  if InicioIndice > FinIndice then
    Result := ''
  else
    Result := CopiarManual(Cadena, InicioIndice, FinIndice - InicioIndice + 1);
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 1: MÉTODOS BÁSICOS Y ESTADÍSTICAS
// ============================================================================

function PrimeraLetra(const Cadena: string): Char;
var
  CadenaLimpia: string;
begin
  CadenaLimpia := TrimManual(Cadena);
  if Length(CadenaLimpia) > 0 then
    Result := CadenaLimpia[1]
  else
    Result := #0;
end;

function UltimaLetra(const Cadena: string): Char;
var
  CadenaLimpia: string;
begin
  CadenaLimpia := TrimManual(Cadena);
  if Length(CadenaLimpia) > 0 then
    Result := CadenaLimpia[Length(CadenaLimpia)]
  else
    Result := #0;
end;

function ContarVocales(const Cadena: string): Integer;
var
  i, Contador: Integer;
begin
  Contador := 0;
  for i := 1 to Length(Cadena) do
  begin
    if EsVocal(Cadena[i]) then
      Inc(Contador);
  end;
  Result := Contador;
end;

function ContarConsonantes(const Cadena: string): Integer;
var
  i, Contador: Integer;
begin
  Contador := 0;
  for i := 1 to Length(Cadena) do
  begin
    if EsConsonante(Cadena[i]) then
      Inc(Contador);
  end;
  Result := Contador;
end;

function ContarMayusculas(const Cadena: string): Integer;
var
  i, Contador: Integer;
begin
  Contador := 0;
  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] in ['A'..'Z'] then
      Inc(Contador);
  end;
  Result := Contador;
end;

function ContarMinusculas(const Cadena: string): Integer;
var
  i, Contador: Integer;
begin
  Contador := 0;
  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] in ['a'..'z'] then
      Inc(Contador);
  end;
  Result := Contador;
end;

function ContarOcurrenciasCaracter(const Cadena: string; CaracterBuscado: Char): Integer;
var
  i, Contador: Integer;
  BuscadoMayus: Char;
begin
  Contador := 0;
  BuscadoMayus := UpCaseChar(CaracterBuscado);
  for i := 1 to Length(Cadena) do
  begin
    if UpCaseChar(Cadena[i]) = BuscadoMayus then
      Inc(Contador);
  end;
  Result := Contador;
end;

function BuscarPosicionesCaracter(const Cadena: string; CaracterBuscado: Char): string;
var
  i: Integer;
  BuscadoMayus: Char;
  ListaPosiciones: string;
begin
  ListaPosiciones := '';
  BuscadoMayus := UpCaseChar(CaracterBuscado);
  for i := 1 to Length(Cadena) do
  begin
    if UpCaseChar(Cadena[i]) = BuscadoMayus then
    begin
      if ListaPosiciones <> '' then
        ListaPosiciones := ListaPosiciones + ', ';
      ListaPosiciones := ListaPosiciones + IntToStr(i);
    end;
  end;
  Result := ListaPosiciones;
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 2: INVERSIÓN Y PALÍNDROMOS
// ============================================================================

function InvertirCadena(const Cadena: string): string;
var
  i, LongitudCadena: Integer;
  Invertida: string;
begin
  LongitudCadena := Length(Cadena);
  Invertida := '';
  for i := LongitudCadena downto 1 do
    Invertida := Invertida + Cadena[i];
  Result := Invertida;
end;

function EsPalindromo(const Cadena: string): Boolean;
var
  CadenaNormalizada: string;
  i: Integer;
begin
  CadenaNormalizada := '';
  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] <> ' ' then
      CadenaNormalizada := CadenaNormalizada + UpCaseChar(Cadena[i]);
  end;
  Result := (CadenaNormalizada = InvertirCadena(CadenaNormalizada)) and (Length(CadenaNormalizada) > 0);
end;

function InvertirPorMitades(const Cadena: string): string;
var
  LongitudCadena, Mitad, i: Integer;
  ParteIzquierda, ParteDerecha, CaracterCentro: string;
begin
  LongitudCadena := Length(Cadena);
  Mitad := LongitudCadena div 2;
  ParteIzquierda := '';
  ParteDerecha := '';
  CaracterCentro := '';

  for i := Mitad downto 1 do
    ParteIzquierda := ParteIzquierda + Cadena[i];

  if (LongitudCadena mod 2 <> 0) then
    CaracterCentro := Cadena[Mitad + 1];

  for i := LongitudCadena downto (LongitudCadena - Mitad + 1) do
    ParteDerecha := ParteDerecha + Cadena[i];

  Result := ParteIzquierda + CaracterCentro + ParteDerecha;
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 3: MANIPULACIÓN DE PALABRAS
// ============================================================================

function ContarPalabras(const Cadena: string): Integer;
var
  i, CantidadPalabras: Integer;
  DentroDePalabra: Boolean;
begin
  CantidadPalabras := 0;
  DentroDePalabra := False;

  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] <> ' ' then
    begin
      if not DentroDePalabra then
      begin
        Inc(CantidadPalabras);
        DentroDePalabra := True;
      end;
    end
    else
      DentroDePalabra := False;
  end;

  Result := CantidadPalabras;
end;

function ExtraerPalabra(const Cadena: string; PosicionPalabra: Integer): string;
var
  i, IndiceActual: Integer;
  DentroDePalabra: Boolean;
  PalabraAcumulada: string;
begin
  IndiceActual := 0;
  DentroDePalabra := False;
  PalabraAcumulada := '';

  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] <> ' ' then
    begin
      if not DentroDePalabra then
      begin
        Inc(IndiceActual);
        DentroDePalabra := True;
      end;
      if IndiceActual = PosicionPalabra then
        PalabraAcumulada := PalabraAcumulada + Cadena[i];
    end
    else
    begin
      if DentroDePalabra and (IndiceActual = PosicionPalabra) then
        Break;
      DentroDePalabra := False;
    end;
  end;

  Result := PalabraAcumulada;
end;

function ReemplazarPalabra(const Cadena: string; PosicionPalabra: Integer; const NuevaPalabra: string): string;
var
  i, Total, IndiceActual: Integer;
  PalabraActual, FraseResultado: string;
begin
  Total := ContarPalabras(Cadena);
  FraseResultado := '';

  for IndiceActual := 1 to Total do
  begin
    if IndiceActual = PosicionPalabra then
      PalabraActual := NuevaPalabra
    else
      PalabraActual := ExtraerPalabra(Cadena, IndiceActual);

    if FraseResultado <> '' then
      FraseResultado := FraseResultado + ' ';
    FraseResultado := FraseResultado + PalabraActual;
  end;

  Result := FraseResultado;
end;

function InvertirPalabraK(const Cadena: string; K: Integer): string;
var
  Palabra: string;
begin
  Palabra := ExtraerPalabra(Cadena, K);
  if Palabra <> '' then
    Result := ReemplazarPalabra(Cadena, K, InvertirCadena(Palabra))
  else
    Result := Cadena;
end;

function InvertirSegundaPalabra(const Cadena: string): string;
begin
  Result := InvertirPalabraK(Cadena, 2);
end;

function EliminarPalabraK(const Cadena: string; K: Integer): string;
var
  Total, IndiceActual: Integer;
  FraseResultado, PalabraActual: string;
begin
  Total := ContarPalabras(Cadena);
  FraseResultado := '';

  for IndiceActual := 1 to Total do
  begin
    if IndiceActual <> K then
    begin
      PalabraActual := ExtraerPalabra(Cadena, IndiceActual);
      if FraseResultado <> '' then
        FraseResultado := FraseResultado + ' ';
      FraseResultado := FraseResultado + PalabraActual;
    end;
  end;

  Result := FraseResultado;
end;

function TieneDosVocalesJuntas(const Palabra: string): Boolean;
var
  i: Integer;
begin
  Result := False;
  for i := 1 to Length(Palabra) - 1 do
  begin
    if EsVocal(Palabra[i]) and EsVocal(Palabra[i + 1]) then
      Exit(True);
  end;
end;

function ContarPalabrasDosVocalesJuntas(const Cadena: string): Integer;
var
  Total, i, Contador: Integer;
  PalabraActual: string;
begin
  Total := ContarPalabras(Cadena);
  Contador := 0;

  for i := 1 to Total do
  begin
    PalabraActual := ExtraerPalabra(Cadena, i);
    if TieneDosVocalesJuntas(PalabraActual) then
      Inc(Contador);
  end;

  Result := Contador;
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 4: ORDENAMIENTO
// ============================================================================

function OrdenarCaracteresAscendente(const Cadena: string): string;
var
  i, j: Integer;
  CaracterAuxiliar: Char;
  CadenaOrdenada: string;
begin
  CadenaOrdenada := Cadena;
  for i := 1 to Length(CadenaOrdenada) - 1 do
  begin
    for j := i + 1 to Length(CadenaOrdenada) do
    begin
      if UpCaseChar(CadenaOrdenada[i]) > UpCaseChar(CadenaOrdenada[j]) then
      begin
        CaracterAuxiliar := CadenaOrdenada[i];
        CadenaOrdenada[i] := CadenaOrdenada[j];
        CadenaOrdenada[j] := CaracterAuxiliar;
      end;
    end;
  end;
  Result := CadenaOrdenada;
end;

function OrdenarCaracteresDescendente(const Cadena: string): string;
var
  i, j: Integer;
  CaracterAuxiliar: Char;
  CadenaOrdenada: string;
begin
  CadenaOrdenada := Cadena;
  for i := 1 to Length(CadenaOrdenada) - 1 do
  begin
    for j := i + 1 to Length(CadenaOrdenada) do
    begin
      if UpCaseChar(CadenaOrdenada[i]) < UpCaseChar(CadenaOrdenada[j]) then
      begin
        CaracterAuxiliar := CadenaOrdenada[i];
        CadenaOrdenada[i] := CadenaOrdenada[j];
        CadenaOrdenada[j] := CaracterAuxiliar;
      end;
    end;
  end;
  Result := CadenaOrdenada;
end;

function OrdenarSegundaPalabra(const Cadena: string): string;
var
  Segunda: string;
begin
  Segunda := ExtraerPalabra(Cadena, 2);
  if Segunda <> '' then
    Result := ReemplazarPalabra(Cadena, 2, OrdenarCaracteresAscendente(Segunda))
  else
    Result := Cadena;
end;

function OrdenarUltimaPalabra(const Cadena: string): string;
var
  Total: Integer;
  Ultima: string;
begin
  Total := ContarPalabras(Cadena);
  if Total > 0 then
  begin
    Ultima := ExtraerPalabra(Cadena, Total);
    Result := ReemplazarPalabra(Cadena, Total, OrdenarCaracteresAscendente(Ultima));
  end
  else
    Result := Cadena;
end;

function OrdenarPalabraQueComienzaEnConsonante(const Frase: string): string;
var
  Total, i: Integer;
  PalabraActual: string;
begin
  Total := ContarPalabras(Frase);
  for i := 1 to Total do
  begin
    PalabraActual := ExtraerPalabra(Frase, i);
    if (Length(PalabraActual) > 0) and EsConsonante(PalabraActual[1]) then
    begin
      Result := OrdenarCaracteresAscendente(PalabraActual);
      Exit;
    end;
  end;
  Result := '';
end;

// ============================================================================
// IMPLEMENTACIÓN BLOQUE 5: TRANSFORMACIONES Y CIFRADO
// ============================================================================

function FormatoTitulo(const Cadena: string): string;
var
  i: Integer;
  CadenaFormateada: string;
  NuevaPalabra: Boolean;
begin
  CadenaFormateada := '';
  NuevaPalabra := True;

  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] <> ' ' then
    begin
      if NuevaPalabra then
      begin
        CadenaFormateada := CadenaFormateada + UpCaseChar(Cadena[i]);
        NuevaPalabra := False;
      end
      else
        CadenaFormateada := CadenaFormateada + LowerCaseChar(Cadena[i]);
    end
    else
    begin
      CadenaFormateada := CadenaFormateada + ' ';
      NuevaPalabra := True;
    end;
  end;

  Result := CadenaFormateada;
end;

function EliminarEspaciosRepetidos(const Cadena: string): string;
var
  i: Integer;
  CadenaLimpia: string;
  EspacioPrevio: Boolean;
begin
  CadenaLimpia := '';
  EspacioPrevio := False;

  for i := 1 to Length(Cadena) do
  begin
    if Cadena[i] <> ' ' then
    begin
      CadenaLimpia := CadenaLimpia + Cadena[i];
      EspacioPrevio := False;
    end
    else
    begin
      if not EspacioPrevio and (CadenaLimpia <> '') then
      begin
        CadenaLimpia := CadenaLimpia + ' ';
        EspacioPrevio := True;
      end;
    end;
  end;

  Result := TrimManual(CadenaLimpia);
end;

function EliminarCaracteresRepetidos(const Cadena: string): string;
var
  i: Integer;
  ResultadoTexto: string;
  CaracterActual: Char;
begin
  ResultadoTexto := '';
  for i := 1 to Length(Cadena) do
  begin
    CaracterActual := Cadena[i];
    if PosicionManual(CaracterActual, ResultadoTexto) = 0 then
      ResultadoTexto := ResultadoTexto + CaracterActual;
  end;
  Result := ResultadoTexto;
end;

function IntercalarCadenas(const Cadena1, Cadena2: string): string;
var
  i, Long1, Long2, MaxLong: Integer;
  ResultadoTexto: string;
begin
  Long1 := Length(Cadena1);
  Long2 := Length(Cadena2);
  if Long1 > Long2 then MaxLong := Long1 else MaxLong := Long2;
  ResultadoTexto := '';

  for i := 1 to MaxLong do
  begin
    if i <= Long1 then
      ResultadoTexto := ResultadoTexto + Cadena1[i];
    if i <= Long2 then
      ResultadoTexto := ResultadoTexto + Cadena2[i];
  end;

  Result := ResultadoTexto;
end;

function CifradoCesar(const Cadena: string; Desplazamiento: Integer): string;
var
  i, CodigoBase, CodigoNuevo: Integer;
  CaracterOriginal: Char;
  ResultadoTexto: string;
begin
  ResultadoTexto := '';
  // Ajuste positivo del desplazamiento
  Desplazamiento := ((Desplazamiento mod 26) + 26) mod 26;

  for i := 1 to Length(Cadena) do
  begin
    CaracterOriginal := Cadena[i];
    if CaracterOriginal in ['A'..'Z'] then
    begin
      CodigoBase := Ord('A');
      CodigoNuevo := CodigoBase + ((Ord(CaracterOriginal) - CodigoBase + Desplazamiento) mod 26);
      ResultadoTexto := ResultadoTexto + Chr(CodigoNuevo);
    end
    else if CaracterOriginal in ['a'..'z'] then
    begin
      CodigoBase := Ord('a');
      CodigoNuevo := CodigoBase + ((Ord(CaracterOriginal) - CodigoBase + Desplazamiento) mod 26);
      ResultadoTexto := ResultadoTexto + Chr(CodigoNuevo);
    end
    else
      ResultadoTexto := ResultadoTexto + CaracterOriginal;
  end;

  Result := ResultadoTexto;
end;

function GenerarCadenaArbol(const Cadena: string): string;
var
  i: Integer;
  ResultadoTexto: string;
begin
  ResultadoTexto := '';
  for i := Length(Cadena) downto 1 do
  begin
    ResultadoTexto := ResultadoTexto + CopiarManual(Cadena, 1, i);
    if i > 1 then
      ResultadoTexto := ResultadoTexto + sLineBreak;
  end;
  Result := ResultadoTexto;
end;

end.
