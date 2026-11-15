# 🎙️ GUIÓN MAESTRO PARA NOTEBOOKLM: LO ESENCIAL DE NÚMEROS Y DÍGITOS
## Cátedra: Introducción a la Informática (INF-110) · FICCT - UAGRM
**Docente:** M.Sc. Ing. Angélica Garzón Cuéllar  
**Tema Core del Examen Final:** Números Naturales, Extracción de Dígitos y Algoritmos Acumulativos  
**Caso de Estudio Modelo:** Raíz Digital de un Número Natural (Suma sucesiva hasta menor a 10)

---

## 🧭 SECCIÓN 1: EL MAPA CONCEPTUAL (CULTURA GENERAL DE DÍGITOS)
*Al igual que en las arquitecturas modernas donde cada petición tiene una regla clara, en la programación de números naturales existen 4 leyes universales:*

1. **La Pinza (`d := N mod 10`):** Extrae siempre el último dígito del extremo derecho (residuo de dividir entre 10).
2. **La Sierra (`N := N div 10`):** Recorta el número eliminando el dígito ya procesado (cociente entero).
3. **El Guardián (`while N > 0 do`):** Bucle que garantiza procesar todos los dígitos hasta que el número se extinga en 0.
4. **La Reconstrucción Ponderada (`res := res + (d * mult)`):** Permite armar un nuevo número conservando el orden original de sus cifras.

> **Regla Mnemotécnica en 1 Línea:**  
> **Mod 10:** saca la cola · **Div 10:** corta la cola · **While > 0:** procesa todo · **Mult * 10:** preserva el orden.

---

## 🎯 SECCIÓN 2: EL PATRÓN DE BUCLES ANIDADOS (EL CASO RAÍZ DIGITAL)

### ¿Qué es la Raíz Digital?
Es la suma iterativa de los dígitos de un número natural hasta que el resultado final sea estrictamente menor a 10 (un solo dígito decimal entre 0 y 9).

### El Concepto Visual: Dos Engranajes Concéntricos
Para resolver este problema no alcanza con un solo bucle, se necesitan **dos bucles trabajando en equipo**:
* **Bucle Externo (`while N >= 10 do`):** Es el supervisor general. Pregunta: *¿El número todavía tiene 2 o más dígitos?* Mientras sea mayor o igual a 10, reinicia el ciclo.
* **Bucle Interno (`while N > 0 do`):** Es el obrero triturador. Toma el valor actual de `N`, le extrae dígito por dígito con `mod 10`, los acumula en `suma`, y los recorta con `div 10`.
* **El Puente de Conexión (`N := suma`):** Al terminar de sumar los dígitos, el total acumulado se convierte en el nuevo `N` para la siguiente ronda.

---

## 📋 SECCIÓN 3: RESOLUCIÓN OFICIAL COMPLETA EN LAS 4 FASES DE EVALUACIÓN

### FASE 1: ANÁLISIS METODOLÓGICO FORMAL (Caja Negra)
* **1.1. Entrada(s):** 
  - `N`: Número natural a procesar. Tipo de dato en Delphi: `Cardinal` (Entero positivo sin signo de 32 bits, rango $0$ a $4,294,967,295$, ideal para evitar desbordamientos).
* **1.2. Salida(s):** 
  - `Resultado`: Dígito final único. Tipo de dato en Delphi: `Byte` (Rango $0$ a $255$, técnicamente entre $0$ y $9$, aplicando Clean Code y optimización de memoria).
* **1.3. Ley de Formación / Lógica Algorítmica:**
  - Si $N < 10$, la raíz digital es el mismo $N$ (caso base directo).
  - Si $N \ge 10$, se descomponen sus dígitos sumándolos en una variable local `suma`. Al terminar esa pasada, $N$ adopta el valor de `suma`. Este ciclo se repite mientras $N \ge 10$.
* **1.4. Módulo Delphi:** 
  - Tipo: `FUNCTION` (porque recibe un valor escalar de entrada y devuelve un único resultado escalar procesado).
  - Firma: `function RaizDigital(NumeroEntrada: Cardinal): Byte;`

---

### FASE 2: DISEÑO EN PSEUDOCÓDIGO OFICIAL (Notación Garzón)

```text
Funcion RaizDigital(N: Cardinal): Byte
Variables:
    sumaAcumulada: Cardinal
    digitoActual: Byte
Inicio
    // Bucle externo: Repite mientras N tenga 2 o más dígitos
    Mientras N >= 10 Hacer
        sumaAcumulada <- 0
        
        // Bucle interno: Descompone y suma todos los dígitos del N actual
        Mientras N > 0 Hacer
            digitoActual <- N MOD 10
            sumaAcumulada <- sumaAcumulada + digitoActual
            N <- N DIV 10
        FinMientras
        
        // Actualizamos N con la suma obtenida para evaluar si ya es < 10
        N <- sumaAcumulada
    FinMientras
    
    Retornar N
FinFuncion
```

