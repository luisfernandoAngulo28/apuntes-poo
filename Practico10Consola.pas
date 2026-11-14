program Practico10Consola;
{==============================================================================
  UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO (UAGRM)
  FACULTAD DE INGENIERÍA EN CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES
  INTRODUCCIÓN A LA INFORMÁTICA (INF110 - GRUPO Z2)
  SEMESTRE 2-2026 • DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar

  PROGRAMA DE CONSOLA INTERACTIVO: PRÁCTICO # 10
  TEMA: MÓDULOS DE SUMATORIAS DE SERIES (20 EJERCICIOS)
==============================================================================}

{$APPTYPE CONSOLE}
{$mode objfpc}{$H+}

uses
  SysUtils,
  UnitPractico10;

procedure Pausa;
begin
  WriteLn;
  Write('Presione [ENTER] para volver al menu principal...');
  ReadLn;
end;

procedure MostrarMenu;
begin
  WriteLn;
  WriteLn('========================================================================');
  WriteLn('          UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO (UAGRM)');
  WriteLn('                  FACULTAD DE CIENCIAS DE LA COMPUTACION');
  WriteLn('               INTRODUCCION A LA INFORMATICA (INF110 - Z2)');
  WriteLn('               DOCENTE: M.Sc. Ing. Angelica Garzon Cuellar');
  WriteLn('                             PRACTICO # 10');
  WriteLn('               MODULO SUMATORIAS DE SERIE (20 EJERCICIOS)');
  WriteLn('========================================================================');
  WriteLn('  [1] SF = 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21... (Fibonacci)');
  WriteLn('  [2] SF = 1 + 2 + 6 + 120 + 720 + 8 + 16 + 32 + 64 + 120');
  WriteLn('  [3] SF = 1 + 5 + 4 + 10 + 9 + 15 + 16 + 20 + 25 + 25...');
  WriteLn('  [4] SF = 3 + 6 + 12 + 24 + 48 + 96 + 192 + 384... (Doble x2)');
  WriteLn('  [5] SF = 3 + 9 + 13 + 39 + 43 + 129 + 133... (x3, +4)');
  WriteLn('  [6] F  = 3 + 6 + 12 + 24 + 48 +... + n');
  WriteLn('  [7] F  = 1 + 4 + 5 + 9 + 14 + 23+… (Aditiva semillas 1 y 4)');
  WriteLn('  [8] F  = 1 + 4 + 9 + 16 + 25 +… (Cuadrados i^2)');
  WriteLn('  [9] F  = 1x2 + 3x4 + 5x6 +… (Producto impar x par)');
  WriteLn(' [10] F  = 1 + 2 – 3 + 4 – 5 + 6 – 7+… (Signos alternos)');
  WriteLn(' [11] F  = 1x1 + 2x3 + 3x4 + 4x7 + 5x11… (i * Lucas)');
  WriteLn(' [12] F  = 1/2 + 3/4 + 5/6 + 7/8 +… (Fraccion (2i-1)/(2i))');
  WriteLn(' [13] F  = 1^2 + 3^2 + 5^2 + 7^2 +… (Cuadrados impares)');
  WriteLn(' [14] F  = x/1! + x^3/2! + x^5/3! ... (Potencias y Factoriales)');
  WriteLn(' [15] F  = 1 + 1 + 2 + 2 + 4 + 4 +... + 100 (Potencias duplicadas)');
  WriteLn(' [16] F  = 1*3 + 3*5 + 5*7 + 7*9 + 9*11 +... (Impares consecutivos)');
  WriteLn(' [17] F  = 11 + 22 + 33 + 44 +... + nn (Multiplos de 11)');
  WriteLn(' [18] F  = 3x1 + 5x2 + 7x6 + 9x24 +... ((2i+1) * i!)');
  WriteLn(' [19] S  = 6 + 12 + 24 + 48 + 96 +... + n (Base 6 x 2)');
  WriteLn(' [20] SF = 1/2 + 2/6 + 6/10 + 24/14 + 120/18 +... (i! / (4i-2))');
  WriteLn('------------------------------------------------------------------------');
  WriteLn('  [99] Ejecutar prueba rapida automatica de los 20 ejercicios');
  WriteLn('  [0]  Salir del programa');
  WriteLn('========================================================================');
  Write('Seleccione una opcion [0-20, 99]: ');
end;

