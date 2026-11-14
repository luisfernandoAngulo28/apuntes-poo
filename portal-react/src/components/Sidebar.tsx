import React, { useState } from 'react';
import { Search, X } from 'lucide-react';

interface SidebarItem {
  id: string;
  label: string;
  icon: string;
  badge?: string;
  badgeColor?: string;
}

interface SidebarCategory {
  titulo: string;
  items: SidebarItem[];
}

interface Props {
  isOpen: boolean;
  onClose: () => void;
  activeSection: string;
  onSelectSection: (id: string) => void;
}

export const Sidebar: React.FC<Props> = ({ isOpen, onClose, activeSection, onSelectSection }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const categorias: SidebarCategory[] = [
    {
      titulo: '👑 Trilogía Examen Final (100p)',
      items: [
        { id: 'trilogia-cockpit', label: 'Cockpit Trilogía 3-en-1', badge: 'CORE', badgeColor: '#6366f1', icon: '👑' },
        { id: 'series-hub', label: '1. Series Numéricas', badge: '30 pts', badgeColor: '#f59e0b', icon: '⚡' },
        { id: 'numeros-hub', label: '2. Números & Dígitos', badge: '35 pts', badgeColor: '#38bdf8', icon: '🔢' },
        { id: 'cadenas-hub', label: '3. Cadenas de Texto', badge: '35 pts', badgeColor: '#a855f7', icon: '🔤' }
      ]
    },
    {
      titulo: '🏆 Banco Oficial de Exámenes',
      items: [
        { id: 'examenes-finales', label: '7 Modelos Examen Final', badge: '28 Prob', badgeColor: '#ef4444', icon: '📋' },
        { id: 'examenes-parciales', label: '7 Modelos 2do Parcial', badge: '2024-2022', badgeColor: '#f59e0b', icon: '📝' }
      ]
    },
    {
      titulo: '🧰 Hojas de Atajos (Cheat Sheets)',
      items: [
        { id: 'atajos-series', label: 'Series (Divide y Vencerás)', icon: '⚡' },
        { id: 'atajos-numeros', label: 'Dígitos & Leyes mod/div', icon: '🔢' },
        { id: 'atajos-cadenas', label: 'Strings & Subcadenas', icon: '🔤' },
        { id: 'atajos-poo', label: 'POO: Clase NumeroNatural', icon: '🏛️' }
      ]
    },
    {
      titulo: '🔬 Laboratorios & Simuladores',
      items: [
        { id: 'lab-trazas', label: 'Generador de Trazas Formales', badge: 'Fase 4', badgeColor: '#0284c7', icon: '📊' },
        { id: 'lab-simulador', label: 'Simulacro Timer (90 min)', badge: '100p', badgeColor: '#10b981', icon: '⏱️' }
      ]
    },
    {
      titulo: '📥 Biblioteca de Descargas',
      items: [
        { id: 'descargas-docx', label: '5 Documentos Word (.docx)', badge: 'Formato', badgeColor: '#3b82f6', icon: '📦' },
        { id: 'descargas-pas', label: '7 Unidades Pascal (.pas)', badge: 'Clean Code', badgeColor: '#10b981', icon: '💾' }
      ]
    }
  ];

  return (
    <>
      {/* Overlay para móviles */}
      <div
        onClick={onClose}
        style={{
          display: isOpen ? 'block' : 'none',
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100vw',
          height: '100vh',
          background: 'rgba(0, 0, 0, 0.7)',
          backdropFilter: 'blur(4px)',
          zIndex: 10000
        }}
      />

      {/* Barra Lateral (Sidebar) */}
      <aside
        style={{
          width: isOpen ? '280px' : '0',
          minWidth: isOpen ? '280px' : '0',
          background: '#080d19',
          borderRight: isOpen ? '1px solid rgba(255, 255, 255, 0.08)' : 'none',
          height: '100vh',
          position: 'sticky',
          top: 0,
          display: 'flex',
          flexDirection: 'column',
          zIndex: 10001,
          transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
          overflow: 'hidden',
          boxShadow: isOpen ? '4px 0 25px rgba(0, 0, 0, 0.5)' : 'none'
        }}
      >
        {/* Encabezado del sidebar */}
        <div style={{
          padding: '1rem',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          background: '#060a14'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span style={{ fontSize: '1.3rem' }}>🏛️</span>
            <div>
              <strong style={{ color: '#fff', fontSize: '0.82rem', display: 'block' }}>INF-110 · UAGRM</strong>
              <span style={{ color: '#94a3b8', fontSize: '0.7rem' }}>Campus Virtual Moodle</span>
            </div>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'transparent',
              border: 'none',
              color: '#94a3b8',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '0.2rem'
            }}
          >
            <X size={18} />
          </button>
        </div>

        {/* Buscador dentro del sidebar */}
        <div style={{ padding: '0.6rem 0.8rem', borderBottom: '1px solid rgba(255, 255, 255, 0.05)' }}>
          <div style={{
            position: 'relative',
            display: 'flex',
            alignItems: 'center'
          }}>
            <Search size={14} color="#64748b" style={{ position: 'absolute', left: '8px' }} />
            <input
              type="text"
              placeholder="🔍 Filtrar sección..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              style={{
                width: '100%',
                background: '#050812',
                color: '#fff',
                border: '1px solid #334155',
                padding: '0.35rem 0.5rem 0.35rem 1.8rem',
                borderRadius: '6px',
                fontSize: '0.75rem',
                outline: 'none'
              }}
            />
          </div>
        </div>

        {/* Contenido con scroll del sidebar */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '0.6rem 0.6rem' }}>
          {categorias.map((cat, idx) => {
            const itemsFiltrados = cat.items.filter(item =>
              item.label.toLowerCase().includes(searchTerm.toLowerCase())
            );

            if (itemsFiltrados.length === 0) return null;

            return (
              <div key={idx} style={{ marginBottom: '1rem' }}>
                <div style={{
                  fontSize: '0.7rem',
                  fontWeight: 800,
                  textTransform: 'uppercase',
                  color: '#64748b',
                  letterSpacing: '0.05em',
                  padding: '0.2rem 0.5rem 0.3rem',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.3rem'
                }}>
                  {cat.titulo}
                </div>

                {itemsFiltrados.map((item) => {
                  const activo = activeSection === item.id;
                  return (
                    <div
                      key={item.id}
                      onClick={() => onSelectSection(item.id)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.5rem',
                        padding: '0.45rem 0.65rem',
                        borderRadius: '6px',
                        fontSize: '0.8rem',
                        fontWeight: activo ? 700 : 500,
                        color: activo ? '#38bdf8' : '#94a3b8',
                        background: activo ? 'rgba(14, 165, 233, 0.15)' : 'transparent',
                        borderLeft: activo ? '3px solid #0284c7' : '3px solid transparent',
                        cursor: 'pointer',
                        marginBottom: '0.15rem',
                        transition: 'all 0.15s ease'
                      }}
                    >
                      <span>{item.icon}</span>
                      <span style={{ flex: 1 }}>{item.label}</span>
                      {item.badge && (
                        <span style={{
                          fontSize: '0.65rem',
                          padding: '0.1rem 0.4rem',
                          borderRadius: '10px',
                          fontWeight: 800,
                          background: item.badgeColor ? `${item.badgeColor}22` : 'rgba(255,255,255,0.1)',
                          color: item.badgeColor || '#cbd5e1'
                        }}>
                          {item.badge}
                        </span>
                      )}
                    </div>
                  );
                })}
              </div>
            );
          })}
        </div>

        {/* Footer del sidebar */}
        <div style={{
          padding: '0.75rem 1rem',
          borderTop: '1px solid rgba(255, 255, 255, 0.08)',
          background: '#060a14',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          fontSize: '0.72rem',
          color: '#64748b'
        }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', color: '#34d399', fontWeight: 700 }}>
            <span>🟢</span> UAGRM Online
          </span>
          <span>v2.0 (React)</span>
        </div>
      </aside>
    </>
  );
};
