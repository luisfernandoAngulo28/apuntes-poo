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

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
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

def generate_all_exam_models_docx():
    doc = Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.55)
        s.bottom_margin = Inches(0.55)
        s.left_margin = Inches(0.7)
        s.right_margin = Inches(0.7)

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(5)
    title_p.paragraph_format.space_after = Pt(3)
    
    r_uni = title_p.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(13.5)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = title_p.add_run("Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones (FICCT)\nCarrera de Ingeniería Informática / Sistemas • INF110-Z2\n")
    r_fac.font.name = "Calibri"
    r_fac.font.size = Pt(10)
    r_fac.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("—" * 55)
    r_line.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
    r_line.font.bold = True

    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_before = Pt(8)
    p_main.paragraph_format.space_after = Pt(4)
    r_title = p_main.add_run("BANCO COMPLETO DE MODELOS DE EXAMEN PARCIAL RESUELTOS\nNÚMEROS NATURALES, SERIES Y MODULARIDAD (DELPHI)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(14)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(18)
    r_sub = p_sub.add_run("Resolución Metodológica Paso a Paso: Análisis • Pseudocódigo • Trazas • Delphi Clean Code")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(6)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
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
    add_h1("MODELO 1: Menor Impar y Mayor Par en un Solo Número (30 Puntos)")
    add_p("Hacer una función para que dado un número natural, obtener el dígito menor impar y el dígito mayor par, mostrar en otro número formado por el menor impar y el mayor par.", bold_prefix="• Enunciado: ")
    add_p("N = 85239  ->  MenorImpar = 3, MayorPar = 8  ->  MOSTRAR: MenorImpar_MayorPar = 38", bold_prefix="• Ejemplo: ")
    add_h2("Análisis:")
    add_p("numeroNatural : Cardinal | Salida: Cardinal | Proceso: Inicializar menorImpar:=10, mayorPar:=-1. Recorrer con mod 10 y div 10; retornar (menorImpar * 10) + mayorPar.")
    add_h2("Codificación Delphi:")
    code_m1 = '''function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;
var
  digitoActual: Cardinal;
  menorImpar, mayorPar: Integer;
begin
  menorImpar := 10;
  mayorPar   := -1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 2 <> 0) then
    begin
      if Integer(digitoActual) < menorImpar then menorImpar := digitoActual;
    end
    else
    begin
      if Integer(digitoActual) > mayorPar then mayorPar := digitoActual;
    end;
    numeroNatural := numeroNatural div 10;
  end;
  if (menorImpar <> 10) and (mayorPar <> -1) then
    Result := (Cardinal(menorImpar) * 10) + Cardinal(mayorPar)
  else
    Result := 0;
end;'''
    add_code_block(doc, code_m1)

    # ==================== MODELO 2 ====================
    add_h1("MODELO 2: Eliminar a PARTIR de la Posición K (30 Puntos)")
    add_p("Dado un número N natural y una posición K registrado por teclado, eliminar todos los dígitos a partir de dicha posición (desde la derecha).", bold_prefix="• Enunciado: ")
    add_p("N = 78143, Posición K = 3  ->  Resultado = 43", bold_prefix="• Ejemplo: ")
    add_h2("Análisis:")
    add_p("numeroNatural : Cardinal, posicionK : Byte | Salida: Cardinal | Proceso: Calcular potencia := 10^(posicionK - 1) y retornar numeroNatural mod potencia.")
    add_h2("Codificación Delphi:")
    code_m2 = '''function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  potencia: Cardinal;
  i: Byte;
begin
  if posicionK <= 1 then Exit(0);
  potencia := 1;
  for i := 1 to (posicionK - 1) do
    potencia := potencia * 10;
  Result := numeroNatural mod potencia;
end;'''
    add_code_block(doc, code_m2)

    # ==================== MODELO 3 ====================
    add_h1("MODELO 3: Eliminar Únicamente el Dígito de la Posición K (30 Puntos)")
    add_p("Dado un número N natural y una posición K, hacer una función para que elimine el dígito de dicha posición.", bold_prefix="• Enunciado: ")
    add_p("N = 78143, K = 2  ->  Resultado = 7813", bold_prefix="• Ejemplo: ")
    add_h2("Análisis:")
    add_p("numeroNatural : Cardinal, posicionK : Byte | Salida: Cardinal | Proceso: Recorrer con mod 10 y posActual:=1; si posActual <> K acumular en res con pot:=pot*10; si posActual = K omitir dígito.")
    add_h2("Codificación Delphi:")
    code_m3 = '''function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  digitoActual, numeroResultado, potencia: Cardinal;
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
    add_code_block(doc, code_m3)

    # ==================== MODELO 4 ====================
    add_h1("MODELO 4: Promedio de Pares y Promedio de Impares (Pizarra Examen)")
    add_p("Dado un número natural, hacer un módulo para obtener el promedio de dígitos pares y el promedio de dígitos impares.", bold_prefix="• Enunciado: ")
    add_p("N = 12345 -> SumaPar = 2+4=6, CantPar=2 -> PromPar = 6/2 = 3.0 | SumaImpar = 1+3+5=9, CantImpar=3 -> PromImpar = 9/3 = 3.0", bold_prefix="• Ejemplo: ")
    add_h2("Análisis:")
    add_p("Al requerir DOS valores resultantes (promedio de pares y promedio de impares), se implementa mediante un Procedimiento con parámetros por referencia (var).")
    add_h2("Codificación Delphi:")
    code_m4 = '''procedure PromedioParesImpares(numeroNatural: Cardinal; var promPares, promImpares: Double);
var
  digitoActual: Cardinal;
  sumaPares, cantPares: Cardinal;
  sumaImpares, cantImpares: Cardinal;
begin
  sumaPares := 0;   cantPares := 0;
  sumaImpares := 0; cantImpares := 0;
  
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual mod 2 = 0 then
    begin
      sumaPares := sumaPares + digitoActual;
      Inc(cantPares);
    end
    else
    begin
      sumaImpares := sumaImpares + digitoActual;
      Inc(cantImpares);
    end;
    numeroNatural := numeroNatural div 10;
  end;
  
  if cantPares > 0 then promPares := sumaPares / cantPares else promPares := 0.0;
  if cantImpares > 0 then promImpares := sumaImpares / cantImpares else promImpares := 0.0;
end;'''
    add_code_block(doc, code_m4, border_color="F59E0B")

    # ==================== MODELO 5 ====================
    add_h1("MODELO 5: Dígito Mayor de los Múltiplos de 3")
    add_p("Dado un número natural, mostrar el dígito mayor entre los que son múltiplos de 3 (3, 6, 9). Retornar -1 si no tiene.", bold_prefix="• Enunciado: ")
    add_p("N = 8326 -> Múltiplos de 3: {3, 6} -> Mayor = 6", bold_prefix="• Ejemplo: ")
    add_h2("Codificación Delphi:")
    code_m5 = '''function MayorDigitoMultiploDe3(numeroNatural: Cardinal): Integer;
var
  digitoActual: Cardinal;
  mayor: Integer;
begin
  mayor := -1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 3 = 0) and (Integer(digitoActual) > mayor) then
      mayor := digitoActual;
    numeroNatural := numeroNatural div 10;
  end;
  Result := mayor;
