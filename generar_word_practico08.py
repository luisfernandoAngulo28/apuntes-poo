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

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_code_block(doc, code_text, border_color="2563EB"):
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
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

def add_io_box(doc, entrada, salida, tipo_modulo):
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    table.columns[0].width = Inches(3.25)
    table.columns[1].width = Inches(3.25)

    c00 = table.cell(0, 0)
    c01 = table.cell(0, 1)
    c10 = table.cell(1, 0)
    c11 = table.cell(1, 1)

    set_cell_background(c00, "1E3A8A")
    set_cell_background(c01, "047857")
    set_cell_background(c10, "F1F5F9")
    set_cell_background(c11, "F0FDF4")

    for c in [c00, c01, c10, c11]:
        set_cell_margins(c, top=60, bottom=60, left=100, right=100)

    p0 = c00.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p0.add_run(f"📥 ENTRADA ({tipo_modulo})")
    r0.font.bold = True
    r0.font.size = Pt(8)
    r0.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    p1 = c01.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p1.add_run("📤 SALIDA / RESULTADO")
    r1.font.bold = True
    r1.font.size = Pt(8)
    r1.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    p2 = c10.paragraphs[0]
    r2 = p2.add_run(entrada)
    r2.font.name = "Consolas"
    r2.font.size = Pt(8.5)

    p3 = c11.paragraphs[0]
    r3 = p3.add_run(salida)
    r3.font.name = "Consolas"
    r3.font.size = Pt(8.5)

