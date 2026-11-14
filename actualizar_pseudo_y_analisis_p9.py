# -*- coding: utf-8 -*-
"""
Script para sincronizar pseudo y analisis en data_practico09.py
con la metodologia de la Ing. Angelica Garzon (cad:String; n,i:Byte).
"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

import data_practico09 as d

ejercicios = d.EJERCICIOS_P9_DATA

analisis_y_pseudo = {
    1: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud calculada con <code>Length(cad)</code>), <code>i</code> (Byte: índice de posición), <code>palBuscada</code> (String: palabra a contabilizar).<br>• <strong>Proceso:</strong> Inicializar <code>i := 1</code> y <code>contador := 0</code>. Recorrer la cadena con ciclo <code>while i &lt;= n</code> saltando espacios en blanco y extrayendo cada palabra continua. Comparar en minúsculas cada palabra extraída contra <code>palBuscada</code>; si coinciden, incrementar <code>contador := contador + 1</code>.<br>• <strong>Salida:</strong> Cantidad de apariciones (Byte).",
        "pseudo": """Funcion ContarPalabra(cad: Cadena; n, i: Entero; palBuscada: Cadena): Entero
  contador <- 0
  palBuscada <- Minusculas(palBuscada)
  i <- 1
  Mientras i <= n Hacer
    Mientras (i <= n) Y (cad[i] = ' ') Hacer
      i <- i + 1
    FinMientras
    palActual <- ''
    Mientras (i <= n) Y (cad[i] <> ' ') Hacer
      palActual <- palActual + cad[i]
      i <- i + 1
    FinMientras
    Si (palActual <> '') Y (Minusculas(palActual) = palBuscada) Entonces
      contador <- contador + 1
    FinSi
  FinMientras
  Retornar contador
