{ delphi}
unit UCNatural;

{==============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE INGENIERÍA EN CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES
  CARRERA: INGENIERÍA INFORMÁTICA / SISTEMAS
  MATERIA: INF110 - INTRODUCCIÓN A LA INFORMÁTICA (GRUPO Z2)
  DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar

  UNIDAD: UCNatural.pas (Unidad de Clase para Números Naturales)
  PARADIGMA: Programación Orientada a Objetos (POO)
  FILOSOFÍA: Clean Code & Estándares Profesionales de Object Pascal / Delphi
==============================================================================}


interface

uses
  SysUtils;

const
  BaseDecimal = 10;
  DivisorPar  = 2;

type
  {============================================================================
    CLASE: NumeroNatural
    Encapsula un número natural entero sin signo.
    Rango de representación: 0 .. 4.294.967.295 (Tipo Cardinal de 32 bits).
  ============================================================================}
  NumeroNatural = class
  private
    // Atributo encapsulado (En Delphi profesional se suele usar prefijo F de Field: FValor)
    Valor: Cardinal;

  public
    // ------------------------------------------------------------------------
    // CONSTRUCTORES Y MÉTODOS DE ACCESO (GETTERS Y SETTERS)
    // ------------------------------------------------------------------------
    constructor Create;
    procedure CambiarValor(nuevoValor: Cardinal);
    function ObtenerValor: Cardinal;

    // ------------------------------------------------------------------------
    // MÉTODOS FUNDAMENTALES DE LA CLASE
    // ------------------------------------------------------------------------
    function ContarDigitos: Word;
    function MultiplicarDigitos: Cardinal;
    function ContarDigitosPares: Byte;
    function ContarDigitosImpares: Byte;
    function EliminarCeros: Cardinal;
    function DigitosIguales: Boolean;
    function ContarFrecuenciaDigito(digitoBuscado: Byte): Byte;
    function DigitosOrdenadosAsc: Boolean;
    procedure SumaParesEImpares(out sumaPares, sumaImpares: Cardinal);

    // ------------------------------------------------------------------------
    // MÉTODOS DEL PRÁCTICO # 13: PROPIEDADES MATEMÁTICAS Y DIVISIBILIDAD
    // ------------------------------------------------------------------------
    function SumaDigitosDivisible3: Boolean;
    function EsDivisible9PorSuma: Boolean;
    function TieneDigitosRepetidos: Boolean;
    function EsPandigital: Boolean;
    function DiferenciaParesImpares: Int64;
    function TodosDigitosPrimos: Boolean;
    procedure MaximoYMinimoReordenado(out numeroMaximo, numeroMinimo: Cardinal);
    function ProductoIgualSuma: Boolean;
    procedure SumaPosicionParEImpar(out sumaPosImpar, sumaPosPar: Cardinal);
    function OrdenarPorFrecuencia: UInt64;

    // ------------------------------------------------------------------------
    // MÉTODOS DE SISTEMAS DE NUMERACIÓN (BINARIO, OCTAL, HEXADECIMAL)
    // ------------------------------------------------------------------------
    function DigitosABinarioConcat: string;
    function SumaEquivalenteOctal: string;
    function EsPalindromoBinario: Boolean;
    function ParesAOctalConcat: string;
    function SumaDigitosHex: string;
    function ContarUnosEnDigitosBinarios: Word;
    function BitsCantidadPar: Boolean;
    function CantidadCerosIgualUnosBinario: Boolean;
    function ImparesAHexConcat: string;
    function Grupos3BitsADecimal: string;

    // ------------------------------------------------------------------------
    // MÉTODOS DE EXÁMENES OFICIALES (TAREA #10 Y EXAMEN FINAL)
    // ------------------------------------------------------------------------
    function NumeroPares: Word;
    function NMenorPar: Byte;
    function NMayorImpar: Byte;
    function NDigitosIguales: Boolean;
    function SiEsCapicua: string;
    function NSumaIndicePar: Byte;
    function MitadDerechaCapicua: string;
    function MitadIzquierdaCapicua: string;
    function SumarDigitosHastaMenor10: Byte;
    function PrimeroYUltimoDigitoPrimos: string;
    function EliminarDigitosRepetidos: Cardinal;
    procedure SepararDigitosMenoresYMayores(criterio: Byte; out menores, mayores: Cardinal);
  end;

implementation

{==============================================================================
  1. CONSTRUCTOR
  Inicializa el objeto en un estado consistente y seguro en la memoria Heap.
==============================================================================}
constructor NumeroNatural.Create;
begin
  Valor := 0;
end;

{==============================================================================
  2. SETTER: CambiarValor
  Permite modificar el estado interno del objeto mediante un mensaje seguro.
==============================================================================}
procedure NumeroNatural.CambiarValor(nuevoValor: Cardinal);
begin
  Valor := nuevoValor;
end;

