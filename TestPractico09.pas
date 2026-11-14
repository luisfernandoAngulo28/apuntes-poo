program TestPractico09;

{ Test de los 31 ejercicios del Práctico #9 - Estilo (cad:String; n,i:Byte) }

{$mode objfpc}{$H+}

uses
  SysUtils, UnitPractico09;

var
  ok, total: Integer;
  cad, cad2, res, inv: String;
  n, i: Byte;
  m, mi: Byte;

procedure Check(const nombre: String; condicion: Boolean);
begin
  Inc(total);
  if condicion then begin
    Inc(ok);
    WriteLn('  [OK] ', nombre);
  end else
    WriteLn('  [FAIL] ', nombre);
end;

begin
  ok := 0; total := 0;
  WriteLn('=== TEST PRACTICO 9 (31 Ejercicios - Estilo n,i:Byte) ===');
  WriteLn;

  // 1. ContarPalabra
  cad := 'hola mundo hola';
  n := Length(cad);
  Check('1. ContarPalabra "hola" en "hola mundo hola" = 2',
        ContarPalabra(cad, n, i, 'hola') = 2);

  // 2. QuitarSignos
  cad := 'Hola, mundo!';
  n := Length(cad);
  Check('2. QuitarSignos "Hola, mundo!" = "Hola mundo"',
        QuitarSignos(cad, n, i) = 'Hola mundo');

  // 3. RepetirCadena
  cad := 'ab';
  n := Length(cad);
  Check('3. RepetirCadena "ab" x3 = "ababab"',
        RepetirCadena(cad, n, i, 3) = 'ababab');

  // 4. MayusculaInicial
  cad := 'hola mundo';
  n := Length(cad);
  Check('4. MayusculaInicial "hola mundo" = "Hola Mundo"',
        MayusculaInicial(cad, n, i) = 'Hola Mundo');

  // 5. ContarMayusMinus
  cad := 'Hola Mundo';
  n := Length(cad);
  res := ContarMayusMinus(cad, n, i);
  Check('5. ContarMayusMinus "Hola Mundo" contiene "Mayusculas: 2"',
        Pos('Mayusculas: 2', res) > 0);

  // 5b. ContarMayusMinusProc
  ContarMayusMinusProc(cad, n, i, m, mi);
  Check('5b. ContarMayusMinusProc may=2, min=7',
        (m = 2) and (mi = 7));

  // 6. CompararCadenas
  Check('6. CompararCadenas "Ana" vs "Pedro"',
        Pos('Ana', CompararCadenas('Ana', 'Pedro')) > 0);

  // 7. Analisis de frase
  cad := 'Hola Mundo';
  n := Length(cad);
  Check('7a. ContarPalabras "Hola Mundo" = 2',
        ContarPalabras(cad, n, i) = 2);
  Check('7b. ContarLetrasTotales "Hola Mundo" = 9',
        ContarLetrasTotales(cad, n, i) = 9);
  Check('7c. ContarVocalesP9 "Hola Mundo" = 4',
        ContarVocalesP9(cad, n, i) = 4);
  Check('7d. ContarConsonantesP9 "Hola Mundo" = 5',
        ContarConsonantesP9(cad, n, i) = 5);
  Check('7e. ContarMayusculas "Hola Mundo" = 2',
        ContarMayusculas(cad, n, i) = 2);
  Check('7f. ContarMinusculas "Hola Mundo" = 7',
        ContarMinusculas(cad, n, i) = 7);
  res := AnalizarFrase(cad, n, i);
  Check('7g. AnalizarFrase contiene "Palabras: 2"',
        Pos('Palabras: 2', res) > 0);

  // 8. ExtraerDominio
  cad := 'alumno@uagrm.edu.bo';
  n := Length(cad);
  Check('8. ExtraerDominio "alumno@uagrm.edu.bo" = "uagrm.edu.bo"',
        ExtraerDominio(cad, n, i) = 'uagrm.edu.bo');

  // 9. EliminarPrimerosN
  cad := 'Hola Mundo';
  n := Length(cad);
  Check('9. EliminarPrimerosN "Hola Mundo" del=5 = "Mundo"',
        EliminarPrimerosN(cad, n, i, 5) = 'Mundo');

  // 10. InsertarSubcadena
  cad := 'HolaMundo';
  n := Length(cad);
  Check('10. InsertarSubcadena "HolaMundo" sub=" " pos=5 = "Hola Mundo"',
        InsertarSubcadena(cad, ' ', n, i, 5) = 'Hola Mundo');

  // 11. UnirCadenas
  Check('11. UnirCadenas "Hola"+"Mundo" = "Hola Mundo"',
        UnirCadenas('Hola', 'Mundo') = 'Hola Mundo');

  // 12. EliminarPalabraK
  cad := 'Hola mundo cruel';
  n := Length(cad);
  Check('12. EliminarPalabraK "Hola mundo cruel" k=2 = "Hola cruel"',
        EliminarPalabraK(cad, n, i, 2) = 'Hola cruel');

  // 13. EliminarPalabrasDelanteDeC
  cad := 'la casa bonita';
  n := Length(cad);
  res := EliminarPalabrasDelanteDeC(cad, n, i);
  Check('13. EliminarPalabrasDelanteDeC "la casa bonita" = "la casa"',
        res = 'la casa');

  // 14. CantidadPalabras
  cad := 'uno dos tres';
  n := Length(cad);
  Check('14. CantidadPalabras "uno dos tres" = 3',
        CantidadPalabras(cad, n, i) = 3);

  // 15. InvertirCadena
  cad := 'Hola';
  n := Length(cad);
  Check('15. InvertirCadena "Hola" = "aloH"',
        InvertirCadena(cad, n, i) = 'aloH');

  // 16. InvertirSegundaPalabra
  cad := 'Hola Mundo';
  n := Length(cad);
  Check('16. InvertirSegundaPalabra "Hola Mundo" = "Hola odnuM"',
        InvertirSegundaPalabra(cad, n, i) = 'Hola odnuM');

  // 17. MayusculaPalabrasImparConC
  cad := 'casa color';
  n := Length(cad);
  res := MayusculaPalabrasImparConC(cad, n, i);
  Check('17. MayusculaPalabrasImparConC "casa color" -> COLOR en mayus',
        Pos('COLOR', res) > 0);

  // 18. MezclarCadenas & IntercalarCaracteres
  Check('18a. MezclarCadenas "ana"+"jose" = "anajose"',
        MezclarCadenas('ana', 'jose') = 'anajose');
  cad := 'abc';
  cad2 := '123';
  n := Length(cad);
  Check('18b. IntercalarCaracteres "abc"+"123" = "a1b2c3"',
        IntercalarCaracteres(cad, cad2, n, i) = 'a1b2c3');

  // 19. CadenaCaracteresOrdenados
  cad := 'dcba';
  n := Length(cad);
  Check('19. CadenaCaracteresOrdenados "dcba" = "abcd"',
        CadenaCaracteresOrdenados(cad, n, i) = 'abcd');

  // 20. OrdenarPalabrasAlfabeticamente
  cad := 'banana apple cherry';
  n := Length(cad);
  Check('20. OrdenarPalabras "banana apple cherry" = "apple banana cherry"',
        OrdenarPalabrasAlfabeticamente(cad, n, i) = 'apple banana cherry');

  // 21. InterseccionConjuntos
  cad := 'abcde';
  cad2 := 'cdefg';
  n := Length(cad);
  res := InterseccionConjuntos(cad, cad2, n, i);
  Check('21. InterseccionConjuntos "abcde" ∩ "cdefg" contiene c,d,e',
        (Pos('c', res) > 0) and (Pos('d', res) > 0) and (Pos('e', res) > 0));

  // 22. DecimalABinario
  Check('22. DecimalABinario(10) = "1010"',
        DecimalABinario(10) = '1010');

  // 23. ContarDosVocalesJuntas
  cad := 'bueno aire';
  n := Length(cad);
  Check('23. ContarDosVocalesJuntas "bueno aire" = 2',
        ContarDosVocalesJuntas(cad, n, i) = 2);

  // 24. InvertirCadenaProc
  cad := 'Hola';
  n := Length(cad);
  inv := '';
  InvertirCadenaProc(cad, n, i, inv);
  Check('24. InvertirCadenaProc "Hola" -> "aloH"',
        inv = 'aloH');

  // 25. OrdenarBurbuja
  cad := 'dcba';
  n := Length(cad);
  OrdenarBurbuja(cad, n, i);
  Check('25. OrdenarBurbuja "dcba" -> "abcd"',
        cad = 'abcd');

  // 26. ContarPalabrasVocalesExtremos
  cad := 'ala este gol uno';
  n := Length(cad);
  Check('26. ContarPalabrasVocalesExtremos "ala este gol uno" = 3',
        ContarPalabrasVocalesExtremos(cad, n, i) = 3);

  // 27. EliminarConsonantesUltimaPal
  cad := 'Hola Mundo';
  n := Length(cad);
  Check('27. EliminarConsonantesUltimaPal "Hola Mundo" = "Hola uo"',
        EliminarConsonantesUltimaPal(cad, n, i) = 'Hola uo');

  // 28. InsertarTrasSegunda
  cad := 'Hola Mundo Cruel';
  n := Length(cad);
  Check('28. InsertarTrasSegunda "Hola Mundo Cruel" pal="Bello" = "Hola Mundo Bello Cruel"',
        InsertarTrasSegunda(cad, 'Bello', n, i) = 'Hola Mundo Bello Cruel');

  // 29. CaracteresIndicesPares
  cad := 'abcdef';
  n := Length(cad);
  Check('29. CaracteresIndicesPares "abcdef" = "bdf"',
        CaracteresIndicesPares(cad, n, i) = 'bdf');

  // 30. EliminarUltimaPalabra
  cad := 'Hola Mundo Cruel';
  n := Length(cad);
  Check('30. EliminarUltimaPalabra "Hola Mundo Cruel" = "Hola Mundo"',
        EliminarUltimaPalabra(cad, n, i) = 'Hola Mundo');

  // 31. EsCapicua / MensajeCapicua
  cad := 'anilina';
  n := Length(cad);
  Check('31a. EsCapicua "anilina" = True',
        EsCapicua(cad, n, i) = True);
  cad := 'hola';
  n := Length(cad);
  Check('31b. EsCapicua "hola" = False',
        EsCapicua(cad, n, i) = False);
  cad := 'anilina';
  n := Length(cad);
  Check('31c. MensajeCapicua contiene "Capicua"',
        Pos('Capicua', MensajeCapicua(cad, n, i)) > 0);

  WriteLn;
  WriteLn('=== Resultado: ', ok, '/', total, ' tests pasaron ===');
  if ok = total then
    WriteLn('** TODOS LOS TESTS PASARON **')
  else
    WriteLn('** ATENCION: ', total - ok, ' tests fallaron **');
end.
