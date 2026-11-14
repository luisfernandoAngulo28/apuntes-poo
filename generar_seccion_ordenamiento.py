# -*- coding: utf-8 -*-
"""
Generador del Módulo Oficial de Ordenamiento en Cadenas & Vectores (INF110-Z2)
Basado en las pizarras y avance de clases de la M.Sc. Ing. Angélica Garzón C.
Incluye:
- Cuadro comparativo de los 5 métodos (Burbuja, Selección, Inserción, Shell, QuickSort).
- Algoritmo de Burbuja / Intercambio Directo con Diagrama de Flujo ANSI (Mermaid).
- Las 3 Reglas de Oro del Intercambio (Swap) explicadas.
- Prueba de escritorio completa paso a paso con el vector de la pizarra [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5].
- Los 5 Ejercicios de examen de la pizarra con código Pascal/Delphi y explicación.
"""

def build_seccion_ordenamiento_html():
    return """
  <!-- ======================================================================= -->
  <!-- SECCIÓN: MÉTODOS DE ORDENAMIENTO EN CADENAS & VECTORES (PIZARRA OFICIAL)-->
  <!-- ======================================================================= -->
  <section id="ordenamiento-cadenas" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🔄 Pizarra Oficial: Métodos de Ordenamiento en Vectores &amp; Cadenas</h2>
        <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">📅 Avance Semanal • M.Sc. Ing. Angélica Garzón C.</span>
      </div>

      <!-- BANNER DE RESUMEN CONCEPTUAL DE LA PIZARRA -->
      <div style="background: linear-gradient(135deg, rgba(14, 165, 233, 0.15), rgba(99, 102, 241, 0.15)); border: 2px solid #38bdf8; border-radius: 12px; padding: 1.5rem; margin: 1.25rem 0;">
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
          <span style="font-size: 2.2rem;">💡</span>
          <div>
            <h3 style="color: #38bdf8; margin: 0; font-size: 1.25rem;">Definición Fundamental de la Docente: ¿Qué es Ordenar?</h3>
            <span style="color: #94a3b8; font-size: 0.85rem;">Cátedra Introducción a la Informática (INF110-Z2) • UAGRM</span>
          </div>
        </div>
        <p style="color: #cbd5e1; font-size: 0.98rem; line-height: 1.6; margin: 0;">
          Un <strong>método de ordenación</strong> maneja <span style="color: #34d399; font-weight: 700;">recorridos</span>, <span style="color: #38bdf8; font-weight: 700;">compara elementos</span>, <span style="color: #fbbf24; font-weight: 700;">intercambia valores</span> y reorganiza los datos bajo un criterio específico:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-top: 1rem;">
          <div style="background: #0b1120; border: 1px solid #10b981; border-radius: 8px; padding: 0.85rem 1rem;">
            <div style="color: #34d399; font-weight: 800; font-size: 0.95rem; margin-bottom: 0.25rem;">▲ Orden Ascendente (Menor a Mayor)</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">Letras: <code>'A' .. 'Z'</code> (o <code>'a' .. 'z'</code>) | Números: <code>0 .. 9</code></div>
            <div style="color: #cbd5e1; font-size: 0.82rem; margin-top: 0.4rem;">Condición: <code>if Cad[I] &gt; Cad[J] then Intercambiar;</code></div>
          </div>
          <div style="background: #0b1120; border: 1px solid #f59e0b; border-radius: 8px; padding: 0.85rem 1rem;">
            <div style="color: #fbbf24; font-weight: 800; font-size: 0.95rem; margin-bottom: 0.25rem;">▼ Orden Descendente (Mayor a Menor)</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">Letras: <code>'Z' .. 'A'</code> (o <code>'z' .. 'a'</code>) | Números: <code>9 .. 0</code></div>
            <div style="color: #cbd5e1; font-size: 0.82rem; margin-top: 0.4rem;">Condición: <code>if Cad[I] &lt; Cad[J] then Intercambiar;</code></div>
          </div>
        </div>
      </div>

      <!-- 1. LOS 5 MÉTODOS DE ORDENACIÓN EXPLICADOS -->
      <div style="margin-top: 2rem;">
        <h3 style="color: #f8fafc; font-size: 1.15rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
          <span>📚</span> 1. Los 5 Métodos de Ordenamiento Avanzados en Teoría
        </h3>
        <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 1rem;">
          La docente mencionó y contrastó los 5 algoritmos clásicos de ordenación en memoria interna (RAM). Es pregunta típica de examen teórico saber la diferencia conceptual de cada uno:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
          <!-- 1. Burbuja -->
          <div style="background: #0f172a; border: 2px solid #10b981; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #10b981; font-weight: 800; font-size: 1rem;">🫧 1. Burbuja (Bubble Sort)</span>
              <span style="font-size: 0.75rem; background: rgba(16, 185, 129, 0.2); color: #34d399; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Visto en Pizarra</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.75rem;">
              Compara elementos adyacentes o posicionales <code>(I, J)</code> mediante dos bucles anidados. Si están en desorden, los intercambia. Los elementos más grandes o más chicos "burbujean" hacia su posición final.
            </p>
            <div style="font-size: 0.8rem; color: #94a3b8;">
              <div>• <strong>Complejidad:</strong> O(n²) comparaciones.</div>
              <div>• <strong>Ventaja:</strong> Muy sencillo de entender y realizar en prueba de escritorio.</div>
            </div>
          </div>

          <!-- 2. Selección -->
          <div style="background: #0f172a; border: 1px solid #38bdf8; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #38bdf8; font-weight: 800; font-size: 1rem;">🎯 2. Selección Directa</span>
              <span style="font-size: 0.75rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Selection Sort</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.75rem;">
              En cada pasada busca el elemento más pequeño del vector restante y lo intercambia con la posición actual <code>I</code>.
            </p>
            <div style="font-size: 0.8rem; color: #94a3b8;">
              <div>• <strong>Complejidad:</strong> O(n²) comparaciones, pero solo O(n) intercambios.</div>
              <div>• <strong>Ventaja:</strong> Minimiza escrituras en memoria (ideal si escribir es costoso).</div>
            </div>
          </div>

          <!-- 3. Inserción -->
          <div style="background: #0f172a; border: 1px solid #a855f7; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #c084fc; font-weight: 800; font-size: 1rem;">🃏 3. Inserción Directa</span>
              <span style="font-size: 0.75rem; background: rgba(168, 85, 247, 0.2); color: #c084fc; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Insertion Sort</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.75rem;">
              Similar a como ordenamos las cartas de naipe en la mano. Toma cada elemento y lo inserta en su lugar correspondiente desplazando los mayores hacia la derecha.
            </p>
            <div style="font-size: 0.8rem; color: #94a3b8;">
              <div>• <strong>Complejidad:</strong> O(n) si ya está casi ordenado; O(n²) en peor caso.</div>
              <div>• <strong>Ventaja:</strong> Altísima velocidad cuando los datos ya tienen cierto orden.</div>
            </div>
          </div>

          <!-- 4. Shell -->
          <div style="background: #0f172a; border: 1px solid #f59e0b; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #fbbf24; font-weight: 800; font-size: 1rem;">🐚 4. Shell Sort</span>
              <span style="font-size: 0.75rem; background: rgba(245, 158, 11, 0.2); color: #fbbf24; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Donald Shell</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.75rem;">
              Mejora de la inserción directa. Compara elementos separados por un salto o intervalo (<code>gap = n div 2</code>) que se va reduciendo progresivamente hasta 1.
            </p>
            <div style="font-size: 0.8rem; color: #94a3b8;">
              <div>• <strong>Complejidad:</strong> O(n log² n) aprox.</div>
              <div>• <strong>Ventaja:</strong> Evita desplazamientos uno a uno de larga distancia.</div>
            </div>
          </div>

          <!-- 5. QuickSort -->
          <div style="background: #0f172a; border: 1px solid #ec4899; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #f472b6; font-weight: 800; font-size: 1rem;">⚡ 5. Quick Sort (Rápido)</span>
              <span style="font-size: 0.75rem; background: rgba(236, 72, 153, 0.2); color: #f472b6; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Tony Hoare</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.75rem;">
              Basado en el paradigma <em>Divide y Vencerás</em>. Elige un elemento llamado <strong>pivote</strong> y particiona el arreglo: los menores al pivote a la izquierda, los mayores a la derecha, y repite recursivamente.
            </p>
            <div style="font-size: 0.8rem; color: #94a3b8;">
              <div>• <strong>Complejidad:</strong> O(n log n) promedio; O(n²) peor caso.</div>
              <div>• <strong>Ventaja:</strong> El algoritmo más veloz en la práctica para grandes volúmenes.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. DIAGRAMA DE FLUJO OFICIAL DE LA PIZARRA (BURBUJA) -->
      <div style="margin-top: 2rem;">
        <h3 style="color: #f8fafc; font-size: 1.15rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
          <span>📐</span> 2. Diagrama de Flujo Oficial de la Pizarra (Ing. Angélica Garzón)
        </h3>
        <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 1rem;">
          Este es el diagrama de flujo exacto que la docente dibujó en la pizarra en la clase de esta semana. Observa los dos bucles anidados con hexágonos <code>Para I = 1 hasta N-1</code> y <code>Para J = I+1 hasta N</code>, y el rombo de decisión:
        </p>

                <!-- DIAGRAMA DE FLUJO ANSI FORMAL DE LA PIZARRA (SVG DE ALTA DEFINICIÓN) -->
        <div style="background: #070a13; border: 1.5px solid #1e293b; border-radius: 10px; padding: 1.5rem 1rem; margin-bottom: 1.5rem; text-align: center; overflow-x: auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
          <svg viewBox="0 0 540 680" width="100%" style="max-width: 520px; font-family: 'Fira Code', 'Inter', monospace; font-size: 13px; margin: 0 auto; display: block;">
            <defs>
              <marker id="arrow-cyan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
              </marker>
              <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
              </marker>
              <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24"/>
              </marker>
            </defs>

            <!-- 1. NODO INICIO (ÓVALO / TERMINAL) -->
            <rect x="120" y="15" width="300" height="42" rx="21" fill="#064e3b" stroke="#10b981" stroke-width="2.5"/>
            <text x="270" y="41" text-anchor="middle" fill="#ecfdf5" font-weight="800" font-size="14">INICIO: OrdenAscendente(cad, n, i)</text>

            <!-- Flecha hacia Bucle I -->
            <line x1="270" y1="57" x2="270" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-cyan)"/>

            <!-- 2. BUCLE I (HEXÁGONO ANSI - PARA I = 1 HASTA N - 1) -->
            <polygon points="120,120 145,95 395,95 420,120 395,145 145,145" fill="#0f172a" stroke="#0284c7" stroke-width="2.5"/>
            <text x="270" y="125" text-anchor="middle" fill="#38bdf8" font-weight="700" font-size="13.5">Para I = 1 hasta N - 1</text>

            <!-- Flecha hacia Bucle J -->
            <line x1="270" y1="145" x2="270" y2="180" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-cyan)"/>

            <!-- 3. BUCLE J (HEXÁGONO ANSI - PARA J = I + 1 HASTA N) -->
            <polygon points="120,205 145,180 395,180 420,205 395,230 145,230" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="270" y="210" text-anchor="middle" fill="#7dd3fc" font-weight="700" font-size="13.5">Para J = I + 1 hasta N</text>

            <!-- Flecha hacia Decisión -->
            <line x1="270" y1="230" x2="270" y2="265" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-cyan)"/>

            <!-- 4. CONDICIÓN (ROMBO DE DECISIÓN) -->
            <polygon points="270,265 410,315 270,365 130,315" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.5"/>
            <text x="270" y="320" text-anchor="middle" fill="#fde68a" font-weight="800" font-size="14">¿Cad[I] &gt; Cad[J]?</text>

            <!-- RAMA VERDADERA (Hacia abajo) -->
            <line x1="270" y1="365" x2="270" y2="405" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
            <rect x="278" y="372" width="65" height="20" rx="4" fill="#064e3b" stroke="#059669" stroke-width="1"/>
            <text x="310" y="386" text-anchor="middle" fill="#34d399" font-weight="800" font-size="11">SÍ (True)</text>

            <!-- RAMA FALSA (Bypass por la izquierda) -->
            <line x1="130" y1="315" x2="60" y2="315" stroke="#f43f5e" stroke-width="2.5"/>
            <line x1="60" y1="315" x2="60" y2="540" stroke="#f43f5e" stroke-width="2.5"/>
            <line x1="60" y1="540" x2="255" y2="540" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrow-amber)"/>
            <rect x="68" y="295" width="55" height="18" rx="4" fill="#881337" stroke="#e11d48" stroke-width="1"/>
            <text x="95" y="308" text-anchor="middle" fill="#fda4af" font-weight="800" font-size="10.5">NO (False)</text>

            <!-- 5. PROCESO DE INTERCAMBIO (SWAP EN 3 PASOS) -->
            <rect x="135" y="405" width="270" height="98" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
            <rect x="135" y="405" width="270" height="24" rx="6" fill="#065f46"/>
            <text x="270" y="421" text-anchor="middle" fill="#a7f3d0" font-weight="800" font-size="11" letter-spacing="0.5">INTERCAMBIO DE 3 PASOS (SWAP)</text>
            <text x="150" y="446" fill="#f8fafc" font-size="12">1) Aux  ←  Cad[I]</text>
            <text x="345" y="446" fill="#64748b" font-size="10.5">(Guarda 1° elem)</text>
            <text x="150" y="468" fill="#f8fafc" font-size="12">2) Cad[I]  ←  Cad[J]</text>
            <text x="345" y="468" fill="#64748b" font-size="10.5">(Actualiza elem)</text>
            <text x="150" y="490" fill="#f8fafc" font-size="12">3) Cad[J]  ←  Aux</text>
            <text x="345" y="490" fill="#64748b" font-size="10.5">(Recupera aux)</text>

            <!-- Flecha de salida del intercambio al punto de unión -->
            <line x1="270" y1="503" x2="270" y2="540" stroke="#34d399" stroke-width="2.5"/>

            <!-- Punto de unión de bucle J -->
            <circle cx="270" cy="540" r="5" fill="#fbbf24"/>

            <!-- Retorno del Bucle J (Por la derecha) -->
            <line x1="275" y1="540" x2="455" y2="540" stroke="#38bdf8" stroke-width="2"/>
            <line x1="455" y1="540" x2="455" y2="205" stroke="#38bdf8" stroke-width="2"/>
            <line x1="455" y1="205" x2="425" y2="205" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
            <rect x="420" y="340" width="70" height="18" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="1"/>
            <text x="455" y="353" text-anchor="middle" fill="#bae6fd" font-size="10">Sig. J</text>

            <!-- Flecha hacia Retornar (cuando I termina) -->
            <line x1="270" y1="545" x2="270" y2="600" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
            <rect x="280" y="565" width="75" height="18" rx="4" fill="#064e3b" stroke="#059669" stroke-width="1"/>
            <text x="317" y="578" text-anchor="middle" fill="#a7f3d0" font-size="10.5">Fin Bucles</text>

            <!-- 6. NODO FIN (RETORNAR) -->
            <rect x="150" y="600" width="240" height="42" rx="21" fill="#064e3b" stroke="#10b981" stroke-width="2.5"/>
            <text x="270" y="626" text-anchor="middle" fill="#ecfdf5" font-weight="800" font-size="14">RETORNAR(cad)</text>
          </svg>
        </div>

        <!-- LAS 3 FASES DEL INTERCAMBIO (SWAP) -->
        <div style="background: #0f172a; border-left: 4px solid #38bdf8; border-radius: 6px; padding: 1rem 1.25rem; margin-bottom: 1.5rem;">
          <h4 style="color: #38bdf8; margin: 0 0 0.5rem 0; font-size: 0.95rem;">
            📌 Las 3 Reglas de Oro del Intercambio (Swap) Explicadas en Pizarra:
          </h4>
          <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.5; margin: 0 0 0.5rem 0;">
            Para intercambiar dos valores sin perder ninguno, se utiliza una variable auxiliar <code>Aux</code> (análogo a pasar agua de vaso A a vaso B usando un vaso vacío Auxiliar):
          </p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem;">
            <div style="background: #070a13; padding: 0.6rem; border-radius: 4px; border: 1px solid #334155;">
              <span style="color: #38bdf8; font-weight: 700;">Paso 1:</span> <span style="color: #f8fafc;">aux := cad[i];</span><br/>
              <span style="color: #94a3b8; font-size: 0.75rem;">Guarda valor de posición I</span>
            </div>
            <div style="background: #070a13; padding: 0.6rem; border-radius: 4px; border: 1px solid #334155;">
              <span style="color: #38bdf8; font-weight: 700;">Paso 2:</span> <span style="color: #f8fafc;">cad[i] := cad[j];</span><br/>
              <span style="color: #94a3b8; font-size: 0.75rem;">Pasa el menor a la izquierda</span>
            </div>
            <div style="background: #070a13; padding: 0.6rem; border-radius: 4px; border: 1px solid #334155;">
              <span style="color: #38bdf8; font-weight: 700;">Paso 3:</span> <span style="color: #f8fafc;">cad[j] := aux;</span><br/>
              <span style="color: #94a3b8; font-size: 0.75rem;">Recupera el valor guardado</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. PRUEBA DE ESCRITORIO PASO A PASO DE LA PIZARRA -->
      <div style="margin-top: 2rem;">
        <h3 style="color: #f8fafc; font-size: 1.15rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
          <span>🧪</span> 3. Prueba de Escritorio Detallada (El Ejercicio de la Pizarra)
        </h3>
        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.5; margin-bottom: 1rem;">
          En la pizarra, la docente colocó el vector numérico <code style="color: #38bdf8;">V = [4, 5, 1, 2, 3]</code> con longitud <code style="color: #34d399;">N = 5</code> y realizó paso a paso cada comparación e intercambio para llegar a <code style="color: #34d399;">[1, 2, 3, 4, 5]</code>. Aquí tienes la tabla formal idéntica a la que se exige en el parcial:
        </p>

        <div style="overflow-x: auto; border: 1px solid #334155; border-radius: 8px; margin-bottom: 1.5rem;">
          <table class="traza-table" style="margin: 0; width: 100%;">
            <thead>
              <tr>
                <th>Pasada</th>
                <th>I</th>
                <th>J</th>
                <th>¿V[I] &gt; V[J]?</th>
                <th>Aux</th>
                <th>V[1]</th>
                <th>V[2]</th>
                <th>V[3]</th>
                <th>V[4]</th>
                <th>V[5]</th>
                <th>Acción Realizada</th>
              </tr>
            </thead>
            <tbody>
              <!-- Inicial -->
              <tr style="background: rgba(56, 189, 248, 0.08);">
                <td><strong>Inicio</strong></td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td><strong>4</strong></td>
                <td><strong>5</strong></td>
                <td><strong>1</strong></td>
                <td><strong>2</strong></td>
                <td><strong>3</strong></td>
                <td>Vector inicial en desorden</td>
              </tr>
              <!-- I = 1 -->
              <tr>
                <td rowspan="4" style="background: rgba(16, 185, 129, 0.1); font-weight: 800; color: #34d399;">I = 1</td>
                <td>1</td><td>2</td>
                <td>4 &gt; 5 (Falso)</td>
                <td>-</td>
                <td>4</td><td>5</td><td>1</td><td>2</td><td>3</td>
                <td>No hay intercambio</td>
              </tr>
              <tr style="background: rgba(245, 158, 11, 0.1);">
                <td>1</td><td>3</td>
                <td><strong style="color: #fbbf24;">4 &gt; 1 (Verdadero)</strong></td>
                <td><strong style="color: #38bdf8;">4</strong></td>
                <td><strong style="color: #34d399;">1</strong></td><td>5</td><td><strong style="color: #fbbf24;">4</strong></td><td>2</td><td>3</td>
                <td><strong>Swap:</strong> Aux:=4; V[1]:=1; V[3]:=4</td>
              </tr>
              <tr>
                <td>1</td><td>4</td>
                <td>1 &gt; 2 (Falso)</td>
                <td>-</td>
                <td>1</td><td>5</td><td>4</td><td>2</td><td>3</td>
                <td>No hay intercambio</td>
              </tr>
              <tr>
                <td>1</td><td>5</td>
                <td>1 &gt; 3 (Falso)</td>
                <td>-</td>
                <td><strong style="color: #34d399;">1</strong></td><td>5</td><td>4</td><td>2</td><td>3</td>
                <td><span style="color: #34d399; font-weight: 700;">✓ El '1' queda fijo en la posición 1</span></td>
              </tr>
              <!-- I = 2 -->
              <tr style="background: rgba(245, 158, 11, 0.1);">
                <td rowspan="3" style="background: rgba(56, 189, 248, 0.1); font-weight: 800; color: #38bdf8;">I = 2</td>
                <td>2</td><td>3</td>
                <td><strong style="color: #fbbf24;">5 &gt; 4 (Verdadero)</strong></td>
                <td><strong style="color: #38bdf8;">5</strong></td>
                <td>1</td><td><strong style="color: #34d399;">4</strong></td><td><strong style="color: #fbbf24;">5</strong></td><td>2</td><td>3</td>
                <td><strong>Swap:</strong> Aux:=5; V[2]:=4; V[3]:=5</td>
              </tr>
              <tr style="background: rgba(245, 158, 11, 0.1);">
                <td>2</td><td>4</td>
                <td><strong style="color: #fbbf24;">4 &gt; 2 (Verdadero)</strong></td>
                <td><strong style="color: #38bdf8;">4</strong></td>
                <td>1</td><td><strong style="color: #34d399;">2</strong></td><td>5</td><td><strong style="color: #fbbf24;">4</strong></td><td>3</td>
                <td><strong>Swap:</strong> Aux:=4; V[2]:=2; V[4]:=4</td>
              </tr>
              <tr>
                <td>2</td><td>5</td>
                <td>2 &gt; 3 (Falso)</td>
                <td>-</td>
                <td>1</td><td><strong style="color: #34d399;">2</strong></td><td>5</td><td>4</td><td>3</td>
                <td><span style="color: #34d399; font-weight: 700;">✓ El '2' queda fijo en la posición 2</span></td>
              </tr>
              <!-- I = 3 -->
              <tr style="background: rgba(245, 158, 11, 0.1);">
                <td rowspan="2" style="background: rgba(168, 85, 247, 0.1); font-weight: 800; color: #c084fc;">I = 3</td>
                <td>3</td><td>4</td>
                <td><strong style="color: #fbbf24;">5 &gt; 4 (Verdadero)</strong></td>
                <td><strong style="color: #38bdf8;">5</strong></td>
                <td>1</td><td>2</td><td><strong style="color: #34d399;">4</strong></td><td><strong style="color: #fbbf24;">5</strong></td><td>3</td>
                <td><strong>Swap:</strong> Aux:=5; V[3]:=4; V[4]:=5</td>
              </tr>
              <tr style="background: rgba(245, 158, 11, 0.1);">
                <td>3</td><td>5</td>
                <td><strong style="color: #fbbf24;">4 &gt; 3 (Verdadero)</strong></td>
                <td><strong style="color: #38bdf8;">4</strong></td>
                <td>1</td><td>2</td><td><strong style="color: #34d399;">3</strong></td><td>5</td><td><strong style="color: #fbbf24;">4</strong></td>
                <td><strong>Swap:</strong> Aux:=4; V[3]:=3; V[5]:=4</td>
              </tr>
              <!-- I = 4 -->
              <tr style="background: rgba(245, 158, 11, 0.1);">
                <td style="background: rgba(236, 72, 153, 0.1); font-weight: 800; color: #f472b6;">I = 4</td>
                <td>4</td><td>5</td>
                <td><strong style="color: #fbbf24;">5 &gt; 4 (Verdadero)</strong></td>
                <td><strong style="color: #38bdf8;">5</strong></td>
                <td>1</td><td>2</td><td>3</td><td><strong style="color: #34d399;">4</strong></td><td><strong style="color: #34d399;">5</strong></td>
                <td><strong>Swap:</strong> Aux:=5; V[4]:=4; V[5]:=5</td>
              </tr>
              <!-- Final -->
              <tr style="background: rgba(16, 185, 129, 0.2); font-weight: 800;">
                <td><strong>FINAL</strong></td>
                <td>-</td><td>-</td><td>-</td><td>-</td>
                <td style="color: #34d399;">1</td>
                <td style="color: #34d399;">2</td>
                <td style="color: #34d399;">3</td>
                <td style="color: #34d399;">4</td>
                <td style="color: #34d399;">5</td>
                <td style="color: #34d399;">🎉 VECTOR 100% ORDENADO ASCENDENTE</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <div style="background: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem 1.2rem; font-size: 0.85rem; color: #94a3b8; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
          <span>Total de Comparaciones: <strong>10</strong> (Fórmula: n*(n-1)/2 = 5*4/2 = 10)</span>
          <span>Total de Intercambios Realizados: <strong>6</strong></span>
        </div>
      </div>

      <!-- 4. LOS 5 EJERCICIOS DE EXAMEN DE LA PIZARRA -->
      <div style="margin-top: 2.5rem;">
        <h3 style="color: #f8fafc; font-size: 1.15rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
          <span>🎯</span> 4. Los 5 Ejercicios de Examen de la Pizarra Resueltos
        </h3>
        <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 1.5rem;">
          A continuación tienes la resolución formal de cada uno de los ejercicios escritos en la pizarra por la docente, con la metodología exacta de parámetros <code>(cad, n)</code> e <code>i</code>:
        </p>

        <!-- EJERCICIO 1: ORDEN ASCENDENTE -->
        <div class="card" style="border: 1px solid rgba(16, 185, 129, 0.4); margin-bottom: 1.5rem; background: #0b1120;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
            <h4 style="color: #34d399; margin: 0; font-size: 1.05rem;">
              ① Ordenar Cadena Completa Ascendente ('A' .. 'Z')
            </h4>
            <span style="font-size: 0.75rem; background: rgba(16, 185, 129, 0.2); color: #34d399; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
              Pizarra Ej. 1
            </span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.88rem; margin-bottom: 0.5rem;">
            <strong>Entrada:</strong> <code>cad = '45123'</code> &rarr; <strong>Salida:</strong> <code>'12345'</code><br/>
            <strong>Entrada:</strong> <code>cad = 'bca'</code> &rarr; <strong>Salida:</strong> <code>'abc'</code>
          </p>
          <div style="position: relative;">
            <pre style="background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; color: #f8fafc; font-family: 'Fira Code', monospace; font-size: 0.85rem; overflow-x: auto;">
function OrdenarCadenaAscendente(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  for i := 1 to n - 1 do
  begin
    for j := i + 1 to n do
    begin
      if cad[i] &gt; cad[j] then
      begin
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
    end;
  end;
  Result := cad;
end;</pre>
          </div>
        </div>

        <!-- EJERCICIO 2: ORDEN DESCENDENTE -->
        <div class="card" style="border: 1px solid rgba(245, 158, 11, 0.4); margin-bottom: 1.5rem; background: #0b1120;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
            <h4 style="color: #fbbf24; margin: 0; font-size: 1.05rem;">
              ② Ordenar Cadena Completa Descendente ('Z' .. 'A')
            </h4>
            <span style="font-size: 0.75rem; background: rgba(245, 158, 11, 0.2); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
              Pizarra Ej. 2
            </span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.88rem; margin-bottom: 0.5rem;">
            <strong>Entrada:</strong> <code>cad = '12345'</code> &rarr; <strong>Salida:</strong> <code>'54321'</code><br/>
            <strong>Entrada:</strong> <code>cad = 'abc'</code> &rarr; <strong>Salida:</strong> <code>'cba'</code>
          </p>
          <div style="position: relative;">
            <pre style="background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; color: #f8fafc; font-family: 'Fira Code', monospace; font-size: 0.85rem; overflow-x: auto;">
function OrdenarCadenaDescendente(cad: String; n: Byte): String;
var
  i, j: Byte;
  aux: Char;
begin
  for i := 1 to n - 1 do
  begin
    for j := i + 1 to n do
    begin
      // Solo cambia el operador de comparación: &lt; en vez de &gt;
      if cad[i] &lt; cad[j] then
      begin
        aux := cad[i];
        cad[i] := cad[j];
        cad[j] := aux;
      end;
    end;
  end;
  Result := cad;
end;</pre>
          </div>
        </div>

        <!-- EJERCICIO 3: ORDENAR ÚLTIMA PALABRA -->
        <div class="card" style="border: 1px solid rgba(56, 189, 248, 0.4); margin-bottom: 1.5rem; background: #0b1120;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
            <h4 style="color: #38bdf8; margin: 0; font-size: 1.05rem;">
              ③ Ordenar la Última Palabra de la Cadena
            </h4>
            <span style="font-size: 0.75rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
              Pizarra Ej. 3
            </span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.88rem; margin-bottom: 0.5rem;">
            <strong>Entrada:</strong> <code>cad = 'Casa de ana'</code> &rarr; <strong>Salida:</strong> <code>'Casa de aan'</code><br/>
            <em>Explicación:</em> Se localiza la última palabra <code>'ana'</code> y se ordena alfabéticamente (las 'a' primero, luego la 'n': <code>'aan'</code>).
          </p>
          <div style="position: relative;">
            <pre style="background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; color: #f8fafc; font-family: 'Fira Code', monospace; font-size: 0.85rem; overflow-x: auto;">
function OrdenarUltimaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palOrd, res: String;
begin
  ObtenerLimitesUltimaPalabra(cad, n, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;

  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palOrd := OrdenarCadenaAscendente(pal, lenPal);

  res := Copy(cad, 1, pIni - 1) + palOrd + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;</pre>
          </div>
        </div>

        <!-- EJERCICIO 4: INVERTIR LA SEGUNDA PALABRA -->
        <div class="card" style="border: 1px solid rgba(168, 85, 247, 0.4); margin-bottom: 1.5rem; background: #0b1120;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
            <h4 style="color: #c084fc; margin: 0; font-size: 1.05rem;">
              ④ Invertir la Segunda Palabra de la Cadena
            </h4>
            <span style="font-size: 0.75rem; background: rgba(168, 85, 247, 0.2); color: #c084fc; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
              Pizarra Ej. 4
            </span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.88rem; margin-bottom: 0.5rem;">
            <strong>Entrada:</strong> <code>cad = 'Hola mundo de Cadena'</code> &rarr; <strong>Salida:</strong> <code>'Hola odnum de Cadena'</code><br/>
            <em>Explicación:</em> La 2da palabra es <code>'mundo'</code>. Al <strong>invertirla</strong> (leer de derecha a izquierda), queda <code>'odnum'</code>.
          </p>
          <div style="position: relative;">
            <pre style="background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; color: #f8fafc; font-family: 'Fira Code', monospace; font-size: 0.85rem; overflow-x: auto;">
function InvertirSegundaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palInv, res: String;
begin
  ObtenerLimitesPalabra(cad, n, 2, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;

  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palInv := InvertirTexto(pal, lenPal); // recorrido n downto 1

  res := Copy(cad, 1, pIni - 1) + palInv + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;</pre>
          </div>
        </div>

        <!-- EJERCICIO 5: ORDENAR LA SEGUNDA PALABRA -->
        <div class="card" style="border: 2px solid #ec4899; margin-bottom: 1.5rem; background: #0b1120;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
            <h4 style="color: #f472b6; margin: 0; font-size: 1.05rem;">
              ⑤ Ordenar Alfabéticamente la Segunda Palabra de la Cadena
            </h4>
            <span style="font-size: 0.75rem; background: rgba(236, 72, 153, 0.2); color: #f472b6; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
              Pizarra Ej. 5 • ¡Cuidado Trampa Examen!
            </span>
          </div>
          <div style="background: rgba(236, 72, 153, 0.1); border-left: 3px solid #ec4899; padding: 0.6rem 0.85rem; margin-bottom: 0.75rem; border-radius: 4px; font-size: 0.85rem; color: #cbd5e1;">
            <strong style="color: #f472b6;">¡Pregunta Trampa Explicada en Pizarra!</strong><br/>
            • Si te piden <strong>INVERTIR</strong>: <code>'mundo'</code> &rarr; <code>'odnum'</code> (orden inverso posicional).<br/>
            • Si te piden <strong>ORDENAR</strong>: <code>'mundo'</code> &rarr; <code>'dmnou'</code> (alfabéticamente por código ASCII: <code>'d' &lt; 'm' &lt; 'n' &lt; 'o' &lt; 'u'</code>).
          </div>
          <p style="color: #cbd5e1; font-size: 0.88rem; margin-bottom: 0.5rem;">
            <strong>Entrada:</strong> <code>cad = 'Hola mundo de Cadena'</code> &rarr; <strong>Salida:</strong> <code>'Hola dmnou de Cadena'</code>
          </p>
          <div style="position: relative;">
            <pre style="background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; color: #f8fafc; font-family: 'Fira Code', monospace; font-size: 0.85rem; overflow-x: auto;">
function OrdenarSegundaPalabra(cad: String; n: Byte): String;
var
  pIni, pFin, lenPal: Byte;
  pal, palOrd, res: String;
begin
  ObtenerLimitesPalabra(cad, n, 2, pIni, pFin);
  if (pIni = 0) or (pFin = 0) then
  begin
    Result := cad;
    Exit;
  end;

  lenPal := pFin - pIni + 1;
  pal := Copy(cad, pIni, lenPal);
  palOrd := OrdenarCadenaAscendente(pal, lenPal); // 'mundo' -> 'dmnou'

  res := Copy(cad, 1, pIni - 1) + palOrd + Copy(cad, pFin + 1, n - pFin);
  Result := res;
end;</pre>
          </div>
        </div>

      </div>

      <!-- 5. CÓDIGO DELPHI VCL LISTO PARA PEGAR EN Unit Cadena -->
      <div style="margin-top: 2rem; background: #070a13; border: 1px solid #334155; border-radius: 8px; padding: 1.25rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <h4 style="color: #38bdf8; margin: 0; font-size: 1rem;">
            🖥️ Código Delphi VCL para los Eventos de Menú (unit Cadena)
          </h4>
          <button class="btn-copy" onclick="copySnippet('codeDelphiOrden')" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">
            📋 Copiar Todo el Código Delphi
          </button>
        </div>
        <pre id="codeDelphiOrden" style="color: #cbd5e1; font-family: 'Fira Code', monospace; font-size: 0.82rem; overflow-x: auto; margin: 0; line-height: 1.4;">
// -------------------------------------------------------------
// EVENTOS PARA EL FORMULARIO DELPHI (TForm1)
// -------------------------------------------------------------

procedure TForm1.Ascendente1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarCadenaAscendente(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Cadena ordenada ascendentemente: ' + cad);
end;

procedure TForm1.Descendente1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarCadenaDescendente(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Cadena ordenada descendentemente: ' + cad);
end;

procedure TForm1.OrdenarUltimaPalabra1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarUltimaPalabra(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Ultima palabra ordenada: ' + cad);
end;

procedure TForm1.InvertirSegundaPalabra1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := InvertirSegundaPalabra(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Segunda palabra invertida: ' + cad);
end;

procedure TForm1.OrdenarSegundaPalabra1Click(Sender: TObject);
begin
  n := Length(cad);
  cad := OrdenarSegundaPalabra(cad, n);
  Edit3.Text := cad;
  Label5.Caption := 'cad=' + cad;
  ShowMessage('Segunda palabra ordenada: ' + cad);
end;</pre>
      </div>

    </div>
  </section>
  <!-- FIN SECCIÓN ORDENAMIENTO CADENAS -->
"""

if __name__ == '__main__':
    html = build_seccion_ordenamiento_html()
    print(f"Módulo generado correctamente ({len(html)} bytes)")

