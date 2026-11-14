program TestPractico08;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  UnitCadenas;

procedure ImprimirSeparador(num: Integer; titulo: String);
begin
  WriteLn('----------------------------------------------------------------------');
  WriteLn('[Ejercicio ', num, '] ', titulo);
  WriteLn('----------------------------------------------------------------------');
end;

var
  s1, s2: String;
  b: Boolean;
  resInt: Integer;
  resStr: String;
  resChr: Char;

begin
  WriteLn('======================================================================');
  WriteLn('       UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO - INF110');
  WriteLn('                     PRACTICO # 8: CADENAS');
  WriteLn('             PRUEBA COMPLETA DE LOS 40 EJERCICIOS');
  WriteLn('======================================================================');
  WriteLn;

  // 1. Contar caracteres
  ImprimirSeparador(1, 'Contar los caracteres de una cadena');
  s1 := 'Universidad Gabriel Rene Moreno';
  WriteLn('Cadena: "', s1, '"');
  WriteLn('Total caracteres: ', ContarCaracteres(s1));
  WriteLn;

  // 2. Primera letra
  ImprimirSeparador(2, 'Mostrar la primera letra de una cadena (Procedimiento)');
  s1 := '  Ingenieria Informatica';
  WriteLn('Cadena: "', s1, '"');
  MostrarPrimeraLetra(s1);
  WriteLn;

  // 3. Ultima letra
  ImprimirSeparador(3, 'Retornar la ultima letra de una cadena');
  s1 := 'Santa Cruz de la Sierra!';
  WriteLn('Cadena: "', s1, '"');
  resChr := UltimaLetra(s1);
  WriteLn('Ultima letra: ', resChr);
  WriteLn;

  // 4. Contar vocales
  ImprimirSeparador(4, 'Contar cuantas vocales tiene una palabra');
  s1 := 'COMPUTADORA';
  WriteLn('Palabra: "', s1, '"');
  WriteLn('Cantidad de vocales: ', ContarVocales(s1));
  WriteLn;

  // 5. Contar consonantes
  ImprimirSeparador(5, 'Contar cuantas consonantes tiene una palabra');
  s1 := 'Algoritmos';
  WriteLn('Palabra: "', s1, '"');
  WriteLn('Cantidad de consonantes: ', ContarConsonantes(s1));
  WriteLn;

  // 6. Cadena en mayúsculas
  ImprimirSeparador(6, 'Mostrar la cadena en mayusculas');
  s1 := 'programacion modular';
  WriteLn('Original:  "', s1, '"');
  WriteLn('Resultado: "', CadenaMayusculas(s1), '"');
  WriteLn;

  // 7. Cadena en minúsculas
  ImprimirSeparador(7, 'Mostrar la cadena en minusculas');
  s1 := 'DELPHI Y PASCAL INF-110';
  WriteLn('Original:  "', s1, '"');
  WriteLn('Resultado: "', CadenaMinusculas(s1), '"');
  WriteLn;

  // 8. Invertir cadena
  ImprimirSeparador(8, 'Invertir una cadena caracter por caracter');
  s1 := 'RENE MORENO';
  WriteLn('Original:  "', s1, '"');
  WriteLn('Invertida: "', InvertirCadena(s1), '"');
  WriteLn;

  // 9. Concatenar dos cadenas
  ImprimirSeparador(9, 'Concatenar dos cadenas');
  s1 := 'Hola ';
  s2 := 'Mundo Delphi';
  WriteLn('Cadena 1: "', s1, '"');
  WriteLn('Cadena 2: "', s2, '"');
  WriteLn('Concatenada: "', ConcatenarCadenas(s1, s2), '"');
  WriteLn;

  // 10. Ocurrencias de letra
  ImprimirSeparador(10, 'Contar cuantas veces aparece una letra especifica');
  s1 := 'Estructuras de Datos y Algoritmos';
  WriteLn('Cadena: "', s1, '"');
  WriteLn('Apariciones de ''a'': ', ContarOcurrenciasLetra(s1, 'a'));
  WriteLn;

  // 11. Eliminar espacios
  ImprimirSeparador(11, 'Eliminar espacios en blanco');
  s1 := ' F I C C T   U A G R M ';
  WriteLn('Original:     "', s1, '"');
  WriteLn('Sin espacios: "', EliminarEspacios(s1), '"');
  WriteLn;

  // 12. Primeros n caracteres
  ImprimirSeparador(12, 'Mostrar solo los primeros N caracteres');
  s1 := 'Facultad de Ciencias de la Computacion';
  WriteLn('Cadena: "', s1, '"');
  WriteLn('Primeros 8 caracteres: "', PrimerosNCaracteres(s1, 8), '"');
  WriteLn;

  // 13. Esta vacia
  ImprimirSeparador(13, 'Determinar si una cadena esta vacia o contiene texto');
  s1 := '   ';
  s2 := 'Hola';
  WriteLn('Cadena 1: "', s1, '" -> Esta vacia? ', EstaVacia(s1));
  WriteLn('Cadena 2: "', s2, '" -> Esta vacia? ', EstaVacia(s2));
  WriteLn;

  // 14. Códigos ASCII
  ImprimirSeparador(14, 'Mostrar codigos ASCII de cada caracter');
  s1 := 'UAGRM';
  WriteLn('Cadena: "', s1, '"');
  MostrarCodigosASCII(s1);
  WriteLn;

  // 15. Contar mayúsculas
  ImprimirSeparador(15, 'Contar cuantas letras mayusculas hay');
  s1 := 'Ingenieria Informatica Sem 2-2025';
  WriteLn('Cadena: "', s1, '"');
  WriteLn('Total mayusculas: ', ContarMayusculas(s1));
  WriteLn;

  // 16. Palíndroma
  ImprimirSeparador(16, 'Determinar si una cadena es palindroma');
  s1 := 'anita lava la tina';
  s2 := 'computadora';
  WriteLn('"', s1, '" -> Es palindroma? ', EsPalindroma(s1));
  WriteLn('"', s2, '" -> Es palindroma? ', EsPalindroma(s2));
  WriteLn;

  // 17. Contar palabras
  ImprimirSeparador(17, 'Contar cuantas palabras hay en una frase');
  s1 := '  El   sol   brilla hoy en Santa Cruz  ';
  WriteLn('Frase: "', s1, '"');
  WriteLn('Cantidad de palabras: ', ContarPalabras(s1));
  WriteLn;

  // 18. Verificar palabra en frase
  ImprimirSeparador(18, 'Verificar si una palabra se encuentra dentro de una frase');
  s1 := 'La tecnologia avanza rapidamente';
  WriteLn('Frase: "', s1, '"');
  WriteLn('Existe "avanza"? ', ExistePalabra(s1, 'avanza'));
  WriteLn('Existe "robot"?  ', ExistePalabra(s1, 'robot'));
  WriteLn;

  // 19. Reemplazar letra
  ImprimirSeparador(19, 'Reemplazar todas las apariciones de una letra por otra');
  s1 := 'banana';
  WriteLn('Original: "', s1, '"');
  WriteLn('Reemplazar ''a'' por ''o'': "', ReemplazarLetra(s1, 'a', 'o'), '"');
  WriteLn;

  // 20. Eliminar letra
  ImprimirSeparador(20, 'Eliminar todas las apariciones de una letra');
  s1 := 'Paralelepipedo';
  WriteLn('Original: "', s1, '"');
  WriteLn('Eliminar ''e'': "', EliminarLetra(s1, 'e'), '"');
  WriteLn;

  // 21. Ocurrencias de palabra
  ImprimirSeparador(21, 'Contar cuantas veces aparece una palabra en un texto');
  s1 := 'sol luna sol estrella sol tierra';
  WriteLn('Texto: "', s1, '"');
  WriteLn('Apariciones de "sol": ', ContarOcurrenciasPalabra(s1, 'sol'));
  WriteLn;

  // 22. Carácter por línea
  ImprimirSeparador(22, 'Mostrar cada caracter en una linea diferente');
  s1 := 'PASCAL';
  WriteLn('Cadena: "', s1, '"');
  MostrarCaracteresPorLinea(s1);
  WriteLn;

  // 23. Contenido: números o letras
  ImprimirSeparador(23, 'Determinar si una cadena contiene numeros o solo letras');
  WriteLn('"HolaMundo"    -> ', DeterminarContenido('HolaMundo'));
  WriteLn('"123456"       -> ', DeterminarContenido('123456'));
  WriteLn('"INF110-2025"  -> ', DeterminarContenido('INF110-2025'));
  WriteLn;

  // 24. Contar dígitos numéricos
  ImprimirSeparador(24, 'Calcular cuantos digitos numericos hay en la cadena');
  s1 := 'Aula 236 Modulo 225 Piso 3';
  WriteLn('Cadena: "', s1, '"');
  WriteLn('Total digitos: ', ContarDigitos(s1));
  WriteLn;

  // 25. Extraer primera palabra
  ImprimirSeparador(25, 'Extraer la primera palabra de una frase');
  s1 := '   Gabriel Rene Moreno fue un ilustre boliviano';
  WriteLn('Frase: "', s1, '"');
  WriteLn('Primera palabra: "', ExtraerPrimeraPalabra(s1), '"');
  WriteLn;

  // 26. Extraer última palabra
  ImprimirSeparador(26, 'Extraer la ultima palabra de una frase');
  s1 := 'Estudiar para el examen final   ';
  WriteLn('Frase: "', s1, '"');
  WriteLn('Ultima palabra: "', ExtraerUltimaPalabra(s1), '"');
  WriteLn;

  // 27. Normalizar espacios
  ImprimirSeparador(27, 'Convertir espacios multiples a un solo espacio');
  s1 := '   Programar    en    Pascal    es    facil   ';
  WriteLn('Original:   "', s1, '"');
  WriteLn('Normalizada:"', NormalizarEspacios(s1), '"');
  WriteLn;

  // 28. Palabras que empiezan con vocal
  ImprimirSeparador(28, 'Mostrar las palabras que empiezan con vocal');
  s1 := 'El aguila vuela sobre el arbol azul y el cielo';
  WriteLn('Frase: "', s1, '"');
  MostrarPalabrasEmpiezanVocal(s1);
  WriteLn;

  // 29. Palabras que terminan en consonante
  ImprimirSeparador(29, 'Mostrar las palabras que terminan en consonante');
  s1 := 'Juan y David juegan futbol en el parque central';
  WriteLn('Frase: "', s1, '"');
  MostrarPalabrasTerminanConsonante(s1);
  WriteLn;

  // 30. Intercalar dos cadenas
  ImprimirSeparador(30, 'Intercalar dos cadenas caracter por caracter');
  s1 := 'ABC';
  s2 := '123';
  WriteLn('Cadena 1: "', s1, '"');
  WriteLn('Cadena 2: "', s2, '"');
  WriteLn('Intercalada: "', IntercalarCadenas(s1, s2), '"');
  WriteLn;

  // 31. Palabras con más de 5 letras
  ImprimirSeparador(31, 'Determinar cuantas palabras con mas de 5 letras hay');
  s1 := 'La programacion estructurada ayuda al desarrollo logico';
  WriteLn('Oracion: "', s1, '"');
  WriteLn('Palabras con > 5 letras: ', ContarPalabrasMasDe5Letras(s1));
  WriteLn;

  // 32. Reemplazar vocales por '*'
  ImprimirSeparador(32, 'Reemplazar todas las vocales por *');
  s1 := 'Ingenieria Informatica';
  WriteLn('Original:   "', s1, '"');
  WriteLn('Con asteriscos: "', ReemplazarVocalesPorAsterisco(s1), '"');
  WriteLn;

  // 33. Eliminar acentos
  ImprimirSeparador(33, 'Eliminar acentos (a, e, i, o, u) de una cadena');
  s1 := 'canción, café, música, árbol, autobús, Perú';
  WriteLn('Original:    "', s1, '"');
  WriteLn('Sin acentos: "', EliminarAcentos(s1), '"');
  WriteLn;

  // 34. Palabra más larga
  ImprimirSeparador(34, 'Mostrar la palabra mas larga de una frase');
  s1 := 'La programacion modular simplifica problemas complejos';
  WriteLn('Frase: "', s1, '"');
  WriteLn('Palabra mas larga: "', PalabraMasLarga(s1), '"');
  WriteLn;

  // 35. Palabra más corta
  ImprimirSeparador(35, 'Mostrar la palabra mas corta de una frase');
  s1 := 'Hoy vi un gran elefante';
  WriteLn('Frase: "', s1, '"');
  WriteLn('Palabra mas corta: "', PalabraMasCorta(s1), '"');
  WriteLn;

  // 36. Contar palabras repetidas
  ImprimirSeparador(36, 'Contar cuantas palabras repetidas hay en un texto');
  s1 := 'el gato y el perro vieron a otro gato bajo el puente';
  WriteLn('Texto: "', s1, '"');
  WriteLn('Cantidad de palabras repetidas distintas: ', ContarPalabrasRepetidas(s1));
  WriteLn;

  // 37. Solo contiene letras
  ImprimirSeparador(37, 'Verificar si una cadena solo contiene letras');
  WriteLn('"SoloLetras" -> ', SoloContieneLetras('SoloLetras'));
  WriteLn('"Letras123"  -> ', SoloContieneLetras('Letras123'));
  WriteLn;

  // 38. Caracteres únicos
  ImprimirSeparador(38, 'Generar nueva cadena con caracteres unicos (sin repetir)');
  s1 := 'FERNANDO ALVAREZ';
  WriteLn('Original: "', s1, '"');
  WriteLn('Unicos:   "', CaracteresUnicos(s1), '"');
  WriteLn;

  // 39. Anagramas
  ImprimirSeparador(39, 'Comprobar si dos cadenas son anagramas');
  WriteLn('"roma" y "amor"       -> Son anagramas? ', SonAnagramas('roma', 'amor'));
  WriteLn('"frase" y "fresa"     -> Son anagramas? ', SonAnagramas('frase', 'fresa'));
  WriteLn('"casa" y "cosa"       -> Son anagramas? ', SonAnagramas('casa', 'cosa'));
  WriteLn;

  // 40. Caracteres de índice impar
  ImprimirSeparador(40, 'Mostrar solo caracteres de indice impar (1, 3, 5...)');
  s1 := 'UNIVERSIDAD';
  WriteLn('Cadena: "', s1, '"');
  WriteLn('Indices impares: "', CaracteresIndiceImpar(s1), '"');
  WriteLn;

  WriteLn('======================================================================');
  WriteLn('          ¡TODOS LOS 40 EJERCICIOS EJECUTADOS CON EXITO!');
  WriteLn('======================================================================');
end.