FinFuncion"""
    },
    2: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud calculada con <code>Length(cad)</code>), <code>i</code> (Byte: índice de recorrido).<br>• <strong>Proceso:</strong> Definir conjunto constante de signos de puntuación (<code>const signos: set of char</code>). Recorrer desde <code>i := 1</code> hasta <code>n</code> con ciclo <code>while</code>; si <code>cad[i]</code> no pertenece al conjunto, concatenarlo a la cadena resultante.<br>• <strong>Salida:</strong> Cadena limpia de signos de puntuación (String).",
        "pseudo": """Funcion QuitarSignos(cad: Cadena; n, i: Entero): Cadena
  res <- ''
  i <- 1
  signos <- ['.', ',', ';', ':', '!', '?', '"', '\'', '(', ')', '[', ']', '{', '}', '-', '_']
  Mientras i <= n Hacer
    Si No (cad[i] En signos) Entonces
      res <- res + cad[i]
    FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    3: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), <code>nVeces</code> (Byte: repeticiones requeridas).<br>• <strong>Proceso:</strong> Con un ciclo externo <code>j &lt;= nVeces</code> y un ciclo interno <code>while i &lt;= n</code> (con <code>i := 1</code>), acumular los caracteres de <code>cad</code> sucesivamente.<br>• <strong>Salida:</strong> Cadena replicada <code>nVeces</code> (String).",
        "pseudo": """Funcion RepetirCadena(cad: Cadena; n, i, nVeces: Entero): Cadena
  res <- ''
  j <- 1
  Mientras j <= nVeces Hacer
    i <- 1
    Mientras i <= n Hacer
      res <- res + cad[i]
      i <- i + 1
    FinMientras
    j <- j + 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    4: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Inicializar <code>i := 1</code> y bandera booleana <code>nuevaPalabra := True</code>. Recorrer con ciclo <code>while i &lt;= n</code>; si se encuentra espacio, se conserva y se activa la bandera. Al encontrar un carácter alfabético bajo la bandera activa, se convierte a mayúscula con <code>UpCase</code> y se apaga la bandera.<br>• <strong>Salida:</strong> Cadena en formato título / mayúscula inicial (String).",
        "pseudo": """Funcion MayusculaInicial(cad: Cadena; n, i: Entero): Cadena
  res <- ''
  nuevaPalabra <- Verdadero
  i <- 1
  Mientras i <= n Hacer
    Si cad[i] = ' ' Entonces
      res <- res + ' '
      nuevaPalabra <- Verdadero
    Sino
      Si nuevaPalabra Entonces
        res <- res + Mayuscula(cad[i])
        nuevaPalabra <- Falso
      Sino
        res <- res + Minuscula(cad[i])
      FinSi
    FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    5: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice). En la variante procedimiento: parámetros por referencia <code>var may, min: Byte</code>.<br>• <strong>Proceso:</strong> Contadores en 0 e <code>i := 1</code>. Recorrer con <code>while i &lt;= n</code> verificando pertenencia a conjuntos <code>['A'..'Z']</code> y <code>['a'..'z']</code> e incrementando el contador correspondiente.<br>• <strong>Salida:</strong> Reporte textual o asignación en parámetros por referencia.",
        "pseudo": """Funcion ContarMayusMinus(cad: Cadena; n, i: Entero): Cadena
  contMay <- 0; contMin <- 0
  i <- 1
  Mientras i <= n Hacer
    Si cad[i] En ['A'..'Z'] Entonces
      contMay <- contMay + 1
    Sino
      Si cad[i] En ['a'..'z'] Entonces
        contMin <- contMin + 1
      FinSi
    FinSi
    i <- i + 1
  FinMientras
  Retornar 'Mayusculas: ' + ConvertirATexto(contMay) + ', Minusculas: ' + ConvertirATexto(contMin)
FinFuncion"""
    },
    6: {
        "analisis": "• <strong>Entradas:</strong> <code>cad1</code> (String), <code>cad2</code> (String).<br>• <strong>Proceso:</strong> Normalizar ambas cadenas a minúsculas y compararlas mediante operadores relacionales lexicográficos (<code>&lt;</code>, <code>&gt;</code>, <code>=</code>) para dictaminar su orden en el abecedario.<br>• <strong>Salida:</strong> Mensaje detallando cuál cadena precede a la otra.",
        "pseudo": """Funcion CompararCadenas(cad1, cad2: Cadena): Cadena
  c1 <- Minusculas(cad1)
  c2 <- Minusculas(cad2)
  Si c1 < c2 Entonces
    Retornar '"' + cad1 + '" va antes que "' + cad2 + '"'
  Sino
    Si c1 > c2 Entonces
      Retornar '"' + cad2 + '" va antes que "' + cad1 + '"'
    Sino
      Retornar 'Ambas cadenas son alfabeticamente iguales'
    FinSi
  FinSi
FinFuncion"""
    },
    7: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Orquestar funciones modulares independientes, cada una con firma <code>(cad: String; n, i: Byte)</code>: contar palabras, letras totales, vocales, consonantes, mayúsculas y minúsculas usando ciclos <code>while i &lt;= n</code>.<br>• <strong>Salida:</strong> Cadena formateada con el diagnóstico integral.",
        "pseudo": """Funcion AnalizarFrase(cad: Cadena; n, i: Entero): Cadena
  cantP <- ContarPalabras(cad, n, i)
  cantL <- ContarLetrasTotales(cad, n, i)
  cantV <- ContarVocalesP9(cad, n, i)
  cantC <- ContarConsonantesP9(cad, n, i)
  cantM <- ContarMayusculas(cad, n, i)
  cantMin <- ContarMinusculas(cad, n, i)
  Retornar 'Palabras: ' + cantP + ' | Letras: ' + cantL + ' | Vocales: ' + cantV + ' | Consonantes: ' + cantC + ' | Mayusculas: ' + cantM + ' | Minusculas: ' + cantMin
FinFuncion"""
    },
    8: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String: correo), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Localizar con <code>while (i &lt;= n) and (encontrado = false)</code> la posición del carácter <code>'@'</code>. Si existe, inicializar nuevo recorrido desde <code>posArroba + 1</code> hasta <code>n</code> concatenando caracteres del dominio.<br>• <strong>Salida:</strong> Nombre del servidor/dominio o mensaje de error.",
        "pseudo": """Funcion ExtraerDominio(cad: Cadena; n, i: Entero): Cadena
  posArroba <- 0; encontrado <- Falso; i <- 1
  Mientras (i <= n) Y (encontrado = Falso) Hacer
    Si cad[i] = '@' Entonces
      posArroba <- i
      encontrado <- Verdadero
    FinSi
    i <- i + 1
  FinMientras
  Si posArroba > 0 Entonces
    dominio <- ''; i <- posArroba + 1
    Mientras i <= n Hacer
      dominio <- dominio + cad[i]
      i <- i + 1
    FinMientras
    Retornar dominio
  Sino
    Retornar 'Correo sin arroba valida'
  FinSi
FinFuncion"""
    },
    9: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), <code>nDel</code> (Byte: caracteres a suprimir).<br>• <strong>Proceso:</strong> Si <code>nDel &gt;= n</code>, retornar cadena vacía. En caso contrario, iniciar índice <code>i := nDel + 1</code> y con ciclo <code>while i &lt;= n</code> copiar los caracteres restantes.<br>• <strong>Salida:</strong> Subcadena sin los primeros <code>nDel</code> elementos.",
        "pseudo": """Funcion EliminarPrimerosN(cad: Cadena; n, i, nDel: Entero): Cadena
  res <- ''
  Si nDel >= n Entonces
    Retornar ''
  FinSi
  i <- nDel + 1
  Mientras i <= n Hacer
    res <- res + cad[i]
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    10: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>sub</code> (String), <code>n</code> (Byte: longitud de cad), <code>i</code> (Byte: índice), <code>posIndex</code> (Byte: posición de inserción).<br>• <strong>Proceso:</strong> Copiar con <code>while</code> los primeros <code>posIndex - 1</code> caracteres de <code>cad</code>, luego todos los caracteres de <code>sub</code>, y finalmente los caracteres restantes de <code>cad</code>.<br>• <strong>Salida:</strong> Cadena modificada con la subcadena insertada.",
        "pseudo": """Funcion InsertarSubcadena(cad, sub: Cadena; n, i, posIndex: Entero): Cadena
  res <- ''; nSub <- Longitud(sub)
  Si posIndex <= 1 Entonces
    res <- sub + cad
  Sino
    Si posIndex > n Entonces
      res <- cad + sub
    Sino
      i <- 1
      Mientras i < posIndex Hacer
        res <- res + cad[i]; i <- i + 1
      FinMientras
      j <- 1
      Mientras j <= nSub Hacer
        res <- res + sub[j]; j <- j + 1
      FinMientras
      Mientras i <= n Hacer
        res <- res + cad[i]; i <- i + 1
      FinMientras
    FinSi
  FinSi
  Retornar res
