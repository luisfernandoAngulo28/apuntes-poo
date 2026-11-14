object FormExamenParcial2: TFormExamenParcial2
  Left = 0
  Top = 0
  Caption = 'Simulador Banco de 2do Parcial - Ing. Angélica Garzón'
  ClientHeight = 560
  ClientWidth = 720
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  Position = poScreenCenter
  TextHeight = 15
  object LabelTitulo: TLabel
    Left = 24
    Top = 16
    Width = 530
    Height = 25
    Caption = 'Banco Maestro: 7 Modelos Reales de 2do Parcial (INF110-Z2)'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clHotLight
    Font.Height = -19
    Font.Name = 'Segoe UI'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object LabelEntrada1: TLabel
    Left = 32
    Top = 64
    Width = 138
    Height = 15
    Caption = 'Entrada 1 (N / X / Cadena):'
  end
  object EditEntrada1: TEdit
    Left = 180
    Top = 60
    Width = 260
    Height = 23
    TabOrder = 0
    Text = 'Segundo examen parcial'
  end
  object LabelEntrada2: TLabel
    Left = 460
    Top = 64
    Width = 92
    Height = 15
    Caption = 'Entrada 2 (K / N):'
  end
  object EditEntrada2: TEdit
    Left = 560
    Top = 60
    Width = 80
    Height = 23
    TabOrder = 1
    Text = '2'
  end
  object LabelResultado: TLabel
    Left = 32
    Top = 104
    Width = 55
    Height = 15
    Caption = 'Resultado:'
  end
  object EditResultado: TEdit
    Left = 180
    Top = 100
    Width = 460
    Height = 23
    ReadOnly = True
    TabOrder = 2
  end
  object Button2024_P1: TButton
    Left = 32
    Top = 150
    Width = 200
    Height = 32
    Caption = '2024-1 Z2: P1 Serie i^i / D_i'
    TabOrder = 3
    OnClick = Button2024_P1Click
  end
  object Button2024_P2: TButton
    Left = 240
    Top = 150
    Width = 220
    Height = 32
    Caption = '2024-1 Z2: P2 MenorImp / MayorPar'
    TabOrder = 4
    OnClick = Button2024_P2Click
  end
  object Button2024_P3a: TButton
    Left = 470
    Top = 150
    Width = 200
    Height = 32
    Caption = '2024-1 Z2: P3a Invertir Última'
    TabOrder = 5
    OnClick = Button2024_P3aClick
  end
  object Button2024_P3b: TButton
    Left = 32
    Top = 190
    Width = 200
    Height = 32
    Caption = '2024-1 Z2: P3b Eliminar Consonantes'
    TabOrder = 6
    OnClick = Button2024_P3bClick
  end
  object Button2024R_P1: TButton
    Left = 240
    Top = 190
    Width = 220
    Height = 32
    Caption = '2024-1 Z2-R: P1 Potencias de X'
    TabOrder = 7
    OnClick = Button2024R_P1Click
  end
  object Button2024R_P2: TButton
    Left = 470
    Top = 190
    Width = 200
    Height = 32
    Caption = '2024-1 Z2-R: P2 Vocal Inicial Mayús'
    TabOrder = 8
    OnClick = Button2024R_P2Click
  end
  object Button2024SF_P1: TButton
    Left = 32
    Top = 235
    Width = 200
    Height = 32
    Caption = '2024-1 SF: P1 Serie 2*i / Fib!'
    TabOrder = 9
    OnClick = Button2024SF_P1Click
  end
  object Button2024SF_P2: TButton
    Left = 240
    Top = 235
    Width = 220
    Height = 32
    Caption = '2024-1 SF: P2 Eliminar Desde Pos K'
    TabOrder = 10
    OnClick = Button2024SF_P2Click
  end
  object Button2024SF_P3: TButton
    Left = 470
    Top = 235
    Width = 200
    Height = 32
    Caption = '2024-1 SF: P3 1ra Letra Mayúscula'
    TabOrder = 11
    OnClick = Button2024SF_P3Click
  end
  object Button2023_2_P2: TButton
    Left = 32
    Top = 280
    Width = 200
    Height = 32
    Caption = '2023-2 Z2: P2 Eliminar Dígito Pos K'
    TabOrder = 12
    OnClick = Button2023_2_P2Click
  end
  object Button2023_2_P3: TButton
    Left = 240
    Top = 280
    Width = 220
    Height = 32
    Caption = '2023-2 Z2: P3 Contar Vocales/Pal'
    TabOrder = 13
    OnClick = Button2023_2_P3Click
  end
  object Button2023_1_P1: TButton
    Left = 470
    Top = 280
    Width = 200
    Height = 32
    Caption = '2023-1 Z2: P1 Serie SF (Sin Power)'
    TabOrder = 14
    OnClick = Button2023_1_P1Click
  end
  object Button2023_1_P3: TButton
    Left = 32
    Top = 325
    Width = 200
    Height = 32
    Caption = '2023-1 Z2: P3 Invertir Cada Palabra'
    TabOrder = 15
    OnClick = Button2023_1_P3Click
  end
  object ButtonBurbuja_2daOrd: TButton
    Left = 240
    Top = 325
    Width = 220
    Height = 32
    Caption = 'Pizarra: Ordenar 2da Palabra'
    TabOrder = 16
    OnClick = ButtonBurbuja_2daOrdClick
  end
  object ButtonBurbuja_2daInv: TButton
    Left = 470
    Top = 325
    Width = 200
    Height = 32
    Caption = 'Pizarra: Invertir 2da Palabra'
    TabOrder = 17
    OnClick = ButtonBurbuja_2daInvClick
  end
  object ButtonBurbuja_Ultima: TButton
    Left = 240
    Top = 370
    Width = 220
    Height = 32
    Caption = 'Pizarra: Ordenar Última Palabra'
    TabOrder = 18
    OnClick = ButtonBurbuja_UltimaClick
  end
  object ButtonSalir: TButton
    Left = 540
    Top = 480
    Width = 130
    Height = 36
    Caption = 'Cerrar'
    TabOrder = 19
    OnClick = ButtonSalirClick
  end
end