end;'''
    add_code_block(doc, code_m5)

    # ==================== MODELO 6 ====================
    add_h1("MODELO 6: Sumar Dígitos Hasta que Sea Menor a 10 (Raíz Digital)")
    add_p("Dado un número natural N, sumar sus dígitos sucesivamente hasta que el resultado final sea estrictamente menor a 10.", bold_prefix="• Enunciado: ")
    add_p("N = 15378 -> (1+5+3+7+8 = 24) -> (2+4 = 6) -> Resultado final = 6", bold_prefix="• Ejemplo: ")
    add_h2("Análisis:")
    add_p("Bucle anidado: Mientras numeroNatural >= 10, calcular la suma de sus dígitos con mod 10 y reasignar numeroNatural := suma; repetir hasta que quede 1 solo dígito.")
    add_h2("Codificación Delphi:")
    code_m6 = '''function SumarHastaMenorA10(numeroNatural: Cardinal): Byte;
var
  suma, temp: Cardinal;
begin
  while numeroNatural >= 10 do
  begin
    suma := 0;
    temp := numeroNatural;
    while temp > 0 do
    begin
      suma := suma + (temp mod 10);
      temp := temp div 10;
    end;
    numeroNatural := suma;
  end;
  Result := numeroNatural;
end;'''
    add_code_block(doc, code_m6, border_color="9333EA")

    # ==================== MODELO 7 ====================
    add_h1("MODELO 7: Serie Mixta Dual y Promedio de N Términos")
    add_p("Generar los N términos de la serie mixta y mostrar el promedio de dicha serie:\nS = 4 + 2 + 8 + 6 + 12 + 18 + 16 + 54 + 20 + 162 + ...", bold_prefix="• Enunciado: ")
    add_p("Para N = 4: Términos = {4, 2, 8, 6} -> Suma = 4+2+8+6 = 20 -> Promedio = 20 / 4 = 5.0", bold_prefix="• Ejemplo: ")
    add_h2("Análisis de la Serie:")
    add_p("• Posiciones Impares (1, 3, 5, 7...): Progresión aritmética con razón +4 (4, 8, 12, 16, 20...).\n• Posiciones Pares (2, 4, 6, 8...): Progresión geométrica con razón *3 (2, 6, 18, 54, 162...).")
    add_h2("Codificación Delphi:")
    code_m7 = '''function PromedioSerieDual(cantidadTerminos: Cardinal): Double;
var
  i: Cardinal;
  terminoImpar, terminoPar, terminoActual: Cardinal;
  sumaTotal: Double;
begin
  if cantidadTerminos = 0 then Exit(0.0);
  
  terminoImpar := 4; // Razón +4
  terminoPar   := 2; // Razón *3
  sumaTotal    := 0.0;
  
  for i := 1 to cantidadTerminos do
  begin
    if (i mod 2 <> 0) then
    begin
      terminoActual := terminoImpar;
      terminoImpar := terminoImpar + 4;
    end
    else
    begin
      terminoActual := terminoPar;
      terminoPar := terminoPar * 3;
    end;
    sumaTotal := sumaTotal + terminoActual;
  end;
  
  Result := sumaTotal / cantidadTerminos;
end;'''
    add_code_block(doc, code_m7, border_color="10B981")

    output_path = "d:\\Introz2\\practico07\\Modelos_De_Examen_Delphi.docx"
    doc.save(output_path)
    print(f"Documento Modelos de Examen completo generado en: {output_path}")

if __name__ == '__main__':
    generate_all_exam_models_docx()