FinFuncion"""
    },
    11: {
        "analisis": "• <strong>Entradas:</strong> <code>cad1</code> (String), <code>cad2</code> (String).<br>• <strong>Proceso:</strong> Concatenar ambas cadenas interponiendo un espacio separador si ninguna de ellas se encuentra vacía.<br>• <strong>Salida:</strong> Cadena resultante unificada.",
        "pseudo": """Funcion UnirCadenas(cad1, cad2: Cadena): Cadena
  Si (cad1 <> '') Y (cad2 <> '') Entonces
    Retornar cad1 + ' ' + cad2
  Sino
    Retornar cad1 + cad2
  FinSi
FinFuncion"""
    },
    12: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), <code>k</code> (Byte: ordinal de la palabra a suprimir).<br>• <strong>Proceso:</strong> Recorrer con ciclo <code>while i &lt;= n</code> extrayendo cada palabra. Llevar un contador <code>numPal</code>. Si <code>numPal &lt;&gt; k</code>, concatenar la palabra al acumulador con espacio separador.<br>• <strong>Salida:</strong> Frase sin la palabra número <code>k</code>.",
        "pseudo": """Funcion EliminarPalabraK(cad: Cadena; n, i, k: Entero): Cadena
  i <- 1; numPal <- 0; res <- ''
  Mientras i <= n Hacer
    Mientras (i <= n) Y (cad[i] = ' ') Hacer i <- i + 1 FinMientras
    pal <- ''
    Mientras (i <= n) Y (cad[i] <> ' ') Hacer
      pal <- pal + cad[i]; i <- i + 1
    FinMientras
    Si pal <> '' Entonces
      numPal <- numPal + 1
      Si numPal <> k Entonces
        Si res <> '' Entonces res <- res + ' ' FinSi
        res <- res + pal
      FinSi
    FinSi
  FinMientras
  Retornar res
