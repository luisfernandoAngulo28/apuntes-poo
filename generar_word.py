# -*- coding: utf-8 -*-
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="2563EB"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_analysis_table(doc, entrada, salida, proceso):
    table = doc.add_table(rows=3, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = [("Datos de Entrada:", entrada), ("Datos de Salida:", salida), ("Proceso / Lógica:", proceso)]
    for idx, (lbl, val) in enumerate(headers):
        c0 = table.cell(idx, 0)
        c1 = table.cell(idx, 1)
        c0.width = Inches(1.8)
        c1.width = Inches(4.7)
        
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        
        # Borde sutil
        for c in (c0, c1):
            tcPr = c._tc.get_or_add_tcPr()
            b = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                    <w:left w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                    <w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                </w:tcBorders>
            ''')
            tcPr.append(b)
            
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(lbl)
        r0.font.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(3)

def create_full_document():
    doc = Document()
    
    # Margins
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # ==================== PORTADA ====================
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(20)
    title_p.paragraph_format.space_after = Pt(4)
    
    r_uni = title_p.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(14)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = title_p.add_run("Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones\nCarrera de Ingeniería Informática / Sistemas\n")
    r_fac.font.name = "Calibri"
    r_fac.font.size = Pt(11)
    r_fac.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("—" * 50)
    r_line.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
    r_line.font.bold = True

    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_before = Pt(18)
    p_main.paragraph_format.space_after = Pt(6)
    r_title = p_main.add_run("INFORME ACADÉMICO: PRÁCTICO #7 Y TAREA DE CLASE\nRESOLUCIÓN METODOLÓGICA DE ALGORITMOS MODULARES")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(30)
    r_sub = p_sub.add_run("Análisis, Diseño Modular, Implementación en Delphi/Pascal y Pruebas de Escritorio\nTratamiento de Dígitos en Números Naturales y Aplicación VCL")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    # Info Table
    info_table = doc.add_table(rows=5, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Materia:", "Introducción a la Informática / Programación I"),
        ("Lenguaje / Entorno:", "Delphi (Object Pascal) / Embarcadero RAD Studio"),
        ("Metodología:", "1. Enunciado | 2. Análisis (E/S/Proceso) | 3. Diseño | 4. Código | 5. Traza"),
        ("Tema:", "Programación Modular y Descomposición de Números Naturales"),
        ("Gestión:", "Semestre II - 2026")
    ]
    for row_idx, (label, val) in enumerate(info_data):
        cell_lbl = info_table.cell(row_idx, 0)
        cell_val = info_table.cell(row_idx, 1)
        cell_lbl.width = Inches(2.0)
        cell_val.width = Inches(4.5)
        
        p0 = cell_lbl.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        
        p1 = cell_val.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)

    doc.add_page_break()

    # Headings
    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
        return h

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.bold = True
            r_b.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        p.add_run(text)
        return p

    # ==================== 1. METODOLOGÍA FORMAL ====================
    add_h1("1. METODOLOGÍA FORMAL DE RESOLUCIÓN DE ALGORITMOS")
    add_p("Para dar cumplimiento a los estándares de desarrollo de software académico y programación modular, cada ejercicio se estructura bajo las 5 etapas metodológicas fundamentales:")
    
    add_p(" Definición clara y precisa de la necesidad o requerimiento computacional a resolver.", bold_prefix="Paso 1. Enunciado del Problema:")
    add_p(" Identificación rigurosa de las variables de entrada (tipos y dominio), salidas esperadas y la lógica matemática/algorítmica de transformación.", bold_prefix="Paso 2. Análisis del Problema:")
    add_p(" Selección del tipo de módulo (Función cuando retorna un único valor escalar, o Procedimiento cuando produce múltiples salidas por referencia 'var' o acciones de interfaz) y definición de su signatura formal.", bold_prefix="Paso 3. Diseño Modular:")
    add_p(" Codificación estructurada en lenguaje Object Pascal / Delphi respetando la sintaxis limpia y estándares de nomenclatura.", bold_prefix="Paso 4. Implementación del Algoritmo:")
    add_p(" Simulación de ejecución paso a paso con valores de prueba (traza) para verificar la consistencia y correcta terminación del ciclo.", bold_prefix="Paso 5. Prueba de Escritorio / Traza:")

    # ==================== 2. TAREA DE CLASE (VCL) ====================
    add_h1("2. TAREA DE CLASE: APLICACIÓN VCL INTERACTIVA (DELPHI)")
    add_p("La tarea de clase implementa un formulario visual interactivo con TEdit para la captura y visualización de datos y botones TButton vinculados a módulos de procesamiento de números naturales.")

    # Ejercicios de Clase detallados
    clase_items = [
        {
            "nombre": "Cargar Número Natural (Button1Click)",
            "enunciado": "Capturar una cadena de texto desde Edit1, validarla, convertirla a tipo numérico Word/Cardinal y almacenarla en la variable global 'n'.",
            "entrada": "Edit1.Text (String: representación en caracteres del número).",
            "salida": "Variable global n (Word), mensaje de confirmación en pantalla.",
            "proceso": "1. Verificar que Edit1 no esté vacío. 2. Convertir texto a entero con StrToInt. 3. Asignar a 'n'. 4. Mostrar ShowMessage.",
            "diseno": "procedure TForm1.Button1Click(Sender: TObject); [Procedimiento de Evento VCL]",
            "code": '''procedure TForm1.Button1Click(Sender: TObject);
begin
  if Edit1.Text <> '' then
  begin
    n := StrToInt(Edit1.Text);
    ShowMessage('Número natural registrado: ' + IntToStr(n));
  end
  else
    ShowMessage('Por favor ingresa un número en Edit1');
end;''',
            "traza": "Edit1.Text = '1234' -> n = 1234 -> ShowMessage('Número natural registrado: 1234')"
        },
        {
            "nombre": "Sumar Dígitos Primos (Button2Click / SumarDigitosPrimos)",
            "enunciado": "Extraer los dígitos del número global 'n', verificar si cada dígito pertenece al conjunto de primos {2, 3, 5, 7} y acumular su suma, mostrándola en Edit2.",
            "entrada": "n : Word (número natural cargado previamente).",
            "salida": "suma : Word (suma total de los dígitos primos encontrados), mostrada en Edit2.Text.",
            "proceso": "1. Inicializar suma := 0. 2. Mientras num > 0: d := num mod 10; si EsPrimo(d) entonces suma := suma + d; num := num div 10. 3. Retornar suma.",
            "diseno": "function SumarDigitosPrimos(num: Word): Word; [Función escalar pura]",
            "code": '''function EsPrimo(d: Byte): Boolean;
begin
  Result := (d = 2) or (d = 3) or (d = 5) or (d = 7);
end;

function SumarDigitosPrimos(num: Word): Word;
var
  d, suma: Word;
begin
  suma := 0;
  while num > 0 do
  begin
    d := num mod 10;
    if EsPrimo(d) then
      suma := suma + d;
    num := num div 10;
  end;
  Result := suma;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(SumarDigitosPrimos(n));
end;''',
            "traza": "Para N = 2374: Iter 1 (d=4, no primo) -> Iter 2 (d=7, suma=7) -> Iter 3 (d=3, suma=10) -> Iter 4 (d=2, suma=12). Resultado = 12."
        },
        {
            "nombre": "Formar Solo Pares (Button3Click / FormarSoloPares)",
            "enunciado": "Construir y retornar un nuevo número natural compuesto únicamente por los dígitos pares de 'n', conservando el orden relativo original.",
            "entrada": "num : Word (número natural a procesar).",
            "salida": "npar : Word (número compuesto por los dígitos pares), mostrado en Edit2.",
            "proceso": "1. Inicializar npar := 0, pot := 1. 2. Mientras num > 0: d := num mod 10; si (d mod 2 = 0) entonces npar := npar + (d * pot), pot := pot * 10; num := num div 10. 3. Retornar npar.",
            "diseno": "function FormarSoloPares(num: Word): Word; [Función escalar con reconstrucción posicional]",
            "code": '''function FormarSoloPares(num: Word): Word;
var
  d, npar, pot: Word;
begin
  npar := 0;
  pot := 1;
  while num > 0 do
  begin
    d := num mod 10;
    if (d mod 2 = 0) then
    begin
      npar := npar + (d * pot);
      pot := pot * 10;
    end;
    num := num div 10;
  end;
  Result := npar;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(FormarSoloPares(n));
end;''',
            "traza": "Para N = 1234: d=4 (par, npar=4, pot=10) -> d=3 (impar) -> d=2 (par, npar=4+20=24, pot=100) -> d=1 (impar). Resultado = 24."
        },
        {
            "nombre": "Sumar Múltiplos de 3 (Button4Click / SumarMultiplosDe3)",
            "enunciado": "Recorrer los dígitos del número y acumular la suma de todos aquellos que sean múltiplos de 3 (0, 3, 6, 9).",
            "entrada": "num : Word (número natural).",
            "salida": "suma : Word (suma de los dígitos múltiplos de 3), mostrado en Edit2.",
            "proceso": "1. Inicializar suma := 0. 2. Mientras num > 0: d := num mod 10; si (d mod 3 = 0) entonces suma := suma + d; num := num div 10. 3. Retornar suma.",
            "diseno": "function SumarMultiplosDe3(num: Word): Word; [Función escalar]",
            "code": '''function SumarMultiplosDe3(num: Word): Word;
var
  d, suma: Word;
begin
  suma := 0;
  while num > 0 do
  begin
    d := num mod 10;
    if (d mod 3 = 0) then
      suma := suma + d;
    num := num div 10;
  end;
  Result := suma;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(SumarMultiplosDe3(n));
end;''',
            "traza": "Para N = 3681: d=1 (no mult 3) -> d=8 (no mult 3) -> d=6 (suma=6) -> d=3 (suma=6+3=9). Resultado = 9."
        },
        {
            "nombre": "Invertir Número (Button5Click / InvertirNumero)",
            "enunciado": "Generar un nuevo número natural invirtiendo el orden de todos los dígitos que componen a 'n'.",
            "entrada": "num : Word (número natural original).",
            "salida": "inv : Word (número invertido), mostrado en Edit2.",
            "proceso": "1. Inicializar inv := 0. 2. Mientras num > 0: d := num mod 10; inv := (inv * 10) + d; num := num div 10. 3. Retornar inv.",
            "diseno": "function InvertirNumero(num: Word): Word; [Función escalar con desplazamiento decimal]",
            "code": '''function InvertirNumero(num: Word): Word;
var
  d, inv: Word;
begin
  inv := 0;
  while num > 0 do
  begin
    d := num mod 10;
    inv := (inv * 10) + d;
    num := num div 10;
  end;
  Result := inv;
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(InvertirNumero(n));
end;''',
            "traza": "Para N = 4782: d=2 (inv=2) -> d=8 (inv=28) -> d=7 (inv=287) -> d=4 (inv=2874). Resultado = 2874."
        }
    ]

    for item in clase_items:
        add_h2(f"Tarea de Clase: {item['nombre']}")
        add_p(item['enunciado'], bold_prefix="1. Enunciado: ")
        add_analysis_table(doc, item['entrada'], item['salida'], item['proceso'])
        add_p(item['diseno'], bold_prefix="2. Diseño Modular: ")
        add_p("3. Implementación en Pascal/Delphi:")
        add_code_block(doc, item['code'])
        add_p(item['traza'], bold_prefix="4. Prueba de Escritorio (Traza): ")

    doc.add_page_break()

    # ==================== 3. DESARROLLO DE LOS 25 EJERCICIOS ====================
    add_h1("3. RESOLUCIÓN METODOLÓGICA DE LOS 25 EJERCICIOS DEL PRÁCTICO #7")
    add_p("A continuación se detallan los 25 ejercicios del práctico siguiendo estrictamente el esquema: Enunciado, Análisis (Entrada/Salida/Proceso), Diseño Modular, Código Pascal y Prueba de Escritorio.")

    ejercicios_completos = [
        {
            "num": 1,
            "titulo": "Suma de los dígitos impares mayores a 3 (5, 7, 9)",
            "enunciado": "Dado un número natural N, calcular y retornar la suma de todos aquellos dígitos que sean simultáneamente impares y mayores a 3 (es decir: 5, 7 y 9).",
            "entrada": "n : Cardinal (Número natural en base 10).",
            "salida": "suma : Cardinal (Suma acumulada de dígitos impares > 3).",
            "proceso": "1. Inicializar suma := 0. 2. Extraer dígitos con n mod 10. 3. Evaluar si (d mod 2 <> 0) AND (d > 3). Si cumple, acumular suma := suma + d. 4. Reducir con n := n div 10. 5. Retornar suma.",
            "diseno": "function SumaImparesMayores3(n: Cardinal): Cardinal; [Función escalar por valor]",
            "code": '''function SumaImparesMayores3(n: Cardinal): Cardinal;
var
  d, suma: Cardinal;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 <> 0) and (d > 3) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;''',
            "traza": "N = 37952: d=2(no), d=5(suma=5), d=9(suma=14), d=7(suma=21), d=3(no > 3). Resultado final: 21."
        },
        {
            "num": 2,
            "titulo": "Dígito mayor de las posiciones/índices impares",
            "enunciado": "Dado un número natural N, evaluar los dígitos que ocupan posiciones impares contando de izquierda a derecha (1ª, 3ª, 5ª posición...) y retornar el mayor de ellos.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "maxD : Integer (Dígito con valor máximo en índices impares, o -1 si vacío).",
            "proceso": "1. Convertir n a String para indexar de izq a der. 2. Recorrer con paso i := i + 2 (posiciones 1, 3, 5...). 3. Obtener valor numérico del carácter y actualizar maxD si valD > maxD. 4. Retornar maxD.",
            "diseno": "function DigitoMayorIndicesImpares(n: Cardinal): Integer; [Función escalar]",
            "code": '''function DigitoMayorIndicesImpares(n: Cardinal): Integer;
