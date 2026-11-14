# -*- coding: utf-8 -*-
"""
Generador del Módulo Interactivo de Series con Programación Modular (Delphi VCL)
Basado en el formulario oficial y código de la clase:
- Form1: "Funciones y Procedimiento Series"
- 1. Suma Doble (1 + 2 + 4 + 8 + 16 = 31)
- 2. Suma Factorial (1! + 2! + 3! + 4! + 5! = 153)
- 3. Suma Cuadrática (1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55)
"""

def build_modulo_series_html():
    return """
      <!-- =====================================================================
           BLOQUE OFICIAL: FORMULARIO DELPHI VCL DE SERIES (CLASE ING. GARZÓN)
           ===================================================================== -->
      <div id="lab-delphi-series-oficial" style="background: rgba(15, 23, 42, 0.95); border: 2px solid #38bdf8; border-radius: 12px; padding: 1.75rem; margin-bottom: 2.5rem; box-shadow: 0 8px 30px rgba(0,0,0,0.5);">
        
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
          <h3 style="color: #38bdf8; margin: 0; font-size: 1.3rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🖥️</span> Formulario Delphi VCL: «Funciones y Procedimiento Series»
          </h3>
          <span style="font-size: 0.8rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8; padding: 0.25rem 0.65rem; border-radius: 4px; border: 1px solid rgba(56, 189, 248, 0.3); font-weight: 700;">
            unit Series.pas • Metodología Oficial
          </span>
        </div>

        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">
          Implementación modular oficial del formulario de clase para el cálculo de series con variables globales <code>numero, contador: Integer;</code> y funciones con bucle <code>while numero &gt;= contador do</code>:
        </p>

        <!-- SIMULADOR INTERACTIVO DEL FORMULARIO DELPHI (IDÉNTICO A LA FOTO) -->
        <div style="max-width: 620px; margin: 0 auto 2rem auto; background: #e2e8f0; border: 2px solid #94a3b8; border-radius: 6px; box-shadow: 0 10px 35px rgba(0,0,0,0.6); overflow: hidden; font-family: 'Segoe UI', Tahoma, sans-serif;">
          
          <!-- BARRA DE TÍTULO DELPHI / WINDOWS -->
          <div style="background: linear-gradient(90deg, #1e3a8a, #0284c7); padding: 6px 12px; display: flex; justify-content: space-between; align-items: center; color: #ffffff;">
            <div style="display: flex; align-items: center; gap: 6px; font-size: 0.85rem; font-weight: 600;">
              <span style="font-size: 0.9rem;">🏛️</span>
              <span>Form1</span>
            </div>
            <div style="display: flex; gap: 4px;">
              <span style="display: inline-block; width: 14px; height: 14px; background: rgba(255,255,255,0.2); text-align: center; line-height: 12px; font-size: 10px; border-radius: 2px;">_</span>
              <span style="display: inline-block; width: 14px; height: 14px; background: rgba(255,255,255,0.2); text-align: center; line-height: 12px; font-size: 10px; border-radius: 2px;">□</span>
              <span style="display: inline-block; width: 14px; height: 14px; background: #ef4444; text-align: center; line-height: 12px; font-size: 10px; border-radius: 2px; cursor: pointer;" onclick="seriesResetForm()">✕</span>
            </div>
          </div>

          <!-- CUERPO DEL FORMULARIO (GRID DE PUNTOS TIPO RAD STUDIO FORM DESIGNER) -->
          <div style="background: #cbd5e1; background-image: radial-gradient(#64748b 1px, transparent 1px); background-size: 10px 10px; padding: 1.75rem 2rem; color: #0f172a;">
            
            <h4 style="text-align: center; margin: 0 0 1.5rem 0; font-size: 1.25rem; font-weight: 800; color: #0f172a; letter-spacing: -0.02em;">
              Funciones y Procedimiento Series
            </h4>

            <!-- CAMPO ENTRADA -->
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
              <label style="width: 110px; font-weight: 800; font-size: 1rem; color: #0f172a;">Entrada</label>
              <input type="number" id="vclSeriesInput" value="5" min="1" max="25" style="width: 220px; background: #ffffff !important; color: #0f172a !important; border: 1.5px solid #64748b !important; padding: 6px 10px; font-size: 1rem; font-family: 'Fira Code', monospace; font-weight: 700; border-radius: 2px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.15);">
            </div>

            <!-- CAMPO RESULTADO -->
            <div style="display: flex; align-items: center; margin-bottom: 1.25rem;">
              <label style="width: 110px; font-weight: 800; font-size: 1rem; color: #0f172a;">Resultado</label>
              <input type="text" id="vclSeriesOutput" readonly value="Resultado aquí..." style="width: 220px; background: #f8fafc !important; color: #0284c7 !important; border: 1.5px solid #64748b !important; padding: 6px 10px; font-size: 1.05rem; font-family: 'Fira Code', monospace; font-weight: 800; border-radius: 2px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.15);">
            </div>

            <!-- BOTÓN REGISTRAR -->
            <div style="margin-bottom: 1.5rem;">
              <button onclick="vclRegistrarNumero()" style="background: #e2e8f0; border: 1.5px solid #475569; padding: 6px 18px; font-weight: 800; font-size: 0.95rem; color: #0f172a; border-radius: 3px; cursor: pointer; box-shadow: 1px 1px 0 #fff inset, 1px 1px 2px rgba(0,0,0,0.2);">
                Registrar
              </button>
              <span id="vclRegistradoBadge" style="margin-left: 10px; font-size: 0.85rem; font-weight: 700; color: #059669; display: none;">
                ✓ Registrado n = 5
              </span>
            </div>

            <!-- BOTONERA DE LAS 3 SERIES + CLOSE -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
              <button onclick="vclEjecutarSerie('doble')" style="flex: 1; min-width: 110px; background: #e2e8f0; border: 1.5px solid #475569; padding: 8px 12px; font-weight: 800; font-size: 0.92rem; color: #0f172a; border-radius: 3px; cursor: pointer; box-shadow: 1px 1px 0 #fff inset, 1px 1px 2px rgba(0,0,0,0.2);">
                SumaDoble
              </button>
              <button onclick="vclEjecutarSerie('factorial')" style="flex: 1; min-width: 120px; background: #e2e8f0; border: 1.5px solid #475569; padding: 8px 12px; font-weight: 800; font-size: 0.92rem; color: #0f172a; border-radius: 3px; cursor: pointer; box-shadow: 1px 1px 0 #fff inset, 1px 1px 2px rgba(0,0,0,0.2);">
                Sumafactorial
              </button>
              <button onclick="vclEjecutarSerie('cuadratica')" style="flex: 1; min-width: 130px; background: #e2e8f0; border: 1.5px solid #475569; padding: 8px 12px; font-weight: 800; font-size: 0.92rem; color: #0f172a; border-radius: 3px; cursor: pointer; box-shadow: 1px 1px 0 #fff inset, 1px 1px 2px rgba(0,0,0,0.2);">
                suma cuadratica
              </button>
              <button onclick="seriesResetForm()" style="background: #e2e8f0; border: 1.5px solid #475569; padding: 8px 16px; font-weight: 800; font-size: 0.92rem; color: #dc2626; border-radius: 3px; cursor: pointer; box-shadow: 1px 1px 0 #fff inset, 1px 1px 2px rgba(0,0,0,0.2);">
                close
              </button>
            </div>

          </div>
        </div>

        <!-- EXPLICACIÓN MATEMÁTICA Y PRUEBAS DE ESCRITORIO DE LAS 3 SERIES -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 2rem;">
          
          <!-- 1. SUMA DOBLE -->
          <div style="background: #0b1120; border: 1.5px solid #10b981; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #34d399; font-weight: 800; font-size: 1rem;">📈 1. Suma Doble (Geométrica)</span>
              <span style="font-size: 0.75rem; background: rgba(16, 185, 129, 0.2); color: #34d399; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Razón ×2</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.5rem;">
              Suma de potencias sucesivas de 2. Para cada término, la variable <code>doble</code> se duplica:
            </p>
            <div style="background: #070a13; border: 1px solid #1e293b; border-radius: 4px; padding: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.82rem; color: #38bdf8; margin-bottom: 0.75rem;">
              n=5 &rarr; 1 + 2 + 4 + 8 + 16 = <strong>31</strong>
            </div>
            <div style="font-size: 0.82rem; color: #94a3b8; line-height: 1.4;">
              • <code>sumadordoble := sumadordoble + doble;</code><br/>
              • <code>doble := doble * 2;</code><br/>
              • <code>contador := contador + 1;</code>
            </div>
          </div>

          <!-- 2. SUMA FACTORIAL -->
          <div style="background: #0b1120; border: 1.5px solid #38bdf8; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #38bdf8; font-weight: 800; font-size: 1rem;">❗ 2. Suma Factorial</span>
              <span style="font-size: 0.75rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 2px 6px; border-radius: 4px; font-weight: 700;">1! + 2! + ... + n!</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.5rem;">
              Acumula factoriales sucesivos sin recalcular desde 1 en cada paso, multiplicando por el contador:
            </p>
            <div style="background: #070a13; border: 1px solid #1e293b; border-radius: 4px; padding: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.82rem; color: #38bdf8; margin-bottom: 0.75rem;">
              n=5 &rarr; 1 + 2 + 6 + 24 + 120 = <strong>153</strong>
            </div>
            <div style="font-size: 0.82rem; color: #94a3b8; line-height: 1.4;">
              • <code>factorial := factorial * contador;</code><br/>
              • <code>sumadorfactorial := sumadorfactorial + factorial;</code><br/>
              • <code>contador := contador + 1;</code>
            </div>
          </div>

          <!-- 3. SUMA CUADRÁTICA -->
          <div style="background: #0b1120; border: 1.5px solid #fbbf24; border-radius: 8px; padding: 1.2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #fbbf24; font-weight: 800; font-size: 1rem;">📐 3. Suma Cuadrática</span>
              <span style="font-size: 0.75rem; background: rgba(245, 158, 11, 0.2); color: #fbbf24; padding: 2px 6px; border-radius: 4px; font-weight: 700;">1² + 2² + ... + n²</span>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.5rem;">
              Suma de los cuadrados de los primeros <code>n</code> números naturales:
            </p>
            <div style="background: #070a13; border: 1px solid #1e293b; border-radius: 4px; padding: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.82rem; color: #38bdf8; margin-bottom: 0.75rem;">
              n=5 &rarr; 1 + 4 + 9 + 16 + 25 = <strong>55</strong>
            </div>
            <div style="font-size: 0.82rem; color: #94a3b8; line-height: 1.4;">
              • <code>cuadratica := contador * contador;</code><br/>
              • <code>sumadorCuadratica := sumadorCuadratica + cuadratica;</code><br/>
              • <code>contador := contador + 1;</code>
            </div>
          </div>

        </div>

        <!-- CÓDIGO DELPHI VCL COMPLETO (unit Series.pas) -->
        <div style="background: #070a13; border: 1px solid #334155; border-radius: 8px; padding: 1.25rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
            <h4 style="color: #38bdf8; margin: 0; font-size: 1rem;">
              📄 Código Delphi VCL Completo: <code>unit Series.pas</code>
            </h4>
            <button class="btn-copy" onclick="copySnippet('codeDelphiSeries')" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">
              📋 Copiar Código Delphi
            </button>
          </div>
          <pre id="codeDelphiSeries" style="color: #cbd5e1; font-family: 'Fira Code', monospace; font-size: 0.82rem; overflow-x: auto; margin: 0; line-height: 1.4;">
unit Series;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Button1: TButton;
    Edit2: TEdit;
    Label3: TLabel;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
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
  // Variables Globales (Metodología Ing. Angélica Garzón)
  numero, contador: Integer;

// Funciones modulares
function sumaDoble(numero, contador: Integer): Integer;
function sumafactorial(numero, contador: Integer): Integer;
function sumaCuadratica(numero, contador: Integer): Integer;

implementation

{$R *.dfm}

// 1. Suma Doble: 1 + 2 + 4 + 8 + 16 + ...
function sumaDoble(numero, contador: Integer): Integer;
var
  doble, sumadordoble: Integer;
begin
  sumadordoble := 0; contador := 1; doble := 1;
  while numero >= contador do
  begin
    sumadordoble := sumadordoble + doble;
    doble := doble * 2;
    contador := contador + 1;
  end;
  Result := sumadordoble;
end;

// 2. Suma Factorial: 1! + 2! + 3! + 4! + 5! = 153
function sumafactorial(numero, contador: Integer): Integer;
var
  factorial, sumadorfactorial: Integer;
begin
  sumadorfactorial := 0; contador := 1; factorial := 1;
  while numero >= contador do
  begin
    factorial := factorial * contador;
    sumadorfactorial := sumadorfactorial + factorial;
    contador := contador + 1;
  end;
  Result := sumadorfactorial;
end;

// 3. Suma Cuadrática: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
function sumaCuadratica(numero, contador: Integer): Integer;
var
  cuadratica, sumadorCuadratica: Integer;
begin
  sumadorCuadratica := 0; contador := 1; cuadratica := 1;
  while numero >= contador do
  begin
    cuadratica := contador * contador;
    sumadorCuadratica := sumadorCuadratica + cuadratica;
    contador := contador + 1;
  end;
  Result := sumadorCuadratica;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  numero := StrToInt(Edit1.Text);
  ShowMessage('Registrado con exito n=' + IntToStr(numero));
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumaDoble(numero, contador));
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumafactorial(numero, contador));
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Edit2.Text := IntToStr(sumaCuadratica(numero, contador));
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
  Close;
end;

end.</pre>
        </div>

      </div>
"""

