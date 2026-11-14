program TestNumeroNatural;

{$mode delphi}

uses
  SysUtils, UCNatural;

var
  Numero: NumeroNatural;
begin
  Writeln('=== PRUEBA UNITARIA DE LA CLASE NumeroNatural (INF110-Z2) ===');
  
  // 1. Instanciación mediante Constructor
  Numero := NumeroNatural.Create;
  Writeln('1. Constructor ejecutado. Valor inicial: ', Numero.ObtenerValor);
  
  // 2. Asignación mediante Setter
  Numero.CambiarValor(4826);
  Writeln('2. CambiarValor(4826) ejecutado. Valor actual: ', Numero.ObtenerValor);
  
  // 3. Método ContarDigitos
  Writeln('3. ContarDigitos() de 4826: ', Numero.ContarDigitos, ' digitos (Esperado: 4)');
  
  // 4. Prueba con 0
  Numero.CambiarValor(0);
  Writeln('4. CambiarValor(0) ejecutado. ContarDigitos(): ', Numero.ContarDigitos, ' digitos (Esperado: 1)');

  // 5. Destrucción del objeto
  Numero.Free;
  Writeln('5. Objeto liberado con exito.');
  Writeln('=== FIN DE LA PRUEBA ===');
end.

