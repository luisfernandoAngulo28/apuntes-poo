# -*- coding: utf-8 -*-
"""
Generador de la sección de teoría y fundamentos interactivos de Cadenas en Delphi
basado en el material oficial 'cadenas.docx'.
"""

def build_cadenas_docx_html():
    return '''
      <!-- ========================================================================= -->
      <!-- BLOQUE TEÓRICO: FUNDAMENTOS Y MANEJO DE CADENAS (cadenas.docx)            -->
      <!-- ========================================================================= -->
      <div style="margin-top: 1.5rem; margin-bottom: 2rem; border-top: 1px solid var(--border-color); padding-top: 1.5rem;">
        
        <!-- ENCABEZADO DE LA SECCIÓN DE TEORÍA -->
        <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95)); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: var(--radius-md); padding: 1.5rem 1.8rem; margin-bottom: 1.5rem; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.8rem; margin-bottom: 0.8rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="font-size: 1.8rem;">📖</span>
              <div>
                <h3 style="color: #fff; margin: 0; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">Manejo de Cadenas en Delphi Pascal</h3>
                <span style="font-size: 0.82rem; color: #38bdf8; font-weight: 600;">MATERIAL OFICIAL DE CLASE • cadenas.docx • INF110-Z2</span>
              </div>
            </div>
            <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; border-color: rgba(56, 189, 248, 0.4); margin: 0;">
              ⚡ TEORÍA & LABORATORIO EN VIVO
            </span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.95rem; margin: 0; line-height: 1.6;">
            Fundamentos teóricos oficiales proporcionados por la docente <strong>M.Sc. Ing. Angélica Garzón C.</strong>: definición del tipo <code>STRING</code>, límites de memoria (<code>ShortString</code> de 255 caracteres), acceso indexado posicional <code>X[i]</code> (base 1), funciones del sistema (<code>Length</code>, <code>LowerCase</code>, <code>UpperCase</code>, <code>Copy</code>), procedimientos por referencia (<code>Delete</code>, <code>Insert</code>) y autoevaluación interactiva.
          </p>
        </div>

        <!-- SUB-SECCIÓN 1: DEFINICIÓN, ASIGNACIÓN E INDEXACIÓN EN MEMORIA -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
          
          <!-- TARJETA A: DEFINICIÓN & TIPOS -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.25rem;">
            <h4 style="color: #38bdf8; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; font-size: 1.05rem;">
              <span>🔤</span> 1. ¿Qué es una Cadena en Delphi?
            </h4>
            <p style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 0.75rem;">
              Una cadena es una <strong>sucesión finita de caracteres</strong>. En el estándar clásico de Delphi / Pascal, el tipo tradicional <code>STRING</code> (ShortString) <strong>no puede exceder los 255 caracteres</strong>.
            </p>
            <div class="code-wrapper" style="margin-bottom: 0.75rem;">
              <div class="code-block" style="font-size: 0.82rem; padding: 0.75rem;">
<span class="keyword">var</span><br>
&nbsp;&nbsp;X: <span class="type">String</span>; <span class="comment">// Hasta 255 caracteres</span><br>
&nbsp;&nbsp;Y: <span class="type">String</span>[<span class="number">50</span>]; <span class="comment">// Límite fijo de 50 caracteres</span><br>
&nbsp;&nbsp;Z: <span class="type">String</span>[<span class="number">30</span>]; <span class="comment">// Límite fijo de 30 caracteres</span>
              </div>
            </div>
            <div style="background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38bdf8; padding: 0.6rem 0.8rem; font-size: 0.82rem; color: #94a3b8;">
              💡 <strong>Regla de Asignación:</strong> Si <code>Y := X;</code>, se asigna a <code>Y</code> una copia completa del contenido actual de <code>X</code>.
            </div>
          </div>

          <!-- TARJETA B: INDEXACIÓN BASE 1 EN MEMORIA -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.25rem;">
            <h4 style="color: #10b981; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; font-size: 1.05rem;">
              <span>🎯</span> 2. Indexación y Acceso Posicional X[i]
            </h4>
            <p style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 0.75rem;">
              En Pascal/Delphi, los caracteres se indexan desde la posición <strong>1 hasta Length(X)</strong> (a diferencia de lenguajes como C++ o Python que empiezan en 0):
            </p>
            <div class="code-wrapper" style="margin-bottom: 0.75rem;">
              <div class="code-block" style="font-size: 0.82rem; padding: 0.75rem;">
X := <span class="string">'Hola como estas'</span>; <span class="comment">// Longitud: 15 caracteres</span><br>
Z := X[<span class="number">4</span>]; <span class="comment">// En Z se almacena la letra 'a'</span><br>
P := <span class="string">'Introducción a la informática'</span>;<br>
L := <span class="keyword">Length</span>(P); <span class="comment">// L = 29 caracteres (con espacios)</span>
              </div>
            </div>
            <div style="background: rgba(16, 185, 129, 0.08); border-left: 3px solid #10b981; padding: 0.6rem 0.8rem; font-size: 0.82rem; color: #94a3b8;">
              ⚠️ <strong>¡Cuidado en Exámenes!</strong> Los espacios en blanco (<code>' '</code>) también cuentan como caracteres válidos en la longitud y en el índice.
            </div>
          </div>

        </div>

        <!-- VISUALIZADOR INTERACTIVO DE CADENA EN MEMORIA (INSPECTOR DE ÍNDICES) -->
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.4rem; margin-bottom: 1.75rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1rem;">
            <h4 style="color: #f59e0b; margin: 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem;">
              <span>🔍</span> Inspector Gráfico de Memoria e Índices (Base 1)
            </h4>
            <span style="font-size: 0.8rem; color: #94a3b8;">Escriba una frase para ver cómo se distribuye en celdas de memoria</span>
          </div>

          <!-- Input interactivo -->
          <div style="display: flex; gap: 0.75rem; margin-bottom: 1.2rem; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px;">
              <input type="text" id="docInspectInput" value="Bolivar Campeón" placeholder="Escriba aquí cualquier cadena..." style="width: 100%; padding: 0.6rem 0.9rem; background: #070a13; border: 1px solid #334155; border-radius: 6px; color: #fff; font-family: 'Fira Code', monospace; font-size: 0.95rem;" oninput="actualizarInspectorMemoriaDoc()">
            </div>
            <button class="btn-print" onclick="inspeccionarEjemploDoc('Hola como estas')" style="font-size: 0.8rem;">Ejemplo 1 ('Hola como estas')</button>
            <button class="btn-print" onclick="inspeccionarEjemploDoc('Introducción a la informática')" style="font-size: 0.8rem;">Ejemplo 2 ('Informática')</button>
            <button class="btn-print" onclick="inspeccionarEjemploDoc('Bolivar Campeón')" style="font-size: 0.8rem;">Ejemplo 3 ('Bolivar Campeón')</button>
          </div>

          <!-- Grilla de Celdas de Memoria -->
          <div style="overflow-x: auto; padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div id="docMemoryGrid" style="display: flex; gap: 5px; min-width: max-content; align-items: flex-start;">
              <!-- Se genera dinámicamente -->
            </div>
          </div>

          <!-- Resumen de inspección -->
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; background: rgba(7, 10, 19, 0.7); border-radius: 6px; padding: 0.75rem 1rem; font-size: 0.88rem;">
            <div>
              <span style="color: #94a3b8;">Longitud Total: </span>
              <strong id="docInspectLength" style="color: #38bdf8;">15 caracteres</strong>
            </div>
            <div id="docInspectCharSelected" style="color: #10b981; font-family: 'Fira Code', monospace;">
              Haga clic sobre cualquier celda para inspeccionar X[i]
            </div>
          </div>
        </div>

        <!-- SUB-SECCIÓN 2: FUNCIONES Y PROCEDIMIENTOS DEL SISTEMA DELPHI -->
        <h3 style="color: #fff; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; font-size: 1.25rem;">
          <span>⚙️</span> Funciones y Procedimientos Estándar de Delphi (cadenas.docx)
        </h3>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem; margin-bottom: 1.75rem;">
          
          <!-- BLOQUE FUNCIONES (PARTE 1 Y 2) -->
          <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.3rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
              <h4 style="color: #38bdf8; margin: 0; font-size: 1.05rem;">📐 Funciones del Sistema (Retornan un Valor)</h4>
              <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; margin: 0; font-size: 0.75rem;">4 FUNCIONES</span>
            </div>
            <p style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 1rem;">
              Una <strong>función</strong> calcula un resultado y lo retorna directamente en el nombre de la función (o mediante <code>Result</code>):
            </p>

            <!-- 1. Length -->
            <div style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem; margin-bottom: 0.85rem;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="color: #38bdf8; font-weight: 700; font-size: 0.88rem;">Length(S: String): Integer</code>
                <span style="font-size: 0.75rem; color: #10b981; font-weight: 600;">Longitud</span>
              </div>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0.4rem 0;">Devuelve el número total de caracteres de la cadena <code>S</code>.</p>
              <div style="font-size: 0.8rem; color: #94a3b8; font-family: 'Fira Code', monospace; background: #0b1120; padding: 0.35rem 0.6rem; border-radius: 4px;">
                X := 'Hola Ruth'; L := Length(X); <span style="color: #10b981;">// L = 9</span>
              </div>
            </div>

            <!-- 2. LowerCase -->
            <div style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem; margin-bottom: 0.85rem;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="color: #38bdf8; font-weight: 700; font-size: 0.88rem;">LowerCase(S: String): String</code>
                <span style="font-size: 0.75rem; color: #38bdf8; font-weight: 600;">Minúsculas</span>
              </div>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0.4rem 0;">Convierte todas las letras mayúsculas de <code>S</code> a minúsculas.</p>
              <div style="font-size: 0.8rem; color: #94a3b8; font-family: 'Fira Code', monospace; background: #0b1120; padding: 0.35rem 0.6rem; border-radius: 4px;">
                P := LowerCase('HoLA'); <span style="color: #10b981;">// P = 'hola'</span>
              </div>
            </div>

            <!-- 3. UpperCase -->
            <div style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem; margin-bottom: 0.85rem;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="color: #38bdf8; font-weight: 700; font-size: 0.88rem;">UpperCase(S: String): String</code>
                <span style="font-size: 0.75rem; color: #f59e0b; font-weight: 600;">Mayúsculas</span>
              </div>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0.4rem 0;">Convierte todas las letras minúsculas de <code>S</code> a mayúsculas.</p>
              <div style="font-size: 0.8rem; color: #94a3b8; font-family: 'Fira Code', monospace; background: #0b1120; padding: 0.35rem 0.6rem; border-radius: 4px;">
                X := UpperCase('Hola Ruth'); <span style="color: #10b981;">// X = 'HOLA RUTH'</span>
              </div>
            </div>

            <!-- 4. Copy -->
            <div style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="color: #38bdf8; font-weight: 700; font-size: 0.88rem;">Copy(S: String; Inicio, Cuantos: Integer): String</code>
                <span style="font-size: 0.75rem; color: #a855f7; font-weight: 600;">Subcadena</span>
              </div>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0.4rem 0;">Devuelve una subcadena de <code>S</code> comenzando en la posición <code>Inicio</code> tomando <code>Cuantos</code> caracteres.</p>
              <div style="font-size: 0.8rem; color: #94a3b8; font-family: 'Fira Code', monospace; background: #0b1120; padding: 0.35rem 0.6rem; border-radius: 4px;">
                X := 'Bolivar Campeón'; Copy(X, 6, 5); <span style="color: #10b981;">// = 'ar ca'</span>
              </div>
            </div>

          </div>

          <!-- BLOQUE PROCEDIMIENTOS (MODIFICACIÓN IN-PLACE CON VAR) -->
          <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.3rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
              <h4 style="color: #a855f7; margin: 0; font-size: 1.05rem;">🔧 Procedimientos del Sistema (Paso por VAR)</h4>
              <span class="badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; margin: 0; font-size: 0.75rem;">2 PROCEDIMIENTOS</span>
            </div>
            <p style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 1rem;">
              Un <strong>procedimiento</strong> modifica la variable directamente en memoria mediante el parámetro de referencia <code>var S: String</code> (no retorna un valor con asignación <code>:=</code>):
            </p>

            <!-- 1. Delete -->
            <div style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem; margin-bottom: 1.15rem;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="color: #a855f7; font-weight: 700; font-size: 0.88rem;">Delete(var S: String; Inicio, Cuantos: Integer)</code>
                <span style="font-size: 0.75rem; color: #f43f5e; font-weight: 600;">Eliminar</span>
              </div>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0.4rem 0;">
                Borra de la cadena <code>S</code> los caracteres desde la posición inicial <code>Inicio</code> y borra la cantidad <code>Cuantos</code>.
              </p>
              <div style="font-size: 0.8rem; color: #94a3b8; font-family: 'Fira Code', monospace; background: #0b1120; padding: 0.5rem 0.65rem; border-radius: 4px; line-height: 1.5;">
                X := 'Hola Campeón';<br>
                Delete(X, 1, 5); <span style="color: #f43f5e;">// Borra 5 caracteres ('Hola ')</span><br>
                <span style="color: #10b981;">// X queda con: 'Campeón'</span>
              </div>
            </div>

            <!-- 2. Insert -->
            <div style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem; margin-bottom: 1rem;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="color: #a855f7; font-weight: 700; font-size: 0.88rem;">Insert(Source: String; var S: String; Indice: Integer)</code>
                <span style="font-size: 0.75rem; color: #10b981; font-weight: 600;">Insertar</span>
              </div>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0.4rem 0;">
                Inserta dentro de la cadena <code>S</code> la cadena <code>Source</code> en la posición <code>Indice</code>.
              </p>
              <div style="font-size: 0.8rem; color: #94a3b8; font-family: 'Fira Code', monospace; background: #0b1120; padding: 0.5rem 0.65rem; border-radius: 4px; line-height: 1.5;">
                A := 'Hola'; B := 'Car';<br>
                Insert(B, A, 2); <span style="color: #a855f7;">// Inserta 'Car' antes de la posición 2</span><br>
                <span style="color: #10b981;">// A queda con: 'HCarola'</span>
              </div>
            </div>

            <!-- Resumen pedagógico -->
            <div style="background: rgba(168, 85, 247, 0.08); border-left: 3px solid #a855f7; padding: 0.6rem 0.8rem; font-size: 0.82rem; color: #cbd5e1;">
              💡 <strong>Diferencia clave en Pascal:</strong><br>
              • <code>X := Copy(S, 1, 3);</code> es una <strong>función</strong> (usa asignación <code>:=</code>).<br>
              • <code>Delete(X, 1, 3);</code> es un <strong>procedimiento</strong> (no se asigna, modifica <code>X</code> in-situ).
            </div>

          </div>

        </div>

        <!-- PLAYGROUND INTERACTIVO DE OPERACIONES (TEST EN VIVO DE LAS FUNCIONES DEL WORD) -->
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-md); padding: 1.4rem; margin-bottom: 1.75rem;">
          <h4 style="color: #10b981; margin: 0 0 0.8rem 0; font-size: 1.15rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🧪</span> Laboratorio Interactivo de Funciones y Procedimientos (cadenas.docx)
          </h4>
          <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 1rem;">
            Prueba en tiempo real cómo actúan <code>Length</code>, <code>LowerCase</code>, <code>UpperCase</code>, <code>Copy</code>, <code>Delete</code> e <code>Insert</code> sobre una cadena:
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 0.35rem; font-weight: 600;">Cadena Base (X):</label>
              <input type="text" id="docLabCadena" value="Bolivar Campeón" style="width: 100%; padding: 0.55rem 0.8rem; background: #070a13; border: 1px solid #334155; border-radius: 6px; color: #fff; font-family: 'Fira Code', monospace; font-size: 0.9rem;">
            </div>

            <div>
              <label style="display: block; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 0.35rem; font-weight: 600;">Operación Delphi:</label>
              <select id="docLabOperacion" onchange="actualizarCamposLabDoc()" style="width: 100%; padding: 0.55rem 0.8rem; background: #070a13; border: 1px solid #334155; border-radius: 6px; color: #fff; font-family: 'Inter', sans-serif; font-size: 0.9rem;">
                <option value="length">Length(X) - Longitud</option>
                <option value="lowercase">LowerCase(X) - Minúsculas</option>
                <option value="uppercase">UpperCase(X) - Mayúsculas</option>
                <option value="copy" selected>Copy(X, Inicio, Cuantos) - Subcadena</option>
                <option value="delete">Delete(X, Inicio, Cuantos) - Borrar</option>
                <option value="insert">Insert(Source, X, Indice) - Insertar</option>
              </select>
            </div>

            <div id="docLabParam1Div">
              <label id="docLabParam1Label" style="display: block; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 0.35rem; font-weight: 600;">Posición Inicio:</label>
              <input type="text" id="docLabParam1" value="6" style="width: 100%; padding: 0.55rem 0.8rem; background: #070a13; border: 1px solid #334155; border-radius: 6px; color: #fff; font-family: 'Fira Code', monospace; font-size: 0.9rem;">
            </div>

            <div id="docLabParam2Div">
              <label id="docLabParam2Label" style="display: block; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 0.35rem; font-weight: 600;">Cantidad Caracteres:</label>
              <input type="text" id="docLabParam2" value="5" style="width: 100%; padding: 0.55rem 0.8rem; background: #070a13; border: 1px solid #334155; border-radius: 6px; color: #fff; font-family: 'Fira Code', monospace; font-size: 0.9rem;">
            </div>
          </div>

          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center; margin-bottom: 1rem;">
            <button class="btn-print" onclick="ejecutarLabDoc()" style="background: #10b981; color: #0f172a; font-weight: bold; border-color: #059669;">
              ▶ Ejecutar en Delphi Virtual
            </button>
            <button class="btn-print" onclick="cargarCasoDoc('copy_bolivar')" style="font-size: 0.8rem;">Cargar Caso: Copy('Bolivar Campeón', 6, 5)</button>
            <button class="btn-print" onclick="cargarCasoDoc('delete_campeon')" style="font-size: 0.8rem;">Cargar Caso: Delete('Hola Campeón', 1, 5)</button>
            <button class="btn-print" onclick="cargarCasoDoc('insert_hcarola')" style="font-size: 0.8rem;">Cargar Caso: Insert('Car', 'Hola', 2)</button>
          </div>

          <!-- Consola de Resultado del Laboratorio -->
          <div style="background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; font-family: 'Fira Code', monospace; font-size: 0.88rem;">
            <div style="color: #64748b; font-size: 0.78rem; margin-bottom: 0.4rem;">// SENTENCIA PASCAL EJECUTADA:</div>
            <div id="docLabCodigoSentencia" style="color: #38bdf8; margin-bottom: 0.6rem;">Resultado := Copy(X, 6, 5);</div>
            <div style="color: #64748b; font-size: 0.78rem; margin-bottom: 0.4rem;">// RESULTADO:</div>
            <div id="docLabResultado" style="color: #10b981; font-weight: 700; font-size: 1.05rem;">'ar ca'</div>
            <div id="docLabExplicacion" style="color: #94a3b8; font-size: 0.82rem; margin-top: 0.5rem; border-top: 1px dashed #1e293b; padding-top: 0.5rem;">
              💡 <strong>Explicación:</strong> Comienza en la posición 6 (letra 'a') y toma 5 caracteres ('a', 'r', ' ' (espacio), 'C', 'a'). Longitud del resultado: 5 caracteres.
            </div>
          </div>
        </div>

        <!-- SUB-SECCIÓN 3: CUESTIONARIO Y AUTOEVALUACIÓN INTERACTIVA (PREGUNTAS DEL WORD) -->
        <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: var(--radius-md); padding: 1.5rem; margin-bottom: 1.75rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.8rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.6rem;">
              <span style="font-size: 1.5rem;">📝</span>
              <div>
                <h4 style="color: #c084fc; margin: 0; font-size: 1.2rem; font-weight: 800;">Mini-Test de Autoevaluación Oficial (cadenas.docx)</h4>
                <span style="font-size: 0.8rem; color: #94a3b8;">5 preguntas oficiales con corrección inmediata y justificación técnica</span>
              </div>
            </div>
            <div id="docQuizScoreBadge" class="badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.4); margin: 0;">
              Puntaje: Sin calificar
            </div>
          </div>

          <!-- PREGUNTA 1 -->
          <div class="doc-quiz-card" style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 0.6rem; font-size: 0.92rem;">
              1. ¿Qué es una cadena en Delphi?
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.86rem;">
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q1" value="a"> Una sucesión de números.
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q1" value="b"> <strong>Una sucesión de caracteres.</strong>
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q1" value="c"> Una sucesión exclusiva de letras sin espacios ni números.
              </label>
            </div>
            <div id="doc_fb_1" style="display: none; margin-top: 0.6rem; font-size: 0.82rem; padding: 0.5rem 0.75rem; border-radius: 4px;"></div>
          </div>

          <!-- PREGUNTA 2 -->
          <div class="doc-quiz-card" style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 0.6rem; font-size: 0.92rem;">
              2. Siendo la cadena <code>P := 'Introducción a la informática';</code> ¿Cuál es la longitud devuelta por <code>Length(P)</code>?
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.86rem;">
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q2" value="a"> 26 caracteres (solo las letras).
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q2" value="b"> <strong>29 caracteres (contando letras y los 3 espacios en blanco).</strong>
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q2" value="c"> 30 caracteres.
              </label>
            </div>
            <div id="doc_fb_2" style="display: none; margin-top: 0.6rem; font-size: 0.82rem; padding: 0.5rem 0.75rem; border-radius: 4px;"></div>
          </div>

          <!-- PREGUNTA 3 -->
          <div class="doc-quiz-card" style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 0.6rem; font-size: 0.92rem;">
              3. ¿Cuál es el resultado de la asignación <code>P := LowerCase('HoLA');</code>?
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.86rem;">
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q3" value="a"> 'HOLA'
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q3" value="b"> 'Hola'
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q3" value="c"> <strong>'hola'</strong>
              </label>
            </div>
            <div id="doc_fb_3" style="display: none; margin-top: 0.6rem; font-size: 0.82rem; padding: 0.5rem 0.75rem; border-radius: 4px;"></div>
          </div>

          <!-- PREGUNTA 4 -->
          <div class="doc-quiz-card" style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 0.6rem; font-size: 0.92rem;">
              4. Si <code>X := 'Bolivar Campeón';</code> aplicando <code>P := Copy(X, 6, 5);</code> ¿Qué se almacena en <code>P</code>?
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.86rem;">
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q4" value="a"> 'campe'
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q4" value="b"> <strong>'ar ca'</strong>
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q4" value="c"> 'var c'
              </label>
            </div>
            <div id="doc_fb_4" style="display: none; margin-top: 0.6rem; font-size: 0.82rem; padding: 0.5rem 0.75rem; border-radius: 4px;"></div>
          </div>

          <!-- PREGUNTA 5 -->
          <div class="doc-quiz-card" style="background: rgba(7, 10, 19, 0.6); border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1.25rem;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 0.6rem; font-size: 0.92rem;">
              5. Siendo <code>A := 'Hola';</code> y <code>B := 'Car';</code> al ejecutar el procedimiento <code>Insert(B, A, 2);</code> ¿Cuál es el resultado final en <code>A</code>?
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.86rem;">
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q5" value="a"> 'CarHola'
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q5" value="b"> <strong>'HCarola'</strong>
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; color: #cbd5e1;">
                <input type="radio" name="doc_q5" value="c"> 'HoCarol'
              </label>
            </div>
            <div id="doc_fb_5" style="display: none; margin-top: 0.6rem; font-size: 0.82rem; padding: 0.5rem 0.75rem; border-radius: 4px;"></div>
          </div>

          <!-- Botón de Calificación -->
          <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
            <button class="btn-print" onclick="calificarQuizDoc()" style="background: #a855f7; color: #fff; font-weight: bold; border-color: #9333ea; padding: 0.6rem 1.4rem;">
              🎯 Calificar Respuestas
            </button>
            <button class="btn-print" onclick="reiniciarQuizDoc()" style="font-size: 0.82rem;">
              🔄 Reiniciar Test
            </button>
          </div>

        </div>

        <!-- SUB-SECCIÓN 4: REFERENCIAS BIBLIOGRÁFICAS OFICIALES -->
        <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1rem 1.4rem; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.4rem;">📚</span>
            <div>
              <div style="font-weight: 700; color: #fff; font-size: 0.9rem;">Bibliografía y Enlaces Oficiales Recomendados (cadenas.docx):</div>
              <div style="font-size: 0.8rem; color: #94a3b8;">Fuentes académicas sugeridas por la docente para profundizar en Delphi Pascal:</div>
            </div>
          </div>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <a href="https://delphiallimite.blogspot.com/2007/08/operaciones-con-cadenas-de-texto-iv.html" target="_blank" class="btn-print" style="font-size: 0.78rem; text-decoration: none;">🌐 Delphi al Límite (Strings IV)</a>
            <a href="http://www.carlospes.com/sintaxis_pascal/" target="_blank" class="btn-print" style="font-size: 0.78rem; text-decoration: none;">📘 Carlos Pes (Sintaxis Pascal)</a>
            <a href="http://www.mailxmail.com/curso-introduccion-lenguaje-pascal/cadenas-strings" target="_blank" class="btn-print" style="font-size: 0.78rem; text-decoration: none;">📄 Mailxmail (Cadenas Pascal)</a>
          </div>
        </div>

      </div>
      <!-- ========================================================================= -->
      <!-- FIN BLOQUE TEÓRICO: FUNDAMENTOS Y MANEJO DE CADENAS (cadenas.docx)        -->
      <!-- ========================================================================= -->
'''

