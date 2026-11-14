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

def add_table_grid(doc, headers, rows):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    
    # Headers
    hdr_cells = table.rows[0].cells
    for idx, text in enumerate(headers):
        hdr_cells[idx].text = text
        set_cell_background(hdr_cells[idx], "1E3A8A")
        set_cell_margins(hdr_cells[idx], 50, 50, 80, 80)
        set_cell_border(hdr_cells[idx], "1E3A8A", "6")
        p = hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Arial"
            r.font.bold = True
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
    # Rows
    for r_idx, row_data in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F1F5F9" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], 40, 40, 70, 70)
            set_cell_border(row_cells[c_idx], "CBD5E1", "4")
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Calibri"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    p_spc = doc.add_paragraph()
    p_spc.paragraph_format.space_after = Pt(4)

def generate_master_11_models_docx():
    doc = Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.5)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.65)
        s.right_margin = Inches(0.65)

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(9.5)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(5)
    title_p.paragraph_format.space_after = Pt(2)
    
    r_uni = title_p.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = title_p.add_run("Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones (FICCT)\nINF110-Z2 • Introducción a la Informática / Programación I\n")
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
    p_main.paragraph_format.space_before = Pt(6)
    p_main.paragraph_format.space_after = Pt(3)
    r_title = p_main.add_run("BANCO MAESTRO DE 11 MODELOS DE EXAMEN PARCIAL RESUELTOS\nNÚMEROS NATURALES, LOTES DE NÚMEROS, SERIES Y MODULARIDAD (DELPHI)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(14)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    r_sub = p_sub.add_run("Estructura Metodológica Formal: Análisis E/P/S • Pseudocódigo • Traza • Código Delphi • Llamada VCL")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return h

    def add_h2(text, color="2563EB"):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(5)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(int(color[0:2],16), int(color[2:4],16), int(color[4:6],16))
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

    # --- MODELO 1 ---
    add_h1("MOD 01: Formar Número con Menor Dígito Impar y Mayor Dígito Par (30 Puntos)")
    add_p("Dado un número natural N, extraer todos sus dígitos y formar un nuevo número uniendo su menor dígito impar y su mayor dígito par.", bold_prefix="• Enunciado: ")
    add_p("Entrada: N = 85239 -> MenorImpar = 3, MayorPar = 8 -> Salida: 38", bold_prefix="• Ejemplo: ")
    add_h2("Análisis E/P/S:")
    add_p("• Entrada: numeroNatural (ej: 85239)\n• Proceso: Extraer dígitos con mod 10. Si es impar y menor a menorImpar, actualizar menorImpar. Si es par y mayor a mayorPar, actualizar mayorPar. Al final unir (menorImpar * 10) + mayorPar.\n• Salida: 38")
    add_h2("Pseudocódigo:", "7C3AED")
    code_1_pseudo = '''Funcion FormarMenorImparMayorPar(n: Entero): Entero
  menorImpar <- 10; mayorPar <- -1
  Mientras n > 0 Hacer
    d <- n MOD 10
    Si (d MOD 2 <> 0) Entonces
      Si d < menorImpar Entonces menorImpar <- d FinSi
    Sino
      Si d > mayorPar Entonces mayorPar <- d FinSi
    FinSi
    n <- n DIV 10
  FinMientras
  Si (menorImpar <> 10) Y (mayorPar <> -1) Entonces
    Retornar (menorImpar * 10) + mayorPar
  Sino Retornar 0 FinSi
FinFuncion'''
    add_code_block(doc, code_1_pseudo, "7C3AED")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["n", "d := n mod 10", "¿Es Impar?", "menorImpar", "mayorPar", "n := n div 10"], [
        ["85239", "9", "Sí (impar)", "9", "-1", "8523"],
        ["8523", "3", "Sí (impar)", "3", "-1", "852"],
        ["852", "2", "No (par)", "3", "2", "85"],
        ["85", "5", "Sí (impar)", "3", "2", "8"],
        ["8", "8", "No (par)", "3", "8", "0 (Fin -> 38)"]
    ])
    add_h2("Codificación Delphi (UnitNumeros.pas):", "10B981")
    code_1_delphi = '''function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;
var
  digitoActual: Cardinal;
  menorImpar, mayorPar: Integer;
begin
  menorImpar := 10; mayorPar := -1;
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
  else Result := 0;
end;'''
    add_code_block(doc, code_1_delphi, "10B981")
    add_h2("Llamada en Botón Delphi (Edit / ShowMessage):", "D97706")
    code_1_btn = '''// En el evento OnClick del botón:
Edit2.Text := IntToStr(FormarMenorImparMayorPar(StrToInt(Edit1.Text)));
ShowMessage('Resultado: ' + IntToStr(FormarMenorImparMayorPar(StrToInt(Edit1.Text))));'''
    add_code_block(doc, code_1_btn, "D97706")

    # --- MODELO 2 ---
    add_h1("MOD 02: Eliminar Dígitos a PARTIR de la Posición K (30 Puntos)")
    add_p("Dado un número natural N y una posición K (1 = unidades), eliminar todos los dígitos a partir de dicha posición hacia la izquierda.", bold_prefix="• Enunciado: ")
    add_p("Entrada: N = 78143, K = 3 -> Corta en posición 3 -> Salida: 43", bold_prefix="• Ejemplo: ")
    add_h2("Análisis E/P/S:")
    add_p("• Entrada: numeroNatural = 78143, posicionK = 3\n• Proceso: Los dígitos preservados corresponden a los primeros K-1 dígitos de la derecha. Se calcula mediante la fórmula modular: numeroNatural mod 10^(posicionK - 1).\n• Salida: 43 (78143 mod 100 = 43)")
    add_h2("Pseudocódigo:", "7C3AED")
    code_2_pseudo = '''Funcion EliminarAPartirDePosicion(n: Entero; k: Entero): Entero
  Si k <= 1 Entonces Retornar 0 FinSi
  potencia <- 1
  Para i <- 1 Hasta (k - 1) Con Paso 1 Hacer
    potencia <- potencia * 10
  FinPara
  Retornar n MOD potencia
FinFuncion'''
    add_code_block(doc, code_2_pseudo, "7C3AED")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["n", "k", "i (bucle)", "potencia := potencia * 10", "Resultado := n mod potencia"], [
        ["78143", "3", "1", "10", "-"],
        ["78143", "3", "2", "100", "78143 mod 100 = 43"]
    ])
    add_h2("Codificación Delphi (UnitNumeros.pas):", "10B981")
    code_2_delphi = '''function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  potencia: Cardinal;
  i: Byte;
begin
  if posicionK <= 1 then Exit(0);
  potencia := 1;
  for i := 1 to (posicionK - 1) do potencia := potencia * 10;
  Result := numeroNatural mod potencia;
end;'''
    add_code_block(doc, code_2_delphi, "10B981")

    # --- MODELO 3 ---
    add_h1("MOD 03: Eliminar Únicamente el Dígito de la Posición K (30 Puntos)")
    add_p("Eliminar el dígito ubicado exactamente en la posición K, preservando todos los demás dígitos en su posición y orden original.", bold_prefix="• Enunciado: ")
    add_p("Entrada: N = 78143, K = 2 -> Elimina el dígito '4' de la posición 2 -> Salida: 7813", bold_prefix="• Ejemplo: ")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["n", "pos", "d := n mod 10", "¿pos <> k (2)?", "res := res + d*pot", "pot", "n div 10"], [
        ["78143", "1", "3", "Sí (1 <> 2)", "3", "10", "7814"],
        ["7814", "2", "4", "No (Se salta)", "3", "10", "781"],
        ["781", "3", "1", "Sí (3 <> 2)", "13", "100", "78"],
        ["78", "4", "8", "Sí (4 <> 2)", "813", "1000", "7"],
        ["7", "5", "7", "Sí (5 <> 2)", "7813", "10000", "0 (Fin -> 7813)"]
    ])
    add_h2("Codificación Delphi (UnitNumeros.pas):", "10B981")
    code_3_delphi = '''function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  digitoActual, numeroResultado, potencia: Cardinal;
  posicionActual: Byte;
begin
  numeroResultado := 0; potencia := 1; posicionActual := 1;
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
    add_code_block(doc, code_3_delphi, "10B981")

    # --- MODELO 4 ---
    add_h1("MOD 04: Promedio de Pares y Promedio de Impares en un solo Procedimiento")
    add_p("N = 12345 -> Promedio Pares = (2+4)/2 = 3.0 | Promedio Impares = (1+3+5)/3 = 3.0", bold_prefix="• Enunciado y Ejemplo: ")
    add_h2("Codificación Delphi (UnitNumeros.pas):", "10B981")
    code_4_delphi = '''procedure PromedioParesImpares(numeroNatural: Cardinal; var promPares, promImpares: Double);