{==============================================================================
  3. GETTER: ObtenerValor
  Permite consultar el estado interno del objeto sin exponer el atributo privado.
==============================================================================}
function NumeroNatural.ObtenerValor: Cardinal;
begin
  Result := Valor;
end;

{==============================================================================
  4. ContarDigitos
  Cuenta la cantidad de dígitos usando división sucesiva protegida.
==============================================================================}
function NumeroNatural.ContarDigitos: Word;
var
  numeroRestante: Cardinal;
  cantidadDigitos: Word;
begin
  numeroRestante := Valor; // Copia de seguridad: protege el atributo encapsulado
  cantidadDigitos := 0;

  repeat
    numeroRestante := numeroRestante div BaseDecimal;
    Inc(cantidadDigitos); // Idiomático de Delphi: más rápido y legible que c := c + 1
  until numeroRestante = 0;

  Result := cantidadDigitos;
end;

{==============================================================================
  5. MultiplicarDigitos
  Multiplica todos los dígitos del número.
  Ejemplo: 423 -> 4 * 2 * 3 = 24.
==============================================================================}
function NumeroNatural.MultiplicarDigitos: Cardinal;
var
  numeroRestante: Cardinal;
  digitoActual: Byte;
  productoAcumulado: Cardinal;
begin
  if Valor = 0 then
    Exit(0);

  numeroRestante := Valor;
  productoAcumulado := 1;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;
    productoAcumulado := productoAcumulado * digitoActual;
    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := productoAcumulado;
end;

{==============================================================================
  6. ContarDigitosPares (EJEMPLO CLEAN CODE PRINCIPAL)
  Cuenta cuántos dígitos pares contiene el número.
  Ejemplo: 48263 -> dígitos pares [4, 8, 2, 6] -> 4 dígitos pares.
==============================================================================}
function NumeroNatural.ContarDigitosPares: Byte;
var
  numeroRestante: Cardinal;
  digitoActual: Byte;
  cantidadDigitosPares: Byte;
begin
  // Caso de guarda especial: el número 0 es natural y es par
  if Valor = 0 then
    Exit(1);

  numeroRestante := Valor;
  cantidadDigitosPares := 0;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;

    // Verificamos si el residuo de dividir entre 2 es cero
    if (digitoActual mod DivisorPar = 0) then
      Inc(cantidadDigitosPares);

    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := cantidadDigitosPares;
end;

{==============================================================================
  7. ContarDigitosImpares
  Cuenta cuántos dígitos impares contiene el número.
  Ejemplo: 48263 -> dígito impar [3] -> 1 dígito impar.
==============================================================================}
function NumeroNatural.ContarDigitosImpares: Byte;
var
  numeroRestante: Cardinal;
  digitoActual: Byte;
  cantidadDigitosImpares: Byte;
begin
  if Valor = 0 then
    Exit(0);

  numeroRestante := Valor;
  cantidadDigitosImpares := 0;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;

    if (digitoActual mod DivisorPar <> 0) then
      Inc(cantidadDigitosImpares);

    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := cantidadDigitosImpares;
end;

{==============================================================================
  8. EliminarCeros
  Reconstruye el número omitiendo todos los ceros mediante aritmética posicional.
  Ejemplo: 10203040 -> 1234.
==============================================================================}
function NumeroNatural.EliminarCeros: Cardinal;
var
  numeroRestante: Cardinal;
  numeroSinCeros: Cardinal;
  factorPosicional: Cardinal;
  digitoActual: Byte;
begin
  if Valor = 0 then
    Exit(0);

  numeroRestante := Valor;
  numeroSinCeros := 0;
  factorPosicional := 1;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;

    if digitoActual <> 0 then
    begin
      numeroSinCeros := numeroSinCeros + (digitoActual * factorPosicional);
      factorPosicional := factorPosicional * BaseDecimal;
    end;

    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := numeroSinCeros;
end;

{==============================================================================
  9. DigitosIguales
  Determina si todos los dígitos del número son idénticos.
  Ejemplo: 7777 -> True; 7776 -> False.
==============================================================================}
function NumeroNatural.DigitosIguales: Boolean;
var
  numeroRestante: Cardinal;
  digitoReferencia: Byte;
  digitoActual: Byte;
begin
  numeroRestante := Valor;
  digitoReferencia := numeroRestante mod BaseDecimal;
  numeroRestante := numeroRestante div BaseDecimal;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;
    if digitoActual <> digitoReferencia then
      Exit(False); // Salida temprana si un dígito discrepa

    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := True;
end;

{==============================================================================
  10. ContarFrecuenciaDigito
  Cuenta cuántas veces aparece un dígito específico.
==============================================================================}
function NumeroNatural.ContarFrecuenciaDigito(digitoBuscado: Byte): Byte;
var
  numeroRestante: Cardinal;
  cantidadApariciones: Byte;
