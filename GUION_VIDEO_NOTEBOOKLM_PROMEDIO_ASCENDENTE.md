# 🎬 GUION DE VIDEO / PODCAST PARA NOTEBOOKLM: PROMEDIO ASCENDENTE EN RANGO [100 - 200]
## Cátedra: Introducción a la Informática (INF-110) · FICCT - UAGRM
**Docente:** M.Sc. Ing. Angélica Garzón Cuéllar  
**Tema:** Procesamiento Secuencial, Filtros Condicionales y Acumuladores  
**Problema:** Examen Final · Pregunta 1 (10 Puntos)

---

## 🎙️ INTRODUCCIÓN DEL VIDEO: LA ADUANA DE DOS PUERTAS
*(Voz de Presentador / Locutor 1)*
> "Imagina que estás en la entrada de un club exclusivo que tiene **dos guardias de seguridad en fila**. 
> - El **Guardia 1** revisa la entrada: solo deja pasar a números que tengan entre **100 y 200** inclusive. Si llega un 211 o un 50, se van a casa inmediatamente.
> - El **Guardia 2** es más exigente: solo te deja pasar si eres **más alto o igual que la última persona que logró entrar**. 
> Al final de la noche, calculamos el **promedio de estatura** de los que lograron entrar. ¡Eso es exactamente este clásico ejercicio de examen!"

---

## 📊 EL EJEMPLO EN NÚMEROS REALES
Dados $N = 5$ números que van llegando por teclado:
`[ 211,  120,  50,  180,  200 ]`

```
  Entrada     ¿Guardia 1 (100..200)?    ¿Guardia 2 (Ascendente)?       Veredicto
 ─────────   ────────────────────────   ──────────────────────────   ─────────────
   211                ❌ NO                    -                     DESCARTADO
   120                ✅ SÍ             ✅ SÍ (Es el primero)        ENTRA (120)
    50                ❌ NO                    -                     DESCARTADO
   180                ✅ SÍ             ✅ SÍ (180 >= 120)           ENTRA (180)
   200                ✅ SÍ             ✅ SÍ (200 >= 180)           ENTRA (200)
```

**Resultado:** Entraron `120`, `180` y `200`.  
$$\text{Promedio} = \frac{120 + 180 + 200}{3} = \frac{500}{3} = 166.66$$

---

## 📋 LAS 4 FASES OFICIALES DE CÁTEDRA (GARZÓN)

### FASE 1: ANÁLISIS METODOLÓGICO FORMAL (Caja Negra)
* **1.1. Entrada:** 
  - `N`: Cantidad de números a evaluar (Entero / Cardinal).
  - Seguido de `N` números enteros introducidos por teclado.
* **1.2. Salida:** 
  - `Promedio`: Valor real (`Double` en Delphi) con decimales.
* **1.3. Ley de Selección / Filtro Doble:**
  - **Filtro 1 (Rango):** `(Num >= 100) and (Num <= 200)`
  - **Filtro 2 (Orden Ascendente):** `(CantidadValidos = 0) or (Num >= UltimoValido)`
* **1.4. Módulo Delphi:** 
  - Tipo: `FUNCTION` (recibe la secuencia y retorna un único valor escalar real: el promedio).

---

### FASE 2: DISEÑO EN PSEUDOCÓDIGO OFICIAL (Algoritmo Estructurado)

```text
Funcion PromedioAscendenteRango(n: Entero): Real
Variables:
    sumaAcumulada, promedio: Real
    contadorValidos, i, numeroActual, ultimoValido: Entero
Inicio
    sumaAcumulada <- 0.0
    contadorValidos <- 0
    ultimoValido <- -1

    Para i <- 1 Hasta n Hacer
        Leer(numeroActual)

        // Puerta 1: ¿Está dentro del rango [100 - 200]?
        Si (numeroActual >= 100) y (numeroActual <= 200) Entonces
            
            // Puerta 2: ¿Es el primero o es mayor/igual al último aceptado?
            Si (contadorValidos = 0) o (numeroActual >= ultimoValido) Entonces
                sumaAcumulada <- sumaAcumulada + numeroActual
                contadorValidos <- contadorValidos + 1
                ultimoValido <- numeroActual
            FinSi

        FinSi
    FinPara

    // Protección matemática contra división entre cero:
    Si contadorValidos > 0 Entonces
        promedio <- sumaAcumulada / contadorValidos
    Sino
        promedio <- 0.0
    FinSi

    Retornar promedio
FinFuncion
```

---

### FASE 3: IMPLEMENTACIÓN EN DELPHI / PASCAL (Clean Code)