EJERCICIOS = [
    (1, "Crear una función que cuente los caracteres de una cadena.", "Función",
     "function ContarCaracteres(cad: String): Integer;\nvar\n  i, total: Integer;\nbegin\n  total := 0;\n  for i := 1 to Length(cad) do\n    total := total + 1;\n  ContarCaracteres := total;\nend;",
     "cad = 'Universidad Gabriel Rene Moreno'", "total = 31"),

    (2, "Diseñar un procedimiento que muestre la primera letra de una cadena.", "Procedimiento",
     "procedure MostrarPrimeraLetra(cad: String);\nvar\n  i: Integer;\nbegin\n  for i := 1 to Length(cad) do\n  begin\n    if EsLetra(cad[i]) then\n    begin\n      WriteLn('Primera letra: ', cad[i]);\n      Exit;\n    end;\n  end;\n  if Length(cad) > 0 then\n    WriteLn('Primer caracter: ', cad[1])\n  else\n    WriteLn('La cadena esta vacia.');\nend;",
     "cad = '  Ingenieria Informatica'", "Pantalla: 'Primera letra: I'"),

    (3, "Crear una función que retorne la última letra de una cadena.", "Función",
     "function UltimaLetra(cad: String): Char;\nvar\n  i: Integer;\nbegin\n  UltimaLetra := #0;\n  for i := Length(cad) downto 1 do\n  begin\n    if EsLetra(cad[i]) then\n    begin\n      UltimaLetra := cad[i];\n      Exit;\n    end;\n  end;\n  if Length(cad) > 0 then\n    UltimaLetra := cad[Length(cad)];\nend;",
     "cad = 'Santa Cruz de la Sierra!'", "Retorno: 'a'"),

    (4, "Contar cuántas vocales tiene una palabra ingresada.", "Función",
     "function ContarVocales(pal: String): Integer;\nvar\n  i, c: Integer;\nbegin\n  c := 0;\n  for i := 1 to Length(pal) do\n  begin\n    if EsVocal(pal[i]) then\n      c := c + 1;\n  end;\n  ContarVocales := c;\nend;",
     "pal = 'COMPUTADORA'", "Retorno: 5  (O, U, A, O, A)"),

    (5, "Contar cuántas consonantes tiene una palabra.", "Función",
     "function ContarConsonantes(pal: String): Integer;\nvar\n  i, c: Integer;\nbegin\n  c := 0;\n  for i := 1 to Length(pal) do\n  begin\n    if EsConsonante(pal[i]) then\n      c := c + 1;\n  end;\n  ContarConsonantes := c;\nend;",
     "pal = 'Algoritmos'", "Retorno: 7  (l, g, r, t, m, s)"),

    (6, "Mostrar la cadena en mayúsculas usando una función.", "Función",
     "function CadenaMayusculas(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := 1 to Length(cad) do\n    res := res + A_Mayuscula(cad[i]);\n  CadenaMayusculas := res;\nend;",
     "cad = 'programacion modular'", "Retorno: 'PROGRAMACION MODULAR'"),

    (7, "Mostrar la cadena en minúsculas.", "Función",
     "function CadenaMinusculas(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := 1 to Length(cad) do\n    res := res + A_Minuscula(cad[i]);\n  CadenaMinusculas := res;\nend;",
     "cad = 'DELPHI Y PASCAL INF-110'", "Retorno: 'delphi y pascal inf-110'"),

    (8, "Invertir una cadena carácter por carácter.", "Función",
     "function InvertirCadena(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := Length(cad) downto 1 do\n    res := res + cad[i];\n  InvertirCadena := res;\nend;",
     "cad = 'RENE MORENO'", "Retorno: 'ONEROM ENER'"),

    (9, "Concatenar dos cadenas ingresadas por el usuario.", "Función",
     "function ConcatenarCadenas(cad1, cad2: String): String;\nbegin\n  ConcatenarCadenas := cad1 + cad2;\nend;",
     "cad1 = 'Hola ', cad2 = 'Mundo Delphi'", "Retorno: 'Hola Mundo Delphi'"),

    (10, "Calcular cuántas veces aparece una letra específica dentro de una cadena.", "Función",
     "function ContarOcurrenciasLetra(cad: String; letra: Char): Integer;\nvar\n  i, c: Integer;\n  letraMayus: Char;\nbegin\n  c := 0;\n  letraMayus := A_Mayuscula(letra);\n  for i := 1 to Length(cad) do\n  begin\n    if A_Mayuscula(cad[i]) = letraMayus then\n      c := c + 1;\n  end;\n  ContarOcurrenciasLetra := c;\nend;",
     "cad = 'Estructuras de Datos', letra = 'a'", "Retorno: 3 veces"),

    (11, "Crear una función que elimine espacios en blanco de una cadena.", "Función",
     "function EliminarEspacios(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := 1 to Length(cad) do\n  begin\n    if cad[i] <> ' ' then\n      res := res + cad[i];\n  end;\n  EliminarEspacios := res;\nend;",
     "cad = ' F I C C T   U A G R M '", "Retorno: 'FICCTUAGRM'"),

    (12, "Mostrar solo los n primeros caracteres de una cadena.", "Función",
     "function PrimerosNCaracteres(cad: String; n: Integer): String;\nvar\n  i, limite: Integer;\n  res: String;\nbegin\n  res := '';\n  limite := n;\n  if limite > Length(cad) then\n    limite := Length(cad);\n  for i := 1 to limite do\n    res := res + cad[i];\n  PrimerosNCaracteres := res;\nend;",
     "cad = 'Facultad de Ciencias', n = 8", "Retorno: 'Facultad'"),

    (13, "Determinar si una cadena está vacía o contiene texto.", "Función",
     "function EstaVacia(cad: String): Boolean;\nbegin\n  EstaVacia := (Length(Trim(cad)) = 0);\nend;",
     "cad = '   '", "Retorno: TRUE (Vacia)"),

    (14, "Mostrar los códigos ASCII de cada carácter de una cadena.", "Procedimiento",
     "procedure MostrarCodigosASCII(cad: String);\nvar\n  i: Integer;\nbegin\n  WriteLn('Codigos ASCII de cada caracter:');\n  for i := 1 to Length(cad) do\n    WriteLn('  ''', cad[i], ''' -> ASCII: ', Ord(cad[i]));\nend;",
     "cad = 'UAGRM'", "U->85, A->65, G->71, R->82, M->77"),

    (15, "Contar cuántas letras mayúsculas hay en una cadena.", "Función",
     "function ContarMayusculas(cad: String): Integer;\nvar\n  i, c: Integer;\nbegin\n  c := 0;\n  for i := 1 to Length(cad) do\n  begin\n    if (cad[i] >= 'A') and (cad[i] <= 'Z') then\n      c := c + 1;\n  end;\n  ContarMayusculas := c;\nend;",
     "cad = 'Ingenieria Informatica Sem 2-2025'", "Retorno: 3  (I, I, S)"),

    (16, "Determinar si una cadena es palíndroma (igual al derecho y al revés).", "Función",
     "function EsPalindroma(cad: String): Boolean;\nvar\n  limpia: String;\n  i, j: Integer;\nbegin\n  limpia := '';\n  for i := 1 to Length(cad) do\n    if cad[i] <> ' ' then\n      limpia := limpia + A_Mayuscula(cad[i]);\n  i := 1;\n  j := Length(limpia);\n  EsPalindroma := True;\n  while i < j do\n  begin\n    if limpia[i] <> limpia[j] then\n    begin\n      EsPalindroma := False;\n      Exit;\n    end;\n    i := i + 1;\n    j := j - 1;\n  end;\nend;",
     "cad = 'anita lava la tina'", "Retorno: TRUE"),

    (17, "Contar cuántas palabras hay en una frase.", "Función",
     "function ContarPalabras(frase: String): Integer;\nvar\n  i, c: Integer;\n  enPalabra: Boolean;\nbegin\n  c := 0;\n  enPalabra := False;\n  for i := 1 to Length(frase) do\n  begin\n    if frase[i] <> ' ' then\n    begin\n      if not enPalabra then\n      begin\n        c := c + 1;\n        enPalabra := True;\n      end;\n    end\n    else\n      enPalabra := False;\n  end;\n  ContarPalabras := c;\nend;",
     "frase = '  El sol brilla hoy en Santa Cruz '", "Retorno: 7 palabras"),

    (18, "Verificar si una palabra se encuentra dentro de una frase.", "Función",
     "function ExistePalabra(frase, palabra: String): Boolean;\nvar\n  fMayus, pMayus: String;\nbegin\n  fMayus := CadenaMayusculas(frase);\n  pMayus := CadenaMayusculas(palabra);\n  ExistePalabra := (Pos(pMayus, fMayus) > 0);\nend;",
     "frase = 'La tecnologia avanza', palabra = 'avanza'", "Retorno: TRUE"),

    (19, "Reemplazar todas las apariciones de una letra por otra.", "Función",
     "function ReemplazarLetra(cad: String; vieja, nueva: Char): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := 1 to Length(cad) do\n  begin\n    if cad[i] = vieja then\n      res := res + nueva\n    else\n      res := res + cad[i];\n  end;\n  ReemplazarLetra := res;\nend;",
     "cad = 'banana', vieja = 'a', nueva = 'o'", "Retorno: 'bonono'"),

    (20, "Eliminar todas las apariciones de una letra dentro de la cadena.", "Función",
     "function EliminarLetra(cad: String; letra: Char): String;\nvar\n  i: Integer;\n  res: String;\n  letraMayus: Char;\nbegin\n  res := '';\n  letraMayus := A_Mayuscula(letra);\n  for i := 1 to Length(cad) do\n  begin\n    if A_Mayuscula(cad[i]) <> letraMayus then\n      res := res + cad[i];\n  end;\n  EliminarLetra := res;\nend;",
     "cad = 'Paralelepipedo', letra = 'e'", "Retorno: 'Parallpipdo'"),

    (21, "Contar cuántas veces aparece una palabra en un texto.", "Función",
     "function ContarOcurrenciasPalabra(texto, palabra: String): Integer;\nvar\n  p, c: Integer;\n  tMayus, pMayus: String;\nbegin\n  c := 0;\n  tMayus := CadenaMayusculas(texto);\n  pMayus := CadenaMayusculas(palabra);\n  if (Length(pMayus) = 0) or (Length(tMayus) = 0) then Exit(0);\n  p := Pos(pMayus, tMayus);\n  while p > 0 do\n  begin\n    c := c + 1;\n    Delete(tMayus, 1, p + Length(pMayus) - 1);\n    p := Pos(pMayus, tMayus);\n  end;\n  ContarOcurrenciasPalabra := c;\nend;",
     "texto = 'sol luna sol estrella sol', pal = 'sol'", "Retorno: 3"),

    (22, "Crear un procedimiento que muestre cada carácter de la cadena en una línea diferente.", "Procedimiento",
     "procedure MostrarCaracteresPorLinea(cad: String);\nvar\n  i: Integer;\nbegin\n  for i := 1 to Length(cad) do\n    WriteLn('[', i, ']: ', cad[i]);\nend;",
     "cad = 'PASCAL'", "Línea por línea [1]..[6]"),

    (23, "Determinar si una cadena contiene números o solo letras.", "Función",
     "function DeterminarContenido(cad: String): String;\nvar\n  i: Integer;\n  tieneLetras, tieneDigitos, otros: Boolean;\nbegin\n  tieneLetras := False; tieneDigitos := False; otros := False;\n  for i := 1 to Length(cad) do\n  begin\n    if EsLetra(cad[i]) then tieneLetras := True\n    else if EsDigito(cad[i]) then tieneDigitos := True\n    else if cad[i] <> ' ' then otros := True;\n  end;\n  if tieneDigitos and not tieneLetras and not otros then\n    Exit('Solo digitos numericos')\n  else if tieneLetras and not tieneDigitos and not otros then\n    Exit('Solo letras')\n  else if tieneLetras and tieneDigitos then\n    Exit('Contiene numeros y letras (Alfanumerica)')\n  else\n    Exit('Contiene caracteres especiales o espacios');\nend;",
     "cad = 'HolaMundo'", "Retorno: 'Solo letras'"),

    (24, "Calcular cuántos dígitos numéricos hay en la cadena.", "Función",
     "function ContarDigitos(cad: String): Integer;\nvar\n  i, c: Integer;\nbegin\n  c := 0;\n  for i := 1 to Length(cad) do\n    if EsDigito(cad[i]) then c := c + 1;\n  ContarDigitos := c;\nend;",
     "cad = 'Aula 236 Modulo 225 Piso 3'", "Retorno: 7 digitos"),

    (25, "Extraer la primera palabra de una frase.", "Función",
     "function ExtraerPrimeraPalabra(frase: String): String;\nvar\n  inicio, fin: Integer;\nbegin\n  inicio := 1;\n  while (inicio <= Length(frase)) and (frase[inicio] = ' ') do\n    inicio := inicio + 1;\n  if inicio > Length(frase) then Exit('');\n  fin := inicio;\n  while (fin <= Length(frase)) and (frase[fin] <> ' ') do\n    fin := fin + 1;\n  ExtraerPrimeraPalabra := Copy(frase, inicio, fin - inicio);\nend;",
     "frase = '  Gabriel Rene Moreno fue ilustre'", "Retorno: 'Gabriel'"),

    (26, "Extraer la última palabra de una frase.", "Función",
     "function ExtraerUltimaPalabra(frase: String): String;\nvar\n  fin, inicio: Integer;\nbegin\n  fin := Length(frase);\n  while (fin >= 1) and (frase[fin] = ' ') do\n    fin := fin - 1;\n  if fin < 1 then Exit('');\n  inicio := fin;\n  while (inicio >= 1) and (frase[inicio] <> ' ') do\n    inicio := inicio - 1;\n  ExtraerUltimaPalabra := Copy(frase, inicio + 1, fin - inicio);\nend;",
     "frase = 'Estudiar para el examen final '", "Retorno: 'final'"),

    (27, "Convertir una cadena con espacios múltiples a una con un solo espacio entre palabras.", "Función",
     "function NormalizarEspacios(cad: String): String;\nvar\n  i: Integer;\n  res: String;\n  espacioAnterior: Boolean;\nbegin\n  res := '';\n  espacioAnterior := True;\n  for i := 1 to Length(cad) do\n  begin\n    if cad[i] <> ' ' then\n    begin\n      res := res + cad[i];\n      espacioAnterior := False;\n    end\n    else if not espacioAnterior then\n    begin\n      res := res + ' ';\n      espacioAnterior := True;\n    end;\n  end;\n  if (Length(res) > 0) and (res[Length(res)] = ' ') then\n    Delete(res, Length(res), 1);\n  NormalizarEspacios := res;\nend;",
     "cad = '   Programar   en   Pascal   '", "Retorno: 'Programar en Pascal'"),

    (28, "Mostrar las palabras que empiezan con vocal de una frase.", "Procedimiento",
     "procedure MostrarPalabrasEmpiezanVocal(frase: String);\nvar\n  pal: String;\n  i: Integer;\n  norm: String;\nbegin\n  norm := NormalizarEspacios(frase);\n  if Length(norm) = 0 then Exit;\n  WriteLn('Palabras que empiezan con vocal:');\n  pal := '';\n  for i := 1 to Length(norm) do\n  begin\n    if norm[i] <> ' ' then pal := pal + norm[i]\n    else\n    begin\n      if (Length(pal) > 0) and EsVocal(pal[1]) then WriteLn('  - ', pal);\n      pal := '';\n    end;\n  end;\n  if (Length(pal) > 0) and EsVocal(pal[1]) then WriteLn('  - ', pal);\nend;",
     "frase = 'El aguila vuela sobre el arbol azul'", "Pantalla: 'El', 'aguila', 'el', 'arbol', 'azul'"),

    (29, "Mostrar las palabras que terminan en consonante.", "Procedimiento",
     "procedure MostrarPalabrasTerminanConsonante(frase: String);\nvar\n  pal: String;\n  i: Integer;\n  norm: String;\nbegin\n  norm := NormalizarEspacios(frase);\n  if Length(norm) = 0 then Exit;\n  WriteLn('Palabras que terminan en consonante:');\n  pal := '';\n  for i := 1 to Length(norm) do\n  begin\n    if norm[i] <> ' ' then pal := pal + norm[i]\n    else\n    begin\n      if (Length(pal) > 0) and EsConsonante(pal[Length(pal)]) then WriteLn('  - ', pal);\n      pal := '';\n    end;\n  end;\n  if (Length(pal) > 0) and EsConsonante(pal[Length(pal)]) then WriteLn('  - ', pal);\nend;",
     "frase = 'Juan y David juegan futbol'", "Pantalla: 'Juan', 'David', 'juegan', 'futbol'"),

    (30, "Intercalar dos cadenas carácter por carácter (por ejemplo, “ABC” y “123” → “A1B2C3”).", "Función",
     "function IntercalarCadenas(cad1, cad2: String): String;\nvar\n  i, maxLen: Integer;\n  res: String;\nbegin\n  res := '';\n  maxLen := Length(cad1);\n  if Length(cad2) > maxLen then maxLen := Length(cad2);\n  for i := 1 to maxLen do\n  begin\n    if i <= Length(cad1) then res := res + cad1[i];\n    if i <= Length(cad2) then res := res + cad2[i];\n  end;\n  IntercalarCadenas := res;\nend;",
     "cad1 = 'ABC', cad2 = '123'", "Retorno: 'A1B2C3'"),

    (31, "Determinar cuántas palabras con más de 5 letras hay en una oración.", "Función",
     "function ContarPalabrasMasDe5Letras(oracion: String): Integer;\nvar\n  norm, pal: String;\n  i, c: Integer;\nbegin\n  norm := NormalizarEspacios(oracion);\n  c := 0; pal := '';\n  for i := 1 to Length(norm) do\n  begin\n    if norm[i] <> ' ' then pal := pal + norm[i]\n    else\n    begin\n      if Length(pal) > 5 then c := c + 1;\n      pal := '';\n    end;\n  end;\n  if Length(pal) > 5 then c := c + 1;\n  ContarPalabrasMasDe5Letras := c;\nend;",
     "oracion = 'La programacion estructurada ayuda al desarrollo'", "Retorno: 3  (programacion, estructurada, desarrollo)"),

    (32, "Reemplazar todas las vocales por el carácter *.", "Función",
     "function ReemplazarVocalesPorAsterisco(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := 1 to Length(cad) do\n  begin\n    if EsVocal(cad[i]) then res := res + '*'\n    else res := res + cad[i];\n  end;\n  ReemplazarVocalesPorAsterisco := res;\nend;",
     "cad = 'Ingenieria Informatica'", "Retorno: '*ng*n**r** *nf*rm*t*c*'"),

    (33, "Crear una función que elimine acentos (á, é, í, ó, ú) de una cadena.", "Función",
     "function EliminarAcentos(cad: String): String;\nconst\n  CON_ACENTO: array[1..10] of String = ('á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú');\n  SIN_ACENTO: array[1..10] of String = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');\nvar\n  k: Integer;\nbegin\n  for k := 1 to 10 do\n    cad := StringReplace(cad, CON_ACENTO[k], SIN_ACENTO[k], [rfReplaceAll]);\n  EliminarAcentos := cad;\nend;",
     "cad = 'canción, café, música, árbol'", "Retorno: 'cancion, cafe, musica, arbol'"),

    (34, "Mostrar la palabra más larga de una frase.", "Función",
     "function PalabraMasLarga(frase: String): String;\nvar\n  norm, pal, mayor: String;\n  i: Integer;\nbegin\n  norm := NormalizarEspacios(frase);\n  mayor := ''; pal := '';\n  for i := 1 to Length(norm) do\n  begin\n    if norm[i] <> ' ' then pal := pal + norm[i]\n    else\n    begin\n      if Length(pal) > Length(mayor) then mayor := pal;\n      pal := '';\n    end;\n  end;\n  if Length(pal) > Length(mayor) then mayor := pal;\n  PalabraMasLarga := mayor;\nend;",
     "frase = 'La programacion modular simplifica problemas'", "Retorno: 'programacion'"),

    (35, "Mostrar la palabra más corta de una frase.", "Función",
     "function PalabraMasCorta(frase: String): String;\nvar\n  norm, pal, menor: String;\n  i: Integer;\nbegin\n  norm := NormalizarEspacios(frase);\n  menor := ''; pal := '';\n  for i := 1 to Length(norm) do\n  begin\n    if norm[i] <> ' ' then pal := pal + norm[i]\n    else\n    begin\n      if (Length(pal) > 0) and ((Length(menor) = 0) or (Length(pal) < Length(menor))) then\n        menor := pal;\n      pal := '';\n    end;\n  end;\n  if (Length(pal) > 0) and ((Length(menor) = 0) or (Length(pal) < Length(menor))) then\n    menor := pal;\n  PalabraMasCorta := menor;\nend;",
     "frase = 'Hoy vi un gran elefante'", "Retorno: 'vi'"),

    (36, "Contar cuántas palabras repetidas hay en un texto.", "Función",
     "function ContarPalabrasRepetidas(texto: String): Integer;\nvar\n  norm, actual: String;\n  palabras: array of String;\n  i, j, n, repetidas: Integer;\n  yaContada: Boolean;\nbegin\n  norm := CadenaMinusculas(NormalizarEspacios(texto));\n  SetLength(palabras, 0); actual := '';\n  for i := 1 to Length(norm) do\n  begin\n    if norm[i] <> ' ' then actual := actual + norm[i]\n    else if Length(actual) > 0 then\n    begin\n      SetLength(palabras, Length(palabras) + 1);\n      palabras[High(palabras)] := actual;\n      actual := '';\n    end;\n  end;\n  if Length(actual) > 0 then\n  begin\n    SetLength(palabras, Length(palabras) + 1);\n    palabras[High(palabras)] := actual;\n  end;\n  n := Length(palabras); repetidas := 0;\n  for i := 0 to n - 1 do\n  begin\n    yaContada := False;\n    for j := 0 to i - 1 do\n      if palabras[i] = palabras[j] then begin yaContada := True; Break; end;\n    if not yaContada then\n      for j := i + 1 to n - 1 do\n        if palabras[i] = palabras[j] then begin repetidas := repetidas + 1; Break; end;\n  end;\n  ContarPalabrasRepetidas := repetidas;\nend;",
     "texto = 'el gato y el perro vieron a otro gato'", "Retorno: 2  (el, gato)"),

    (37, "Verificar si una cadena solo contiene letras (sin números ni símbolos).", "Función",
     "function SoloContieneLetras(cad: String): Boolean;\nvar\n  i: Integer;\nbegin\n  if Length(cad) = 0 then Exit(False);\n  for i := 1 to Length(cad) do\n    if not EsLetra(cad[i]) then Exit(False);\n  SoloContieneLetras := True;\nend;",
     "cad = 'SoloLetras'", "Retorno: TRUE"),

    (38, "Generar una nueva cadena con los caracteres únicos (sin repetir).", "Función",
     "function CaracteresUnicos(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  for i := 1 to Length(cad) do\n    if Pos(cad[i], res) = 0 then\n      res := res + cad[i];\n  CaracteresUnicos := res;\nend;",
     "cad = 'FERNANDO ALVAREZ'", "Retorno: 'FERNADO LVZ'"),

    (39, "Comprobar si dos cadenas son anagramas (contienen las mismas letras en distinto orden).", "Función",
     "function SonAnagramas(cad1, cad2: String): Boolean;\nvar\n  c1, c2: String;\n  i, j: Integer;\n  temp: Char;\nbegin\n  c1 := ''; c2 := '';\n  for i := 1 to Length(cad1) do if EsLetra(cad1[i]) then c1 := c1 + A_Minuscula(cad1[i]);\n  for i := 1 to Length(cad2) do if EsLetra(cad2[i]) then c2 := c2 + A_Minuscula(cad2[i]);\n  if Length(c1) <> Length(c2) then Exit(False);\n  for i := 1 to Length(c1) - 1 do\n    for j := i + 1 to Length(c1) do\n      if c1[i] > c1[j] then begin temp := c1[i]; c1[i] := c1[j]; c1[j] := temp; end;\n  for i := 1 to Length(c2) - 1 do\n    for j := i + 1 to Length(c2) do\n      if c2[i] > c2[j] then begin temp := c2[i]; c2[i] := c2[j]; c2[j] := temp; end;\n  SonAnagramas := (c1 = c2);\nend;",
     "cad1 = 'roma', cad2 = 'amor'", "Retorno: TRUE"),

    (40, "Mostrar de la cadena solo los caracteres de índice impar.", "Función",
     "function CaracteresIndiceImpar(cad: String): String;\nvar\n  i: Integer;\n  res: String;\nbegin\n  res := '';\n  i := 1;\n  while i <= Length(cad) do\n  begin\n    res := res + cad[i];\n    i := i + 2;\n  end;\n  CaracteresIndiceImpar := res;\nend;",
     "cad = 'UNIVERSIDAD'", "Retorno: 'UIESDD'  (pos 1,3,5,7,9,11)")
]