begin
  if (Valor = 0) and (digitoBuscado = 0) then
    Exit(1);

  numeroRestante := Valor;
  cantidadApariciones := 0;

  while numeroRestante > 0 do
  begin
    if (numeroRestante mod BaseDecimal) = digitoBuscado then
      Inc(cantidadApariciones);

    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := cantidadApariciones;
end;

{==============================================================================
  11. DigitosOrdenadosAsc
  Verifica si los dígitos están ordenados de menor a mayor (de izq a der).
==============================================================================}
function NumeroNatural.DigitosOrdenadosAsc: Boolean;
var
  numeroRestante: Cardinal;
  digitoDerecha, digitoIzquierda: Byte;
begin
  numeroRestante := Valor;
  if numeroRestante < BaseDecimal then
    Exit(True); // Números de 1 solo dígito siempre están ordenados

  digitoDerecha := numeroRestante mod BaseDecimal;
  numeroRestante := numeroRestante div BaseDecimal;

  while numeroRestante > 0 do
  begin
    digitoIzquierda := numeroRestante mod BaseDecimal;

    // En orden ascendente de izquierda a derecha, la izquierda no puede ser mayor
    if digitoIzquierda > digitoDerecha then
      Exit(False);

    digitoDerecha := digitoIzquierda;
    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := True;
end;

{==============================================================================
  12. SumaParesEImpares
  Genera la suma de pares separada de impares mediante parámetros por referencia.
==============================================================================}
procedure NumeroNatural.SumaParesEImpares(out sumaPares, sumaImpares: Cardinal);
var
  numeroRestante: Cardinal;
  digitoActual: Byte;
begin
  numeroRestante := Valor;
  sumaPares := 0;
  sumaImpares := 0;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;

    if (digitoActual mod DivisorPar = 0) then
      sumaPares := sumaPares + digitoActual
    else
      sumaImpares := sumaImpares + digitoActual;

    numeroRestante := numeroRestante div BaseDecimal;
  end;
end;

// Función de soporte interna para calcular suma de dígitos
function SumarDigitosInterno(numero: Cardinal): Cardinal;
var
  suma: Cardinal;
begin
  suma := 0;
  while numero > 0 do
  begin
    suma := suma + (numero mod BaseDecimal);
    numero := numero div BaseDecimal;
  end;
  Result := suma;
end;

{==============================================================================
  13. SumaDigitosDivisible3
==============================================================================}
function NumeroNatural.SumaDigitosDivisible3: Boolean;
begin
  Result := (SumarDigitosInterno(Valor) mod 3 = 0);
end;

{==============================================================================
  14. EsDivisible9PorSuma
==============================================================================}
function NumeroNatural.EsDivisible9PorSuma: Boolean;
begin
  Result := (SumarDigitosInterno(Valor) mod 9 = 0);
end;

{==============================================================================
  15. TieneDigitosRepetidos
==============================================================================}
function NumeroNatural.TieneDigitosRepetidos: Boolean;
var
  numeroRestante: Cardinal;
  frecuenciaDigitos: array[0..9] of Byte;
  digitoActual, i: Byte;
begin
  for i := 0 to 9 do
    frecuenciaDigitos[i] := 0;

  numeroRestante := Valor;
  repeat
    digitoActual := numeroRestante mod BaseDecimal;

    if frecuenciaDigitos[digitoActual] > 0 then
      Exit(True); // Se repite

    frecuenciaDigitos[digitoActual] := 1;
    numeroRestante := numeroRestante div BaseDecimal;
  until numeroRestante = 0;

  Result := False;
end;

{==============================================================================
  16. EsPandigital
==============================================================================}
function NumeroNatural.EsPandigital: Boolean;
var
  numeroRestante: Cardinal;
  digitoVisto: array[0..9] of Boolean;
  digitoActual, i: Byte;
begin
  for i := 0 to 9 do
    digitoVisto[i] := False;

  numeroRestante := Valor;
  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;
    digitoVisto[digitoActual] := True;
    numeroRestante := numeroRestante div BaseDecimal;
  end;

  for i := 0 to 9 do
    if not digitoVisto[i] then
      Exit(False);

  Result := True;
end;

{==============================================================================
  17. DiferenciaParesImpares
==============================================================================}
function NumeroNatural.DiferenciaParesImpares: Int64;
var
  numeroRestante: Cardinal;
  factorPosPar, factorPosImp: Cardinal;
  numeroParFormado, numeroImpFormado: Cardinal;
  digitoActual: Byte;
begin
  numeroRestante := Valor;
  numeroParFormado := 0;
  numeroImpFormado := 0;
  factorPosPar := 1;
  factorPosImp := 1;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;

    if (digitoActual mod DivisorPar = 0) then
    begin
      numeroParFormado := numeroParFormado + (digitoActual * factorPosPar);
      factorPosPar := factorPosPar * BaseDecimal;
    end
    else
    begin
      numeroImpFormado := numeroImpFormado + (digitoActual * factorPosImp);
      factorPosImp := factorPosImp * BaseDecimal;
    end;

    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := Int64(numeroParFormado) - Int64(numeroImpFormado);