var
  s: String;
  i, maxD, valD: Integer;
begin
  s := IntToStr(n);
  maxD := -1;
  i := 1;
  while i <= Length(s) do
  begin
    valD := Ord(s[i]) - Ord('0');
    if valD > maxD then
      maxD := valD;
    i := i + 2;
  end;
  Result := maxD;
end;''',
            "traza": "N = 48291: s='48291'. Pos 1: '4' (max=4). Pos 3: '2' (2 < 4). Pos 5: '1' (1 < 4). Resultado final: 4."
        },
        {
            "num": 3,
            "titulo": "Sumar todos los dígitos de un número",
            "enunciado": "Hacer un algoritmo para sumar todos los dígitos de un número natural N dado.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "suma : Cardinal (Suma de todos los dígitos de N).",
            "proceso": "1. Inicializar suma := 0. 2. En bucle mientras n > 0, sumar (n mod 10) a suma. 3. n := n div 10. 4. Retornar suma.",
            "diseno": "function SumaDigitos(n: Cardinal): Cardinal; [Función acumuladora]",
            "code": '''function SumaDigitos(n: Cardinal): Cardinal;
var
  suma: Cardinal;
begin
  suma := 0;
  while n > 0 do
  begin
    suma := suma + (n mod 10);
    n := n div 10;
  end;
  Result := suma;
