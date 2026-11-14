program Practico07;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  UnitNumeros in 'UnitNumeros.pas';

procedure MostrarMenu;
var
  opcion: Integer;
  n, n2, nPares, nImpares: Cardinal;
  dMayor, dMenor, primero, ultimo: Byte;
  octStr: String;
begin
  repeat
    Writeln('===============================================================');
    Writeln('             PRACTICO # 7 - NUMEROS NATURALES (DELPHI)        ');
    Writeln('===============================================================');
    Writeln(' 1. Suma de digitos impares mayores a 3 (5, 7, 9)');
    Writeln(' 2. Digito mayor de los indices impares');
    Writeln(' 3. Sumar digitos de un numero');
    Writeln(' 4. Promedio de digitos menores a 7');
    Writeln(' 5. Digito mayor y digito menor');
    Writeln(' 6. Formar numero con los digitos pares');
    Writeln(' 7. Separar numero en pares e impares');
    Writeln(' 8. Digito mayor de los digitos pares');
    Writeln(' 9. Mostrar digitos multiplos de 3');
    Writeln('10. Obtener el primer y ultimo digito');
    Writeln('11. Eliminar el primer y ultimo digito');
    Writeln('12. Invertir numero');
    Writeln('13. Contar digitos multiplos de 4');
    Writeln('14. Digito menor de los multiplos de 3');
    Writeln('15. Verificar si es Capicua');
    Writeln('16. Convertir a Binario');
    Writeln('17. Convertir a Hexadecimal');
    Writeln('18. Convertir a Octal');
    Writeln('19. Sumar digitos primos');
    Writeln('20. Promedio de digitos multiplos de 3 y 5');
    Writeln('21. Promedio de digitos primos');
    Writeln('22. Formar numero con digitos primos');
    Writeln('23. Decimal a Hexadecimal');
    Writeln('24. Decimal a Binario');
    Writeln('25. Octal a Hexadecimal');
    Writeln(' 0. Salir');
    Writeln('===============================================================');
    Write('Seleccione una opcion (0-25): ');
    Readln(opcion);

    if (opcion >= 1) and (opcion <= 24) then
    begin
      Write('Ingrese un numero natural: ');
      Readln(n);
    end;

    Writeln;
    case opcion of
      1: Writeln('Resultado: ', SumaImparesMayores3(n));
      2: Writeln('Resultado: ', DigitoMayorIndicesImpares(n));
      3: Writeln('Resultado: ', SumaDigitos(n));
      4: Writeln('Resultado: ', PromedioDigitosMenores7(n):0:2);
      5:
        begin
          MayorYMenorDigito(n, dMayor, dMenor);
          Writeln('Mayor digito: ', dMayor, ' | Menor digito: ', dMenor);
        end;
      6: Writeln('Numero formado por pares: ', FormarNumeroPares(n));
      7:
        begin
          SepararParesImpares(n, nPares, nImpares);
          Writeln('Pares: ', nPares, ' | Impares: ', nImpares);
        end;
      8:
        begin
          if MayorDigitoPar(n) = -1 then
            Writeln('No tiene digitos pares')
          else
            Writeln('Mayor digito par: ', MayorDigitoPar(n));
        end;
      9: Writeln('Digitos multiplos de 3: ', DigitosMultiplosDe3(n));
      10:
        begin
          PrimerYUltimoDigito(n, primero, ultimo);
          Writeln('Primero: ', primero, ' | Ultimo: ', ultimo);
        end;
      11: Writeln('Numero sin extremos: ', EliminarPrimerYUltimoDigito(n));
      12: Writeln('Numero invertido: ', InvertirNumero(n));
      13: Writeln('Cantidad de digitos multiplos de 4: ', ContarMultiplosDeCuatro(n));
      14:
        begin
          if MenorDigitoMultiploDeTres(n) = -1 then
            Writeln('No tiene multiplos de 3')
          else
            Writeln('Menor digito multiplo de 3: ', MenorDigitoMultiploDeTres(n));
        end;
      15:
        begin
          if EsCapicua(n) then
            Writeln(n, ' SI es capicua')
          else
            Writeln(n, ' NO es capicua');
        end;
      16: Writeln('Binario: ', DecimalABinario(n));
      17: Writeln('Hexadecimal: ', DecimalAHexadecimal(n));
      18: Writeln('Octal: ', DecimalAOctal(n));
      19: Writeln('Suma de digitos primos: ', SumaDigitosPrimos(n));
      20: Writeln('Promedio multiplos de 3 o 5: ', PromedioMultiplos3y5(n):0:2);
      21: Writeln('Promedio digitos primos: ', PromedioDigitosPrimos(n):0:2);
      22: Writeln('Numero con digitos primos: ', FormarNumeroPrimos(n));
      23: Writeln('Hexadecimal: ', DecimalAHexadecimal2(n));
      24: Writeln('Binario: ', DecimalABinario2(n));
      25:
        begin
          Write('Ingrese numero en base Octal (ej. 752): ');
          Readln(octStr);
          Writeln('Hexadecimal: ', OctalAHexadecimal(octStr));
        end;
      0: Writeln('Saliendo del programa...');
    else
      Writeln('Opcion no valida.');
    end;

    if opcion <> 0 then
    begin
      Writeln;
      Write('Presione [ENTER] para continuar...');
      Readln;
    end;

  until opcion = 0;
end;

begin
  try
    MostrarMenu;
  except
    on E: Exception do
      Writeln('Error: ', E.Message);
  end;
end.
