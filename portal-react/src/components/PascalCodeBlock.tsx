import React, { useState } from 'react';
import { Copy, Check } from 'lucide-react';

interface Props {
  codigo: string;
  titulo?: string;
}

export const PascalCodeBlock: React.FC<Props> = ({ codigo, titulo = 'Código Pascal / Delphi (Clean Code)' }) => {
  const [copiado, setCopiado] = useState(false);

  const handleCopiar = () => {
    navigator.clipboard.writeText(codigo);
    setCopiado(true);
    setTimeout(() => setCopiado(false), 2000);
  };

  const lineas = codigo.split('\n');

  return (
    <div style={{
      background: '#040812',
      border: '1px solid rgba(255, 255, 255, 0.1)',
      borderRadius: '8px',
      overflow: 'hidden',
      marginTop: '0.75rem',
      boxShadow: '0 4px 15px rgba(0,0,0,0.4)'
    }}>
      {/* Barra superior del bloque de código */}
      <div style={{
        background: '#090f1d',
        padding: '0.5rem 0.85rem',
        borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        fontSize: '0.75rem',
        color: '#94a3b8'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', fontWeight: 700, color: '#38bdf8' }}>
          <span>💻</span>
          <span>{titulo}</span>
        </div>
        <button
          onClick={handleCopiar}
          className="btn btn-secondary"
          style={{ padding: '0.25rem 0.6rem', fontSize: '0.72rem' }}
          title="Copiar código Pascal"
        >
          {copiado ? <Check size={14} color="#34d399" /> : <Copy size={14} />}
          <span>{copiado ? '¡Copiado!' : 'Copiar'}</span>
        </button>
      </div>

      {/* Contenido con números de línea */}
      <div style={{
        display: 'flex',
        overflowX: 'auto',
        fontFamily: 'var(--font-mono)',
        fontSize: '0.82rem',
        padding: '0.85rem 0.5rem',
        lineHeight: 1.6
      }}>
        {/* Números de línea */}
        <div style={{
          userSelect: 'none',
          color: '#475569',
          textAlign: 'right',
          paddingRight: '0.85rem',
          borderRight: '1px solid rgba(255,255,255,0.06)'
        }}>
          {lineas.map((_, i) => (
            <div key={i}>{i + 1}</div>
          ))}
        </div>

        {/* Código fuente */}
        <pre style={{
          paddingLeft: '0.85rem',
          color: '#e2e8f0',
          margin: 0,
          whiteSpace: 'pre',
          fontFamily: 'inherit'
        }}>
          {codigo}
        </pre>
      </div>
    </div>
  );
};

