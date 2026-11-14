# 🎨 GUÍA DE MODELOS MENTALES GRÁFICOS · EXAMEN FINAL INF-110
## Universidad Autónoma Gabriel René Moreno · FICCT
**Materia:** Introducción a la Informática (INF-110) · **Grupos:** Z2 y SF  
**Docente:** M.Sc. Ing. Angélica Garzón Cuéllar  

---

## 📌 INTRODUCCIÓN: EL ENFOQUE VISUAL EN PASCAL / DELPHI

Para los programadores visuales, la memoria de la computadora y los bucles no son conceptos abstractos: son **mecanismos físicos, engranajes sincronizados y cintas transportadoras**.

Esta guía condensa la **Trilogía del Examen Final (Series, Números y Cadenas)** y la **Metodología de las 4 Fases** en diagramas gráficos intuitivos que puedes recordar en tu mente durante la prueba.

---

## 🔢 1. NÚMEROS Y DÍGITOS: «La Máquina Extractora MOD 10 & DIV 10»

Cada vez que tengas que procesar un `NumeroNatural`, visualízalo como un bloque que entra a una **máquina trituradora con dos cuchillas**:

```
                         NÚMERO ORIGINAL: [ 4 5 2 1 ]
                                      │
                                      ▼
                   ┌──────────────────────────────────────┐
                   │    MÁQUINA EXTRACTORA DE DÍGITOS     │
                   └──────────────────┬───────────────────┘
                                      │
             ┌────────────────────────┴────────────────────────┐
             ▼                                                 ▼
      d := n MOD 10;                                    n := n DIV 10;
  (La PINZA saca el último dígito)                  (La SIERRA corta la cola)
             │                                                 │
             ▼                                                 ▼
     DÍGITO EXTRAÍDO                                  NÚMERO QUE QUEDA
         [ 1 ]                                            [ 4 5 2 ]
```

### 🎞️ La Película de Ejecución Paso a Paso (`while n > 0 do`)

```
Paso 1:  [ 4 5 2 1 ]  ──►  d = 1  ──►  Queda: [ 4 5 2 ]
Paso 2:  [ 4 5 2 ]    ──►  d = 2  ──►  Queda: [ 4 5 ]
Paso 3:  [ 4 5 ]      ──►  d = 5  ──►  Queda: [ 4 ]
Paso 4:  [ 4 ]        ──►  d = 4  ──►  Queda: [ 0 ]  ──►  FIN (n = 0)
```

---

### 🏗️ Las 2 Formas Gráficas de Reconstruir un Número

```
FORMA A: Ponderación Decimal (De derecha a izquierda)
Uso: Eliminar repetidos, preservar orden original.

Fórmula:
  Resultado := Resultado + (Digito * Multiplicador);
  Multiplicador := Multiplicador * 10;

Diagrama:
  [ 1 ] * 1       =        1
  [ 2 ] * 10      =       20
  [ 5 ] * 100     =      500
  [ 4 ] * 1000    =   + 4000
  ──────────────────────────
  Resultado final =     4521

────────────────────────────────────────────────────────────

FORMA B: Empuje hacia la Izquierda (De izquierda a derecha)
Uso: Invertir número, apilado de dígitos.

Fórmula:
  Resultado := (Resultado * 10) + Digito;

Diagrama:
  Inicio:   0
  Paso 1:   (0 * 10) + 1   = 1
  Paso 2:   (1 * 10) + 2   = 12
  Paso 3:   (12 * 10) + 5  = 125
  Paso 4:   (125 * 10) + 4 = 1254  ◄── (¡Queda invertido!)
```

---

## ⚡ 2. SERIES NUMÉRICAS: «El Sistema de Tres Engranajes»

Toda sumatoria fraccionaria en los exámenes de la Ing. Garzón es una máquina con **tres engranajes sincronizados** que giran al mismo tiempo dentro de un ciclo `for Contador := 1 to NumeroTerminos do`:

$$\text{Ejemplo Examen:} \quad S = +\frac{1}{2} - \frac{3}{4} + \frac{5}{8} - \frac{7}{16} + \frac{9}{32} \dots$$