var
  digitoActual: Cardinal;
  sumaPares, cantPares, sumaImpares, cantImpares: Cardinal;
begin
  sumaPares := 0; cantPares := 0; sumaImpares := 0; cantImpares := 0;
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
    add_code_block(doc, code_4_delphi, "10B981")

    # --- MODELO 5 ---
    add_h1("MOD 05: Mayor Dígito de los Múltiplos de 3")
    add_p("N = 8326 -> Múltiplos de 3: {3, 6} -> Mayor = 6", bold_prefix="• Enunciado y Ejemplo: ")
    code_5_delphi = '''function MayorDigitoMultiploDe3(numeroNatural: Cardinal): Integer;
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
    add_code_block(doc, code_5_delphi, "10B981")

    # --- MODELO 6 ---
    add_h1("MOD 06: Sumar Dígitos Hasta que Sea Menor a 10 / Raíz Digital (10 Puntos)")
    add_p("Dado un número natural N, sumar sus dígitos sucesivamente hasta que el resultado sea menor a 10.", bold_prefix="• Enunciado: ")
    add_p("N = 15378 -> (1+5+3+7+8 = 24) -> (2+4 = 6) -> Salida: 6", bold_prefix="• Ejemplo: ")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["Iteración", "n Inicial", "Suma de Dígitos", "¿n >= 10?", "Nuevo n"], [
        ["1", "15378", "1+5+3+7+8 = 24", "Sí (24 >= 10)", "24"],
        ["2", "24", "2+4 = 6", "No (6 < 10) -> Fin", "6"]
    ])
    code_6_delphi = '''function SumarHastaMenorA10(numeroNatural: Cardinal): Byte;