end;''',
            "traza": "N = 5821: d=1 (suma=1) -> d=2 (suma=3) -> d=8 (suma=11) -> d=5 (suma=16). Resultado final: 16."
        },
        {
            "num": 4,
            "titulo": "Promedio de los dígitos menores a 7",
            "enunciado": "Calcular el promedio aritmético (media) de todos los dígitos del número N que sean estrictamente menores a 7.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "promedio : Double (Promedio real = suma / cantidad).",
            "proceso": "1. Inicializar suma := 0, cont := 0. 2. Mientras n > 0: d := n mod 10; si d < 7 entonces sumar a suma e incrementar cont; n := n div 10. 3. Si cont > 0 retornar suma/cont, sino 0.0.",
            "diseno": "function PromedioDigitosMenores7(n: Cardinal): Double; [Función de valor real]",
            "code": '''function PromedioDigitosMenores7(n: Cardinal): Double;
var
  d, suma, cont: Cardinal;
begin
  suma := 0;
  cont := 0;
  if n = 0 then Exit(0.0);
  while n > 0 do
  begin
    d := n mod 10;
    if d < 7 then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then
    Result := suma / cont
  else
    Result := 0.0;
end;''',
            "traza": "N = 85293: Dígitos < 7 son {3, 2, 5}. Suma = 10, Cont = 3. Promedio = 10 / 3 = 3.33."
        },
        {
            "num": 5,
            "titulo": "Obtener el dígito mayor y el dígito menor",
            "enunciado": "De un número natural N, determinar cuál es el dígito mayor y cuál es el dígito menor utilizando un solo módulo.",
            "entrada": "n : Cardinal (Número natural de entrada).",
            "salida": "var digMayor, var digMenor : Byte (Retornados por referencia).",
            "proceso": "1. Inicializar digMayor := 0, digMenor := 9. 2. Mientras n > 0: d := n mod 10; si d > digMayor actualizar digMayor; si d < digMenor actualizar digMenor; n := n div 10.",
            "diseno": "procedure MayorYMenorDigito(n: Cardinal; var digMayor, digMenor: Byte); [Procedimiento con parámetros por referencia]",
            "code": '''procedure MayorYMenorDigito(n: Cardinal; var digMayor, digMenor: Byte);
