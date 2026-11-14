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

def add_code_box(doc, code_text, border_color="2563EB"):
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
    p_after.paragraph_format.space_after = Pt(2)

def add_table_grid(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        if col_widths and col_idx < len(col_widths):
            cell.width = col_widths[col_idx]
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
        bg = "FFFFFF" if row_idx % 2 == 0 else "F8FAFC"
        for col_idx, val_text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            if col_widths and col_idx < len(col_widths):
                cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=90, right=90)
            set_cell_border(cell, color="CBD5E1", sz="4")
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(str(val_text))
                r.font.name = "Consolas"
                r.font.bold = True
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(str(val_text))
                r.font.name = "Calibri"
                r.font.size = Pt(9)
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
            
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(3)

def generate_super_cheatsheet_word():
    doc = Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.45)
        s.bottom_margin = Inches(0.45)
        s.left_margin = Inches(0.6)
        s.right_margin = Inches(0.6)

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(9.5)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    
    r_uni = title_p.add_run("GUÍA DE BOLSILLO Y HOJA DE ATAJOS PROFESIONAL (CHEAT SHEET)\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_sub = title_p.add_run("Delphi RAD Studio • Depuración (Debugger) • Buenas Prácticas (Clean Code) • InputBox • Fórmulas de Números Naturales\nUAGRM - FICCT • INF110-Z2")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(8)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
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

    # 1. ATAJOS DE TECLADO Y DEPURACIÓN (DEBUGGER)
    add_h1("🐞 1. ATAJOS DEL IDE Y GUÍA DE DEPURACIÓN (DEBUGGING) EN DELPHI")
    headers_debug = ["Atajo de Teclado", "Herramienta de Depuración", "Para Qué Sirve en el Examen / Laboratorio"]
    rows_debug = [
        ["F5", "Poner / Quitar Breakpoint", "Marca una línea con un punto rojo donde la ejecución se pausará automáticamente para inspeccionar la memoria."],
        ["F9", "Run (Ejecutar con Debugger)", "Inicia el programa y se detiene exactamente al llegar al primer Breakpoint."],
        ["F8", "Step Over (Paso a Paso)", "Avanza a la siguiente línea de código sin entrar dentro de funciones auxiliares."],
        ["F7", "Trace Into (Entrar al Módulo)", "Entra dentro de la función (ej. dentro de EsPrimo o InvertirNumero) para ver qué hace línea por línea."],
        ["Shift + F8", "Step Out (Salir del Módulo)", "Ejecuta lo que queda de la función actual y regresa inmediatamente al módulo que la llamó."],
        ["Ctrl + F5", "Add Watch (Inspeccionar Variable)", "Añade una variable (ej: digito, suma, pot) a la ventana 'Watch List' para ver su valor cambiar en vivo."],
        ["Ctrl + F7", "Evaluate / Modify", "Abre una ventana para evaluar expresiones al vuelo o cambiar temporalmente el valor de una variable."],
        ["Ctrl + F2", "Program Reset (Detener Debug)", "Detiene inmediatamente la depuración forzada y regresa el IDE al estado de edición normal."],
        ["F12", "Alternar Código / Form", "Cambia entre el archivo .pas y el diseñador visual del formulario .dfm."],
        ["Ctrl + Shift + C", "Class Completion", "Genera automáticamente en implementation la cabecera de los botones declarados en la clase TForm1."]
    ]
    add_table_grid(doc, headers_debug, rows_debug, [Inches(1.5), Inches(2.2), Inches(3.1)])

    # 2. BUENAS PRÁCTICAS Y CLEAN CODE
    add_h1("✨ 2. BUENAS PRÁCTICAS DE PROGRAMACIÓN: NOMBRES AUTO-EXPLICATIVOS")
    add_p("Un buen estándar de programación exige que el código se explique por sí mismo sin necesidad de adivinar qué significa cada letra. Evita variables crípticas de una sola letra y usa nombres descriptivos:")

    headers_names = ["Nombre Corto (Malo)", "Nombre Auto-Descriptivo (Recomendado)", "Significado y Rol en el Algoritmo"]
    rows_names = [
        ["n", "numeroNatural / numeroRestante", "El número que se va dividiendo entre 10 sucesivamente en cada ciclo."],
        ["d", "digitoActual", "El residuo extraído con mod 10 (las unidades del número actual)."],
        ["suma / s", "sumaDigitosAcumulada", "Acumulador aditivo donde se suman los dígitos que cumplen la condición."],
        ["inv", "numeroInvertido", "Acumulador multiplicativo donde se arma el número al revés."],
        ["npar", "numeroSoloPares", "Número resultante formado únicamente con los dígitos pares."],
        ["pot", "potenciaPosicional", "Multiplicador (1, 10, 100...) para armar el número en su orden original."],
        ["c / cont", "cantidadDigitosValidos", "Contador de dígitos que cumplen la condición para promedios o frecuencias."],
        ["p / u", "primerDigito / ultimoDigito", "Variables de salida para los extremos más y menos significativos."]
    ]
    add_table_grid(doc, headers_names, rows_names, [Inches(1.5), Inches(2.5), Inches(2.8)])

    add_p("Ejemplo comparativo de código limpio y auto-descriptivo:")
    clean_code_example = '''// CÓDIGO LIMPIO, ELEGANTE Y FÁCIL DE ENTENDER:
function SumarDigitosPrimos(numeroNatural: Word): Word;
var
  digitoActual, sumaDigitosPrimos: Word;
begin
  sumaDigitosPrimos := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if EsPrimo(digitoActual) then
      sumaDigitosPrimos := sumaDigitosPrimos + digitoActual;
      
    numeroNatural := numeroNatural div 10;
  end;
  Result := sumaDigitosPrimos;
end;'''
    add_code_box(doc, clean_code_example, border_color="10B981")

    # 3. USO DE INPUTBOX EN DELPHI
    add_h1("📥 3. CAPTURA RÁPIDA DE DATOS CON InputBox (VENTANA EMERGENTE)")
    add_p("La función InputBox permite solicitar números o textos al usuario mediante una ventana de diálogo modal sin necesidad de depender únicamente de un control TEdit en el formulario.")

    headers_ib = ["Parámetro de InputBox", "Tipo de Dato", "Propósito en la Pantalla"]
    rows_ib = [
        ["1. ACaption (Título)", "String", "El texto que aparece en la barra de título superior de la ventanita."],
        ["2. APrompt (Instrucción)", "String", "El mensaje que le indica al usuario qué debe ingresar."],
        ["3. ADefault (Por defecto)", "String", "El valor prellenado sugerido en la caja (ej. '1234')."]
    ]
    add_table_grid(doc, headers_ib, rows_ib, [Inches(2.0), Inches(1.5), Inches(3.3)])

    add_p("Ejemplo de implementación en el evento de un botón:")
    inputbox_code = '''procedure TForm1.ButtonCargarConInputBoxClick(Sender: TObject);
var
  textoIngresado: String;
begin
  // Abre ventana modal pidiendo el número:
  textoIngresado := InputBox('Cargar Número Natural', 'Por favor ingrese un número:', '1234');
  
  // Validamos que el usuario no haya cancelado ni dejado vacío:
  if textoIngresado <> '' then
  begin
    n := StrToInt(textoIngresado);
    Edit1.Text := IntToStr(n);
    ShowMessage('Número registrado exitosamente: ' + IntToStr(n));
  end
  else
    ShowMessage('Operación cancelada por el usuario.');
end;'''
    add_code_box(doc, inputbox_code, border_color="F59E0B")

    # 4. FÓRMULAS ESENCIALES DE NÚMEROS NATURALES
    add_h1("🔢 4. FÓRMULAS Y PATRONES ESENCIALES DE NÚMEROS NATURALES")
    headers_pat = ["Patrón / Operación", "Sintaxis Limpia en Delphi", "Resultado y Uso"]
    rows_pat = [
        ["Extraer último dígito", "digitoActual := numero mod 10;", "Obtiene las unidades. Ej: 1234 mod 10 = 4"],
        ["Eliminar último dígito", "numero := numero div 10;", "División entera, reduce magnitud: 1234 div 10 = 123"],
        ["Bucle estándar", "while numero > 0 do begin ... end;", "Recorre de der. a izq. hasta que el número queda en 0."],
        ["Filtro de Dígito Par", "if (digitoActual mod 2 = 0) then", "Dígitos 0, 2, 4, 6, 8."],
        ["Filtro de Dígito Impar", "if (digitoActual mod 2 <> 0) then", "Dígitos 1, 3, 5, 7, 9."],
        ["Filtro de Dígito Primo", "(d=2) or (d=3) or (d=5) or (d=7)", "Únicos números primos entre 0 y 9."],
        ["Múltiplo de K", "if (digitoActual mod K = 0) then", "Divisible exactamente entre K (ej. mod 3 = 0)."],
        ["Invertir número", "inv := (inv * 10) + digitoActual;", "Desplaza a la izquierda multiplicando por 10."],
        ["Construir en orden", "res := res + (digito * pot);\npot := pot * 10;", "Conserva el orden original de izquierda a derecha."],
        ["Verificar Capicúa", "EsCapicua := (numero = InvertirNumero(numero));", "Compara si el número original es igual a su invertido."]
    ]
    add_table_grid(doc, headers_pat, rows_pat, [Inches(1.8), Inches(2.4), Inches(2.6)])

    output_path = "d:\\Introz2\\practico07\\Hoja_De_Atajos_Delphi_Numeros.docx"
    doc.save(output_path)
    print(f"Hoja de atajos actualizada con Clean Code, Debugging e InputBox en: {output_path}")

if __name__ == '__main__':
    generate_super_cheatsheet_word()