---

### FASE 3: IMPLEMENTACIÓN DELPHI / PASCAL (Clean Code & Buenas Prácticas)

```pascal
unit UNumerosRaizDigital;

interface

// Declaración pública de la función modular
function CalcularRaizDigital(NumeroEntrada: Cardinal): Byte;

implementation

function CalcularRaizDigital(NumeroEntrada: Cardinal): Byte;
var
  NumeroActual: Cardinal;
  SumaParcial: Cardinal;
  DigitoExtraido: Byte;
begin
  NumeroActual := NumeroEntrada;

  // Bucle Externo: Controla que el número resultante tenga un solo dígito (< 10)
  while NumeroActual >= 10 do
  begin
    SumaParcial := 0;

    // Bucle Interno: Suma todos los dígitos del número actual
    while NumeroActual > 0 do
    begin
      DigitoExtraido := NumeroActual mod 10;
      SumaParcial := SumaParcial + DigitoExtraido;
      NumeroActual := NumeroActual div 10;
    end;

    // El resultado parcial se convierte en el nuevo número a evaluar
    NumeroActual := SumaParcial;
  end;

  Result := NumeroActual;
end;

end.
```

#### 🛡️ Justificación de Buenas Prácticas Aplicadas (Clean Code):
1. **Tipado Estricto:** Uso de `Cardinal` para el número (evita números negativos accidentales) y `Byte` para el dígito y el resultado final (ocupa solo 1 byte en RAM).
2. **Variables Autodescriptivas:** Cero nombres confusos como `a`, `b`, `c`. Se usan `NumeroActual`, `SumaParcial`, `DigitoExtraido`.
3. **Aislamiento Funcional:** No se usan variables globales; todos los recursos son locales y la función es 100% determinista y reutilizable.

---

### FASE 4: PRUEBA DE ESCRITORIO TABULAR (Traza de Ejecución en Cámara Lenta)
*Datos de prueba oficial: $N = 15378$*

| Iteración Externa | N al Inicio | Dígitos Procesados (`mod 10`) | Operación Matemática de Suma | N al Finalizar Vuelta | ¿N < 10? (Condición de Parada) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Inicio** | `15378` | - | Inicialización de variables | `15378` | ¿$15378 < 10$? **NO** (Entra al bucle) |
| **Vuelta 1** | `15378` | $8, 7, 3, 5, 1$ | $8 + 7 + 3 + 5 + 1$ | `24` | ¿$24 < 10$? **NO** (Continúa) |
| **Vuelta 2** | `24` | $4, 2$ | $4 + 2$ | `6` | ¿$6 < 10$? **SÍ** (Condición cumplida) |
| **Salida** | `6` | - | Termina el bucle externo | `Result = 6` | **FIN DEL ALGORITMO** |

**Conclusión Científica de la Traza:**  
Para la entrada $N = 15378$, la secuencia de reducciones es $15378 \longrightarrow 24 \longrightarrow 6$. El resultado final escalar retornado es **`6`**, verificado formalmente.

---

## ⚠️ SECCIÓN 4: LAS 3 TRAMPAS TÍPICAS DE EXAMEN (PREGUNTAS PARA EL PODCAST)

1. **¿Qué pasa si olvidamos reiniciar `suma := 0` dentro del bucle externo?**
   - *Error fatal:* La variable `suma` acumularía los valores de las vueltas anteriores, provocando un bucle infinito o un resultado astronómico erróneo. `suma := 0` **debe estar obligatoriamente** justo antes del bucle interno.
2. **¿Qué ocurre si el usuario ingresa un número que ya tiene un solo dígito (ej: $N = 7$)?**
   - *Comportamiento correcto:* La condición externa `while N >= 10` evalúa $7 \ge 10$ como **Falso**. El bucle nunca se ejecuta y devuelve directamente `Result := 7` en 0 milisegundos.
3. **¿Por qué la docente prefiere `mod 10` y `div 10` en vez de convertir a texto (`IntToStr`)?**
   - *Criterio de ingeniería:* La manipulación matemática mediante divisiones enteras opera en registros nativos de la CPU a nivel binario en 1 ciclo de reloj, sin sobrecargar la memoria dinámica (Heap) con asignaciones de cadenas de texto.
