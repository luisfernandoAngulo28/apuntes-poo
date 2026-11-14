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

def generate_10_exam_models_docx():
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
    r_title = p_main.add_run("BANCO MAESTRO DE 10 MODELOS DE EXAMEN PARCIAL RESUELTOS\nNÚMEROS NATURALES, LOTES DE NÚMEROS, SERIES Y MODULARIDAD (DELPHI)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(14)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    r_sub = p_sub.add_run("Resolución Completa con Clean Code, Análisis, Pseudocódigo, Trazas y Eventos en Delphi")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(11)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(5)
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

    # --- MODELO 1 ---
    add_h1("MODELO 1: Menor Impar y Mayor Par en un Solo Número (30 Puntos)")
    add_p("N = 85239 -> MenorImpar = 3, MayorPar = 8 -> Resultado: 38", bold_prefix="• Enunciado y Ejemplo: ")
    code_1 = '''function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;
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
    add_code_block(doc, code_1)

    # --- MODELO 2 ---
    add_h1("MODELO 2: Eliminar a PARTIR de la Posición K (30 Puntos)")
    add_p("N = 78143, K = 3 -> Resultado: 43", bold_prefix="• Enunciado y Ejemplo: ")
    code_2 = '''function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  potencia: Cardinal;
  i: Byte;
begin
  if posicionK <= 1 then Exit(0);
  potencia := 1;
  for i := 1 to (posicionK - 1) do potencia := potencia * 10;
  Result := numeroNatural mod potencia;
end;'''
    add_code_block(doc, code_2)

    # --- MODELO 3 ---
    add_h1("MODELO 3: Eliminar Únicamente el Dígito de la Posición K (30 Puntos)")
    add_p("N = 78143, K = 2 -> Resultado: 7813", bold_prefix="• Enunciado y Ejemplo: ")
    code_3 = '''function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
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
    add_code_block(doc, code_3)

    # --- MODELO 4 ---
    add_h1("MODELO 4: Promedio de Pares y Promedio de Impares (Pizarra)")
    add_p("N = 12345 -> PromPar = (2+4)/2 = 3.0 | PromImpar = (1+3+5)/3 = 3.0", bold_prefix="• Enunciado y Ejemplo: ")
    code_4 = '''procedure PromedioParesImpares(numeroNatural: Cardinal; var promPares, promImpares: Double);
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
    add_code_block(doc, code_4, border_color="F59E0B")

    # --- MODELO 5 ---
    add_h1("MODELO 5: Mayor Dígito de los Múltiplos de 3")
    add_p("N = 8326 -> Múltiplos de 3: {3, 6} -> Mayor = 6", bold_prefix="• Enunciado y Ejemplo: ")
    code_5 = '''function MayorDigitoMultiploDe3(numeroNatural: Cardinal): Integer;
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
    add_code_block(doc, code_5)

    # --- MODELO 6 ---
    add_h1("MODELO 6: Sumar Dígitos Hasta que Sea Menor a 10 (Raíz Digital)")
    add_p("N = 15378 -> (1+5+3+7+8 = 24) -> (2+4 = 6) -> Resultado final = 6", bold_prefix="• Enunciado y Ejemplo: ")
    code_6 = '''function SumarHastaMenorA10(numeroNatural: Cardinal): Byte;
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
    add_code_block(doc, code_6, border_color="9333EA")

    # --- MODELO 7 ---
    add_h1("MODELO 7: Promedio de la Serie Mixta Dual (4+2+8+6+12+18...)")
    add_p("Para N = 4: S = (4 + 2 + 8 + 6) / 4 = 20 / 4 = 5.0", bold_prefix="• Enunciado y Ejemplo: ")
    code_7 = '''function PromedioSerieDual(cantidadTerminos: Cardinal): Double;
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
    add_code_block(doc, code_7, border_color="10B981")

    # --- MODELO 8 (NUEVO) ---
    add_h1("MODELO 8: Sumar Sumas de Dígitos que Resulten Impares en N Números (10p)")
    add_p("Hacer una función para sumar los dígitos de cada número y acumular la suma de aquellos que resulten ser impares.", bold_prefix="• Enunciado: ")
    add_p("Si n = 5  {123, 25, 281, 94, 46} -> Sumas: 6, 7 (impar), 11 (impar), 13 (impar), 10 -> SumaNumeroImpar = 7 + 11 + 13 = 31", bold_prefix="• Ejemplo: ")
    add_h2("Análisis y Algoritmo:")
    add_p("Por cada número ingresado, se calculan sus dígitos con mod 10 y div 10; si la suma resultante es impar (suma mod 2 <> 0), se acumula en el total global.")
    code_8 = '''// Función que procesa un arreglo o lote de n números naturales:
function SumaDigitosImparesDeLote(const listaNumeros: array of Cardinal): Cardinal;
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
    
    // Si la suma de sus dígitos resultó ser impar:
    if (sumaDigitos mod 2 <> 0) then
      sumaTotalImpares := sumaTotalImpares + sumaDigitos;
  end;
  Result := sumaTotalImpares;
end;'''
    add_code_block(doc, code_8, border_color="F59E0B")

    # --- MODELO 9 (NUEVO) ---
    add_h1("MODELO 9: Separar Dígitos Menores a 6 y Mayores o Iguales a 6 (10p)")
    add_p("Dado un número natural, separar los dígitos menores a 6 en un número y los mayores o iguales a 6 en otro número.", bold_prefix="• Enunciado: ")
    add_p("Entrada = 16327 -> < 6: Resultado = 231 (o 132) | >= 6: Resultado = 76 (o 67)", bold_prefix="• Ejemplo: ")
    code_9 = '''procedure SepararMenoresYMayores6(numeroNatural: Cardinal; var numMenores6, numMayores6: Cardinal);
var
  digitoActual: Cardinal;
begin
  numMenores6 := 0;
  numMayores6 := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual < 6 then
      numMenores6 := (numMenores6 * 10) + digitoActual // Formato inverso de pizarra: 231
    else
      numMayores6 := (numMayores6 * 10) + digitoActual; // Formato inverso de pizarra: 76
    numeroNatural := numeroNatural div 10;
  end;
end;'''
    add_code_block(doc, code_9, border_color="9333EA")

    # --- MODELO 10 (NUEVO) ---
    add_h1("MODELO 10: Promedio de Números Ascendentes en Rango [100-200] (10p)")
    add_p("Introducir n números por teclado y mostrar el promedio de aquellos números que llegan de forma ascendente dentro del rango [100-200].", bold_prefix="• Enunciado: ")
    add_p("Si n = 5, números = 211, 120, 50, 180, 200 -> Válidos ascendentes: 120, 180, 200 -> Promedio = (120+180+200)/3 = 500/3 = 166.66", bold_prefix="• Ejemplo: ")
    code_10 = '''function PromedioAscendentesRango100_200(const listaNumeros: array of Cardinal): Double;
var
  i: Integer;
  numActual, ultimoValido, sumaValidos, cantValidos: Cardinal;
begin
  sumaValidos := 0;
  cantValidos := 0;
  ultimoValido := 0;
  
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    // Verificar que esté en el rango [100, 200] y que sea estrictamente mayor al anterior válido
    if (numActual >= 100) and (numActual <= 200) and (numActual > ultimoValido) then
    begin
      sumaValidos := sumaValidos + numActual;
      Inc(cantValidos);
      ultimoValido := numActual;
    end;
  end;
  
  if cantValidos > 0 then
    Result := sumaValidos / cantValidos
  else
    Result := 0.0;
end;'''
    add_code_block(doc, code_10, border_color="10B981")

    # --- MODELO 11 (NUEVO PIZARRA) ---
    add_h1("MODELO 11: Sumatoria Global de Dígitos Primos en N Números (Pizarra)")
    add_p("Dado N números naturales, verificar si existen dígitos primos y realizar la sumatoria acumulada total.", bold_prefix="• Enunciado: ")
    add_p("N = 4, Números: 123 (primos 2+3=5), 249 (primo 2), 729 (primos 7+2=9), 562 (primos 5+2=7) -> SN = 5 + 2 + 9 + 7 = 23", bold_prefix="• Ejemplo: ")
    code_11 = '''function SumatoriaPrimosDeLote(const listaNumeros: array of Cardinal): Cardinal;
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
    add_code_block(doc, code_11, border_color="38BDF8")

    output_path = "d:\\Introz2\\practico07\\Modelos_De_Examen_Delphi.docx"
    doc.save(output_path)
    print(f"Documento Maestro de 10 Modelos de Examen guardado exitosamente en: {output_path}")

if __name__ == '__main__':
    generate_10_exam_models_docx()