end;

{==============================================================================
  18. TodosDigitosPrimos
==============================================================================}
function NumeroNatural.TodosDigitosPrimos: Boolean;
var
  numeroRestante: Cardinal;
  digitoActual: Byte;
begin
  numeroRestante := Valor;
  repeat
    digitoActual := numeroRestante mod BaseDecimal;

    // Solo los dígitos [2, 3, 5, 7] son números primos
    if not (digitoActual in [2, 3, 5, 7]) then
      Exit(False);

    numeroRestante := numeroRestante div BaseDecimal;
  until numeroRestante = 0;

  Result := True;
end;

{==============================================================================
  19. MaximoYMinimoReordenado
==============================================================================}
procedure NumeroNatural.MaximoYMinimoReordenado(out numeroMaximo, numeroMinimo: Cardinal);
var
  numeroRestante: Cardinal;
  frecuencia: array[0..9] of Byte;
  digitoActual, i, k: Byte;
begin
  for i := 0 to 9 do
    frecuencia[i] := 0;

  numeroRestante := Valor;
  repeat
    digitoActual := numeroRestante mod BaseDecimal;
    Inc(frecuencia[digitoActual]);
    numeroRestante := numeroRestante div BaseDecimal;
  until numeroRestante = 0;

  // Número Máximo: Dígitos ordenados de 9 a 0
  numeroMaximo := 0;
  for i := 9 downto 0 do
    for k := 1 to frecuencia[i] do
      numeroMaximo := numeroMaximo * BaseDecimal + i;

  // Número Mínimo: Primer dígito distinto de 0 (para evitar ceros a la izquierda)
  numeroMinimo := 0;
  for i := 1 to 9 do
    if frecuencia[i] > 0 then
    begin
      numeroMinimo := i;
      Dec(frecuencia[i]);
      Break;
    end;

  for i := 0 to 9 do
    for k := 1 to frecuencia[i] do
      numeroMinimo := numeroMinimo * BaseDecimal + i;
end;

{==============================================================================
  20. ProductoIgualSuma
==============================================================================}
function NumeroNatural.ProductoIgualSuma: Boolean;
begin
  Result := (MultiplicarDigitos = SumarDigitosInterno(Valor));
end;

{==============================================================================
  21. SumaPosicionParEImpar
==============================================================================}
procedure NumeroNatural.SumaPosicionParEImpar(out sumaPosImpar, sumaPosPar: Cardinal);
var
  cadenaTexto: string;
  indicePosicion: Integer;
  digitoActual: Byte;
begin
  cadenaTexto := IntToStr(Valor);
  sumaPosImpar := 0;
  sumaPosPar := 0;

  for indicePosicion := 1 to Length(cadenaTexto) do
  begin
    digitoActual := Ord(cadenaTexto[indicePosicion]) - Ord('0');

    if (indicePosicion mod DivisorPar <> 0) then
      sumaPosImpar := sumaPosImpar + digitoActual
    else
      sumaPosPar := sumaPosPar + digitoActual;
  end;
end;

{==============================================================================
  22. OrdenarPorFrecuencia
==============================================================================}
function NumeroNatural.OrdenarPorFrecuencia: UInt64;
var
  numeroRestante: Cardinal;
  conteoFrecuencia: array[0..9] of Byte;
  digitoActual, mayorFrecuencia, digitoSeleccionado, k: Byte;
  numeroResultado: UInt64;
begin
  for digitoActual := 0 to 9 do
    conteoFrecuencia[digitoActual] := 0;

  numeroRestante := Valor;
  repeat
    digitoActual := numeroRestante mod BaseDecimal;
    Inc(conteoFrecuencia[digitoActual]);
    numeroRestante := numeroRestante div BaseDecimal;
  until numeroRestante = 0;

  numeroResultado := 0;
  while True do
  begin
    mayorFrecuencia := 0;
    digitoSeleccionado := 0;

    for digitoActual := 9 downto 0 do
    begin
      if conteoFrecuencia[digitoActual] > mayorFrecuencia then
      begin
        mayorFrecuencia := conteoFrecuencia[digitoActual];
        digitoSeleccionado := digitoActual;
      end;
    end;

    if mayorFrecuencia = 0 then
      Break;

    for k := 1 to mayorFrecuencia do
      numeroResultado := numeroResultado * BaseDecimal + digitoSeleccionado;

    conteoFrecuencia[digitoSeleccionado] := 0;
  end;

  Result := numeroResultado;
end;

// Auxiliar para convertir entero a cadena binaria de ancho fijo
function EnteroABinarioBits(valorByte: Byte; cantidadBits: Byte): string;
var
  cadenaBinaria: string;
  bitIndex: Byte;
begin
  cadenaBinaria := '';
  for bitIndex := cantidadBits - 1 downto 0 do
  begin
    if (valorByte and (1 shl bitIndex)) <> 0 then
      cadenaBinaria := cadenaBinaria + '1'
    else
      cadenaBinaria := cadenaBinaria + '0';
  end;
  Result := cadenaBinaria;
