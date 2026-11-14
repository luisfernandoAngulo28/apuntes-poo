# -*- coding: utf-8 -*-
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_border(cell, color="CBD5E1", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def add_code_block(doc, code_text, border_color="2563EB"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=80, bottom=80, left=130, right=130)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
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
    p_after.paragraph_format.space_after = Pt(3)

def add_trace_table(doc, headers, rows):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
        set_cell_border(cell, color="1E3A8A", sz="6")
        
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    for row_idx, row_data in enumerate(rows):
        bg = "FFFFFF" if row_idx % 2 == 0 else "F1F5F9"
        for col_idx, val_text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=90, right=90)
            set_cell_border(cell, color="CBD5E1", sz="4")
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(str(val_text))
            r.font.name = "Consolas"
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
            
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(3)

def generate_exam_models_word():
    doc = Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.6)
        s.bottom_margin = Inches(0.6)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Header
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(10)
    title_p.paragraph_format.space_after = Pt(3)
    
    r_uni = title_p.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(13.5)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = title_p.add_run("Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones (FICCT)\nCarrera de Ingeniería Informática / Sistemas • INF110-Z2\n")
    r_fac.font.name = "Calibri"
    r_fac.font.size = Pt(10.5)
    r_fac.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("—" * 50)
    r_line.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
    r_line.font.bold = True

    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_before = Pt(12)
    p_main.paragraph_format.space_after = Pt(4)
    r_title = p_main.add_run("RESOLUCIÓN METODOLÓGICA DE MODELOS DE EXAMEN\nPROGRAMACIÓN MODULAR Y NÚMEROS NATURALES (DELPHI)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(15)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(25)
    r_sub = p_sub.add_run("Ejercicios de Examen Parcial Resueltos (Ponderación 30 Puntos c/u)\nAnálisis • Pseudocódigo • Prueba de Escritorio • Código Delphi • Llamada en Botón")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(8)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        return h

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.bold = True
            r_b.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        p.add_run(text)
        return p

    # ==================== MODELO 1 ====================
    add_h1("MODELO DE EXAMEN #1 (30 Puntos)")
    add_p("Hacer una función para que dado un número natural, obtener el dígito menor impar y el dígito mayor par, mostrar en otro número formado por el menor impar y el mayor par.", bold_prefix="2) Enunciado: ")
    add_p("N = 85239  ->  MenorImpar = 3, MayorPar = 8  ->  MOSTRAR: MenorImpar_MayorPar = 38", bold_prefix="Ejemplo: ")

    add_h2("▼ Análisis del Problema:")
    add_p("numeroNatural : Cardinal (ej. 85239)", bold_prefix="• Entrada: ")
    add_p("1. Inicializar menorImpar := 10 y mayorPar := -1. 2. Mientras numeroNatural > 0: extraer digitoActual := numeroNatural mod 10; si es impar (digitoActual mod 2 <> 0) y digitoActual < menorImpar actualizar menorImpar; si es par (digitoActual mod 2 = 0) y digitoActual > mayorPar actualizar mayorPar; numeroNatural := numeroNatural div 10. 3. Reconstruir: si menorImpar <> 10 y mayorPar <> -1 retornar (menorImpar * 10) + mayorPar.", bold_prefix="• Proceso: ")
    add_p("resultado : Cardinal (Número formado por menor impar a la izquierda y mayor par a la derecha, ej. 38)", bold_prefix="• Salida: ")

    add_h2("Pseudocódigo:")
    code_pseudo_m1 = '''Funcion FormarMenorImparMayorPar(numeroNatural: Entero): Entero
  menorImpar <- 10
  mayorPar   <- -1
  Mientras numeroNatural > 0 Hacer
    digitoActual <- numeroNatural MOD 10
    Si (digitoActual MOD 2 <> 0) Entonces
      Si digitoActual < menorImpar Entonces
        menorImpar <- digitoActual
      FinSi
    Sino
      Si digitoActual > mayorPar Entonces
        mayorPar <- digitoActual
      FinSi
    FinSi
    numeroNatural <- numeroNatural DIV 10
  FinMientras
  
  Si (menorImpar <> 10) Y (mayorPar <> -1) Entonces
    Retornar (menorImpar * 10) + mayorPar
  Sino
    Retornar 0
  FinSi
FinFuncion'''
    add_code_block(doc, code_pseudo_m1, border_color="10B981")

    add_h2("Prueba de Escritorio:")
    headers_m1 = ["numeroNatural", "digitoActual", "¿Es Impar?", "menorImpar", "¿Es Par?", "mayorPar", "n := n div 10"]
    rows_m1 = [
        ["85239", "9", "Sí (9 < 10)", "9", "No", "-1", "8523"],
        ["8523", "3", "Sí (3 < 9)", "3", "No", "-1", "852"],
        ["852", "2", "No", "3", "Sí (2 > -1)", "2", "85"],
        ["85", "5", "Sí (5 > 3)", "3", "No", "2", "8"],
        ["8", "8", "No", "3", "Sí (8 > 2)", "8", "0"]
    ]
    add_trace_table(doc, headers_m1, rows_m1)
    add_p("Reconstrucción final: (3 * 10) + 8 = 38.", bold_prefix="Resultado: ")

    add_h2("Codificación Delphi (Clean Code):")
    code_delphi_m1 = '''function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;
var
  digitoActual: Cardinal;
  menorImpar: Integer;
  mayorPar: Integer;
begin
  menorImpar := 10;
  mayorPar   := -1;
  
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 2 <> 0) then
    begin
      if (Integer(digitoActual) < menorImpar) then
        menorImpar := digitoActual;
    end
    else
    begin
      if (Integer(digitoActual) > mayorPar) then
        mayorPar := digitoActual;
    end;
    numeroNatural := numeroNatural div 10;
  end;
  
  if (menorImpar <> 10) and (mayorPar <> -1) then
    Result := (Cardinal(menorImpar) * 10) + Cardinal(mayorPar)
  else
    Result := 0;
end;'''
    add_code_block(doc, code_delphi_m1)

    add_h2("Llamada en Botón Delphi:")
    code_btn_m1 = '''procedure TForm1.ButtonExamen1Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(FormarMenorImparMayorPar(n));
  ShowMessage('MenorImpar_MayorPar = ' + IntToStr(FormarMenorImparMayorPar(n)));
end;'''
    add_code_block(doc, code_btn_m1, border_color="9333EA")

    doc.add_page_break()

    # ==================== MODELO 2 ====================
    add_h1("MODELO DE EXAMEN #2 (30 Puntos)")
    add_p("Dado un número N natural y una posición K registrado por teclado, eliminar todos los dígitos a partir de dicha posición (contando desde la derecha).", bold_prefix="2) Enunciado: ")
    add_p("N = 78143, Posición K = 3  ->  Resultado = 43", bold_prefix="Ejemplo: ")

    add_h2("▼ Análisis del Problema:")
    add_p("numeroNatural : Cardinal (ej. 78143), posicionK : Byte (ej. 3)", bold_prefix="• Entrada: ")
    add_p("En el número 78143: Posición 1 = '3', Posición 2 = '4', Posición 3 = '1', Posición 4 = '8', Posición 5 = '7'. Al eliminar a partir de la posición 3 inclusive hacia la izquierda, quedan únicamente los dígitos anteriores a K (posiciones 1 y 2 -> '43'). Matemáticamente: se calcula pot := 10^(K-1) y se obtiene el residuo: resultado := numeroNatural mod pot.", bold_prefix="• Proceso: ")
    add_p("resultado : Cardinal (Número resultante truncado, ej. 43)", bold_prefix="• Salida: ")

    add_h2("Pseudocódigo:")
    code_pseudo_m2 = '''Funcion EliminarAPartirDePosicion(numeroNatural: Entero; posicionK: Entero): Entero
  Si posicionK <= 1 Entonces
    Retornar 0
  FinSi
  
  potencia <- 1
  Para i <- 1 Hasta (posicionK - 1) Hacer
    potencia <- potencia * 10
  FinPara
  
  Retornar numeroNatural MOD potencia
FinFuncion'''
    add_code_block(doc, code_pseudo_m2, border_color="10B981")

    add_h2("Prueba de Escritorio:")
    headers_m2 = ["numeroNatural", "posicionK", "i (1 .. K-1)", "potencia := pot * 10", "numeroNatural mod potencia", "Resultado"]
    rows_m2 = [
        ["78143", "3", "i = 1", "pot = 1 * 10 = 10", "-", "-"],
        ["78143", "3", "i = 2", "pot = 10 * 10 = 100", "78143 mod 100 = 43", "43"]
    ]
    add_trace_table(doc, headers_m2, rows_m2)

    add_h2("Codificación Delphi (Clean Code):")
    code_delphi_m2 = '''function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  potencia: Cardinal;
  i: Byte;
begin
  if posicionK <= 1 then
    Exit(0);
    
  potencia := 1;
  for i := 1 to (posicionK - 1) do
    potencia := potencia * 10;
    
  Result := numeroNatural mod potencia;
end;'''
    add_code_block(doc, code_delphi_m2)

    add_h2("Llamada en Botón Delphi con InputBox para K:")
    code_btn_m2 = '''procedure TForm1.ButtonExamen2Click(Sender: TObject);
var
  k: Byte;
begin
  k := StrToInt(InputBox('Posición K', 'Ingrese la posición K a eliminar a partir de ella:', '3'));
  Edit2.Text := IntToStr(EliminarAPartirDePosicion(n, k));
  ShowMessage('Resultado tras eliminar a partir de pos ' + IntToStr(k) + ': ' + IntToStr(EliminarAPartirDePosicion(n, k)));
end;'''
    add_code_block(doc, code_btn_m2, border_color="9333EA")

    doc.add_page_break()

    # ==================== MODELO 3 ====================
    add_h1("MODELO DE EXAMEN #3 (30 Puntos)")
    add_p("Dado un número N natural y una posición K, hacer una función para que elimine únicamente el dígito de dicha posición (contando desde la derecha).", bold_prefix="2) Enunciado: ")
    add_p("N = 78143, K = 2  ->  Resultado = 7813", bold_prefix="Ejemplo: ")

    add_h2("▼ Análisis del Problema:")
    add_p("numeroNatural : Cardinal (ej. 78143), posicionK : Byte (ej. 2)", bold_prefix="• Entrada: ")
    add_p("1. Inicializar numeroResultado := 0, potencia := 1, posicionActual := 1. 2. Mientras numeroNatural > 0: extraer digitoActual := numeroNatural mod 10; si posicionActual <> posicionK entonces acumular numeroResultado := numeroResultado + (digitoActual * potencia) y multiplicar potencia := potencia * 10 (si posicionActual = K, el dígito se omite); incrementar posicionActual := posicionActual + 1; reducir numeroNatural := numeroNatural div 10. 3. Retornar numeroResultado.", bold_prefix="• Proceso: ")
    add_p("numeroResultado : Cardinal (Número sin el dígito de la posición K, ej. 7813)", bold_prefix="• Salida: ")

    add_h2("Pseudocódigo:")
    code_pseudo_m3 = '''Funcion EliminarDigitoEnPosicion(numeroNatural: Entero; posicionK: Entero): Entero
  numeroResultado <- 0
  potencia <- 1
  posicionActual <- 1
  
  Mientras numeroNatural > 0 Hacer
    digitoActual <- numeroNatural MOD 10
    Si posicionActual <> posicionK Entonces
      numeroResultado <- numeroResultado + (digitoActual * potencia)
      potencia <- potencia * 10
    FinSi
    posicionActual <- posicionActual + 1
    numeroNatural <- numeroNatural DIV 10
  FinMientras
  
  Retornar numeroResultado
FinFuncion'''
    add_code_block(doc, code_pseudo_m3, border_color="10B981")

    add_h2("Prueba de Escritorio:")
    headers_m3 = ["numeroNatural", "digitoActual", "posActual", "¿pos <> K (2)?", "numeroResultado", "potencia", "n div 10"]
    rows_m3 = [
        ["78143", "3", "1", "Sí (1 <> 2)", "0 + 3*1 = 3", "10", "7814"],
        ["7814", "4", "2", "NO (Se omite '4')", "3 (sin cambio)", "10 (sin cambio)", "781"],
        ["781", "1", "3", "Sí (3 <> 2)", "3 + 1*10 = 13", "100", "78"],
        ["78", "8", "4", "Sí (4 <> 2)", "13 + 8*100 = 813", "1000", "7"],
        ["7", "7", "5", "Sí (5 <> 2)", "813 + 7*1000 = 7813", "10000", "0"]
    ]
    add_trace_table(doc, headers_m3, rows_m3)
    add_p("Resultado obtenido: 7813 (el dígito '4' en pos 2 fue exitosamente eliminado).", bold_prefix="Resultado: ")

    add_h2("Codificación Delphi (Clean Code):")
    code_delphi_m3 = '''function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  digitoActual: Cardinal;
  numeroResultado, potencia: Cardinal;
  posicionActual: Byte;
begin
  numeroResultado := 0;
  potencia := 1;
  posicionActual := 1;
  
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if posicionActual <> posicionK then
    begin
      numeroResultado := numeroResultado + (digitoActual * potencia);
      potencia := potencia * 10;
    end;
    Inc(posicionActual);
    numeroNatural := numeroNatural div 10;
  end;
  
  Result := numeroResultado;
end;'''
    add_code_block(doc, code_delphi_m3)

    add_h2("Llamada en Botón Delphi con InputBox para K:")
    code_btn_m3 = '''procedure TForm1.ButtonExamen3Click(Sender: TObject);
var
  k: Byte;
begin
  k := StrToInt(InputBox('Eliminar Dígito', 'Ingrese la posición K del dígito a eliminar:', '2'));
  Edit2.Text := IntToStr(EliminarDigitoEnPosicion(n, k));
  ShowMessage('Resultado sin el dígito en pos ' + IntToStr(k) + ': ' + IntToStr(EliminarDigitoEnPosicion(n, k)));
end;'''
    add_code_block(doc, code_btn_m3, border_color="9333EA")

    output_path = "d:\\Introz2\\practico07\\Modelos_De_Examen_Delphi.docx"
    doc.save(output_path)
    print(f"Documento Modelos de Examen guardado en: {output_path}")

if __name__ == '__main__':
    generate_exam_models_word()
