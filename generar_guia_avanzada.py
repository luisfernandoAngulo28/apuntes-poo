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

def set_cell_margins(cell, top=70, bottom=70, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_code_box(doc, code_text, border_color="2563EB"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=90, bottom=90, left=140, right=140)
    
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

def create_advanced_guide():
    doc = Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.65)
        s.bottom_margin = Inches(0.65)
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
    title_p.paragraph_format.space_after = Pt(4)
    
    r_uni = title_p.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = title_p.add_run("Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones (FICCT)\n")
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
    p_main.paragraph_format.space_before = Pt(10)
    p_main.paragraph_format.space_after = Pt(4)
    r_title = p_main.add_run("GUÍA AVANZADA: POO (CLASE TNUMERO), DIAGRAMAS DE FLUJO Y SOLUCIÓN DE ERRORES EN DELPHI")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(15)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

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
        r.font.size = Pt(10.5)
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
            r_b.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        p.add_run(text)
        return p

    # 1. PUENTE HACIA POO
    add_h1("1. PUENTE HACIA PROGRAMACIÓN ORIENTADA A OBJETOS (POO)")
    add_p("En el paradigma modular tradicional, las funciones operan recibiendo el número como parámetro en cada llamada. En Programación Orientada a Objetos (POO), encapsulamos el valor como un atributo interno dentro de una clase (TNumero) y los algoritmos pasan a ser métodos miembros que operan directamente sobre dicho estado.")

    add_h2("1.1. Definición de la Clase TNumero (UnitClaseNumero.pas)")
    code_poo_def = '''type
  TNumero = class
  private
    FValor: Cardinal; // Atributo encapsulado (estado del objeto)
    function EsPrimoAux(d: Byte): Boolean;
  public
    constructor Create; overload;
    constructor Create(AValor: Cardinal); overload;
    
    property Valor: Cardinal read FValor write FValor;
    
    procedure Cargar(AValor: Cardinal);
    function Descargar: Cardinal;
    
    // Métodos del negocio
    function SumarDigitosPrimos: Cardinal;
    function FormarSoloPares: Cardinal;
    function SumarMultiplosDe3: Cardinal;
    function InvertirNumero: Cardinal;
    function EsCapicua: Boolean;
  end;'''
    add_code_box(doc, code_poo_def, border_color="10B981")

    add_h2("1.2. Uso en el Formulario Delphi VCL")
    code_poo_usage = '''var
  MiNumero: TNumero; // Declaración del objeto

procedure TForm1.FormCreate(Sender: TObject);
begin
  MiNumero := TNumero.Create(0); // Instanciación
end;

procedure TForm1.ButtonCargarClick(Sender: TObject);
begin
  MiNumero.Cargar(StrToInt(Edit1.Text));
  ShowMessage('Objeto cargado con valor: ' + IntToStr(MiNumero.Descargar));
end;

procedure TForm1.ButtonPrimosClick(Sender: TObject);
begin
  Edit2.Text := IntToStr(MiNumero.SumarDigitosPrimos);
end;'''
    add_code_box(doc, code_poo_usage, border_color="9333EA")

    doc.add_page_break()

    # 2. DIAGRAMAS DE FLUJO
    add_h1("2. DIAGRAMAS DE FLUJO (FLOWCHARTS ANSI) DE LOS PATRONES CLAVE")
    add_p("A continuación se detallan las estructuras lógicas de control para los algoritmos fundamentales de números naturales.")

    add_h2("2.1. Patrón 1: Bucle de Descomposición y Filtro de Primos")
    flow_1 = '''[ INICIO: SumarDigitosPrimos(n) ]
               │
               ▼
        [ suma := 0 ]
               │
               ▼
       /   ¿ n > 0 ?   \  ──── (NO) ───► [ RESULT := suma ] ───► [ FIN ]
       \               /
               │ (SÍ)
               ▼
        [ d := n MOD 10 ]
               │
               ▼
     /  ¿EsPrimo(d)?  \ ─── (NO) ──┐
     \  (2, 3, 5, 7)  /            │
               │ (SÍ)              │
               ▼                   │
     [ suma := suma + d ]          │
               │                   │
               ▼ ◄─────────────────┘
        [ n := n DIV 10 ]
               │
               ▼
     ( Regresa a evaluar n > 0 )'''
    add_code_box(doc, flow_1, border_color="3B82F6")

    add_h2("2.2. Patrón 2: Reconstrucción Posicional en Orden Original (SoloPares)")
    flow_2 = '''[ INICIO: FormarSoloPares(n) ]
               │
               ▼
    [ npar := 0 ; pot := 1 ]
               │
               ▼
       /   ¿ n > 0 ?   \  ──── (NO) ───► [ RESULT := npar ] ───► [ FIN ]
       \               /
               │ (SÍ)
               ▼
        [ d := n MOD 10 ]
               │
               ▼
     /  ¿ d MOD 2 = 0 ? \ ── (NO) ─┐
     \      (Par)       /          │
               │ (SÍ)              │
               ▼                   │
    [ npar := npar + (d * pot) ]   │
    [ pot  := pot * 10         ]   │
               │                   │
               ▼ ◄─────────────────┘
        [ n := n DIV 10 ]
               │
               ▼
     ( Regresa a evaluar n > 0 )'''
    add_code_box(doc, flow_2, border_color="F59E0B")

    doc.add_page_break()

    # 3. GUÍA DE ERRORES DE COMPILACIÓN
    add_h1("3. GUÍA DE ERRORES TÍPICOS DE COMPILACIÓN EN DELPHI Y CÓMO RESOLVERLOS")
    
    add_h2("3.1. Error E2003: Undeclared identifier")
    add_p("El compilador no reconoce un nombre de variable, tipo, palabra reservada o función.", bold_prefix="• Causa: ")
    add_p("1. Olvidar declarar la variable en la sección 'var'. 2. Copiar código de webs/chats con espacios invisibles (Non-breaking space \\u00A0). 3. Escribir una función debajo de donde se la llama sin declararla antes en interface.", bold_prefix="• Solución: ")

    add_h2("3.2. Error E2010: Incompatible types: 'String' and 'Integer'")
    add_p("Se intenta asignar texto a una variable numérica o viceversa sin conversión.", bold_prefix="• Causa: ")
    add_p("Usar 'StrToInt(Edit1.Text)' para pasar de texto a entero y 'IntToStr(n)' para pasar de entero a texto en 'Edit2.Text'.", bold_prefix="• Solución: ")

    add_h2("3.3. Error E2029: ';' expected but 'ELSE' found")
    add_p("Se colocó un punto y coma ';' justo antes de un 'else'. En Pascal, la sentencia previa al else NO lleva punto y coma.", bold_prefix="• Causa: ")
    add_p("Escribir 'if condición then acción else otraAccion;' (sin ';' antes de else).", bold_prefix="• Solución: ")

    add_h2("3.4. Error E2065: Unsatisfied forward or external declaration: 'TForm1.ButtonXClick'")
    add_p("El botón está declarado en la clase TForm1 dentro de interface, pero no existe su implementación en implementation.", bold_prefix="• Causa: ")
    add_p("Presionar 'Ctrl + Shift + C' con el cursor dentro de la clase para autogenerar el método, o crearlo manualmente con 'procedure TForm1.ButtonXClick(Sender: TObject); begin ... end;'.", bold_prefix="• Solución: ")

    # 4. SUITE DE PRUEBAS UNITARIAS
    add_h1("4. SUITE DE PRUEBAS UNITARIAS AUTOMÁTICAS (TestPractico07.dpr)")
    add_p("Para validar que los 25 algoritmos funcionan correctamente sin necesidad de probar a mano uno por uno, se implementó un ejecutor automatizado con assertions.")
    add_p("Verifica entradas normales, casos con 0, números de un solo dígito y números capicúa, arrojando un resumen 100% verificado en verde.")

    output_path = "d:\\Introz2\\practico07\\Guia_Avanzada_POO_Errores_Y_Diagramas.docx"
    doc.save(output_path)
    print(f"Guia avanzada guardada en: {output_path}")

if __name__ == '__main__':
    create_advanced_guide()