var
  suma, temp: Cardinal;
begin
  while numeroNatural >= 10 do
  begin
    suma := 0; temp := numeroNatural;
    while temp > 0 do
    begin
      suma := suma + (temp mod 10);
      temp := temp div 10;
    end;
    numeroNatural := suma;
  end;
  Result := numeroNatural;
end;'''
    add_code_block(doc, code_6_delphi, "10B981")

    # --- MODELO 7 ---
    add_h1("MOD 07: Promedio de la Serie Dual S = 4+2+8+6+12+18... (n términos)")
    add_p("Para n = 4: S = (4 + 2 + 8 + 6) / 4 = 20 / 4 = 5.0", bold_prefix="• Enunciado y Ejemplo: ")
    code_7_delphi = '''function PromedioSerieDual(cantidadTerminos: Cardinal): Double;
var
  i, terminoImpar, terminoPar, terminoActual: Cardinal;
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
      terminoActual := terminoImpar; terminoImpar := terminoImpar + 4;
    end
    else
    begin
      terminoActual := terminoPar; terminoPar := terminoPar * 3;
    end;
    sumaTotal := sumaTotal + terminoActual;
  end;
  Result := sumaTotal / cantidadTerminos;
end;'''
    add_code_block(doc, code_7_delphi, "10B981")

    # --- MODELO 8 ---
    add_h1("MOD 08: Sumar Dígitos de Cada Número y Acumular las Sumas Impares (10 Puntos)")
    add_p("Hacer una función para sumar los dígitos de cada número y mostrar la sumatoria acumulada de aquellas sumas que resulten ser impares.", bold_prefix="• Enunciado: ")
    add_p("Si n=5, {123, 25, 281, 94, 46} -> Sumas: 6, 7 (impar), 11 (impar), 13 (impar), 10 -> SumaNumeroImpar = 7+11+13 = 31", bold_prefix="• Ejemplo: ")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["Número", "Suma de Dígitos", "¿Suma es Impar?", "sumaTotalImpares"], [
        ["123", "1+2+3 = 6", "No (par)", "0"],
        ["25", "2+5 = 7", "Sí (7 es impar)", "7"],
        ["281", "2+8+1 = 11", "Sí (11 es impar)", "18"],
        ["94", "9+4 = 13", "Sí (13 es impar)", "31"],
        ["46", "4+6 = 10", "No (par)", "31"]
    ])
    code_8_delphi = '''function SumaDigitosImparesDeLote(const listaNumeros: array of Cardinal): Cardinal;
var
  i: Integer;
  numActual, temp, sumaDigitos, sumaTotalImpares: Cardinal;
begin
  sumaTotalImpares := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    sumaDigitos := 0;
    temp := numActual;
    while temp > 0 do
    begin
      sumaDigitos := sumaDigitos + (temp mod 10);
      temp := temp div 10;
    end;
    if (sumaDigitos mod 2 <> 0) then
      sumaTotalImpares := sumaTotalImpares + sumaDigitos;
  end;
  Result := sumaTotalImpares;
end;'''
    add_code_block(doc, code_8_delphi, "10B981")

    # --- MODELO 9 ---
    add_h1("MOD 09: Separar Dígitos Menores a 6 y Mayores o Iguales a 6 (10 Puntos)")
    add_p("Dado un número natural, separar los dígitos menores a 6 en un número y los mayores o iguales a 6 en otro número.", bold_prefix="• Enunciado: ")
    add_p("Entrada: 16327 -> < 6: 231 | >= 6: 76", bold_prefix="• Ejemplo: ")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["n", "d := n mod 10", "¿d < 6?", "numMenores6", "numMayores6", "n div 10"], [
        ["16327", "7", "No (7 >= 6)", "0", "7", "1632"],
        ["1632", "2", "Sí (2 < 6)", "2", "7", "163"],
        ["163", "3", "Sí (3 < 6)", "23", "7", "16"],
        ["16", "6", "No (6 >= 6)", "23", "76", "1"],
        ["1", "1", "Sí (1 < 6)", "231", "76", "0 (Fin)"]
    ])
    code_9_delphi = '''procedure SepararMenoresYMayores6(numeroNatural: Cardinal; var numMenores6, numMayores6: Cardinal);