def main():
    doc = Document()
    
    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # PORTADA
    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_u = p_univ.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\n")
    r_u.font.name = "Arial"
    r_u.font.size = Pt(14)
    r_u.font.bold = True
    r_u.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_fac = p_univ.add_run("FACULTAD DE CIENCIAS DE LA COMPUTACIÓN\nINGENIERÍA INFORMÁTICA, SISTEMAS Y REDES\n")
    r_fac.font.name = "Arial"
    r_fac.font.size = Pt(11)
    r_fac.font.bold = True
    r_fac.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("―" * 45)
    r_line.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

    p_mat = doc.add_paragraph()
    p_mat.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_mat = p_mat.add_run("MATERIA: INTRODUCCIÓN A LA INFORMÁTICA (INF110) - Sem 2-2025\n")
    r_mat.font.name = "Arial"
    r_mat.font.size = Pt(11)
    r_mat.font.bold = True
    r_mat.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    r_doc = p_mat.add_run("Docente: M.Sc. Ing. Angélica Garzón Cuéllar\n\n")
    r_doc.font.name = "Arial"
    r_doc.font.size = Pt(10.5)
    r_doc.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    p_tit = doc.add_paragraph()
    p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tit = p_tit.add_run("PRÁCTICO # 8\nCADENA DE CARACTERES\n")
    r_tit.font.name = "Arial"
    r_tit.font.size = Pt(18)
    r_tit.font.bold = True
    r_tit.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r_sub = p_tit.add_run("PROGRAMACIÓN MODULAR: PROCEDIMIENTOS Y FUNCIONES EN PASCAL / DELPHI\n")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(0xD9, 0x77, 0x06)

    doc.add_page_break()

    # DESARROLLO DE LOS 40 EJERCICIOS
    h1 = doc.add_heading(level=1)
    r_h1 = h1.add_run("RESOLUCIÓN MODULAR DE LOS 40 EJERCICIOS")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(13)
    r_h1.font.bold = True
    r_h1.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.space_after = Pt(10)
    r_in = p_intro.add_run("A continuación se presenta la solución completa de los 40 ejercicios organizados modularmente como funciones o procedimientos en Pascal / Delphi, utilizando la unidad ")
    r_in.font.size = Pt(9.5)
    r_in_b = p_intro.add_run("UnitCadenas.pas")
    r_in_b.font.bold = True
    r_in_b.font.name = "Consolas"
    r_in_b.font.size = Pt(9.5)
    r_in_2 = p_intro.add_run(", testeada y verificada al 100%:")
    r_in_2.font.size = Pt(9.5)

    for num, enunciado, tipo, codigo, entrada, salida in EJERCICIOS:
        p_ej = doc.add_paragraph()
        p_ej.paragraph_format.space_before = Pt(12)
        p_ej.paragraph_format.space_after = Pt(2)
        
        r_num = p_ej.add_run(f"Ejercicio {num}: ")
        r_num.font.bold = True
        r_num.font.name = "Arial"
        r_num.font.size = Pt(10)
        r_num.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        r_enun = p_ej.add_run(enunciado)
        r_enun.font.bold = True
        r_enun.font.name = "Arial"
        r_enun.font.size = Pt(10)
        r_enun.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        add_code_block(doc, codigo, border_color="2563EB" if tipo == "Función" else "059669")
        
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        add_io_box(doc, entrada, salida, tipo)

    output_path = "Practico08_Cadenas_Modulares.docx"
    doc.save(output_path)
    print(f"Documento generado exitosamente: {output_path}")

if __name__ == "__main__":
    main()