var
  d: Byte;
begin
  if n = 0 then
  begin
    digMayor := 0;
    digMenor := 0;
    Exit;
  end;
  digMayor := 0;
  digMenor := 9;
  while n > 0 do
  begin
    d := n mod 10;
    if d > digMayor then digMayor := d;
    if d < digMenor then digMenor := d;
    n := n div 10;
  end;
end;''',
            "traza": "N = 93184: Compara dígitos {4, 8, 1, 3, 9} contra mayor y menor. Salida: digMayor = 9, digMenor = 1."
        },
        {
            "num": 6,
            "titulo": "Formar otro número con los dígitos pares",
            "enunciado": "Dado un número natural N, formar y retornar un nuevo número compuesto únicamente por los dígitos pares de N, preservando su orden original.",
            "entrada": "n : Cardinal (Número natural original).",
            "salida": "res : Cardinal (Nuevo número formado por dígitos pares).",
            "proceso": "1. Inicializar res := 0, pot := 1. 2. Mientras n > 0: d := n mod 10; si (d mod 2 = 0) sumar d * pot a res y multiplicar pot := pot * 10; n := n div 10. 3. Retornar res.",
            "diseno": "function FormarNumeroPares(n: Cardinal): Cardinal; [Función con reconstrucción posicional]",
            "code": '''function FormarNumeroPares(n: Cardinal): Cardinal;
var
  d, res, pot: Cardinal;
begin
  res := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  Result := res;
end;''',
            "traza": "N = 741829: d=9(no), d=2(res=2, pot=10), d=8(res=82, pot=100), d=1(no), d=4(res=482, pot=1000), d=7(no). Resultado = 482."
        },
        {
            "num": 7,
            "titulo": "Separar un número en dos: pares e impares",
            "enunciado": "Dado un número natural N, retornar dos números: uno formado únicamente por sus dígitos pares y otro por sus dígitos impares.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "var numPares, var numImpares : Cardinal (Dos números resultantes por referencia).",
            "proceso": "1. Inicializar numPares := 0, numImpares := 0, potPar := 1, potImpar := 1. 2. Descomponer n: si d es par acumular en numPares y avanzar potPar; sino acumular en numImpares y avanzar potImpar. 3. n := n div 10.",
            "diseno": "procedure SepararParesImpares(n: Cardinal; var numPares, numImpares: Cardinal); [Procedimiento con doble salida]",
            "code": '''procedure SepararParesImpares(n: Cardinal; var numPares, numImpares: Cardinal);
var
  d, potPar, potImpar: Cardinal;
begin
  numPares := 0;
  numImpares := 0;
  potPar := 1;
  potImpar := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 2 = 0 then
    begin
      numPares := numPares + (d * potPar);
      potPar := potPar * 10;
    end
    else
    begin
      numImpares := numImpares + (d * potImpar);
      potImpar := potImpar * 10;
    end;
    n := n div 10;
  end;