def build_cadenas_docx_js():
    return '''
  // ===========================================================================
  //      MOTOR JAVASCRIPT: FUNDAMENTOS TEÓRICOS DE CADENAS (cadenas.docx)
  // ===========================================================================

  // 1. Inspector Gráfico de Memoria
  function actualizarInspectorMemoriaDoc() {
    const input = document.getElementById('docInspectInput');
    const grid = document.getElementById('docMemoryGrid');
    const lenLabel = document.getElementById('docInspectLength');
    if (!input || !grid || !lenLabel) return;

    const texto = input.value;
    lenLabel.innerText = texto.length + ' caracteres';
    grid.innerHTML = '';

    if (texto.length === 0) {
      grid.innerHTML = '<div style="color: #64748b; font-size: 0.85rem; padding: 0.5rem;">(Cadena vacía: Length = 0)</div>';
      return;
    }

    for (let i = 0; i < texto.length; i++) {
      const ch = texto[i];
      const idx = i + 1; // Base 1 en Pascal
      const esEspacio = (ch === ' ');

      const cell = document.createElement('div');
      cell.style.cssText = `
        display: flex;
        flex-direction: column;
        align-items: center;
        background: ${esEspacio ? 'rgba(244, 63, 94, 0.12)' : 'rgba(30, 41, 59, 0.8)'};
        border: 1px solid ${esEspacio ? 'rgba(244, 63, 94, 0.4)' : '#334155'};
        border-radius: 6px;
        min-width: 44px;
        padding: 0.45rem 0.3rem;
        cursor: pointer;
        transition: all 0.2s;
      `;

      cell.onmouseover = () => { cell.style.borderColor = '#38bdf8'; cell.style.transform = 'translateY(-2px)'; };
      cell.onmouseout = () => { cell.style.borderColor = esEspacio ? 'rgba(244, 63, 94, 0.4)' : '#334155'; cell.style.transform = 'translateY(0)'; };
      cell.onclick = () => {
        const displayChar = esEspacio ? "' ' (Espacio en blanco, ASCII 32)" : `'${ch}' (ASCII ${ch.charCodeAt(0)})`;
        document.getElementById('docInspectCharSelected').innerHTML = `Posición <strong>X[${idx}]</strong> = <span style="color: #38bdf8; font-weight: bold;">${displayChar}</span>`;
      };

      const charSpan = document.createElement('span');
      charSpan.style.cssText = `
        font-family: 'Fira Code', monospace;
        font-size: 1.15rem;
        font-weight: 700;
        color: ${esEspacio ? '#fb7185' : '#f8fafc'};
        height: 28px;
        display: flex;
        align-items: center;
      `;
      charSpan.innerText = esEspacio ? '␣' : ch;

      const idxSpan = document.createElement('span');
      idxSpan.style.cssText = `
        font-family: 'Fira Code', monospace;
        font-size: 0.72rem;
        color: ${esEspacio ? '#fda4af' : '#94a3b8'};
        margin-top: 0.25rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        width: 100%;
        text-align: center;
        padding-top: 0.2rem;
      `;
      idxSpan.innerText = idx;

      cell.appendChild(charSpan);
      cell.appendChild(idxSpan);
      grid.appendChild(cell);
    }
  }

  function inspeccionarEjemploDoc(ejTexto) {
    const input = document.getElementById('docInspectInput');
    if (input) {
      input.value = ejTexto;
      actualizarInspectorMemoriaDoc();
    }
  }

  // 2. Laboratorio Interactivo de Funciones y Procedimientos
  function actualizarCamposLabDoc() {
    const op = document.getElementById('docLabOperacion').value;
    const p1Div = document.getElementById('docLabParam1Div');
    const p2Div = document.getElementById('docLabParam2Div');
    const p1Label = document.getElementById('docLabParam1Label');
    const p2Label = document.getElementById('docLabParam2Label');
    const p1Input = document.getElementById('docLabParam1');
    const p2Input = document.getElementById('docLabParam2');

    if (op === 'length' || op === 'lowercase' || op === 'uppercase') {
      p1Div.style.display = 'none';
      p2Div.style.display = 'none';
    } else if (op === 'copy' || op === 'delete') {
      p1Div.style.display = 'block';
      p2Div.style.display = 'block';
      p1Label.innerText = 'Posición Inicio:';
      p2Label.innerText = 'Cantidad Caracteres:';
      if (!p1Input.value) p1Input.value = '1';
      if (!p2Input.value) p2Input.value = '3';
    } else if (op === 'insert') {
      p1Div.style.display = 'block';
      p2Div.style.display = 'block';
      p1Label.innerText = 'Texto a Insertar (Source):';
      p2Label.innerText = 'Posición Índice:';
      p1Input.value = 'Car';
      p2Input.value = '2';
    }
    ejecutarLabDoc();
  }

  function ejecutarLabDoc() {
    const cad = document.getElementById('docLabCadena').value;
    const op = document.getElementById('docLabOperacion').value;
    const p1 = document.getElementById('docLabParam1').value;
    const p2 = document.getElementById('docLabParam2').value;

    const lblCode = document.getElementById('docLabCodigoSentencia');
    const lblRes = document.getElementById('docLabResultado');
    const lblExp = document.getElementById('docLabExplicacion');

    if (op === 'length') {
      lblCode.innerText = `L := Length(X); // X = '${cad}'`;
      lblRes.innerText = cad.length;
      lblExp.innerHTML = `💡 <strong>Explicación:</strong> Devuelve la cantidad de caracteres que tiene <code>X</code>. En este caso son <strong>${cad.length}</strong> caracteres.`;
    } else if (op === 'lowercase') {
      lblCode.innerText = `Resultado := LowerCase(X); // X = '${cad}'`;
      lblRes.innerText = `'${cad.toLowerCase()}'`;
      lblExp.innerHTML = `💡 <strong>Explicación:</strong> Todas las letras mayúsculas se convierten a sus equivalentes en minúsculas.`;
    } else if (op === 'uppercase') {
      lblCode.innerText = `Resultado := UpperCase(X); // X = '${cad}'`;
      lblRes.innerText = `'${cad.toUpperCase()}'`;
      lblExp.innerHTML = `💡 <strong>Explicación:</strong> Todas las letras minúsculas se convierten a sus equivalentes en mayúsculas.`;
    } else if (op === 'copy') {
      const inicio = parseInt(p1, 10) || 1;
      const cuantos = parseInt(p2, 10) || 0;
      // En JS substring/substr: base 0
      const sub = cad.substr(Math.max(0, inicio - 1), Math.max(0, cuantos));
      lblCode.innerText = `Resultado := Copy(X, ${inicio}, ${cuantos}); // X = '${cad}'`;
      lblRes.innerText = `'${sub}'`;
      lblExp.innerHTML = `💡 <strong>Explicación:</strong> Toma la cadena desde la posición <strong>${inicio}</strong> (base 1) y extrae <strong>${cuantos}</strong> caracteres. El resultado obtenido es <code>'${sub}'</code>.`;
    } else if (op === 'delete') {
      const inicio = parseInt(p1, 10) || 1;
      const cuantos = parseInt(p2, 10) || 0;
      let copia = cad;
      if (inicio >= 1 && inicio <= copia.length) {
        copia = copia.slice(0, inicio - 1) + copia.slice(inicio - 1 + cuantos);
      }
      lblCode.innerText = `Delete(X, ${inicio}, ${cuantos}); // X antes: '${cad}'`;
      lblRes.innerText = `'${copia}'`;
      lblExp.innerHTML = `💡 <strong>Explicación:</strong> Modifica <code>X</code> eliminando <strong>${cuantos}</strong> caracteres a partir de la posición <strong>${inicio}</strong>. <code>X</code> pasa a valer <code>'${copia}'</code>.`;
    } else if (op === 'insert') {
      const source = p1;
      const indice = parseInt(p2, 10) || 1;
      let res = cad;
      if (indice <= 1) {
        res = source + cad;
      } else if (indice > cad.length) {
        res = cad + source;
      } else {
        res = cad.slice(0, indice - 1) + source + cad.slice(indice - 1);
      }
      lblCode.innerText = `Insert('${source}', X, ${indice}); // X antes: '${cad}'`;
      lblRes.innerText = `'${res}'`;
      lblExp.innerHTML = `💡 <strong>Explicación:</strong> Inserta la cadena <code>'${source}'</code> en la posición <strong>${indice}</strong> de <code>X</code>. <code>X</code> queda como <code>'${res}'</code>.`;
    }
  }

  function cargarCasoDoc(caso) {
    if (caso === 'copy_bolivar') {
      document.getElementById('docLabCadena').value = 'Bolivar Campeón';
      document.getElementById('docLabOperacion').value = 'copy';
      actualizarCamposLabDoc();
      document.getElementById('docLabParam1').value = '6';
      document.getElementById('docLabParam2').value = '5';
    } else if (caso === 'delete_campeon') {
      document.getElementById('docLabCadena').value = 'Hola Campeón';
      document.getElementById('docLabOperacion').value = 'delete';
      actualizarCamposLabDoc();
      document.getElementById('docLabParam1').value = '1';
      document.getElementById('docLabParam2').value = '5';
    } else if (caso === 'insert_hcarola') {
      document.getElementById('docLabCadena').value = 'Hola';
      document.getElementById('docLabOperacion').value = 'insert';
      actualizarCamposLabDoc();
      document.getElementById('docLabParam1').value = 'Car';
      document.getElementById('docLabParam2').value = '2';
    }
    ejecutarLabDoc();
  }

  // 3. Mini-Test de Autoevaluación
  function calificarQuizDoc() {
    let score = 0;
    const total = 5;

    const answers = {
      doc_q1: { correct: 'b', exp: '¡Excelente! Una cadena es una sucesión de caracteres (letras, números, símbolos y espacios).' },
      doc_q2: { correct: 'b', exp: '¡Correcto! Length(\\'Introducción a la informática\\') = 29 caracteres, tomando en cuenta las letras y los 3 espacios en blanco.' },
      doc_q3: { correct: 'c', exp: '¡Correcto! LowerCase convierte todas las letras a minúsculas, por lo que \\'HoLA\\' pasa a ser \\'hola\\'.' },
      doc_q4: { correct: 'b', exp: '¡Correcto! En \\'Bolivar Campeón\\', la posición 6 es \\'a\\', posición 7 es \\'r\\', posición 8 es el espacio \\' \\', 9 es \\'C\\', y 10 es \\'a\\'. Por tanto Copy(X, 6, 5) devuelve \\'ar ca\\'.' },
      doc_q5: { correct: 'b', exp: '¡Correcto! Al insertar \\'Car\\' en la posición 2 de \\'Hola\\', se coloca justo antes de la \\'o\\', quedando \\'H\\' + \\'Car\\' + \\'ola\\' = \\'HCarola\\'.' }
    };

    for (let i = 1; i <= total; i++) {
      const qName = 'doc_q' + i;
      const radios = document.getElementsByName(qName);
      let selected = null;
      for (const r of radios) {
        if (r.checked) { selected = r.value; break; }
      }

      const fb = document.getElementById('doc_fb_' + i);
      fb.style.display = 'block';

      if (selected === answers[qName].correct) {
        score++;
        fb.style.background = 'rgba(16, 185, 129, 0.15)';
        fb.style.border = '1px solid #10b981';
        fb.style.color = '#10b981';
        fb.innerHTML = '✅ ' + answers[qName].exp;
      } else {
        fb.style.background = 'rgba(244, 63, 94, 0.15)';
        fb.style.border = '1px solid #f43f5e';
        fb.style.color = '#fb7185';
        fb.innerHTML = '❌ ' + (selected ? 'Respuesta incorrecta. ' : 'No respondiste esta pregunta. ') + answers[qName].exp;
      }
    }

    const badge = document.getElementById('docQuizScoreBadge');
    badge.innerText = `Puntaje: ${score}/${total} (${Math.round((score/total)*100)}%)`;
    if (score === total) {
      badge.style.background = 'rgba(16, 185, 129, 0.2)';
      badge.style.color = '#10b981';
      badge.style.borderColor = '#10b981';
      showMobileToast('¡Felicidades! 5/5 respuestas correctas en el test de cadenas.');
    } else {
      badge.style.background = 'rgba(245, 158, 11, 0.2)';
      badge.style.color = '#fbbf24';
      badge.style.borderColor = '#fbbf24';
      showMobileToast(`Test calificado: ${score}/${total} correctas.`);
    }
  }

  function reiniciarQuizDoc() {
    for (let i = 1; i <= 5; i++) {
      const radios = document.getElementsByName('doc_q' + i);
      for (const r of radios) r.checked = false;
      const fb = document.getElementById('doc_fb_' + i);
      if (fb) fb.style.display = 'none';
    }
    const badge = document.getElementById('docQuizScoreBadge');
    if (badge) {
      badge.innerText = 'Puntaje: Sin calificar';
      badge.style.background = 'rgba(168, 85, 247, 0.15)';
      badge.style.color = '#c084fc';
      badge.style.borderColor = 'rgba(168, 85, 247, 0.4)';
    }
    showMobileToast('Test de autoevaluación restablecido.');
  }

  // Inicializar inspector al cargar
  window.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
      actualizarInspectorMemoriaDoc();
      actualizarCamposLabDoc();
    }, 200);
  });
'''