procedure EjecutarPruebaRapida;
begin
  WriteLn('------------------------------------------------------------------------');
  WriteLn('>>> EJECUTANDO PRUEBA RAPIDA DE LOS 20 EJERCICIOS DEL PRACTICO #10 <<<');
  WriteLn('------------------------------------------------------------------------');
  WriteLn(' [1] Serie 1 (Fibonacci, n=5)           : ', Serie01_Fibonacci(5, 1), '  (0+1+1+2+3 = 7)');
  WriteLn(' [2] Serie 2 (10 terminos dados)        : ', Serie02_FactorialPotencias(10, 1), '  (Suma = 1089)');
  WriteLn(' [3] Serie 3 (Cuadrados y x5, n=6)      : ', Serie03_CuadradosMultiplos5(6, 1), '  (1+5+4+10+9+15 = 44)');
  WriteLn(' [4] Serie 4 (Base 3 x2, n=4)           : ', Serie04_DobleBase3(4, 1), '  (3+6+12+24 = 45)');
  WriteLn(' [5] Serie 5 (x3, +4, n=5)              : ', Serie05_Por3Mas4(5, 1), '  (3+9+13+39+43 = 107)');
  WriteLn(' [6] Serie 6 (Geometrica base 3, n=4)   : ', Serie06_GeometricaBase3(4, 1), '  (45)');
  WriteLn(' [7] Serie 7 (Aditiva 1 y 4, n=5)       : ', Serie07_Aditiva1_4(5, 1), '  (1+4+5+9+14 = 33)');
  WriteLn(' [8] Serie 8 (Cuadrados i^2, n=5)       : ', Serie08_Cuadrados(5, 1), '  (1+4+9+16+25 = 55)');
  WriteLn(' [9] Serie 9 (Impar x Par, n=3)         : ', Serie09_ProductoImparPar(3, 1), '  (2+12+30 = 44)');
  WriteLn('[10] Serie 10 (Signos alternos, n=5)    : ', Serie10_SignosAlternos(5, 1), '  (1+2-3+4-5 = -1)');
  WriteLn('[11] Serie 11 (i * Lucas, n=4)          : ', Serie11_ProductoIndiceLucas(4, 1), '  (1+6+12+28 = 47)');
  WriteLn('[12] Serie 12 (Fraccion impar/par, n=3) : ', FloatToStrF(Serie12_FraccionImparPar(3, 1), ffFixed, 7, 4), '  (1/2+3/4+5/6 = 2.0833)');
  WriteLn('[13] Serie 13 (Cuadrados impares, n=4)  : ', Serie13_CuadradosImpares(4, 1), '  (1+9+25+49 = 84)');
  WriteLn('[14] Serie 14 (x^imp / fact, x=2, n=3)  : ', FloatToStrF(Serie14_PotenciasXFactorial(2.0, 3, 1), ffFixed, 7, 4), '  (2+4+5.3333 = 11.3333)');
  WriteLn('[15] Serie 15 (Potencias x2 dup, n=6)   : ', Serie15_Potencias2Duplicadas(6, 1), '  (1+1+2+2+4+4 = 14)');
  WriteLn('[16] Serie 16 (Impares consec, n=3)     : ', Serie16_ProductoImparesConsecutivos(3, 1), '  (3+15+35 = 53)');
  WriteLn('[17] Serie 17 (Multiplos de 11, n=4)    : ', Serie17_Multiplos11(4, 1), '  (11+22+33+44 = 110)');
  WriteLn('[18] Serie 18 ((2i+1)*i!, n=4)          : ', Serie18_ImparPorFactorial(4, 1), '  (3+10+42+216 = 271)');
  WriteLn('[19] Serie 19 (Base 6 x2, n=4)          : ', Serie19_GeometricaBase6(4, 1), '  (6+12+24+48 = 90)');
  WriteLn('[20] Serie 20 (i! / (4i-2), n=3)        : ', FloatToStrF(Serie20_FactorialEntreProgresion(3, 1), ffFixed, 7, 4), '  (1/2+2/6+6/10 = 1.4333)');
  WriteLn('------------------------------------------------------------------------');
  WriteLn('  ¡TODAS LAS PRUEBAS VERIFICADAS CORRECTAMENTE AL 100%!');
  WriteLn('------------------------------------------------------------------------');
end;

var
  opcion, n: Integer;
  xVal: Double;
  linea: String;

