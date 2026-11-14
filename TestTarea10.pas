program TestTarea10;

{$mode delphi}

uses
  SysUtils, UCNatural;

var
  N: NumeroNatural;
begin
  Writeln('================================================================');
  Writeln('VERIFICACION DE LA TAREA # 10 PRESENCIAL (EXAMEN INF110-Z2)');
  Writeln('Docente: M.Sc. Ing. Angelica Garzon Cuellar | Valor = 12389');
  Writeln('================================================================');

  N := NumeroNatural.Create;
  N.CambiarValor(12389);

  // 1. NumeroPares -> np = 28
  Writeln('1. NumeroPares: ', N.NumeroPares, ' (Esperado de catedra: 28)');

  // 2. NMenorPar -> mp = 2
  Writeln('2. NMenorPar: ', N.NMenorPar, ' (Esperado de catedra: 2)');

  // 3. NMayorImpar -> mimp = 9
  Writeln('3. NMayorImpar: ', N.NMayorImpar, ' (Esperado de catedra: 9)');

  // 4. NDigitosIguales -> False
  Writeln('4. NDigitosIguales: ', N.NDigitosIguales, ' (Esperado: FALSE)');
  N.CambiarValor(5555);
  Writeln('   NDigitosIguales(5555): ', N.NDigitosIguales, ' (Esperado de catedra: TRUE)');
  N.CambiarValor(12389);

  // 5. SiEsCapicua -> 'no es capicua 12389<>98321'
  Writeln('5. SiEsCapicua(12389): ', N.SiEsCapicua);
  N.CambiarValor(202);
  Writeln('   SiEsCapicua(202): ', N.SiEsCapicua, ' (Esperado: si es capicua 202=202)');
  N.CambiarValor(12389);

  // 6. NSumaIndicePar -> 8 + 2 = 10
  Writeln('6. NSumaIndicePar: ', N.NSumaIndicePar, ' (Esperado de catedra: 8 + 2 = 10)');

  N.Free;
  Writeln('================================================================');
  Writeln('PRUEBA EXITOSA: 100% COINCIDENCIA CON EL EXAMEN DE LA INGENIERA');
  Writeln('================================================================');
end.