end;''',
            "traza": "N = 852174 -> Pares extraídos en orden: 8, 2, 4 -> numPares = 824. Impares: 5, 1, 7 -> numImpares = 517."
        },
        {
            "num": 8,
            "titulo": "Dígito mayor de los dígitos pares",
            "enunciado": "Dado un número natural N, encontrar y mostrar el dígito mayor entre los pares. Si no contiene pares, retornar -1.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "mayor : Integer (Mayor dígito par o -1 si no tiene).",
            "proceso": "1. Inicializar mayor := -1. 2. Mientras n > 0: d := n mod 10; si (d mod 2 = 0) y (d > mayor) entonces mayor := d; n := n div 10. 3. Retornar mayor.",
            "diseno": "function MayorDigitoPar(n: Cardinal): Integer; [Función escalar con control de existencia]",
            "code": '''function MayorDigitoPar(n: Cardinal): Integer;
var
  d: Cardinal;
  mayor: Integer;
begin
  mayor := -1;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) and (Integer(d) > mayor) then
      mayor := d;
    n := n div 10;
  end;
  Result := mayor;
end;''',
            "traza": "N = 173825 -> Pares presentes: {8, 2}. mayor inicial = -1 -> pasa a 2 -> pasa a 8. Resultado final: 8."
        },
        {
            "num": 9,
            "titulo": "Mostrar los dígitos múltiplos de 3",
            "enunciado": "De un número natural N, mostrar en forma de lista o cadena de texto todos los dígitos que sean múltiplos de 3 (0, 3, 6, 9).",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "res : String (Cadena con los dígitos múltiplos de 3 separados por comas).",
            "proceso": "1. Convertir n a String. 2. Iterar del primer al último carácter: si el dígito numérico d mod 3 = 0, concatenar a res. 3. Si res queda vacía retornar 'Ninguno', sino res.",
            "diseno": "function DigitosMultiplosDe3(n: Cardinal): String; [Función formateadora de salida]",
            "code": '''function DigitosMultiplosDe3(n: Cardinal): String;
var
  s, res: String;
  i, d: Integer;
begin
  s := IntToStr(n);
  res := '';
  for i := 1 to Length(s) do
  begin
    d := Ord(s[i]) - Ord('0');
    if d mod 3 = 0 then
    begin
      if res <> '' then res := res + ', ';
      res := res + s[i];
    end;
  end;
  if res = '' then Result := 'Ninguno' else Result := res;
end;''',
            "traza": "N = 439260 -> Recorrido: 4(no), 3(sí), 9(sí), 2(no), 6(sí), 0(sí). Cadena resultante: '3, 9, 6, 0'."
        },
        {
            "num": 10,
            "titulo": "Obtener el primero y el último dígito",
            "enunciado": "Hacer un algoritmo modular para obtener el primer dígito (más significativo) y el último dígito (menos significativo) de un número natural.",
            "entrada": "n : Cardinal (Número natural de entrada).",
            "salida": "var primero, var ultimo : Byte (Devueltos por referencia).",
            "proceso": "1. ultimo := n mod 10. 2. Bucle mientras n >= 10: n := n div 10. 3. Al terminar el bucle, primero := n.",
            "diseno": "procedure PrimerYUltimoDigito(n: Cardinal; var primero, ultimo: Byte); [Procedimiento con parámetros por referencia]",
            "code": '''procedure PrimerYUltimoDigito(n: Cardinal; var primero, ultimo: Byte);
begin
  ultimo := n mod 10;
  while n >= 10 do
    n := n div 10;
  primero := n;
end;''',
            "traza": "N = 74582 -> ultimo = 74582 mod 10 = 2. Reducción: 7458 -> 745 -> 74 -> 7 (< 10). primero = 7."
        },
        {
            "num": 11,
            "titulo": "Eliminar el primero y el último dígito de un número",
            "enunciado": "Eliminar el primer dígito y el último dígito de un número natural N y retornar el número resultante.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "res : Cardinal (Número truncado sin extremos).",
            "proceso": "1. Si n < 100 retornar 0 (no quedan dígitos intermedios). 2. Quitar el último dígito: n := n div 10. 3. Calcular la potencia pot de 10 del primer dígito restante. 4. Quitar primer dígito con n := n mod pot. 5. Retornar n.",
            "diseno": "function EliminarPrimerYUltimoDigito(n: Cardinal): Cardinal; [Función escalar]",
            "code": '''function EliminarPrimerYUltimoDigito(n: Cardinal): Cardinal;
var
  pot: Cardinal;
begin
  if n < 100 then Exit(0);
  n := n div 10;
  pot := 1;
  while (n div pot) >= 10 do
    pot := pot * 10;
  n := n mod pot;
  Result := n;
end;''',
            "traza": "N = 93451 -> Quita último (div 10) => 9345. pot calculada = 1000. 9345 mod 1000 => 345. Resultado = 345."
        },
        {
            "num": 12,
            "titulo": "Invertir número",
            "enunciado": "Dado un número natural N, mostrar dicho número de forma invertida.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "inv : Cardinal (Número invertido).",
            "proceso": "1. Inicializar inv := 0. 2. Mientras n > 0: d := n mod 10; inv := (inv * 10) + d; n := n div 10. 3. Retornar inv.",
            "diseno": "function InvertirNumero(n: Cardinal): Cardinal; [Función de inversión numérica]",
            "code": '''function InvertirNumero(n: Cardinal): Cardinal;
