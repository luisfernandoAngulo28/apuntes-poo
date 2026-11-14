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

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
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
    set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
    
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
    p_after.paragraph_format.space_after = Pt(2)

def add_trace_table(doc, headers, rows):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    
    # Headers
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        set_cell_border(cell, color="1E3A8A", sz="6")
        
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    # Rows
    for row_idx, row_data in enumerate(rows):
        bg = "FFFFFF" if row_idx % 2 == 0 else "F1F5F9"
        for col_idx, val_text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
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
    p_after.paragraph_format.space_after = Pt(4)

def build_tarea_clase_word():
    doc = Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # ==================== PORTADA ====================
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(15)
    title_p.paragraph_format.space_after = Pt(4)
    
    r_uni = title_p.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(14)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = title_p.add_run("Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones\n")
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
    p_main.paragraph_format.space_before = Pt(14)
    p_main.paragraph_format.space_after = Pt(6)
    r_title = p_main.add_run("TAREA DE CLASE: NÚMEROS NATURALES EN DELPHI\n(ANÁLISIS, PSEUDOCÓDIGO, TRAZA Y CÓDIGO)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(25)
    r_sub = p_sub.add_run("Formulario VCL: Cargar, SumarDigitosPrimos, SoloPares, SumarMultiplosDe3 e InvertirNumero")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    info_table = doc.add_table(rows=4, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Materia:", "Introducción a la Informática / Programación I"),
        ("Docente:", "Ingeniera Docente de la Materia"),
        ("Tema:", "Tratamiento y Descomposición de Dígitos en Delphi (VCL)"),
        ("Estructura:", "Análisis • Pseudocódigo • Traza • Código Delphi • Llamada en Botón")
    ]
    for row_idx, (label, val) in enumerate(info_data):
        cell_lbl = info_table.cell(row_idx, 0)
        cell_val = info_table.cell(row_idx, 1)
        cell_lbl.width = Inches(1.8)
        cell_val.width = Inches(4.7)
        
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

    # Helpers
    def add_ej_header(title):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(title)
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    def add_section_title(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(title)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

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

    # ==================== FUNCIÓN AUXILIAR ESPRIMO ====================
    add_ej_header("FUNCIÓN AUXILIAR: EsPrimo (Determinar si un dígito 0..9 es primo)")
    
    add_section_title("▼")
    add_section_title("Análisis:")
    add_p("d (Byte / Dígito de 0 a 9)", bold_prefix="• Entrada: ")
    add_p("Verificar si el dígito d es exactamente igual a 2, 3, 5 o 7 (únicos dígitos primos del sistema decimal).", bold_prefix="• Proceso: ")
    add_p("Booleano (Verdadero / Falso)", bold_prefix="• Salida: ")

    add_section_title("Pseudocódigo:")
    code_pseudo_esprimo = '''Funcion EsPrimo(d: Byte): Booleano
  Retornar (d = 2) O (d = 3) O (d = 5) O (d = 7)
FinFuncion'''
    add_code_block(doc, code_pseudo_esprimo, border_color="10B981")

    add_section_title("Prueba de Escritorio:")
    headers_ep = ["d (Dígito)", "¿d = 2?", "¿d = 3?", "¿d = 5?", "¿d = 7?", "Resultado EsPrimo"]
    rows_ep = [
        ["2", "Sí", "No", "No", "No", "TRUE"],
        ["3", "No", "Sí", "No", "No", "TRUE"],
        ["4", "No", "No", "No", "No", "FALSE"],
        ["5", "No", "No", "Sí", "No", "TRUE"],
        ["7", "No", "No", "No", "Sí", "TRUE"],
        ["9", "No", "No", "No", "No", "FALSE"]
    ]
    add_trace_table(doc, headers_ep, rows_ep)

    add_section_title("Codificación Delphi (Unit1.pas):")
    code_delphi_esprimo = '''function EsPrimo(d: Byte): Boolean;
begin
  Result := (d = 2) or (d = 3) or (d = 5) or (d = 7);
end;'''
    add_code_block(doc, code_delphi_esprimo)

    # ==================== EJ 01 ====================
    add_ej_header("EJ 01: Sumar los dígitos primos de un número natural (SumarDigitosPrimos)")
    
    add_section_title("▼")
    add_section_title("Análisis:")
    add_p("n (Número natural, tipo Word/Cardinal)", bold_prefix="• Entrada: ")
    add_p("Extraer dígitos con n MOD 10. Evaluar con la función EsPrimo(d); si es primo acumular en suma. Reducir con n DIV 10.", bold_prefix="• Proceso: ")
    add_p("suma (Número natural con la suma de los dígitos primos)", bold_prefix="• Salida: ")

    add_section_title("Pseudocódigo:")
    code_pseudo_1 = '''Funcion SumarDigitosPrimos(n: Entero): Entero
  suma <- 0
  Mientras n > 0 Hacer
    d <- n MOD 10
    Si EsPrimo(d) Entonces
      suma <- suma + d
    FinSi
    n <- n DIV 10
  FinMientras
  Retornar suma
FinFuncion'''
    add_code_block(doc, code_pseudo_1, border_color="10B981")

    add_section_title("Prueba de Escritorio:")
    headers_1 = ["n", "d := n mod 10", "¿EsPrimo(d)?", "suma := suma + d", "n := n div 10"]
    rows_1 = [
        ["2374", "4", "No (4 no es primo)", "0", "237"],
        ["237", "7", "Sí (7 es primo)", "7", "23"],
        ["23", "3", "Sí (3 es primo)", "10", "2"],
        ["2", "2", "Sí (2 es primo)", "12", "0"]
    ]
    add_trace_table(doc, headers_1, rows_1)

    add_section_title("Codificación Delphi (Unit1.pas):")
    code_delphi_1 = '''function SumarDigitosPrimos(n: Word): Word;
var
  d, suma: Word;
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
end;'''
    add_code_block(doc, code_delphi_1)

    add_section_title("Llamada en Botón Delphi (Button2 / Edit2 / ShowMessage):")
    code_btn_1 = '''// Procedimiento del botón Button2 (SumarDigitosPrimos):
procedure TForm1.Button2Click(Sender: TObject);
begin
  // 1. Mostrar resultado en Edit2:
  Edit2.Text := IntToStr(SumarDigitosPrimos(n));

  // 2. Opcional con ShowMessage (Ventana emergente):
  // ShowMessage('Suma de dígitos primos: ' + IntToStr(SumarDigitosPrimos(n)));
end;'''
    add_code_block(doc, code_btn_1, border_color="9333EA")

    doc.add_page_break()

    # ==================== EJ 02 ====================
    add_ej_header("EJ 02: Formar otro número solo con los dígitos pares (FormarSoloPares)")
    
    add_section_title("▼")
    add_section_title("Análisis:")
    add_p("n (Número natural, tipo Word/Cardinal. Ejemplo pizarra: N = 1234)", bold_prefix="• Entrada: ")
    add_p("Inicializar npar := 0 y pot := 1. Extraer d := n MOD 10. Si (d MOD 2 = 0) entonces acumular posicionalmente npar := npar + (d * pot) y multiplicar pot := pot * 10. Reducir n := n DIV 10.", bold_prefix="• Proceso: ")
    add_p("npar (Número natural formado únicamente con los dígitos pares en su orden original, ej. 24)", bold_prefix="• Salida: ")

    add_section_title("Pseudocódigo:")
    code_pseudo_2 = '''Funcion FormarSoloPares(n: Entero): Entero
  npar <- 0
  pot <- 1
  Mientras n > 0 Hacer
    d <- n MOD 10
    Si (d MOD 2 = 0) Entonces
      npar <- npar + (d * pot)
      pot <- pot * 10
    FinSi
    n <- n DIV 10
  FinMientras
  Retornar npar
FinFuncion'''
    add_code_block(doc, code_pseudo_2, border_color="10B981")

    add_section_title("Prueba de Escritorio:")
    headers_2 = ["n", "d := n mod 10", "¿d mod 2 = 0?", "npar := npar + (d*pot)", "pot := pot * 10", "n := n div 10"]
    rows_2 = [
        ["1234", "4", "Sí (Par)", "0 + 4*1 = 4", "10", "123"],
        ["123", "3", "No (Impar)", "4 (sin cambio)", "10 (sin cambio)", "12"],
        ["12", "2", "Sí (Par)", "4 + 2*10 = 24", "100", "1"],
        ["1", "1", "No (Impar)", "24 (sin cambio)", "100 (sin cambio)", "0"]
    ]
    add_trace_table(doc, headers_2, rows_2)

    add_section_title("Codificación Delphi (Unit1.pas):")
    code_delphi_2 = '''function FormarSoloPares(n: Word): Word;
var
  d, npar, pot: Word;
begin
  npar := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) then
    begin
      npar := npar + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  Result := npar;
end;'''
    add_code_block(doc, code_delphi_2)

    add_section_title("Llamada en Botón Delphi (Button3 / Edit2 / ShowMessage):")
    code_btn_2 = '''// Procedimiento del botón Button3 (SoloPares):
procedure TForm1.Button3Click(Sender: TObject);
begin
  // 1. Mostrar en Edit2:
  Edit2.Text := IntToStr(FormarSoloPares(n));

  // 2. Opcional con ShowMessage:
  // ShowMessage('Número solo con pares: ' + IntToStr(FormarSoloPares(n)));
end;'''
    add_code_block(doc, code_btn_2, border_color="9333EA")

    doc.add_page_break()

    # ==================== EJ 03 ====================
    add_ej_header("EJ 03: Sumar los dígitos múltiplos de 3 (SumarMultiplosDe3)")
    
    add_section_title("▼")
    add_section_title("Análisis:")
    add_p("n (Número natural)", bold_prefix="• Entrada: ")
    add_p("Extraer dígitos con n MOD 10. Si (d MOD 3 = 0) sumar d a suma. Reducir número con n DIV 10.", bold_prefix="• Proceso: ")
    add_p("suma (Suma total de los dígitos múltiplos de 3)", bold_prefix="• Salida: ")

    add_section_title("Pseudocódigo:")
    code_pseudo_3 = '''Funcion SumarMultiplosDe3(n: Entero): Entero
  suma <- 0
  Mientras n > 0 Hacer
    d <- n MOD 10
    Si (d MOD 3 = 0) Entonces
      suma <- suma + d
    FinSi
    n <- n DIV 10
  FinMientras
  Retornar suma
FinFuncion'''
    add_code_block(doc, code_pseudo_3, border_color="10B981")

    add_section_title("Prueba de Escritorio:")
    headers_3 = ["n", "d := n mod 10", "¿d mod 3 = 0?", "suma := suma + d", "n := n div 10"]
    rows_3 = [
        ["3681", "1", "No (1 mod 3 <> 0)", "0", "368"],
        ["368", "8", "No (8 mod 3 <> 0)", "0", "36"],
        ["36", "6", "Sí (6 mod 3 = 0)", "6", "3"],
        ["3", "3", "Sí (3 mod 3 = 0)", "6 + 3 = 9", "0"]
    ]
    add_trace_table(doc, headers_3, rows_3)

    add_section_title("Codificación Delphi (Unit1.pas):")
    code_delphi_3 = '''function SumarMultiplosDe3(n: Word): Word;
var
  d, suma: Word;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;'''
    add_code_block(doc, code_delphi_3)

    add_section_title("Llamada en Botón Delphi (Button4 / Edit2 / ShowMessage):")
    code_btn_3 = '''// Procedimiento del botón Button4 (SumarMultiplosDe3):
procedure TForm1.Button4Click(Sender: TObject);
begin
  // 1. Mostrar en Edit2:
  Edit2.Text := IntToStr(SumarMultiplosDe3(n));

  // 2. Opcional con ShowMessage:
  // ShowMessage('Suma de múltiplos de 3: ' + IntToStr(SumarMultiplosDe3(n)));
end;'''
    add_code_block(doc, code_btn_3, border_color="9333EA")

    doc.add_page_break()

    # ==================== EJ 04 ====================
    add_ej_header("EJ 04: Invertir un número natural (InvertirNumero)")
    
    add_section_title("▼")
    add_section_title("Análisis:")
    add_p("n (Número natural original, ej. 4782)", bold_prefix="• Entrada: ")
    add_p("Inicializar inv := 0. Mientras n > 0: d := n MOD 10; desplazar dígitos anteriores con inv := (inv * 10) + d; reducir n := n DIV 10.", bold_prefix="• Proceso: ")
    add_p("inv (Número invertido, ej. 2874)", bold_prefix="• Salida: ")

    add_section_title("Pseudocódigo:")
    code_pseudo_4 = '''Funcion InvertirNumero(n: Entero): Entero
  inv <- 0
  Mientras n > 0 Hacer
    d <- n MOD 10
    inv <- (inv * 10) + d
    n <- n DIV 10
  FinMientras
  Retornar inv
FinFuncion'''
    add_code_block(doc, code_pseudo_4, border_color="10B981")

    add_section_title("Prueba de Escritorio:")
    headers_4 = ["n", "d := n mod 10", "inv := (inv * 10) + d", "n := n div 10"]
    rows_4 = [
        ["4782", "2", "(0 * 10) + 2 = 2", "478"],
        ["478", "8", "(2 * 10) + 8 = 28", "47"],
        ["47", "7", "(28 * 10) + 7 = 287", "4"],
        ["4", "4", "(287 * 10) + 4 = 2874", "0"]
    ]
    add_trace_table(doc, headers_4, rows_4)

    add_section_title("Codificación Delphi (Unit1.pas):")
    code_delphi_4 = '''function InvertirNumero(n: Word): Word;
var
  d, inv: Word;
begin
  inv := 0;
  while n > 0 do
  begin
    d := n mod 10;
    inv := (inv * 10) + d;
    n := n div 10;
  end;
  Result := inv;
end;'''
    add_code_block(doc, code_delphi_4)

    add_section_title("Llamada en Botón Delphi (Button5 / Edit2 / ShowMessage):")
    code_btn_4 = '''// Procedimiento del botón Button5 (InvertirNumero):
procedure TForm1.Button5Click(Sender: TObject);
begin
  // 1. Mostrar en Edit2:
  Edit2.Text := IntToStr(InvertirNumero(n));

  // 2. Opcional con ShowMessage:
  // ShowMessage('Número invertido: ' + IntToStr(InvertirNumero(n)));
end;'''
    add_code_block(doc, code_btn_4, border_color="9333EA")

    doc.add_page_break()

    # ==================== BOTÓN CARGAR Y CÓDIGO COMPLETO UNIT1 ====================
    add_ej_header("INTEGRACIÓN VCL: BOTÓN CARGAR Y CÓDIGO COMPLETO DE UNIT1.PAS")
    
    add_section_title("Procedimiento del Botón Cargar (Button1):")
    code_btn_cargar = '''procedure TForm1.Button1Click(Sender: TObject);
begin
  if Edit1.Text <> '' then
  begin
    n := StrToInt(Edit1.Text);
    ShowMessage('Número natural registrado: ' + IntToStr(n));
  end
  else
    ShowMessage('Por favor ingresa un número en Edit1');
end;'''
    add_code_block(doc, code_btn_cargar, border_color="F59E0B")

    add_section_title("Código Fuente Completo de Unit1.pas listo para compilar en Delphi:")
    code_unit1_total = '''unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  n: Word; // Variable global para almacenar el número ingresado

implementation

{$R *.dfm}

// ==========================================
// MÉTODOS Y FUNCIONES DE LA TAREA
// ==========================================

// Función auxiliar: Determina si un dígito (0..9) es primo
function EsPrimo(d: Byte): Boolean;
begin
  Result := (d = 2) or (d = 3) or (d = 5) or (d = 7);
end;

// 1. Sumar dígitos primos
function SumarDigitosPrimos(n: Word): Word;
var
  d, suma: Word;
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
end;

// 2. Mostrar en otro número solo pares (Ejemplo pizarra: N = 1234 -> NPar = 24)
function FormarSoloPares(n: Word): Word;
var
  d, npar, pot: Word;
begin
  npar := 0;
  pot := 1;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 2 = 0) then
    begin
      npar := npar + (d * pot);
      pot := pot * 10;
    end;
    n := n div 10;
  end;
  Result := npar;
end;

// 3. Sumar múltiplos de 3
function SumarMultiplosDe3(n: Word): Word;
var
  d, suma: Word;
begin
  suma := 0;
  while n > 0 do
  begin
    d := n mod 10;
    if (d mod 3 = 0) then
      suma := suma + d;
    n := n div 10;
  end;
  Result := suma;
end;

// 4. Invertir número
function InvertirNumero(n: Word): Word;
var
  d, inv: Word;
begin
  inv := 0;
  while n > 0 do
  begin
    d := n mod 10;
    inv := (inv * 10) + d;
    n := n div 10;
  end;
  Result := inv;
end;

// ==========================================
// EVENTOS ONCLICK DE LOS BOTONES
// ==========================================

// Botón: Cargar
procedure TForm1.Button1Click(Sender: TObject);
begin
  if Edit1.Text <> '' then
  begin
    n := StrToInt(Edit1.Text);
    ShowMessage('Número natural registrado: ' + IntToStr(n));
  end
  else
    ShowMessage('Por favor ingresa un número en Edit1');
end;

// Botón: SumarDigitosPrimos
procedure TForm1.Button2Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(SumarDigitosPrimos(n));
end;

// Botón: SoloPares
procedure TForm1.Button3Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(FormarSoloPares(n));
end;

// Botón: SumarMultiplosDe3
procedure TForm1.Button4Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(SumarMultiplosDe3(n));
end;

// Botón: InvertirNumero
procedure TForm1.Button5Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(InvertirNumero(n));
end;

end.'''
    add_code_block(doc, code_unit1_total)

    output_path = "d:\\Introz2\\practico07\\Tarea_De_Clase_Delphi.docx"
    doc.save(output_path)
    print(f"Documento Tarea de Clase generado con exito en: {output_path}")

if __name__ == "__main__":
    build_tarea_clase_word()