```
                       CICLO FOR (Contador = 1 hasta N)
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         ▼                            ▼                            ▼
   [ ENGRANAJE 1 ]              [ ENGRANAJE 2 ]              [ ENGRANAJE 3 ]
        SIGNO                      NUMERADOR                   DENOMINADOR
  + , - , + , - , +           1 , 3 , 5 , 7 , 9            2 , 4 , 8 , 16 , 32
         │                            │                            │
  Signo := -Signo             Num := 2 * i - 1             Den := Den * 2
         │                            │                            │
         └────────────────────────────┼────────────────────────────┘
                                      ▼
                        FRACCIÓN DE CADA TÉRMINO:
                           Signo * (Num / Den)
                                      │
                                      ▼
                         [ ACUMULADOR / ALCANCÍA ]
                        Suma := Suma + TerminoActual
```

### 🧭 Regla de Oro Visual («Divide y Vencerás»)
> **Nunca mires la serie completa como un monstruo.**  
> Tapa con tu mano el denominador y resuelve solo el numerador. Luego tapa el numerador y resuelve el denominador. Al final, únelos con `/`.

---

## 🔤 3. CADENAS DE CARACTERES: «El Tren de Vagones Numerados»

En Delphi/Pascal, un `string` es un tren de vagones ordenados con base 1:

```
Texto = 'DELPHI'    ──►   Longitud = 6

   Vagón 1     Vagón 2     Vagón 3     Vagón 4     Vagón 5     Vagón 6
  ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐
  │   D   │   │   E   │   │   L   │   │   P   │   │   H   │   │   I   │
  └───────┘   └───────┘   └───────┘   └───────┘   └───────┘   └───────┘
  ▲                               ▲   ▲                               ▲
  │                               │   │                               │
  └─── MITAD 1: Copy(Valor, 1, 3) ┘   └─── MITAD 2: Copy(Valor, 4, 3) ┘
```

### 🪞 Operación Examen Final: Invertir por Mitades

```
Caso Par ('DELPHI', L = 6):
  TamanoMitad = 6 div 2 = 3
  
  Mitad 1: [ D ][ E ][ L ]    ──(Espejo)──►    [ L ][ E ][ D ]
  Mitad 2: [ P ][ H ][ I ]    ──(Espejo)──►    [ I ][ H ][ P ]

  Concatenación:
  [ L ][ E ][ D ]  +  [ I ][ H ][ P ]   =   [ L E D I H P ]

Caso Impar ('RADAR', L = 5):
  TamanoMitad = 5 div 2 = 2
  
  Mitad 1: [ R ][ A ]         ──(Espejo)──►    [ A ][ R ]
  Centro:  [ D ]              ──(Fijo)────►    [ D ]
  Mitad 2: [ A ][ R ]         ──(Espejo)──►    [ R ][ A ]

  Concatenación:
  [ A ][ R ]  +  [ D ]  +  [ R ][ A ]   =   [ A R D R A ]
```

---

## 🏛️ 4. LA METODOLOGÍA OFICIAL DE LAS 4 FASES (CÓMO CALIFICA LA DOCENTE)

```
┌────────────────────────────────────────────────────────────────────────┐
│ FASE 1: ANÁLISIS METODOLÓGICO (Caja Negra)                            │
│ ┌───────────────┐     ┌────────────────────────┐     ┌───────────────┐ │
│ │ 📥 ENTRADAS   │ ──► │  ⚙️ PROCESO             │ ──► │ 📤 SALIDA     │ │
│ │ X: Real       │     │  Ley de Formación:     │     │ S: Double     │ │
│ │ N: Cardinal   │     │  Término i = (X^i)/i!  │     └───────────────┘ │
│ └───────────────┘     └────────────────────────┘                       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ FASE 2: ALGORITMO / PSEUDOCÓDIGO FORMAL                               │
│  Inicio                                                                │
│      Suma := 0; Factorial := 1;                                        │
│      Para i := 1 Hasta N Hacer ...                                     │
│  Fin                                                                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ FASE 3: IMPLEMENTACIÓN PASCAL / DELPHI (CLEAN CODE)                   │
│  • Tipos fuertes: Cardinal, Byte, Double                               │
│  • Variables autodescriptivas (NumeroTerminos, SumaTotal)              │
│  • 100% libre de variables globales innecesarias                       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ FASE 4: PRUEBA DE ESCRITORIO (TRAZA TABULAR)                          │
│  Contador  |  Factorial  |  Potencia  |  Termino  |  SumaAcumulada     │
│  ──────────┼─────────────┼────────────┼───────────┼───────────────     │
│      1     |      1      |     2      |   0.5000  |    0.5000          │
│      2     |      2      |     4      |   0.5000  |    1.0000          │
│      3     |      6      |     8      |   0.7500  |    1.7500          │
└────────────────────────────────────────────────────────────────────────┘
```