end;

{==============================================================================
  23. DigitosABinarioConcat
==============================================================================}
function NumeroNatural.DigitosABinarioConcat: string;
var
  cadenaTexto, resultadoConcatenado: string;
  i: Integer;
  digitoActual: Byte;
begin
  cadenaTexto := IntToStr(Valor);
  resultadoConcatenado := '';

  for i := 1 to Length(cadenaTexto) do
  begin
    digitoActual := Ord(cadenaTexto[i]) - Ord('0');
    if resultadoConcatenado <> '' then
      resultadoConcatenado := resultadoConcatenado + ' ';
    resultadoConcatenado := resultadoConcatenado + EnteroABinarioBits(digitoActual, 4);
  end;

  Result := resultadoConcatenado;
end;

// Auxiliar para convertir entero a octal
function DecimalAOctalTexto(numeroDecimal: Cardinal): string;
var
  cadenaOctal: string;
begin
  if numeroDecimal = 0 then
    Exit('0');
  cadenaOctal := '';
  while numeroDecimal > 0 do
  begin
    cadenaOctal := IntToStr(numeroDecimal mod 8) + cadenaOctal;
    numeroDecimal := numeroDecimal div 8;
  end;
  Result := cadenaOctal;
end;

{==============================================================================
  24. SumaEquivalenteOctal
==============================================================================}
function NumeroNatural.SumaEquivalenteOctal: string;
var
  sumaDecimal: Cardinal;
  representacionOctal: string;
begin
  sumaDecimal := SumarDigitosInterno(Valor);
  representacionOctal := DecimalAOctalTexto(sumaDecimal);
  Result := 'Suma ' + IntToStr(sumaDecimal) + ' dec = ' + representacionOctal + ' octal';
end;

// Auxiliar para convertir Cardinal a binario sin ceros a la izquierda
function CardinalABinarioTexto(numero: Cardinal): string;
var
  cadenaBinaria: string;
begin
  if numero = 0 then
    Exit('0');
  cadenaBinaria := '';
  while numero > 0 do
  begin
    if (numero mod 2) = 1 then
      cadenaBinaria := '1' + cadenaBinaria
    else
      cadenaBinaria := '0' + cadenaBinaria;
    numero := numero div 2;
  end;
  Result := cadenaBinaria;
end;

{==============================================================================
  25. EsPalindromoBinario
==============================================================================}
function NumeroNatural.EsPalindromoBinario: Boolean;
var
  cadenaBinaria: string;
  indiceInicio, indiceFin: Integer;
begin
  cadenaBinaria := CardinalABinarioTexto(Valor);
  indiceInicio := 1;
  indiceFin := Length(cadenaBinaria);

  while indiceInicio < indiceFin do
  begin
    if cadenaBinaria[indiceInicio] <> cadenaBinaria[indiceFin] then
      Exit(False);
    Inc(indiceInicio);
    Dec(indiceFin);
  end;

  Result := True;
end;

{==============================================================================
  26. ParesAOctalConcat
==============================================================================}
function NumeroNatural.ParesAOctalConcat: string;
var
  cadenaTexto, resultadoConcatenado: string;
  i: Integer;
  digitoActual: Byte;
begin
  cadenaTexto := IntToStr(Valor);
  resultadoConcatenado := '';

  for i := 1 to Length(cadenaTexto) do
  begin
    digitoActual := Ord(cadenaTexto[i]) - Ord('0');
    if (digitoActual mod DivisorPar = 0) then
    begin
      if resultadoConcatenado <> '' then
        resultadoConcatenado := resultadoConcatenado + ' ';
      resultadoConcatenado := resultadoConcatenado + DecimalAOctalTexto(digitoActual);
    end;
  end;

  Result := resultadoConcatenado;
end;

{==============================================================================
  27. SumaDigitosHex
==============================================================================}
function NumeroNatural.SumaDigitosHex: string;
var
  sumaDecimal: Cardinal;
begin
  sumaDecimal := SumarDigitosInterno(Valor);
  Result := IntToHex(sumaDecimal, 1);
end;

{==============================================================================
  28. ContarUnosEnDigitosBinarios
==============================================================================}
function NumeroNatural.ContarUnosEnDigitosBinarios: Word;
var
  numeroRestante: Cardinal;
  digitoActual: Byte;
  totalBitsEncendidos: Word;
begin
  numeroRestante := Valor;
  totalBitsEncendidos := 0;

  repeat
    digitoActual := numeroRestante mod BaseDecimal;
    while digitoActual > 0 do
    begin
      if (digitoActual mod 2 = 1) then
        Inc(totalBitsEncendidos);
      digitoActual := digitoActual div 2;
    end;
    numeroRestante := numeroRestante div BaseDecimal;
  until numeroRestante = 0;

  Result := totalBitsEncendidos;
end;

