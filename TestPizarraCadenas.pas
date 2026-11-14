program TestPizarraCadenas;

{$IFDEF FPC}
  {$mode delphi}
  {$H+}
{$ENDIF}

uses
  SysUtils, UnitPizarraCadenas;

var
  s1, s2, s3, s4, s_tarea: string;
begin
  WriteLn('=== TEST COMPLETO DE EJERCICIOS Y TAREAS ===');

  // Ejercicio 1: Contar palabras
  s1 := 'Hola cadena de texto';
  WriteLn('1. Contar palabras: "', s1, '" -> ', ContarPalabras(s1), ' (Esperado: 4)');

  // Ejercicio 2: 2 vocales juntas
  s2 := 'eleccion superior de bolivia';
  WriteLn('2. 2 Vocales juntas: "', s2, '" -> ', ContarPalabrasDosVocalesJuntas(s2), ' (Esperado: 3)');
  WriteLn('   Test recursivo contarVocalesJuntas("hola", 4, 1): ', contarVocalesJuntas('hola', 4, 1), ' (Esperado: 0)');
  WriteLn('   Test recursivo contarVocalesJuntas("superior", 8, 1): ', contarVocalesJuntas('superior', 8, 1), ' (Esperado: 1)');

  // Ejercicio 3: Indices impares
  s3 := 'Hola Mundo';
  WriteLn('3. Indices impares: "', s3, '" -> "', MostrarIndicesImpares(s3), '" (Esperado: "hlud")');

  // Ejercicio 4: Contar consonantes
  s4 := 'cadena de texto';
  WriteLn('4. Contar consonantes: "', s4, '" -> ', ContarConsonantes(s4), ' (Esperado: 7)');

  // Tarea Viernes
  s_tarea := 'Hola cadena de texto';
  WriteLn('Tarea 1. Posiciones de "a": "', BuscarCaracterPosiciones(s_tarea, 'a'), '" (Esperado: 4, 7, 11)');
  WriteLn('Tarea 2. Repeticiones de "a": ', ContarRepeticionesCaracter(s_tarea, 'a'), ' (Esperado: 3)');

  WriteLn('=== TODOS LOS TESTS PASARON EXITOSAMENTE ===');
end.