```pascal
unit UPromedioAscendente;

interface

// Función modular limpia que procesa una lista de números
function CalcularPromedioAscendente(CantidadNumeros: Integer; Numeros: array of Integer): Double;

implementation

function CalcularPromedioAscendente(CantidadNumeros: Integer; Numeros: array of Integer): Double;
var
  Indice: Integer;
  NumeroActual: Integer;
  ContadorValidos: Integer;
  UltimoValido: Integer;
  SumaAcumulada: Double;
begin
  // Inicialización de acumuladores
  SumaAcumulada := 0.0;
  ContadorValidos := 0;
  UltimoValido := -1; // Centinela inicial

  for Indice := 0 to High(Numeros) do
  begin
    NumeroActual := Numeros[Indice];

    // FILTRO 1: Rango cerrado [100 .. 200]
    if (NumeroActual >= 100) and (NumeroActual <= 200) then
    begin
      // FILTRO 2: Si es el primer válido (Contador=0) o supera al anterior
      if (ContadorValidos = 0) or (NumeroActual >= UltimoValido) then
      begin
        SumaAcumulada := SumaAcumulada + NumeroActual;
        Inc(ContadorValidos);
        UltimoValido := NumeroActual; // Actualizamos el listón de altura
      end;
    end;
  end;

  // REGLA CLEAN CODE: Evitar división por cero si ningún número calificó
  if ContadorValidos > 0 then
    Result := SumaAcumulada / ContadorValidos
  else
    Result := 0.0;
end;

end.
```

---

### FASE 4: PRUEBA DE ESCRITORIO TABULAR (Traza de Ejecución Formal)
*Datos de prueba: $N = 5$, secuencia: `[211, 120, 50, 180, 200]`*

| $i$ | `NumeroActual` | ¿En $[100..200]$? | ¿Ascendente? | `SumaAcumulada` | `ContadorValidos` | `UltimoValido` |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Inicio** | - | - | - | `0.0` | `0` | `-1` |
| **1** | `211` | ❌ No ($211 > 200$) | - | `0.0` | `0` | `-1` |
| **2** | `120` | ✅ Sí ($100 \le 120 \le 200$) | ✅ Sí (`Contador=0`) | `120.0` | `1` | `120` |
| **3** | `50` | ❌ No ($50 < 100$) | - | `120.0` | `1` | `120` |
| **4** | `180` | ✅ Sí ($100 \le 180 \le 200$) | ✅ Sí ($180 \ge 120$) | `300.0` | `2` | `180` |
| **5** | `200` | ✅ Sí ($100 \le 200 \le 200$) | ✅ Sí ($200 \ge 180$) | `500.0` | `3` | `200` |

**Cálculo Final:**  
$$\text{Promedio} = \frac{\text{SumaAcumulada}}{\text{ContadorValidos}} = \frac{500.0}{3} = 166.666\dots \longrightarrow \mathbf{166.66}$$

---

## 🔍 ZOOM AL CÓDIGO: LOS 3 SECRETOS QUE TE DAN LOS 10 PUNTOS

### 1. El Secreto del Primer Número (`ContadorValidos = 0`)
```pascal
if (ContadorValidos = 0) or (NumeroActual >= UltimoValido) then
```
*(Locutor 2):*  
> "¿Por qué ponemos `ContadorValidos = 0`? Porque cuando entra el **primer número válido** (el `120`), ¡no existe ningún número anterior con quién compararlo! La condición `ContadorValidos = 0` le da un pase VIP automático al primer elegido y fija el récord en `UltimoValido := 120`."

---

### 2. El Escudo Protector: Cero Division Error
```pascal
if ContadorValidos > 0 then
  Result := SumaAcumulada / ContadorValidos
else
  Result := 0.0;
```
*(Locutor 1):*  
> "Imagínate que el usuario introduce: `[50, 60, 70, 80, 90]`. Todos están fuera del rango [100-200]. Si intentas dividir `0 / 0`, Delphi detendrá el programa con error fatal `EZeroDivide`. Esta pequeña validación de 3 líneas te salva 5 puntos en la corrección de la docente."

---

### 3. La Diferencia entre `array` y lectura interactiva
*(Locutor 2):*  
> "En consola o examen escrito, la docente suele pedir `ReadLn(num)` dentro de un bucle `for i := 1 to n do`. En Delphi moderno o Clean Code, encapsularlo como `array of Integer` permite que el algoritmo sea probado con tests automáticos sin depender del teclado."

---

## 💡 RESUMEN MNEMOTÉCNICO PARA EL EXAMEN
> **Filtro 1:** `(num >= 100) and (num <= 200)` (Dentro de la cerca).  
> **Filtro 2:** `(c = 0) or (num >= ultimo)` (El primero o más grande).  
> **Actualizar:** `ultimo := num` (Mover la barra).  
> **Salida:** `if c > 0 then suma/c else 0` (Blindaje contra cero).
