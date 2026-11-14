program TestPractico10;
{==============================================================================
  SUITE DE PRUEBAS AUTOMATIZADAS - PRÁCTICO # 10 : MÓDULOS SERIE
  INF110-Z2 • DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar
==============================================================================}

{$mode objfpc}{$H+}

uses
  SysUtils,
  Math,
  UnitPractico10;

var
  total, ok: Integer;

procedure CheckInt(num: Integer; const desc: String; obtenido, esperado: Int64);
begin
  Inc(total);
  if obtenido = esperado then
  begin
    Inc(ok);
    WriteLn('  [OK] Ejercicio ', num, ': ', desc, ' -> ', obtenido);
  end
  else
  begin
    WriteLn('  [FAIL] Ejercicio ', num, ': ', desc, ' -> Obtenido: ', obtenido, ' | Esperado: ', esperado);
  end;
end;

procedure CheckReal(num: Integer; const desc: String; obtenido, esperado: Double);
begin
  Inc(total);
  if SameValue(obtenido, esperado, 0.0001) then
  begin
    Inc(ok);
    WriteLn('  [OK] Ejercicio ', num, ': ', desc, ' -> ', FloatToStrF(obtenido, ffFixed, 7, 4));
  end
  else
  begin
    WriteLn('  [FAIL] Ejercicio ', num, ': ', desc, ' -> Obtenido: ', FloatToStrF(obtenido, ffFixed, 7, 4), ' | Esperado: ', FloatToStrF(esperado, ffFixed, 7, 4));
  end;
end;

begin
  total := 0;
  ok := 0;
  WriteLn('================================================================');
  WriteLn('   VERIFICACION AUTOMATIZADA: PRACTICO # 10 - MODULOS SERIE     ');
  WriteLn('   (METODOLOGIA OFICIAL: numero, contador: Integer)            ');
  WriteLn('================================================================');
  WriteLn;

  // Pruebas de Clase Oficial
  CheckInt(0, 'Clase: sumaDoble(5, 1)', sumaDoble(5, 1), 31);
  CheckInt(0, 'Clase: sumafactorial(5, 1)', sumafactorial(5, 1), 153);
  CheckInt(0, 'Clase: sumaCuadratica(5, 1)', sumaCuadratica(5, 1), 55);
  CheckInt(0, 'Clase: sumaParImpar(5, 1)', sumaParImpar(5, 1), 70);

  // 20 Ejercicios del Práctico #10
  CheckInt(1, 'SF = 0+1+1+2+3 (n=5)', Serie01_Fibonacci(5, 1), 7);
  CheckInt(1, 'SF = Fibonacci hasta 21 (n=9)', Serie01_Fibonacci(9, 1), 54);

  CheckInt(2, 'SF = 1+2+6+120+720 (n=5)', Serie02_FactorialPotencias(5, 1), 849);
  CheckInt(2, 'SF = 10 terminos dados (n=10)', Serie02_FactorialPotencias(10, 1), 1089);

  CheckInt(3, 'SF = 1+5+4+10+9+15 (n=6)', Serie03_CuadradosMultiplos5(6, 1), 44);
  CheckInt(3, 'SF = 10 terminos (n=10)', Serie03_CuadradosMultiplos5(10, 1), 130);

  CheckInt(4, 'SF = 3+6+12+24 (n=4)', Serie04_DobleBase3(4, 1), 45);
  CheckInt(4, 'SF = 8 terminos dados (n=8)', Serie04_DobleBase3(8, 1), 765);

  CheckInt(5, 'SF = 3+9+13+39+43 (n=5)', Serie05_Por3Mas4(5, 1), 107);
  CheckInt(5, 'SF = 7 terminos dados (n=7)', Serie05_Por3Mas4(7, 1), 369);

  CheckInt(6, 'F = 3+6+12+24 (n=4)', Serie06_GeometricaBase3(4, 1), 45);

  CheckInt(7, 'F = 1+4+5+9+14 (n=5)', Serie07_Aditiva1_4(5, 1), 33);
  CheckInt(7, 'F = 6 terminos dados (n=6)', Serie07_Aditiva1_4(6, 1), 56);

  CheckInt(8, 'F = 1+4+9+16+25 (n=5)', Serie08_Cuadrados(5, 1), 55);

  CheckInt(9, 'F = 1x2 + 3x4 + 5x6 (n=3)', Serie09_ProductoImparPar(3, 1), 44);

  CheckInt(10, 'F = 1+2-3+4-5 (n=5)', Serie10_SignosAlternos(5, 1), -1);
  CheckInt(10, 'F = 1+2-3+4-5+6-7 (n=7)', Serie10_SignosAlternos(7, 1), -2);

  CheckInt(11, 'F = 1x1 + 2x3 + 3x4 + 4x7 (n=4)', Serie11_ProductoIndiceLucas(4, 1), 47);

  CheckReal(12, 'F = 1/2 + 3/4 + 5/6 (n=3)', Serie12_FraccionImparPar(3, 1), 2.083333);

  CheckInt(13, 'F = 1^2 + 3^2 + 5^2 + 7^2 (n=4)', Serie13_CuadradosImpares(4, 1), 84);

  CheckReal(14, 'F = x/1! + x^3/2! + x^5/3! (x=2, n=3)', Serie14_PotenciasXFactorial(2.0, 3, 1), 11.333333);

  CheckInt(15, 'F = 1+1+2+2+4+4 (n=6)', Serie15_Potencias2Duplicadas(6, 1), 14);

  CheckInt(16, 'F = 1*3 + 3*5 + 5*7 (n=3)', Serie16_ProductoImparesConsecutivos(3, 1), 53);

  CheckInt(17, 'F = 11 + 22 + 33 + 44 (n=4)', Serie17_Multiplos11(4, 1), 110);

  CheckInt(18, 'F = 3x1 + 5x2 + 7x6 + 9x24 (n=4)', Serie18_ImparPorFactorial(4, 1), 271);

  CheckInt(19, 'S = 6 + 12 + 24 + 48 (n=4)', Serie19_GeometricaBase6(4, 1), 90);

  CheckReal(20, 'SF = 1/2 + 2/6 + 6/10 (n=3)', Serie20_FactorialEntreProgresion(3, 1), 1.433333);

  WriteLn;
  WriteLn('----------------------------------------------------------------');
  WriteLn('  RESULTADO: ', ok, ' de ', total, ' pruebas pasaron exitosamente (', (ok * 100) div total, '%)');
  WriteLn('================================================================');
end.