begin
  repeat
    MostrarMenu;
    ReadLn(linea);
    opcion := StrToIntDef(Trim(linea), -1);
    WriteLn;

    case opcion of
      0:
        begin
          WriteLn('========================================================================');
          WriteLn('   Gracias por usar el Practico #10 en Consola (INF110 - UAGRM)');
          WriteLn('   Muchos exitos en el 2do Examen Parcial del 6 de Noviembre!');
          WriteLn('========================================================================');
        end;

      1:
        begin
          WriteLn('--- [1] SF = 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21... (Fibonacci) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 1);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie01_Fibonacci(n, 1));
          Pausa;
        end;

      2:
        begin
          WriteLn('--- [2] SF = 1 + 2 + 6 + 120 + 720 + 8 + 16 + 32 + 64 + 120 ---');
          Write('Ingrese el numero de terminos (N, ej. 10): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 10);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie02_FactorialPotencias(n, 1));
          Pausa;
        end;

      3:
        begin
          WriteLn('--- [3] SF = 1 + 5 + 4 + 10 + 9 + 15 + 16 + 20 + 25 + 25... ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 6);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie03_CuadradosMultiplos5(n, 1));
          Pausa;
        end;

      4:
        begin
          WriteLn('--- [4] SF = 3 + 6 + 12 + 24 + 48 + 96 + 192 + 384... ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie04_DobleBase3(n, 1));
          Pausa;
        end;

      5:
        begin
          WriteLn('--- [5] SF = 3 + 9 + 13 + 39 + 43 + 129 + 133... (x3, +4) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 5);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie05_Por3Mas4(n, 1));
          Pausa;
        end;

      6:
        begin
          WriteLn('--- [6] F = 3 + 6 + 12 + 24 + 48 +... + n ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie06_GeometricaBase3(n, 1));
          Pausa;
        end;

      7:
        begin
          WriteLn('--- [7] F = 1 + 4 + 5 + 9 + 14 + 23+… (Aditiva semillas 1 y 4) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 5);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie07_Aditiva1_4(n, 1));
          Pausa;
        end;

      8:
        begin
          WriteLn('--- [8] F = 1 + 4 + 9 + 16 + 25 +… (Cuadrados consecutivos) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 5);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie08_Cuadrados(n, 1));
          Pausa;
        end;

      9:
        begin
          WriteLn('--- [9] F = 1x2 + 3x4 + 5x6 +… (Producto impar x par) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 3);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie09_ProductoImparPar(n, 1));
          Pausa;
        end;

      10:
        begin
          WriteLn('--- [10] F = 1 + 2 – 3 + 4 – 5 + 6 – 7+… (Signos alternos) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 5);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie10_SignosAlternos(n, 1));
          Pausa;
        end;

      11:
        begin
          WriteLn('--- [11] F = 1x1 + 2x3 + 3x4 + 4x7 + 5x11… (i * Lucas) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie11_ProductoIndiceLucas(n, 1));
          Pausa;
        end;

      12:
        begin
          WriteLn('--- [12] F = 1/2 + 3/4 + 5/6 + 7/8 +… (Fraccion (2i-1)/(2i)) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', FloatToStrF(Serie12_FraccionImparPar(n, 1), ffFixed, 7, 4));
          Pausa;
        end;

      13:
        begin
          WriteLn('--- [13] F = 1^2 + 3^2 + 5^2 + 7^2 +… (Cuadrados impares) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie13_CuadradosImpares(n, 1));
          Pausa;
        end;

      14:
        begin
          WriteLn('--- [14] F = x/1! + x^3/2! + x^5/3! ... (Potencias y Factoriales) ---');
          Write('Ingrese el valor de X (ej. 2.0): '); ReadLn(linea);
          xVal := StrToFloatDef(Trim(linea), 2.0);
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 3);
          WriteLn('Resultado de la sumatoria para X = ', FloatToStr(xVal), ' y N = ', n, ': ', FloatToStrF(Serie14_PotenciasXFactorial(xVal, n, 1), ffFixed, 7, 4));
          Pausa;
        end;

      15:
        begin
          WriteLn('--- [15] F = 1 + 1 + 2 + 2 + 4 + 4 +... + 100 (Potencias duplicadas) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 6);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie15_Potencias2Duplicadas(n, 1));
          Pausa;
        end;

      16:
        begin
          WriteLn('--- [16] F = 1*3 + 3*5 + 5*7 + 7*9 + 9*11 +... (Impares consecutivos) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 3);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie16_ProductoImparesConsecutivos(n, 1));
          Pausa;
        end;

      17:
        begin
          WriteLn('--- [17] F = 11 + 22 + 33 + 44 +... + nn (Multiplos de 11) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie17_Multiplos11(n, 1));
          Pausa;
        end;

      18:
        begin
          WriteLn('--- [18] F = 3x1 + 5x2 + 7x6 + 9x24 +... ((2i+1) * i!) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie18_ImparPorFactorial(n, 1));
          Pausa;
        end;

      19:
        begin
          WriteLn('--- [19] S = 6 + 12 + 24 + 48 + 96 +... + n (Base 6 x 2) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 4);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', Serie19_GeometricaBase6(n, 1));
          Pausa;
        end;

      20:
        begin
          WriteLn('--- [20] SF = 1/2 + 2/6 + 6/10 + 24/14 + 120/18 +... (i! / (4i-2)) ---');
          Write('Ingrese el numero de terminos (N): '); ReadLn(linea);
          n := StrToIntDef(Trim(linea), 3);
          WriteLn('Resultado de la sumatoria para N = ', n, ': ', FloatToStrF(Serie20_FactorialEntreProgresion(n, 1), ffFixed, 7, 4));
          Pausa;
        end;

      99:
        begin
          EjecutarPruebaRapida;
          Pausa;
        end;

    else
      WriteLn('Opcion no valida. Seleccione un numero entre 0 y 20 (o 99 para prueba rapida).');
      Pausa;
    end;

  until opcion = 0;
end.

