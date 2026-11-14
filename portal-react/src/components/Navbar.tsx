import React from 'react';
import { Menu, ShieldCheck } from 'lucide-react';

interface Props {
  onToggleSidebar: () => void;
  sidebarOpen: boolean;
}

export const Navbar: React.FC<Props> = ({ onToggleSidebar, sidebarOpen }) => {
  return (
    <header style={{
      position: 'sticky',
      top: 0,
      zIndex: 9999,
      background: 'rgba(9, 14, 26, 0.92)',
      backdropFilter: 'blur(12px)',
      borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
      padding: '0.65rem 1.25rem',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between'
    }}>
      {/* Lado izquierdo: Botón menú y Logo UAGRM */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.85rem' }}>
        <button
          onClick={onToggleSidebar}
          className="btn btn-secondary"
          style={{ padding: '0.4rem 0.75rem', fontSize: '0.8rem', gap: '0.4rem' }}
          title="Colapsar / Mostrar Sidebar (Ctrl + B)"
        >
          <Menu size={16} />
          <span>{sidebarOpen ? 'Menú' : 'Abrir'}</span>
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <span style={{ fontSize: '1.4rem' }}>🏛️</span>
          <div>
            <strong style={{ color: '#ffffff', fontSize: '0.88rem', display: 'block', lineHeight: 1.2 }}>
              UAGRM · FICCT · INF-110 (React SPA)
            </strong>
            <span style={{ color: '#94a3b8', fontSize: '0.72rem' }}>
              M.Sc. Ing. Angélica Garzón Cuéllar · Examen Final
            </span>
          </div>
        </div>
      </div>

      {/* Lado derecho: Badges informativos */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
        <span style={{
          background: 'rgba(16, 185, 129, 0.12)',
          border: '1px solid rgba(16, 185, 129, 0.3)',
          color: '#34d399',
          fontSize: '0.75rem',
          padding: '0.25rem 0.6rem',
          borderRadius: '20px',
          fontWeight: 700,
          display: 'flex',
          alignItems: 'center',
          gap: '0.35rem'
        }}>
          <ShieldCheck size={14} /> 100% Offline Ready
        </span>

        <span style={{
          background: 'rgba(56, 189, 248, 0.12)',
          border: '1px solid rgba(56, 189, 248, 0.3)',
          color: '#38bdf8',
          fontSize: '0.75rem',
          padding: '0.25rem 0.6rem',
          borderRadius: '20px',
          fontWeight: 700
        }}>
          React + Vite + TS
        </span>
      </div>
    </header>
  );
};