FinFuncion"""
    },
    13: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Segmentar la cadena en un arreglo de palabras. Analizar si la palabra anterior contenía la consonante 'c' o 'C'; si es así, descartar la palabra actual al reconstruir.<br>• <strong>Salida:</strong> Frase filtrada sin palabras precedidas por términos con 'c'.",
        "pseudo": """Funcion EliminarPalabrasDelanteDeC(cad: Cadena; n, i: Entero): Cadena
  // 1. Extraer palabras con i <- 1; Mientras i <= n
  // 2. Por cada palabra j desde 1 hasta totalP:
  //    Verificar si palabra[j - 1] contiene consonante 'c'
  //    Si no la contiene, añadir palabra[j] a res
  Retornar res
FinFuncion"""
    },
    14: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Máquina de estados con bandera booleana <code>enPalabra := False</code> e <code>i := 1</code>. Al encontrar un carácter no espacio cuando <code>enPalabra = False</code>, se incrementa el contador y se activa la bandera.<br>• <strong>Salida:</strong> Cantidad total de palabras (Byte).",
        "pseudo": """Funcion CantidadPalabras(cad: Cadena; n, i: Entero): Entero
  cantPal <- 0; enPalabra <- Falso; i <- 1
  Mientras i <= n Hacer
    Si cad[i] <> ' ' Entonces
      Si enPalabra = Falso Entonces
        cantPal <- cantPal + 1
        enPalabra <- Verdadero
      FinSi
    Sino
      enPalabra <- Falso
    FinSi
    i <- i + 1
  FinMientras
  Retornar cantPal
