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

def add_table_grid(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Headers
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        if col_widths and col_idx < len(col_widths):
            cell.width = col_widths[col_idx]
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
        bg = "FFFFFF" if row_idx % 2 == 0 else "F8FAFC"
        for col_idx, val_text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            if col_widths and col_idx < len(col_widths):
                cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            set_cell_border(cell, color="CBD5E1", sz="4")
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            
            # Align center for short keys, left for description
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

def create_cheatsheet():
    doc = Document()
    
    # Compact margins for a clean 2-page print cheatsheet
    for s in doc.sections:
        s.top_margin = Inches(0.5)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6)
        s.right_margin = Inches(0.6)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(9.5)
    normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Header Title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    
    r_uni = title_p.add_run("HOJA DE ATAJOS Y GUÍA RÁPIDA (CHEAT SHEET)\n")
    r_uni.font.name = "Arial"
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_sub = title_p.add_run("Delphi RAD Studio • Programación Modular • Algoritmos con Dígitos de Números Naturales\nUAGRM - FICCT • INF110-Z2")
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

    # 1. ATAJOS DE TECLADO DELPHI
    add_h1("⌨️ 1. ATAJOS DE TECLADO INDISPENSABLES EN DELPHI (RAD STUDIO)")
    headers_ide = ["Atajo de Teclado", "Acción y Utilidad en Clase"]
    rows_ide = [
        ["F9", "Compilar y Ejecutar el programa (Run con debugger)."],
        ["F12", "Alternar instantáneamente entre la vista de Código (.pas) y el Diseñador Visual del Formulario (.dfm)."],
        ["Ctrl + Shift + C", "Class Completion: Genera automáticamente la estructura de los métodos declarados en la clase TForm1 dentro de implementation."],
        ["Ctrl + Espacio", "Code Completion (IntelliSense): Muestra sugerencias de funciones, propiedades y variables."],
        ["Ctrl + Shift + ↑ / ↓", "Navegación Rápida: Salta entre la declaración de una función en interface y su código en implementation."],
        ["Ctrl + F9", "Compilar y verificar errores de sintaxis sin ejecutar."],
        ["F11", "Object Inspector: Abre la barra lateral para cambiar Properties (Text, Caption) y Events (OnClick)."],
        ["F8 / F7", "Trace / Debugger: F8 ejecuta la siguiente línea (Step Over); F7 entra dentro de la función (Trace Into)."],
        ["Ctrl + Shift + F9", "Ejecutar sin depurador (Run Without Debugging, más rápido)."],
        ["Ctrl + /", "Comentar o descomentar las líneas seleccionadas con //."]
    ]
    add_table_grid(doc, headers_ide, rows_ide, [Inches(1.8), Inches(5.0)])

    # 2. PATRONES Y FÓRMULAS DE NÚMEROS NATURALES
    add_h1("🔢 2. FÓRMULAS Y PATRONES CLAVE PARA TRATAMIENTO DE DÍGITOS")
    headers_dig = ["Operación / Patrón", "Sintaxis en Delphi / Pascal", "Explicación / Resultado"]
    rows_dig = [
        ["Extraer último dígito", "d := n mod 10;", "Obtiene el residuo (el dígito de las unidades). Ej: 1234 mod 10 = 4"],
        ["Eliminar último dígito", "n := n div 10;", "División entera, trunca el último dígito. Ej: 1234 div 10 = 123"],
        ["Bucle de descomposición", "while n > 0 do begin ... end;", "Recorre todos los dígitos de derecha a izquierda hasta agotar n."],
        ["Verificar si es Par", "if (d mod 2 = 0) then", "El residuo de dividir entre 2 es cero (0, 2, 4, 6, 8)."],
        ["Verificar si es Impar", "if (d mod 2 <> 0) then", "El residuo no es cero (1, 3, 5, 7, 9)."],
        ["Verificar si es Primo", "(d=2) or (d=3) or (d=5) or (d=7)", "Conjunto exacto de dígitos primos en base 10."],
        ["Verificar Múltiplo de K", "if (d mod K = 0) then", "Dígito divisible entre K (ej. d mod 3 = 0, d mod 4 = 0)."],
        ["Invertir número", "inv := (inv * 10) + d;", "Desplaza los dígitos acumulados multiplicando por 10 y suma d."],
        ["Construir en orden original", "res := res + (d * pot);\npot := pot * 10;", "Conserva el orden relativo de izquierda a derecha (ej. SoloPares)."],
        ["Contador de dígitos", "cont := cont + 1; // Inc(cont);", "Incrementa en 1 por cada dígito procesado."],
        ["Suma acumulativa", "suma := suma + d;", "Suma el valor del dígito extraído."],
        ["Primer dígito (MSD)", "while n >= 10 do n := n div 10;\nprimero := n;", "Reduce sucesivamente hasta dejar únicamente el dígito inicial."],
        ["Último dígito (LSD)", "ultimo := n mod 10;", "El dígito menos significativo."],
        ["Eliminar extremos", "n := (n div 10) mod pot;", "Quita el último con div 10 y el primero con mod (10^(c-1))."],
        ["Capicúa / Palíndromo", "EsCapicua := (n = InvertirNumero(n));", "Verifica si el número original es idéntico a su número invertido."]
    ]
    add_table_grid(doc, headers_dig, rows_dig, [Inches(1.8), Inches(2.3), Inches(2.7)])

    # 3. CONVERSIONES DE TIPOS Y VCL
    add_h1("🔄 3. CONVERSIONES DE TIPO Y MANIPULACIÓN VCL (EDIT / BOTONES)")
    headers_vcl = ["Conversión / Acción", "Código Pascal en Delphi", "Uso Común en el Formulario"]
    rows_vcl = [
        ["Texto a Entero", "n := StrToInt(Edit1.Text);", "Capturar el número natural desde la caja de texto Edit1."],
        ["Entero a Texto", "Edit2.Text := IntToStr(resultado);", "Mostrar el resultado numérico de la función en Edit2."],
        ["Real a Texto", "Edit2.Text := FloatToStr(promedio);", "Mostrar promedios o valores con decimales."],
        ["Real con 2 decimales", "Edit2.Text := FloatToStrF(prom, ffFixed, 8, 2);", "Formatea a 2 decimales fijos (ej: 4.67)."],
        ["Mensaje Emergente", "ShowMessage('Resultado: ' + IntToStr(res));", "Muestra una ventana modal de diálogo con el mensaje."],
        ["Char dígito a Entero", "d := Ord(cad[i]) - Ord('0');", "Convierte el carácter '7' a su valor numérico entero 7."],
        ["Evento Botón Cargar", "n := StrToInt(Edit1.Text);", "Almacena en variable global n el valor ingresado."],
        ["Evento Botón Función", "Edit2.Text := IntToStr(NombreFuncion(n));", "Ejecuta la función modular y asigna a la caja Edit2."]
    ]
    add_table_grid(doc, headers_vcl, rows_vcl, [Inches(1.7), Inches(2.6), Inches(2.5)])

    # 4. PLANTILLA MODULAR RÁPIDA
    add_h1("📐 4. PLANTILLA BASE: FUNCIÓN vs PROCEDIMIENTO")
    headers_mod = ["Tipo de Módulo", "Sintaxis Base", "Cuándo Usarlo"]
    rows_mod = [
        ["FUNCIÓN\n(function)", "function Nombre(n: Word): Word;\nvar d, res: Word;\nbegin\n  res := 0;\n  // algoritmo...\n  Result := res;\nend;", "Cuando el algoritmo debe calcular y devolver UN SOLO valor resultante (suma, contador, número invertido, etc.)."],
        ["PROCEDIMIENTO\n(procedure)", "procedure Nombre(n: Word; var s1, s2: Byte);\nbegin\n  s1 := ...;\n  s2 := ...;\nend;", "Cuando el algoritmo debe devolver DOS O MÁS valores (ej. digMayor y digMenor, primero y último) usando parámetros var."]
    ]
    add_table_grid(doc, headers_mod, rows_mod, [Inches(1.4), Inches(2.8), Inches(2.6)])

    output_path = "d:\\Introz2\\practico07\\Hoja_De_Atajos_Delphi_Numeros.docx"
    doc.save(output_path)
    print(f"Hoja de atajos creada exitosamente en: {output_path}")

if __name__ == '__main__':
    create_cheatsheet()