var
  digitoActual: Cardinal;
begin
  numMenores6 := 0; numMayores6 := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual < 6 then
      numMenores6 := (numMenores6 * 10) + digitoActual
    else
      numMayores6 := (numMayores6 * 10) + digitoActual;
    numeroNatural := numeroNatural div 10;
  end;
end;'''
    add_code_block(doc, code_9_delphi, "10B981")

    # --- MODELO 10 ---
    add_h1("MOD 10: Promedio de Números Ascendentes en Rango [100-200] (10 Puntos)")
    add_p("Introducir n números por teclado y mostrar el promedio de aquellos números que llegan de forma ascendente dentro del rango [100-200].", bold_prefix="• Enunciado: ")
    add_p("Si n=5, números = 211, 120, 50, 180, 200 -> Válidos: 120, 180, 200 -> Promedio = (120+180+200)/3 = 166.66", bold_prefix="• Ejemplo: ")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["Entrada", "¿En [100, 200]?", "¿Mayor al Anterior Válido?", "sumaValidos", "cantValidos", "ultimoValido"], [
        ["211", "No (> 200)", "-", "0", "0", "0"],
        ["120", "Sí (120)", "Sí (120 > 0)", "120", "1", "120"],
        ["50", "No (< 100)", "-", "120", "1", "120"],
        ["180", "Sí (180)", "Sí (180 > 120)", "300", "2", "180"],
        ["200", "Sí (200)", "Sí (200 > 180)", "500", "3 -> 500/3 = 166.66", "200"]
    ])
    code_10_delphi = '''function PromedioAscendentesRango100_200(const listaNumeros: array of Cardinal): Double;
var
  i: Integer;
  numActual, ultimoValido, sumaValidos, cantValidos: Cardinal;
begin
  sumaValidos := 0; cantValidos := 0; ultimoValido := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    if (numActual >= 100) and (numActual <= 200) and (numActual > ultimoValido) then
    begin
      sumaValidos := sumaValidos + numActual;
      Inc(cantValidos);
      ultimoValido := numActual;
    end;
  end;
  if cantValidos > 0 then Result := sumaValidos / cantValidos else Result := 0.0;
end;'''
    add_code_block(doc, code_10_delphi, "10B981")

    # --- MODELO 11 ---
    add_h1("MOD 11: Sumatoria Global de Dígitos Primos en Lote (Pizarra)")
    add_p("Dado N números naturales, verificar si existen dígitos primos (2, 3, 5, 7) en cada uno y realizar la sumatoria acumulada total.", bold_prefix="• Enunciado: ")
    add_p("N = 4, Números: 123 (2+3=5), 249 (2), 729 (7+2=9), 562 (5+2=7) -> SN = 5 + 2 + 9 + 7 = 23", bold_prefix="• Ejemplo: ")
    add_h2("Prueba de Escritorio:", "0284C7")
    add_table_grid(doc, ["Número", "Dígitos Primos Detectados", "Suma de Primos del Número", "Suma Total Acumulada (SN)"], [
        ["123", "'2', '3'", "2 + 3 = 5", "5"],
        ["249", "'2'", "2", "7"],
        ["729", "'7', '2'", "7 + 2 = 9", "16"],
        ["562", "'5', '2'", "5 + 2 = 7", "23"]
    ])
    code_11_delphi = '''function SumatoriaPrimosDeLote(const listaNumeros: array of Cardinal): Cardinal;
var
  i: Integer;
  numActual, digito, temp, sumaTotalPrimos: Cardinal;
begin
  sumaTotalPrimos := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    temp := numActual;
    while temp > 0 do
    begin
      digito := temp mod 10;
      if (digito = 2) or (digito = 3) or (digito = 5) or (digito = 7) then
        sumaTotalPrimos := sumaTotalPrimos + digito;
      temp := temp div 10;
    end;
  end;
  Result := sumaTotalPrimos;
end;'''
    add_code_block(doc, code_11_delphi, "10B981")

    output_path = "d:\\Introz2\\practico07\\Modelos_De_Examen_Delphi.docx"
    doc.save(output_path)
    print(f"Documento Maestro de 11 Modelos de Examen guardado exitosamente en: {output_path}")

if __name__ == '__main__':
    generate_master_11_models_docx()