FinFuncion"""
    },
    15: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Iniciar índice en <code>i := n</code> y mediante ciclo regresivo <code>while i &gt;= 1</code> acumular <code>cad[i]</code> decrementando <code>i := i - 1</code>.<br>• <strong>Salida:</strong> Cadena invertida de caracteres.",
        "pseudo": """Funcion InvertirCadena(cad: Cadena; n, i: Entero): Cadena
  res <- ''; i <- n
  Mientras i >= 1 Hacer
    res <- res + cad[i]
    i <- i - 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    16: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer las palabras de la cadena. Si existen al menos 2 palabras, invertir los caracteres de <code>palabras[2]</code> con ciclo decreciente y recomponer la frase completa.<br>• <strong>Salida:</strong> Frase con la segunda palabra invertida.",
        "pseudo": """Funcion InvertirSegundaPalabra(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Invertir caracteres de palabras[2]
  // Reconstruir frase uniendo con espacios
  Retornar res
FinFuncion"""
    },
    17: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer palabras con ciclo <code>while i &lt;= n</code>. Para cada palabra evaluar si <code>(Length(p) mod 2 &lt;&gt; 0)</code> y si contiene el carácter 'c'/'C'. Si ambas condiciones se cumplen, transformar a mayúsculas con <code>UpperCase</code>.<br>• <strong>Salida:</strong> Frase con las palabras impares con 'c' en mayúsculas.",
        "pseudo": """Funcion MayusculaPalabrasImparConC(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Para cada palabra j:
  //   Si (Longitud(pal[j]) Mod 2 <> 0) Y (Tiene 'c') Entonces
  //     pal[j] <- Mayusculas(pal[j])
  // Reconstruir frase
  Retornar res
FinFuncion"""
    },
    18: {
        "analisis": "• <strong>Entradas:</strong> <code>cad1</code> (String), <code>cad2</code> (String), <code>n</code> (Byte: longitud de cad1), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Proporciona dos modalidades: concatenación directa con <code>MezclarCadenas</code> o intercalado carácter a carácter con <code>IntercalarCaracteres</code> usando ciclo <code>while i &lt;= maxLen</code>.<br>• <strong>Salida:</strong> Cadena mezclada o intercalada.",
        "pseudo": """Funcion IntercalarCaracteres(cad1, cad2: Cadena; n, i: Entero): Cadena
  res <- ''; n1 <- Longitud(cad1); n2 <- Longitud(cad2)
  maxLen <- n1; Si n2 > maxLen Entonces maxLen <- n2 FinSi
  i <- 1
  Mientras i <= maxLen Hacer
    Si i <= n1 Entonces res <- res + cad1[i] FinSi
    Si i <= n2 Entonces res <- res + cad2[i] FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    19: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Recorrer la cadena carácter por carácter con ciclo <code>while i &lt;= n</code>. Cada carácter no espacio se inserta directamente en su posición ordenada dentro de la cadena resultado mediante comparación secuencial.<br>• <strong>Salida:</strong> Cadena con caracteres ordenados alfabéticamente.",
        "pseudo": """Funcion CadenaCaracteresOrdenados(cad: Cadena; n, i: Entero): Cadena
  res <- ''; i <- 1
  Mientras i <= n Hacer
    Si cad[i] <> ' ' Entonces
      // Insertar ordenadamente cad[i] en res
    FinSi
    i <- i + 1
  FinMientras
  Retornar res
FinFuncion"""
    },
    20: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Conforme se extrae cada palabra con ciclo <code>while i &lt;= n</code>, se busca su posición alfabética en un arreglo y se realiza desplazamiento de elementos para insertarla en tiempo real.<br>• <strong>Salida:</strong> Cadena con las palabras ordenadas de la A a la Z.",
        "pseudo": """Funcion OrdenarPalabrasAlfabeticamente(cad: Cadena; n, i: Entero): Cadena
  // Extraer cada palabra y desplazar elementos para insercion ordenada
  // Reconstruir la oracion con las palabras ordenadas
  Retornar res
FinFuncion"""
    },
    21: {
        "analisis": "• <strong>Entradas:</strong> <code>cadA</code> (String), <code>cadB</code> (String), <code>n</code> (Byte: longitud cadA), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Poblar dos conjuntos tipo <code>set of Char</code> recorriendo cada cadena con ciclos <code>while</code>. Calcular la intersección matemática con el operador <code>*</code> (<code>setC := setA * setB</code>) y retornar los elementos comunes formateados.<br>• <strong>Salida:</strong> Representación textual del conjunto intersección (ej: <code>{c, d, e}</code>).",
        "pseudo": """Funcion InterseccionConjuntos(cadA, cadB: Cadena; n, i: Entero): Cadena
  // Poblar setA con cadA usando i <- 1; Mientras i <= nA
  // Poblar setB con cadB usando i <- 1; Mientras i <= nB
  // setC <- setA * setB
  // Retornar '{' + elementos comunes + '}'
FinFuncion"""
    },
    22: {
        "analisis": "• <strong>Entradas:</strong> <code>num</code> (Integer: valor decimal).<br>• <strong>Proceso:</strong> Algoritmo de divisiones sucesivas entre 2 con ciclo <code>while num &gt; 0</code>; el residuo (<code>num mod 2</code>) se convierte a carácter y se antepone a la cadena binaria.<br>• <strong>Salida:</strong> Representación binaria en String.",
        "pseudo": """Funcion DecimalABinario(num: Entero): Cadena
  Si num = 0 Entonces Retornar '0' FinSi
  res <- ''
  Mientras num > 0 Hacer
    dig <- num Mod 2
    res <- ConvertirATexto(dig) + res
    num <- num Div 2
  FinMientras
  Retornar res
FinFuncion"""
    },
    23: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Inicializar <code>contador := 0</code> e <code>i := 1</code>. Recorrer con ciclo <code>while i &lt;= n</code> evaluando parejas adyacentes <code>cad[i]</code> y <code>cad[i + 1]</code>; si ambas pertenecen al conjunto de vocales <code>voc: set of char</code>, incrementar el contador.<br>• <strong>Salida:</strong> Cantidad de parejas vocálicas contiguas (Byte).",
        "pseudo": """Funcion ContarDosVocalesJuntas(cad: Cadena; n, i: Entero): Entero
  contador <- 0; i <- 1
  Mientras i <= n Hacer
    ayudante <- i + 1
    Si ayudante <= n Entonces
      Si (cad[i] En Vocales) Y (cad[ayudante] En Vocales) Entonces
        contador <- contador + 1
      FinSi
    FinSi
    i <- i + 1
  FinMientras
  Retornar contador
FinFuncion"""
    },
    24: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice), parámetro por referencia <code>var invertida: String</code>.<br>• <strong>Proceso:</strong> Limpiar <code>invertida := ''</code> e iniciar <code>i := n</code>. Mediante ciclo regresivo <code>while i &gt;= 1</code> acumular <code>cad[i]</code> en <code>invertida</code> y decrementar <code>i := i - 1</code>.<br>• <strong>Salida:</strong> Retorno en el parámetro por referencia <code>invertida</code>.",
        "pseudo": """Procedimiento InvertirCadenaProc(cad: Cadena; n, i: Entero; Var invertida: Cadena)
  invertida <- ''; i <- n
  Mientras i >= 1 Hacer
    invertida <- invertida + cad[i]
    i <- i - 1
  FinMientras
FinProcedimiento"""
    },
    25: {
        "analisis": "• <strong>Entradas:</strong> Parámetro por referencia <code>var cad: String</code>, <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Método clásico de ordenación por intercambio directo (burbuja) adaptado a ciclo <code>while huboIntercambio</code> e índice interno <code>while i &lt;= n - 1</code>, permutando caracteres contiguos con variable auxiliar.<br>• <strong>Salida:</strong> Modificación directa de la variable de entrada por referencia.",
        "pseudo": """Procedimiento OrdenarBurbuja(Var cad: Cadena; n, i: Entero)
  huboIntercambio <- Verdadero
  Mientras huboIntercambio Hacer
    huboIntercambio <- Falso
    i <- 1
    Mientras i <= n - 1 Hacer
      Si cad[i] > cad[i + 1] Entonces
        aux <- cad[i]; cad[i] <- cad[i + 1]; cad[i + 1] <- aux
        huboIntercambio <- Verdadero
      FinSi
      i <- i + 1
    FinMientras
  FinMientras
FinProcedimiento"""
    },
    26: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer cada palabra individualmente con ciclo <code>while i &lt;= n</code>. Para cada palabra extraída verificar si tanto el primer carácter <code>pal[1]</code> como el último <code>pal[Length(pal)]</code> pertenecen al conjunto de vocales <code>voc: set of char</code>.<br>• <strong>Salida:</strong> Cantidad de palabras con inicio y fin vocálico (Byte).",
        "pseudo": """Funcion ContarPalabrasVocalesExtremos(cad: Cadena; n, i: Entero): Entero
  contador <- 0; i <- 1
  Mientras i <= n Hacer
    Mientras (i <= n) Y (cad[i] = ' ') Hacer i <- i + 1 FinMientras
    pal <- ''
    Mientras (i <= n) Y (cad[i] <> ' ') Hacer
      pal <- pal + cad[i]; i <- i + 1
    FinMientras
    Si pal <> '' Entonces
      nPal <- Longitud(pal)
      Si (pal[1] En Vocales) Y (pal[nPal] En Vocales) Entonces
        contador <- contador + 1
      FinSi
    FinSi
  FinMientras
  Retornar contador
FinFuncion"""
    },
    27: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer las palabras al arreglo. Tomar la última palabra (<code>palabras[totalP]</code>) y filtrar sus caracteres eliminando todas las consonantes mediante verificación con conjuntos <code>letras - voc</code>.<br>• <strong>Salida:</strong> Frase con la última palabra desprovista de consonantes.",
        "pseudo": """Funcion EliminarConsonantesUltimaPal(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Filtrar palabras[totalP] omitiendo consonantes
  // Reconstruir frase con palabras unidas por espacios
  Retornar res
FinFuncion"""
    },
    28: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>palNueva</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer palabras al arreglo. Desplazar los elementos a partir de la tercera posición hacia adelante con ciclo regresivo para liberar la posición 3, asignando <code>palabras[3] := palNueva</code>.<br>• <strong>Salida:</strong> Frase con la nueva palabra insertada tras la segunda palabra.",
        "pseudo": """Funcion InsertarTrasSegunda(cad, palNueva: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Desplazar palabras desde totalP hacia 3
  // palabras[3] <- palNueva
  // Reconstruir frase
  Retornar res
FinFuncion"""
    },
    29: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Iniciar índice par en <code>i := 2</code>. Mediante ciclo <code>while i &lt;= n</code> concatenar <code>cad[i]</code> e incrementar de dos en dos con <code>i := i + 2</code>.<br>• <strong>Salida:</strong> Cadena compuesta únicamente por los caracteres en índices pares.",
        "pseudo": """Funcion CaracteresIndicesPares(cad: Cadena; n, i: Entero): Cadena
  res <- ''; i <- 2
  Mientras i <= n Hacer
    res <- res + cad[i]
    i <- i + 2
  FinMientras
  Retornar res
FinFuncion"""
    },
    30: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Extraer todas las palabras al arreglo. Al reconstruir la frase resultante, recorrer únicamente desde 1 hasta <code>totalP - 1</code>, suprimiendo la última palabra.<br>• <strong>Salida:</strong> Frase sin la última palabra.",
        "pseudo": """Funcion EliminarUltimaPalabra(cad: Cadena; n, i: Entero): Cadena
  // Extraer palabras con i <- 1; Mientras i <= n
  // Reconstruir frase concatenando desde 1 hasta totalP - 1
  Retornar res
FinFuncion"""
    },
    31: {
        "analisis": "• <strong>Entradas:</strong> <code>cad</code> (String), <code>n</code> (Byte: longitud), <code>i</code> (Byte: índice).<br>• <strong>Proceso:</strong> Normalizar la cadena eliminando espacios y convirtiendo a mayúsculas con ciclo <code>while i &lt;= n</code>. Recorrer la cadena limpia con dos índices convergentes (<code>i := 1</code> y <code>j := nLimpia</code>); si en algún momento <code>limpia[i] &lt;&gt; limpia[j]</code>, se determina que no es capicúa.<br>• <strong>Salida:</strong> Booleano <code>True/False</code> o mensaje descriptivo.",
        "pseudo": """Funcion EsCapicua(cad: Cadena; n, i: Entero): Booleano
  // 1. Limpiar espacios y pasar a mayusculas con i <- 1; Mientras i <= n
  // 2. Comprobar simetria:
  i <- 1; j <- Longitud(limpia); esCap <- Verdadero
  Mientras (i < j) Y esCap Hacer
    Si limpia[i] <> limpia[j] Entonces
      esCap <- Falso
    FinSi
    i <- i + 1; j <- j - 1
  FinMientras
  Retornar esCap
FinFuncion"""
    }
}

# Aplicar a los ejercicios
for ej in ejercicios:
    num = ej["num"]
    if num in analisis_y_pseudo:
        ej["analisis"] = analisis_y_pseudo[num]["analisis"]
        ej["pseudo"] = analisis_y_pseudo[num]["pseudo"]

# Escribir data_practico09.py
ruta = 'd:/Introz2/practico07/data_practico09.py'
output_lines = []
output_lines.append('# -*- coding: utf-8 -*-')
output_lines.append('"""')
output_lines.append('Datos completos de los 31 ejercicios del Práctico #9 (Cadenas, Funciones y Procedimientos)')
output_lines.append('Materia: INF110 - Introducción a la Informática')
output_lines.append('Docente: M.Sc. Angélica Garzón Cuéllar - UAGRM')
output_lines.append('METODOLOGÍA DOCENTE: function Nombre(cad:String; n,i:Byte):Tipo;')
output_lines.append('"""')
output_lines.append('')
output_lines.append('EJERCICIOS_P9_DATA = [')

for idx, ej in enumerate(ejercicios):
    output_lines.append('    {')
    for key in ["num", "titulo", "tipo", "categoria", "analisis", "pseudo",
                "traza_headers", "traza_rows", "codigo_pascal", "codigo_vcl",
                "entrada_ejemplo", "salida_ejemplo", "extra_req", "extra_label", "extra_default"]:
        if key not in ej:
            continue
        val = ej[key]
        if key in ("pseudo", "codigo_pascal", "codigo_vcl", "analisis") and isinstance(val, str) and '\n' in val:
            output_lines.append(f'        "{key}": """{val}""",')
        elif isinstance(val, str):
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            output_lines.append(f'        "{key}": "{escaped}",')
        elif isinstance(val, bool):
            output_lines.append(f'        "{key}": {str(val)},')
        elif isinstance(val, (int, float)):
            output_lines.append(f'        "{key}": {val},')
        elif isinstance(val, list):
            list_repr = repr(val)
            if len(list_repr) < 100:
                output_lines.append(f'        "{key}": {list_repr},')
            else:
                output_lines.append(f'        "{key}": [')
                for item in val:
                    output_lines.append(f'            {repr(item)},')
                output_lines.append(f'        ],')
    
    if idx < len(ejercicios) - 1:
        output_lines.append('    },')
    else:
        output_lines.append('    }')

output_lines.append(']')
output_lines.append('')

with open(ruta, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("data_practico09.py actualizado con analisis y pseudo homogéneos.")