var
  inv: Cardinal;
begin
  inv := 0;
  while n > 0 do
  begin
    inv := (inv * 10) + (n mod 10);
    n := n div 10;
  end;
  Result := inv;
end;''',
            "traza": "N = 4782 -> d=2(inv=2) -> d=8(inv=28) -> d=7(inv=287) -> d=4(inv=2874). Resultado = 2874."
        },
        {
            "num": 13,
            "titulo": "Contar los dígitos múltiplos de cuatro (0, 4, 8)",
            "enunciado": "Hacer un algoritmo para contar cuántos dígitos de un número N son múltiplos de cuatro.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "c : Cardinal (Cantidad de dígitos múltiplos de 4).",
            "proceso": "1. Inicializar c := 0. 2. Mientras n > 0: d := n mod 10; si (d mod 4 = 0) incrementar c; n := n div 10. 3. Retornar c.",
            "diseno": "function ContarMultiplosDeCuatro(n: Cardinal): Cardinal; [Función contadora]",
            "code": '''function ContarMultiplosDeCuatro(n: Cardinal): Cardinal;
var
  d, c: Cardinal;
begin
  c := 0;
  if n = 0 then Exit(1);
  while n > 0 do
  begin
    d := n mod 10;
    if d mod 4 = 0 then Inc(c);
    n := n div 10;
  end;
  Result := c;
end;''',
            "traza": "N = 480124 -> Dígitos evaluados: 4(sí), 2(no), 1(no), 0(sí), 8(sí), 4(sí). Contador = 4."
        },
        {
            "num": 14,
            "titulo": "Dígito menor de los múltiplos de tres",
            "enunciado": "Hacer un algoritmo para mostrar el dígito menor entre los que sean múltiplos de tres (0, 3, 6, 9). Retornar -1 si no tiene.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "menor : Integer (Menor dígito múltiplo de 3 o -1).",
            "proceso": "1. Inicializar menor := 10. 2. Mientras n > 0: d := n mod 10; si (d mod 3 = 0) y (d < menor) entonces menor := d; n := n div 10. 3. Si menor = 10 retornar -1, sino menor.",
            "diseno": "function MenorDigitoMultiploDeTres(n: Cardinal): Integer; [Función con centinela]",
            "code": '''function MenorDigitoMultiploDeTres(n: Cardinal): Integer;
var
  d: Cardinal;
  menor: Integer;
begin
  menor := 10;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) and (Integer(d) < menor) then
      menor := d;
    n := n div 10;
  end;
  if menor = 10 then Result := -1 else Result := menor;
end;''',
            "traza": "N = 79638 -> Múltiplos de 3: {9, 6, 3}. menor inicial=10 -> 3 -> compara con 6 y 9 -> queda en 3. Resultado = 3."
        },
        {
            "num": 15,
            "titulo": "Verificar si un número es capicúa o palíndromo",
            "enunciado": "Hacer un algoritmo para determinar si un número natural N es capicúa (se lee igual al derecho y al revés).",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "Result : Boolean (True si es capicúa, False si no lo es).",
            "proceso": "1. Reutilizar el módulo InvertirNumero(n). 2. Comparar directamente si n = InvertirNumero(n). 3. Retornar el valor booleano.",
            "diseno": "function EsCapicua(n: Cardinal): Boolean; [Función de predicado booleano]",
            "code": '''function EsCapicua(n: Cardinal): Boolean;
begin
  Result := (n = InvertirNumero(n));
end;''',
            "traza": "N = 12321 -> InvertirNumero(12321) = 12321 -> 12321 = 12321 es TRUE."
        },
        {
            "num": 16,
            "titulo": "Convertir de Decimal a Binario",
            "enunciado": "De un número natural N en base 10, obtener su equivalente en sistema binario (base 2).",
            "entrada": "n : Cardinal (Número natural en base 10).",
            "salida": "res : String (Cadena de caracteres con bits 0 y 1).",
            "proceso": "1. Si n = 0 retornar '0'. 2. Mientras n > 0: extraer residuo (n mod 2), anteponerlo a res: res := IntToStr(n mod 2) + res; n := n div 2. 3. Retornar res.",
            "diseno": "function DecimalABinario(n: Cardinal): String; [Función de cambio de base]",
            "code": '''function DecimalABinario(n: Cardinal): String;
var
  res: String;
begin
  if n = 0 then Exit('0');
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 2) + res;
    n := n div 2;
  end;
  Result := res;
end;''',
            "traza": "N = 13 -> 13 mod 2 = 1 (n=6) -> 6 mod 2 = 0 (n=3) -> 3 mod 2 = 1 (n=1) -> 1 mod 2 = 1 (n=0). Resultado: '1101'."
        },
        {
            "num": 17,
            "titulo": "Convertir de Decimal a Hexadecimal",
            "enunciado": "De un número natural N en base 10, obtener su equivalente en sistema hexadecimal (base 16: 0-9, A-F).",
            "entrada": "n : Cardinal (Número decimal).",
            "salida": "res : String (Cadena con representación hexadecimal).",
            "proceso": "1. Definir vector de símbolos HexChars = ['0'..'F']. 2. Mientras n > 0: residuo := n mod 16; anteponer HexChars[residuo] a res; n := n div 16. 3. Retornar res.",
            "diseno": "function DecimalAHexadecimal(n: Cardinal): String; [Función con mapeo de caracteres]",
            "code": '''function DecimalAHexadecimal(n: Cardinal): String;
