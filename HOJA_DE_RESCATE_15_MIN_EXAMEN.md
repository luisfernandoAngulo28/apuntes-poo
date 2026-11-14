# 📑 HOJA DE RESCATE: LOS 6 ALGORITMOS CLAVE
## Repaso Rápido 15 Minutos Antes de Entrar al Examen Final · INF-110
**Universidad Autónoma Gabriel René Moreno · FICCT**  
**Docente:** M.Sc. Ing. Angélica Garzón Cuéllar  

---

### 1. DESCOMPONER Y PROCESAR DÍGITOS (La Pinza y la Sierra)
```pascal
while NumeroTemporal > 0 do
begin
  DigitoActual := NumeroTemporal mod 10;
  
  // Condición de análisis (ej: si es par)
  if (DigitoActual mod 2 = 0) then
    CantidadPares := CantidadPares + 1;
    
  NumeroTemporal := NumeroTemporal div 10;
end;
```
> **Mnemotécnica:** `mod 10` te da el último dígito; `div 10` le corta la cola.

---

### 2. RECONSTRUCCIÓN CON MULTIPLICADOR (Conserva el Orden Original)
```pascal
Resultado := 0;
Multiplicador := 1;

while NumeroTemporal > 0 do
begin
  DigitoActual := NumeroTemporal mod 10;
  if not ExisteDigito(Resultado, DigitoActual) then
  begin
    Resultado := Resultado + (DigitoActual * Multiplicador);
    Multiplicador := Multiplicador * 10;
  end;
  NumeroTemporal := NumeroTemporal div 10;
end;
```
> **Mnemotécnica:** El multiplicador ($1, 10, 100, 1000$) mantiene a cada dígito en su lugar original.

---

### 3. INVERTIR NÚMERO Y VERIFICAR SI ES CAPICÚA
```pascal
NumeroInvertido := 0;
Copia := Valor;

while Copia > 0 do
begin
  NumeroInvertido := (NumeroInvertido * 10) + (Copia mod 10);
  Copia := Copia div 10;
end;

EsCapicua := (NumeroInvertido = Valor);
```
> **Mnemotécnica:** Multiplicar por 10 empuja los dígitos hacia la izquierda. Si el invertido es igual al original, es Capicúa.

---

### 4. LOS 3 ENGRANAJES DE LAS SERIES NUMÉRICAS («Divide y Vencerás»)
```pascal
Signo := 1;
SumaTotal := 0.0;
Denominador := 2;

for TerminoActual := 1 to NumeroTerminos do
begin
  Numerador := (2 * TerminoActual) - 1; // Impares: 1, 3, 5, 7...
  
  SumaTotal := SumaTotal + (Signo * (Numerador / Denominador));
  
  Signo := -Signo;           // Alternar: +1, -1, +1, -1...
  Denominador := Denominador * 2; // Potencias: 2, 4, 8, 16...
end;
```
> **Mnemotécnica:** Nunca programes la serie completa. Programa el numerador, el denominador y el signo como 3 engranajes separados.

---

### 5. PARTICIÓN Y MITADES DE CADENAS (Copy y Espejos)
```pascal
LongitudTexto := Length(Valor);
TamanoMitad := LongitudTexto div 2;

MitadIzquierda := InvertirTexto(Copy(Valor, 1, TamanoMitad));

if (LongitudTexto mod 2 <> 0) then
begin
  CaracterCentral := Valor[TamanoMitad + 1];
  MitadDerecha := InvertirTexto(Copy(Valor, TamanoMitad + 2, TamanoMitad));
  Result := MitadIzquierda + CaracterCentral + MitadDerecha;
end
else
begin
  MitadDerecha := InvertirTexto(Copy(Valor, TamanoMitad + 1, TamanoMitad));
  Result := MitadIzquierda + MitadDerecha;
end;
```
> **Mnemotécnica:** `div 2` calcula el centro exacto. Si la longitud es impar, el caracter central se rescata intacto.

---

### 6. CONTADOR DE PALABRAS (Detector de Transición)
```pascal
TextoLimpio := Trim(Valor);
CantidadPalabras := 0;

for Indice := 1 to Length(TextoLimpio) do
begin
  // Detecta el inicio de una palabra (cuando no es espacio y el anterior sí lo era)
  if (TextoLimpio[Indice] <> ' ') and ((Indice = 1) or (TextoLimpio[Indice - 1] = ' ')) then
    CantidadPalabras := CantidadPalabras + 1;
end;
```
> **Mnemotécnica:** Cuenta el primer caracter de cada palabra para no tropezar con múltiples espacios seguidos.

---

## 🛑 CHECKLIST DE 30 SEGUNDOS ANTES DE ENTREGAR EL EXAMEN
1. ¿Declaré todas las variables en `var` con tipos fuertes (`Cardinal`, `Byte`, `Double`) en vez de `Integer`?
2. ¿Inicialicé los acumuladores (`Suma := 0;`, `Producto := 1;`, `Multiplicador := 1;`) antes del bucle?
3. ¿Puse la condición de avance (`n := n div 10;` o `i := i + 1;`) para evitar bucles infinitos?
4. ¿Verifiqué el caso borde de número `0` o cadena vacía `''`?
5. ¿Dibujé la tabla de traza con al menos 3 filas para asegurar los 100 puntos de la Fase 4?