{==============================================================================
  29. BitsCantidadPar
==============================================================================}
function NumeroNatural.BitsCantidadPar: Boolean;
var
  cadenaBinaria: string;
begin
  cadenaBinaria := CardinalABinarioTexto(Valor);
  Result := (Length(cadenaBinaria) mod 2 = 0);
end;

{==============================================================================
  30. CantidadCerosIgualUnosBinario
==============================================================================}
function NumeroNatural.CantidadCerosIgualUnosBinario: Boolean;
var
  cadenaBinaria: string;
  i, cantidadCeros, cantidadUnos: Integer;
begin
  cadenaBinaria := CardinalABinarioTexto(Valor);
  cantidadCeros := 0;
  cantidadUnos := 0;

  for i := 1 to Length(cadenaBinaria) do
  begin
    if cadenaBinaria[i] = '0' then
      Inc(cantidadCeros)
    else
      Inc(cantidadUnos);
  end;

  Result := (cantidadCeros = cantidadUnos);
end;

{==============================================================================
  31. ImparesAHexConcat
==============================================================================}
function NumeroNatural.ImparesAHexConcat: string;
var
  cadenaTexto, resultadoConcatenado: string;
  i: Integer;
  digitoActual: Byte;
begin
  cadenaTexto := IntToStr(Valor);
  resultadoConcatenado := '';

  for i := 1 to Length(cadenaTexto) do
  begin
    digitoActual := Ord(cadenaTexto[i]) - Ord('0');
    if (digitoActual mod DivisorPar <> 0) then
    begin
      if resultadoConcatenado <> '' then
        resultadoConcatenado := resultadoConcatenado + ', ';
      resultadoConcatenado := resultadoConcatenado + IntToHex(digitoActual, 1);
    end;
  end;

  Result := resultadoConcatenado;
end;

{==============================================================================
  32. Grupos3BitsADecimal
==============================================================================}
function NumeroNatural.Grupos3BitsADecimal: string;
var
  cadenaBinaria, triadaBits, resultadoTexto: string;
  i, bitsFaltantes, valorDecimalTriada: Integer;
begin
  cadenaBinaria := CardinalABinarioTexto(Valor);
  bitsFaltantes := Length(cadenaBinaria) mod 3;

  if bitsFaltantes <> 0 then
    cadenaBinaria := StringOfChar('0', 3 - bitsFaltantes) + cadenaBinaria;

  resultadoTexto := '';
  i := 1;

  while i <= Length(cadenaBinaria) do
  begin
    triadaBits := Copy(cadenaBinaria, i, 3);
    valorDecimalTriada := (Ord(triadaBits[1]) - Ord('0')) * 4 +
                          (Ord(triadaBits[2]) - Ord('0')) * 2 +
                          (Ord(triadaBits[3]) - Ord('0')) * 1;

    if resultadoTexto <> '' then
      resultadoTexto := resultadoTexto + ' y ';

    resultadoTexto := resultadoTexto + IntToStr(valorDecimalTriada);
    i := i + 3;
  end;

  Result := resultadoTexto;
end;

{==============================================================================
  33. TAREA #10 PRESENCIAL: NumeroPares
==============================================================================}
function NumeroNatural.NumeroPares: Word;
var
  numeroRestante, factorPosicional, numeroParesFormado: Cardinal;
  digitoActual: Byte;
begin
  numeroRestante := Valor;
  numeroParesFormado := 0;
  factorPosicional := 1;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;
    if (digitoActual mod DivisorPar = 0) then
    begin
      numeroParesFormado := numeroParesFormado + (digitoActual * factorPosicional);
      factorPosicional := factorPosicional * BaseDecimal;
    end;
    numeroRestante := numeroRestante div BaseDecimal;
  end;

  Result := numeroParesFormado;
end;

{==============================================================================
  34. TAREA #10 PRESENCIAL: NMenorPar
==============================================================================}
function NumeroNatural.NMenorPar: Byte;
var
  numeroRestante: Cardinal;
  digitoActual, menorDigitoPar: Byte;
  existePar: Boolean;
begin
  numeroRestante := Valor;
  menorDigitoPar := 99;
  existePar := False;

  repeat
    digitoActual := numeroRestante mod BaseDecimal;
    if (digitoActual mod DivisorPar = 0) then
    begin
      existePar := True;
      if digitoActual < menorDigitoPar then
        menorDigitoPar := digitoActual;
    end;
    numeroRestante := numeroRestante div BaseDecimal;
  until numeroRestante = 0;

  if existePar then
    Result := menorDigitoPar
  else
    Result := 0;
end;

{==============================================================================
  35. TAREA #10 PRESENCIAL: NMayorImpar
==============================================================================}
function NumeroNatural.NMayorImpar: Byte;
var
  numeroRestante: Cardinal;
  digitoActual, mayorDigitoImpar: Byte;
  existeImpar: Boolean;
