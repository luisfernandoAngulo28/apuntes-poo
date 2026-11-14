export interface MetodoTrilogia {
  id: string;
  categoria: 'series' | 'numeros' | 'cadenas';
  titulo: string;
  enunciado: string;
  puntos: number;
  fase1Analisis: {
    entradas: string;
    salidas: string;
    leyFormacion: string;
    tipoModulo: string;
  };
  fase2Pseudocodigo: string;
  fase3Pascal: string;
  fase4TrazaEjemplo: {
    descripcion: string;
    columnas: string[];
    filas: (string | number)[][];
  };
}

export const METODOS_TRILOGIA: MetodoTrilogia[] = [
  // 1. TEMA SERIES NUMÉRICAS
  {
    id: 'serie-factorial-doble',
    categoria: 'series',
    titulo: 'Serie 1: Sumatoria Factorial / Doble',
    enunciado: 'Calcular la sumatoria: S = 1/2 + 2/4 + 6/8 + 24/16 + 120/32 + ... para N términos.',
    puntos: 30,
    fase1Analisis: {
      entradas: 'N (Cardinal, cantidad de términos a sumar).',
      salidas: 'S (Real / Double, sumatoria total acumulada).',
      leyFormacion: 'Término i: Numerador = i!, Denominador = 2^i. Cada término vale (i!) / (2^i).',
      tipoModulo: 'FUNCTION SumaFactorialDoble(NumeroTerminos: Cardinal): Double;'
    },
    fase2Pseudocodigo: `Funcion SumaFactorialDoble(n: Cardinal): Real
Variables:
    contador, factorial, potencia: Cardinal
    sumatoria: Real
Inicio
    sumatoria := 0.0
    factorial := 1
    potencia := 1
    Para contador := 1 Hasta n Hacer
        factorial := factorial * contador
        potencia := potencia * 2
        sumatoria := sumatoria + (factorial / potencia)
    FinPara
    Retornar sumatoria
FinFuncion`,
    fase3Pascal: `function SumaFactorialDoble(NumeroTerminos: Cardinal): Double;
var
  Contador: Cardinal;
  FactorialAcumulado: Cardinal;
  PotenciaDosAcumulada: Cardinal;
  SumaTotal: Double;
begin
  SumaTotal := 0.0;
  FactorialAcumulado := 1;
  PotenciaDosAcumulada := 1;
  
  for Contador := 1 to NumeroTerminos do
  begin
    FactorialAcumulado := FactorialAcumulado * Contador;
    PotenciaDosAcumulada := PotenciaDosAcumulada * 2;
    SumaTotal := SumaTotal + (FactorialAcumulado / PotenciaDosAcumulada);
  end;
  
  Result := SumaTotal;
end;`,
    fase4TrazaEjemplo: {
      descripcion: 'Prueba de escritorio para N = 4',
      columnas: ['Contador (i)', 'Factorial (i!)', 'Potencia (2^i)', 'Término (i! / 2^i)', 'Suma Total'],
      filas: [
        ['Inicial', '1', '1', '-', '0.0000'],
        ['1', '1', '2', '0.5000', '0.5000'],
        ['2', '2', '4', '0.5000', '1.0000'],
        ['3', '6', '8', '0.7500', '1.7500'],
        ['4', '24', '16', '1.5000', '3.2500']
      ]
    }
  },

  // 2. TEMA NÚMEROS NATURALES (POO)
  {
    id: 'numero-eliminar-repetidos',
    categoria: 'numeros',
    titulo: 'Número 1: Eliminar Dígitos Repetidos',
    enunciado: 'Método para que un NúmeroNatural elimine todas las ocurrencias repetidas dejando solo 1 aparición de cada dígito.',
    puntos: 35,
    fase1Analisis: {
      entradas: 'Valor interno del objeto NumeroNatural (Cardinal).',
      salidas: 'Objeto modificado o nuevo Valor sin duplicados.',
      leyFormacion: 'Descomponer dígitos de derecha a izquierda. Si el dígito no está aún en el acumulador resultante, agregarlo.',
      tipoModulo: 'PROCEDURE NumeroNatural.EliminarDigitosRepetidos;'
    },
    fase2Pseudocodigo: `Procedimiento NumeroNatural.EliminarDigitosRepetidos()
Variables:
    numeroTemporal, resultado, multiplicador: Cardinal
    digitoActual: Byte
Inicio
    numeroTemporal := Valor
    resultado := 0
    multiplicador := 1
    Mientras numeroTemporal > 0 Hacer
        digitoActual := numeroTemporal MOD 10
        Si NO ExisteDigito(resultado, digitoActual) Entonces
            resultado := resultado + (digitoActual * multiplicador)
            multiplicador := multiplicador * 10
        FinSi
        numeroTemporal := numeroTemporal DIV 10
    FinMientras
    Valor := resultado
FinProcedimiento`,
    fase3Pascal: `function NumeroNatural.ExisteDigito(NumeroAnalizar: Cardinal; DigitoBuscado: Byte): Boolean;
var
  Copia: Cardinal;
begin
  Copia := NumeroAnalizar;
  while Copia > 0 do
  begin
    if (Copia mod 10) = DigitoBuscado then
      Exit(True);
    Copia := Copia div 10;
  end;
  Result := False;
end;

procedure NumeroNatural.EliminarDigitosRepetidos;
var
  NumeroTemporal, Resultado: Cardinal;
  DigitoActual: Byte;
  Multiplicador: Cardinal;
begin
  NumeroTemporal := Valor;
  Resultado := 0;
  Multiplicador := 1;
  
  while NumeroTemporal > 0 do
  begin
    DigitoActual := NumeroTemporal mod 10;
    if not ExisteDigito(Resultado, DigitoActual) then
    begin
      Resultado := Resultado + (DigitoActual * Multiplicador);
      Multiplicador := Multiplicador * 10;
    end;
    NumeroTemporal := NumeroTemporal div 10;
  end;
  
  Valor := Resultado;
end;`,
    fase4TrazaEjemplo: {
      descripcion: 'Prueba de escritorio para Valor = 445122',
      columnas: ['Paso', 'NumeroTemporal', 'Digito', 'Existe?', 'Multiplicador', 'Resultado'],
      filas: [
        ['Inicio', '445122', '-', '-', '1', '0'],
        ['1', '44512', '2', 'NO', '10', '2'],
        ['2', '4451', '2', 'SÍ (ignora)', '10', '2'],
        ['3', '445', '1', 'NO', '100', '12'],
        ['4', '44', '5', 'NO', '1000', '512'],
        ['5', '4', '4', 'NO', '10000', '4512'],
        ['6', '0', '4', 'SÍ (ignora)', '10000', '4512 (Final)']
      ]
    }
  },

  // 3. TEMA CADENAS DE CARACTERES (POO)
  {
    id: 'cadena-invertir-mitades',
    categoria: 'cadenas',
    titulo: 'Cadena 1: Invertir por Mitades',
    enunciado: 'Invertir la primera mitad de la cadena y la segunda mitad de forma independiente. Si la longitud es impar, el caracter central se conserva.',
    puntos: 35,
    fase1Analisis: {
      entradas: 'Cadena de texto fuente (string).',
      salidas: 'Cadena resultante con ambas mitades invertidas.',
      leyFormacion: 'Longitud L. Mitad 1 = caracteres [1 .. L div 2]. Mitad 2 = [L - (L div 2) + 1 .. L]. Si es impar, centro = Caracter[(L div 2) + 1].',
      tipoModulo: 'FUNCTION ClaseCadena.InvertirPorMitades: string;'
    },
    fase2Pseudocodigo: `Funcion ClaseCadena.InvertirPorMitades(): Cadena
Variables:
    longitudTexto, tamanoMitad, indice: Entero
    mitadIzquierda, mitadDerecha, caracterCentral: Cadena
Inicio
    longitudTexto := Longitud(Valor)
    tamanoMitad := longitudTexto DIV 2
    mitadIzquierda := InvertirTexto(SubCadena(Valor, 1, tamanoMitad))
    Si (longitudTexto MOD 2 <> 0) Entonces
        caracterCentral := Valor[tamanoMitad + 1]
        mitadDerecha := InvertirTexto(SubCadena(Valor, tamanoMitad + 2, tamanoMitad))
        Retornar mitadIzquierda + caracterCentral + mitadDerecha
    Sino
        mitadDerecha := InvertirTexto(SubCadena(Valor, tamanoMitad + 1, tamanoMitad))
        Retornar mitadIzquierda + mitadDerecha
    FinSi
FinFuncion`,
    fase3Pascal: `function InvertirTextoManual(const TextoFuente: string): string;
var
  Indice: Integer;
  ResultadoInvertido: string;
begin
  ResultadoInvertido := '';
  for Indice := Length(TextoFuente) downto 1 do
    ResultadoInvertido := ResultadoInvertido + TextoFuente[Indice];
  Result := ResultadoInvertido;
end;

function ClaseCadena.InvertirPorMitades: string;
var
  LongitudTexto, TamanoMitad: Integer;
  Mitad1, Mitad2, Central: string;
begin
  LongitudTexto := Length(Valor);
  if LongitudTexto <= 1 then
    Exit(Valor);
    
  TamanoMitad := LongitudTexto div 2;
  Mitad1 := InvertirTextoManual(Copy(Valor, 1, TamanoMitad));
  
  if (LongitudTexto mod 2 <> 0) then
  begin
    Central := Valor[TamanoMitad + 1];
    Mitad2 := InvertirTextoManual(Copy(Valor, TamanoMitad + 2, TamanoMitad));
    Result := Mitad1 + Central + Mitad2;
  end
  else
  begin
    Mitad2 := InvertirTextoManual(Copy(Valor, TamanoMitad + 1, TamanoMitad));
    Result := Mitad1 + Mitad2;
  end;
end;`,
    fase4TrazaEjemplo: {
      descripcion: 'Prueba con Valor = "DELPHI"',
      columnas: ['Longitud', 'TamanoMitad', 'Mitad 1 ("DEL")', 'Mitad 2 ("PHI")', 'Resultado Concatenado'],
      filas: [
        ['6 (Par)', '3', '"LED"', '"IHP"', '"LEDIHP"']
      ]
    }
  }
];