const
  HexChars: array[0..15] of Char = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F');
var
  res: String;
begin
  if n = 0 then Exit('0');
  res := '';
  while n > 0 do
  begin
    res := HexChars[n mod 16] + res;
    n := n div 16;
  end;
  Result := res;
end;''',
            "traza": "N = 254 -> 254 mod 16 = 14 ('E'), n=15 -> 15 mod 16 = 15 ('F'), n=0. Resultado: 'FE'."
        },
        {
            "num": 18,
            "titulo": "Convertir de Decimal a Octal",
            "enunciado": "De un número natural N, obtener su representación en sistema octal (base 8).",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "res : String (Cadena con dígitos en base 8).",
            "proceso": "1. Si n = 0 retornar '0'. 2. Mientras n > 0: anteponer IntToStr(n mod 8) a res; n := n div 8. 3. Retornar res.",
            "diseno": "function DecimalAOctal(n: Cardinal): String; [Función de cambio de base]",
            "code": '''function DecimalAOctal(n: Cardinal): String;
var
  res: String;
begin
  if n = 0 then Exit('0');
  res := '';
  while n > 0 do
  begin
    res := IntToStr(n mod 8) + res;
    n := n div 8;
  end;
  Result := res;
end;''',
            "traza": "N = 65 -> 65 mod 8 = 1 (n=8) -> 8 mod 8 = 0 (n=1) -> 1 mod 8 = 1 (n=0). Resultado: '101'."
        },
        {
            "num": 19,
            "titulo": "Sumar los dígitos primos (2, 3, 5, 7)",
            "enunciado": "De un número natural N, sumar únicamente los dígitos que sean números primos.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "suma : Cardinal (Suma total de dígitos primos).",
            "proceso": "1. Inicializar suma := 0. 2. Mientras n > 0: d := n mod 10; si EsPrimo(d) sumar a suma; n := n div 10. 3. Retornar suma.",
            "diseno": "function SumaDigitosPrimos(n: Cardinal): Cardinal; [Función con filtro modular]",
            "code": '''function SumaDigitosPrimos(n: Cardinal): Cardinal;
var
  d, suma: Cardinal;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;''',
            "traza": "N = 24783 -> Primos: {3, 7, 2}. suma = 3 + 7 + 2 = 12. Resultado final: 12."
        },
        {
            "num": 20,
            "titulo": "Promedio de los dígitos múltiplos de 3 o 5",
            "enunciado": "De un número natural N, calcular el promedio aritmético de aquellos dígitos que sean múltiplos de 3 o de 5.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "promedio : Double (Promedio real).",
            "proceso": "1. Inicializar suma := 0, cont := 0. 2. Mientras n > 0: d := n mod 10; si (d mod 3 = 0) OR (d mod 5 = 0) sumar d a suma e incrementar cont; n := n div 10. 3. Retornar suma / cont.",
            "diseno": "function PromedioMultiplos3y5(n: Cardinal): Double; [Función con condición lógica OR]",
            "code": '''function PromedioMultiplos3y5(n: Cardinal): Double;
var
  d, suma, cont: Cardinal;
begin
  suma := 0;
  cont := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) or (d mod 5 = 0) then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then Result := suma / cont else Result := 0.0;
end;''',
            "traza": "N = 35681 -> Múltiplos 3 o 5: {6, 5, 3}. Suma = 14, Cant = 3. Promedio = 14 / 3 = 4.67."
        },
        {
            "num": 21,
            "titulo": "Promedio de los dígitos primos",
            "enunciado": "De un número natural N, calcular el promedio de los dígitos primos presentes.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "promedio : Double (Promedio de dígitos primos).",
            "proceso": "1. Inicializar suma := 0, cont := 0. 2. Mientras n > 0: d := n mod 10; si EsPrimo(d) sumar a suma e incrementar cont; n := n div 10. 3. Retornar suma / cont.",
            "diseno": "function PromedioDigitosPrimos(n: Cardinal): Double; [Función escalar real]",
            "code": '''function PromedioDigitosPrimos(n: Cardinal): Double;
var
  d, suma, cont: Cardinal;
begin
  suma := 0;
  cont := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
    begin
      suma := suma + d;
      Inc(cont);
    end;
    n := n div 10;
  end;
  if cont > 0 then Result := suma / cont else Result := 0.0;
end;''',
            "traza": "N = 2738 -> Primos: {3, 7, 2}. Suma = 12, Cont = 3. Promedio = 12 / 3 = 4.00."
        },
        {
            "num": 22,
            "titulo": "Formar otro número con los dígitos primos",
            "enunciado": "De un número natural N, formar un nuevo número compuesto únicamente por los dígitos primos, manteniendo su orden original.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "res : Cardinal (Número con dígitos primos).",
            "proceso": "1. Inicializar res := 0, pot := 1. 2. Mientras n > 0: d := n mod 10; si EsPrimo(d) sumar (d * pot) a res y pot := pot * 10; n := n div 10. 3. Retornar res.",
            "diseno": "function FormarNumeroPrimos(n: Cardinal): Cardinal; [Función con reconstrucción posicional]",
            "code": '''function FormarNumeroPrimos(n: Cardinal): Cardinal;