begin
  numeroRestante := Valor;
  mayorDigitoImpar := 0;
  existeImpar := False;

  while numeroRestante > 0 do
  begin
    digitoActual := numeroRestante mod BaseDecimal;
    if (digitoActual mod DivisorPar <> 0) then
    begin
      existeImpar := True;
      if digitoActual > mayorDigitoImpar then
        mayorDigitoImpar := digitoActual;
    end;
    numeroRestante := numeroRestante div BaseDecimal;
  end;

  if existeImpar then
    Result := mayorDigitoImpar
  else
    Result := 0;
end;

{==============================================================================
  36. TAREA #10 PRESENCIAL: NDigitosIguales
==============================================================================}
function NumeroNatural.NDigitosIguales: Boolean;
begin
  Result := DigitosIguales;
end;

{==============================================================================
  37. TAREA #10 PRESENCIAL: SiEsCapicua
==============================================================================}
function NumeroNatural.SiEsCapicua: string;
var
  numeroRestante, numeroInvertido: Cardinal;
begin
  numeroRestante := Valor;
  numeroInvertido := 0;

  while numeroRestante > 0 do
  begin
    numeroInvertido := numeroInvertido * BaseDecimal + (numeroRestante mod BaseDecimal);
    numeroRestante := numeroRestante div BaseDecimal;
  end;

  if Valor = numeroInvertido then
    Result := 'si es capicua ' + IntToStr(Valor) + '=' + IntToStr(numeroInvertido)
  else
    Result := 'no es capicua ' + IntToStr(Valor) + '<>' + IntToStr(numeroInvertido);
end;

{==============================================================================
  38. TAREA #10 PRESENCIAL: NSumaIndicePar
==============================================================================}
function NumeroNatural.NSumaIndicePar: Byte;
var
  cadenaTexto: string;
  indicePosicion: Integer;
  sumaAcumulada: Byte;
begin
  cadenaTexto := IntToStr(Valor);
  sumaAcumulada := 0;

  for indicePosicion := 1 to Length(cadenaTexto) do
  begin
    if (indicePosicion mod DivisorPar = 0) then
      sumaAcumulada := sumaAcumulada + (Ord(cadenaTexto[indicePosicion]) - Ord('0'));
  end;

  Result := sumaAcumulada;
end;

{==============================================================================
  39. EXAMEN FINAL (08/07/2024): MitadDerechaCapicua
==============================================================================}
function NumeroNatural.MitadDerechaCapicua: string;
var
  cantidadTotalDigitos, mitadCantidadDigitos, i: Integer;
  factorPotenciaDiez, parteDerecha, numeroTemporal, mitadInvertida: Cardinal;
begin
  cantidadTotalDigitos := ContarDigitos;
  mitadCantidadDigitos := cantidadTotalDigitos div 2;

  if mitadCantidadDigitos = 0 then
    Exit('Si es capicua. ' + IntToStr(Valor));

  factorPotenciaDiez := 1;
  for i := 1 to mitadCantidadDigitos do
    factorPotenciaDiez := factorPotenciaDiez * BaseDecimal;

  parteDerecha := Valor mod factorPotenciaDiez;

  // Invertir aritméticamente la mitad derecha
  numeroTemporal := parteDerecha;
  mitadInvertida := 0;

  while numeroTemporal > 0 do
  begin
    mitadInvertida := mitadInvertida * BaseDecimal + (numeroTemporal mod BaseDecimal);
    numeroTemporal := numeroTemporal div BaseDecimal;
  end;

  if parteDerecha = mitadInvertida then
    Result := 'Si es capicua. ' + IntToStr(parteDerecha)
  else
    Result := 'no es capicua ' + IntToStr(mitadInvertida);
end;


{==============================================================================
 EXAMEN FINAL 2023-2 SF (P4): Mitad Izquierda Capicua
 Extrae la mitad izquierda de los dígitos y verifica si es capicúa.
 Ej: 12357 -> mitad izq 12 -> no es capicua 21
     11567 -> mitad izq 11 -> Si es capicua. 11
 ==============================================================================}
function NumeroNatural.MitadIzquierdaCapicua: string;
const
  BaseDecimal = 10;
var
  cantidadTotalDigitos, mitadCantidadDigitos, i: Integer;
  factorPotenciaDiez, parteIzquierda, numeroTemporal, mitadInvertida: Cardinal;
begin
  cantidadTotalDigitos := ContarDigitos;
  mitadCantidadDigitos := cantidadTotalDigitos div 2;

  if mitadCantidadDigitos = 0 then
    Exit('Si es capicua. ' + IntToStr(Valor));

  factorPotenciaDiez := 1;
  for i := 1 to (cantidadTotalDigitos - mitadCantidadDigitos) do
    factorPotenciaDiez := factorPotenciaDiez * BaseDecimal;

  parteIzquierda := Valor div factorPotenciaDiez;

  numeroTemporal := parteIzquierda;
  mitadInvertida := 0;
  while numeroTemporal > 0 do
  begin
    mitadInvertida := (mitadInvertida * BaseDecimal) + (numeroTemporal mod BaseDecimal);
    numeroTemporal := numeroTemporal div BaseDecimal;
  end;

  if parteIzquierda = mitadInvertida then
    Result := 'Si es capicua. ' + IntToStr(parteIzquierda)
  else
    Result := 'no es capicua ' + IntToStr(mitadInvertida);
