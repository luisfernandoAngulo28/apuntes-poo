import React from 'react';

interface Props {
  descripcion: string;
  columnas: string[];
  filas: (string | number)[][];
}

export const TrazaViewer: React.FC<Props> = ({ descripcion, columnas, filas }) => {
  return (
    <div style={{
      background: '#070d19',
      border: '1px solid rgba(255, 255, 255, 0.08)',
      borderRadius: '8px',
      overflow: 'hidden',
      marginTop: '0.75rem'
    }}>
      <div style={{
        padding: '0.5rem 0.85rem',
        background: 'rgba(2, 132, 199, 0.1)',
        borderBottom: '1px solid rgba(2, 132, 199, 0.2)',
        fontSize: '0.78rem',
        fontWeight: 700,
        color: '#38bdf8'
      }}>
        📊 Fase 4: Prueba de Escritorio Formal · {descripcion}
      </div>

      <div style={{ overflowX: 'auto', padding: '0.5rem' }}>
        <table style={{
          width: '100%',
          borderCollapse: 'collapse',
          fontSize: '0.8rem',
          textAlign: 'left'
        }}>
          <thead>
            <tr style={{ background: '#0f172a', borderBottom: '2px solid rgba(255,255,255,0.1)' }}>
              {columnas.map((col, idx) => (
                <th key={idx} style={{ padding: '0.5rem 0.75rem', color: '#93c5fd', fontWeight: 800 }}>
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filas.map((fila, rowIdx) => (
              <tr
                key={rowIdx}
                style={{
                  borderBottom: '1px solid rgba(255,255,255,0.04)',
                  background: rowIdx % 2 === 0 ? 'rgba(255,255,255,0.015)' : 'transparent'
                }}
              >
                {fila.map((celda, cellIdx) => (
                  <td
                    key={cellIdx}
                    style={{
                      padding: '0.45rem 0.75rem',
                      color: cellIdx === fila.length - 1 ? '#34d399' : '#cbd5e1',
                      fontWeight: cellIdx === fila.length - 1 ? 700 : 400,
                      fontFamily: 'var(--font-mono)'
                    }}
                  >
                    {celda}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