var
  d, res, pot: Cardinal;
begin
  res := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if EsPrimo(d) then
    begin
      res := res + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  Result := res;
end;''',
            "traza": "N = 427951 -> Primos evaluados: 5 (res=5, pot=10) -> 7 (res=75, pot=100) -> 2 (res=275, pot=1000). Resultado = 275."
        },
        {
            "num": 23,
            "titulo": "Llevar un número decimal a Hexadecimal (Módulo secundario)",
            "enunciado": "Módulo modular para convertir número natural decimal a Hexadecimal.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "res : String (Representación hexadecimal).",
            "proceso": "Invocación directa a la función base DecimalAHexadecimal(n).",
            "diseno": "function DecimalAHexadecimal2(n: Cardinal): String; [Función delegada]",
            "code": '''function DecimalAHexadecimal2(n: Cardinal): String;
begin
  Result := DecimalAHexadecimal(n);
end;''',
            "traza": "N = 4095 -> Invocación -> Salida: 'FFF'."
        },
        {
            "num": 24,
            "titulo": "Llevar un número decimal a Binario (Módulo secundario)",
            "enunciado": "Módulo modular para convertir número natural decimal a Binario.",
            "entrada": "n : Cardinal (Número natural).",
            "salida": "res : String (Representación binaria).",
            "proceso": "Invocación directa a la función base DecimalABinario(n).",
            "diseno": "function DecimalABinario2(n: Cardinal): String; [Función delegada]",
            "code": '''function DecimalABinario2(n: Cardinal): String;
begin
  Result := DecimalABinario(n);
end;''',
            "traza": "N = 35 -> Invocación -> Salida: '100011'."
        },
        {
            "num": 25,
            "titulo": "Convertir un número Octal a Hexadecimal",
            "enunciado": "De un número representado en base Octal (como cadena de texto), convertirlo a su equivalente en sistema Hexadecimal.",
            "entrada": "octalStr : String (Cadena con caracteres octales '0'..'7').",
            "salida": "res : String (Cadena con caracteres hexadecimales '0'..'F').",
            "proceso": "1. Recorrer octalStr de derecha a izquierda acumulando valDec := valDec + (d * pot) con pot := pot * 8. 2. Convertir valDec obtenido a Hexadecimal invocando DecimalAHexadecimal(valDec). 3. Retornar resultado.",
            "diseno": "function OctalAHexadecimal(octalStr: String): String; [Función de conversión compuesta de bases]",
            "code": '''function OctalAHexadecimal(octalStr: String): String;
var
  i, d: Integer;
  valDec, pot: Cardinal;
begin
  valDec := 0;
  pot := 1;
  for i := Length(octalStr) downto 1 do
  begin
    d := Ord(octalStr[i]) - Ord('0');
    valDec := valDec + (Cardinal(d) * pot);
    pot := pot * 8;
  end;
  Result := DecimalAHexadecimal(valDec);
end;''',
            "traza": "octalStr = '752' -> valDec = 2*1 + 5*8 + 7*64 = 2 + 40 + 448 = 490 (decimal). 490 a Hexadecimal: 490 div 16 = 30 (res=10 'A'), 30 div 16 = 1 (res=14 'E'), 1 div 16 = 0 (res=1). Resultado: '1EA'."
        }
    ]

    for ej in ejercicios_completos:
        add_h2(f"Ejercicio #{ej['num']}: {ej['titulo']}")
        add_p(ej['enunciado'], bold_prefix="1. Enunciado: ")
        add_analysis_table(doc, ej['entrada'], ej['salida'], ej['proceso'])
        add_p(ej['diseno'], bold_prefix="2. Diseño Modular: ")
        add_p("3. Implementación en Pascal / Delphi:")
        add_code_block(doc, ej['code'])
        add_p(ej['traza'], bold_prefix="4. Prueba de Escritorio (Traza): ")

    doc.add_page_break()

    # ==================== 4. CONCLUSIONES ====================
    add_h1("4. CONCLUSIONES METODOLÓGICAS")
    add_p("1. La aplicación rigurosa de las 5 fases metodológicas (Enunciado, Análisis E/S/Proceso, Diseño Modular, Implementación y Traza) garantiza la claridad conceptual, la verificación formal del algoritmo y la prevención de errores en tiempo de diseño.")
    add_p("2. El desacoplamiento entre la lógica de negocio (funciones en UnitNumeros) y la capa de presentación (eventos en Unit1 VCL) permite reutilizar el 100% de los algoritmos tanto en interfaces gráficas de escritorio como en programas de consola.")
    add_p("3. Las pruebas de escritorio realizadas confirmaron que la descomposición mediante divisiones enteras sucesivas (mod 10 y div 10) es óptima en consumo de memoria O(1) y complejidad temporal O(log10 N).")

    output_path = "d:\\Introz2\\practico07\\Practico07_Tarea_Delphi.docx"
    doc.save(output_path)
    print(f"Documento completo generado exitosamente en: {output_path}")

if __name__ == "__main__":
    create_full_document()