end;

{==============================================================================
 EXAMEN FINAL 2023-2 Z2 (P1) y 2023-1 Z2 (P4): Raiz Digital
 Sumar los dígitos sucesivamente hasta que el resultado sea menor a 10.
 Ej: 15378 -> 24 -> 6
 ==============================================================================}
function NumeroNatural.SumarDigitosHastaMenor10: Byte;
const
  BaseDecimal = 10;
var
  numeroActual, sumaParcial: Cardinal;
begin
  numeroActual := Valor;
  while numeroActual >= BaseDecimal do
  begin
    sumaParcial := 0;
    while numeroActual > 0 do
    begin
      sumaParcial  := sumaParcial + (numeroActual mod BaseDecimal);
      numeroActual := numeroActual div BaseDecimal;
    end;
    numeroActual := sumaParcial;
  end;
  Result := numeroActual;
end;

{==============================================================================
 EXAMEN FINAL 2023-2 Z2 (P3): Primero y Ultimo Digito Primos
 Verifica si el primer y el último dígito del número son números primos.
 Primos permitidos: [2, 3, 5, 7].
 Ej: 3147 -> Si los digitos son primos (3 y 7)
     1589 -> No, los digitos no son primos (1 y 9)
 ==============================================================================}
function NumeroNatural.PrimeroYUltimoDigitoPrimos: string;
const
  BaseDecimal = 10;
var
  primerDigito, ultimoDigito: Byte;
  numeroTemporal: Cardinal;
begin
  if Valor = 0 then
    Exit('No, los digitos no son primos');

  ultimoDigito := Valor mod BaseDecimal;

  numeroTemporal := Valor;
  while numeroTemporal >= BaseDecimal do
    numeroTemporal := numeroTemporal div BaseDecimal;
  primerDigito := numeroTemporal;

  if (primerDigito in [2, 3, 5, 7]) and (ultimoDigito in [2, 3, 5, 7]) then
    Result := 'Si los digitos son primos'
  else
    Result := 'No, los digitos no son primos';
end;

{==============================================================================
 EXAMEN FINAL 2023-1 SF (P2): Eliminar Digitos Repetidos
 Elimina todos aquellos dígitos que aparecen más de una vez en el número.
 Ej: 23254 -> El 2 se repite -> Queda 354.
 ==============================================================================}
function NumeroNatural.EliminarDigitosRepetidos: Cardinal;
const
  BaseDecimal = 10;
var
  frecuenciaDigitos: array[0..9] of Integer;
  numeroTemporal, numeroSinRepetidos, factorPosicional: Cardinal;
  digitoActual, i: Byte;
begin
  for i := 0 to 9 do
    frecuenciaDigitos[i] := 0;

  numeroTemporal := Valor;
  while numeroTemporal > 0 do
  begin
    Inc(frecuenciaDigitos[numeroTemporal mod BaseDecimal]);
    numeroTemporal := numeroTemporal div BaseDecimal;
  end;

  numeroTemporal     := Valor;
  numeroSinRepetidos := 0;
  factorPosicional   := 1;

  while numeroTemporal > 0 do
  begin
    digitoActual := numeroTemporal mod BaseDecimal;
    if frecuenciaDigitos[digitoActual] = 1 then
    begin
      numeroSinRepetidos := numeroSinRepetidos + (digitoActual * factorPosicional);
      factorPosicional   := factorPosicional * BaseDecimal;
    end;
    numeroTemporal := numeroTemporal div BaseDecimal;
  end;

  Result := numeroSinRepetidos;
end;

{==============================================================================
 EXAMEN FINAL 2024-1 SF (P3): Separar Digitos Menores y Mayores/Iguales
 Separa en dos números: uno con dígitos < criterio y otro con >= criterio.
 Ej: Entrada = 16327, criterio = 6
     < 6  Resultado = 231
     >= 6 Resultado = 76
 ==============================================================================}
procedure NumeroNatural.SepararDigitosMenoresYMayores(criterio: Byte; out menores, mayores: Cardinal);
const
  BaseDecimal = 10;
var
  digitoActual: Byte;
  numeroTemporal: Cardinal;
begin
  menores := 0;
  mayores := 0;
  numeroTemporal := Valor;

  while numeroTemporal > 0 do
  begin
    digitoActual := numeroTemporal mod BaseDecimal;
    if digitoActual < criterio then
      menores := (menores * BaseDecimal) + digitoActual
    else
      mayores := (mayores * BaseDecimal) + digitoActual;

    numeroTemporal := numeroTemporal div BaseDecimal;
  end;
end;

end.
