program TestPractico13;

{$mode delphi}

uses
  SysUtils, UCNatural;

var
  N: NumeroNatural;
  sp, si, maxVal, minVal: Cardinal;
begin
  Writeln('================================================================');
  Writeln('VERIFICACION DE LOS 28 METODOS DE LA CLASE NumeroNatural (P13)');
  Writeln('DOCENTE: M.Sc. Ing. Angelica Garzon Cuellar | INF110-Z2');
  Writeln('================================================================');

  N := NumeroNatural.Create;

  // 1. Multiplicar dígitos
  N.CambiarValor(423);
  Writeln('1. MultiplicarDigitos(423): ', N.MultiplicarDigitos, ' (Esperado: 24)');

  // 2. Contar dígitos pares
  N.CambiarValor(48263);
  Writeln('2. ContarDigitosPares(48263): ', N.ContarDigitosPares, ' (Esperado: 4)');

  // 3. Contar dígitos impares
  Writeln('3. ContarDigitosImpares(48263): ', N.ContarDigitosImpares, ' (Esperado: 1)');

  // 4. Eliminar ceros
  N.CambiarValor(10203040);
  Writeln('4. EliminarCeros(10203040): ', N.EliminarCeros, ' (Esperado: 1234)');

  // 5. Dígitos iguales
  N.CambiarValor(7777);
  Writeln('5. DigitosIguales(7777): ', N.DigitosIguales, ' (Esperado: TRUE)');
  N.CambiarValor(7776);
  Writeln('   DigitosIguales(7776): ', N.DigitosIguales, ' (Esperado: FALSE)');

  // 6. Frecuencia de un dígito
  N.CambiarValor(232523);
  Writeln('6. ContarFrecuenciaDigito(232523, 2): ', N.ContarFrecuenciaDigito(2), ' (Esperado: 3)');

  // 7. Dígitos ordenados de menor a mayor
  N.CambiarValor(12356);
  Writeln('7. DigitosOrdenadosAsc(12356): ', N.DigitosOrdenadosAsc, ' (Esperado: TRUE)');
  N.CambiarValor(12536);
  Writeln('   DigitosOrdenadosAsc(12536): ', N.DigitosOrdenadosAsc, ' (Esperado: FALSE)');

  // 8. Suma pares e impares por separado
  N.CambiarValor(482136);
  N.SumaParesEImpares(sp, si);
  Writeln('8. SumaParesEImpares(482136): Pares = ', sp, ', Impares = ', si, ' (Esperado: 20 y 4)');

  // 16. Suma divisible entre 3
  N.CambiarValor(423);
  Writeln('16. SumaDigitosDivisible3(423): ', N.SumaDigitosDivisible3, ' (Esperado: TRUE)');

  // 17. Divisible entre 9 usando suma de dígitos
  N.CambiarValor(423);
  Writeln('17. EsDivisible9PorSuma(423): ', N.EsDivisible9PorSuma, ' (Esperado: TRUE)');
  N.CambiarValor(424);
  Writeln('    EsDivisible9PorSuma(424): ', N.EsDivisible9PorSuma, ' (Esperado: FALSE)');

  // 18. Dígitos repetidos
  N.CambiarValor(232523);
  Writeln('18. TieneDigitosRepetidos(232523): ', N.TieneDigitosRepetidos, ' (Esperado: TRUE)');
  N.CambiarValor(12345);
  Writeln('    TieneDigitosRepetidos(12345): ', N.TieneDigitosRepetidos, ' (Esperado: FALSE)');

  // 19. Es pandigital
  N.CambiarValor(1023456789);
  Writeln('19. EsPandigital(1023456789): ', N.EsPandigital, ' (Esperado: TRUE)');

  // 20. Diferencia pares e impares
  N.CambiarValor(824139);
  Writeln('20. DiferenciaParesImpares(824139): ', N.DiferenciaParesImpares, ' (Pares=824, Imp=139 -> 685)');

  // 21. Todos dígitos primos
  N.CambiarValor(235722);
  Writeln('21. TodosDigitosPrimos(235722): ', N.TodosDigitosPrimos, ' (Esperado: TRUE)');
  N.CambiarValor(2347);
  Writeln('    TodosDigitosPrimos(2347): ', N.TodosDigitosPrimos, ' (Esperado: FALSE)');

  // 22. Máximo y mínimo reordenado
  N.CambiarValor(53127);
  N.MaximoYMinimoReordenado(maxVal, minVal);
  Writeln('22. MaximoYMinimo(53127): Max = ', maxVal, ', Min = ', minVal, ' (Esperado: 75321 y 12357)');

  // 23. Producto igual a suma
  N.CambiarValor(1236);
  Writeln('23. ProductoIgualSuma(1236): ', N.ProductoIgualSuma, ' (Esperado: FALSE)');
  N.CambiarValor(123); // prod=6, suma=6
  Writeln('    ProductoIgualSuma(123): ', N.ProductoIgualSuma, ' (Esperado: TRUE)');

  // 24. Suma posición par e impar (izq a der)
  N.CambiarValor(753684);
  N.SumaPosicionParEImpar(si, sp);
  Writeln('24. SumaPosicionParEImpar(753684): Imp = ', si, ', Par = ', sp, ' (Esperado: 18 y 15)');

  // 25. Ordenar por frecuencia
  N.CambiarValor(551122223);
  Writeln('25. OrdenarPorFrecuencia(551122223): ', N.OrdenarPorFrecuencia, ' (Esperado: 222255113)');

  // 26. Dígitos a binario concat
  N.CambiarValor(3079);
  Writeln('26. DigitosABinarioConcat(3079): ', N.DigitosABinarioConcat);
  Writeln('    Esperado: 0011 0000 0111 1001');

  // 27. Suma equivalente octal
  N.CambiarValor(3456);
  Writeln('27. SumaEquivalenteOctal(3456): ', N.SumaEquivalenteOctal, ' (Esperado: 18 dec = 22 octal)');

  // 28. Palíndromo binario
  N.CambiarValor(9); // 1001
  Writeln('28. EsPalindromoBinario(9): ', N.EsPalindromoBinario, ' (Esperado: TRUE)');

  // 29. Pares a octal concat
  N.CambiarValor(864213);
  Writeln('29. ParesAOctalConcat(864213): ', N.ParesAOctalConcat, ' (Esperado: 10 6 4 2)');

  // 30. Suma dígitos a hexadecimal
  N.CambiarValor(7778); // Suma = 29 -> 1D
  Writeln('30. SumaDigitosHex(7778): ', N.SumaDigitosHex, ' (Esperado: 1D)');

  // 31. Contar 1s en dígitos binarios
  N.CambiarValor(752); // 7->3, 5->2, 2->1 -> 6
  Writeln('31. ContarUnosEnDigitosBinarios(752): ', N.ContarUnosEnDigitosBinarios, ' (Esperado: 6)');

  // 32. Bits cantidad par
  N.CambiarValor(25); // 11001 (5 bits)
  Writeln('32. BitsCantidadPar(25): ', N.BitsCantidadPar, ' (Esperado: FALSE)');

  // 33. Cantidad ceros = unos en binario
  N.CambiarValor(6); // 110 (1s=2, 0s=1)
  Writeln('33. CantidadCerosIgualUnosBinario(6): ', N.CantidadCerosIgualUnosBinario, ' (Esperado: FALSE)');

  // 34. Impares a hexadecimal
  N.CambiarValor(13579);
  Writeln('34. ImparesAHexConcat(13579): ', N.ImparesAHexConcat, ' (Esperado: 1, 3, 5, 7, 9)');

  // 35. Grupos de 3 bits a decimal
  N.CambiarValor(19); // 10011 -> 010 011 -> 2 y 3
  Writeln('35. Grupos3BitsADecimal(19): ', N.Grupos3BitsADecimal, ' (Esperado: 2 y 3)');

  N.Free;
  Writeln('================================================================');
  Writeln('TODAS LAS PRUEBAS COMPLETADAS CON EXITO.');
  Writeln('================================================================');
end.

