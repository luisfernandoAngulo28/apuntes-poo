import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { CockpitTrilogia } from './components/CockpitTrilogia';
import { ModelosVisuales } from './components/ModelosVisuales';
import { BookOpen, FileText, Award, ShieldCheck, Download } from 'lucide-react';

export const App: React.FC = () => {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [activeSection, setActiveSection] = useState('trilogia-cockpit');

  // Atajo de teclado: Ctrl + B para colapsar/abrir el sidebar
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && (e.key === 'b' || e.key === 'B')) {
        e.preventDefault();
        setSidebarOpen(prev => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--bg-dark)' }}>
      {/* Navbar Superior */}
      <Navbar
        onToggleSidebar={() => setSidebarOpen(prev => !prev)}
        sidebarOpen={sidebarOpen}
      />

      {/* Layout Principal: Sidebar + Contenido */}
      <div style={{ display: 'flex', flex: 1, position: 'relative' }}>
        <Sidebar
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
          activeSection={activeSection}
          onSelectSection={(id) => setActiveSection(id)}
        />

        <main style={{
          flex: 1,
          minWidth: 0,
          padding: '1.5rem',
          maxWidth: '1200px',
          margin: '0 auto',
          width: '100%'
        }}>
          {/* Hero Banner Estilo Campus UAGRM */}
          <div style={{
            background: 'linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(99, 102, 241, 0.1) 100%)',
            border: '1px solid rgba(14, 165, 233, 0.25)',
            borderRadius: '14px',
            padding: '1.5rem',
            position: 'relative',
            overflow: 'hidden'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#38bdf8', fontSize: '0.8rem', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              <span>🏛️</span> Universidad Autónoma Gabriel René Moreno · FICCT
            </div>
            <h1 style={{ fontSize: '1.75rem', fontWeight: 900, color: '#ffffff', marginTop: '0.4rem', letterSpacing: '-0.02em' }}>
              Plataforma de Preparación para el Examen Final
            </h1>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginTop: '0.4rem', maxWidth: '750px', lineHeight: 1.6 }}>
              Sistema interactivo desarrollado en <strong>React + TypeScript</strong> para la cátedra de <strong>INF-110 (Grupos Z2 y SF)</strong> dictada por la <strong>M.Sc. Ing. Angélica Garzón Cuéllar</strong>. Basado en la metodología oficial de 4 fases y Clean Code.
            </p>

            {/* Metadatos rápidos en tarjetas */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.75rem', marginTop: '1.25rem' }}>
              <div style={{ background: '#0a1020', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '0.75rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: '#fbbf24', fontSize: '0.75rem', fontWeight: 800 }}>
                  <Award size={14} /> La Trilogía Final
                </div>
                <div style={{ color: '#fff', fontWeight: 800, fontSize: '1.1rem', marginTop: '0.2rem' }}>
                  100 Puntos
                </div>
                <div style={{ color: '#64748b', fontSize: '0.72rem' }}>Series (30) + Núm (35) + Cad (35)</div>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '0.75rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: '#38bdf8', fontSize: '0.75rem', fontWeight: 800 }}>
                  <BookOpen size={14} /> Banco de Exámenes
                </div>
                <div style={{ color: '#fff', fontWeight: 800, fontSize: '1.1rem', marginTop: '0.2rem' }}>
                  28 Problemas
                </div>
                <div style={{ color: '#64748b', fontSize: '0.72rem' }}>7 Finales + 7 Parciales resueltos</div>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '0.75rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: '#34d399', fontSize: '0.75rem', fontWeight: 800 }}>
                  <ShieldCheck size={14} /> Buenas Prácticas
                </div>
                <div style={{ color: '#fff', fontWeight: 800, fontSize: '1.1rem', marginTop: '0.2rem' }}>
                  Clean Code
                </div>
                <div style={{ color: '#64748b', fontSize: '0.72rem' }}>Tipos Cardinal, variables legibles</div>
              </div>
            </div>
          </div>

          {/* COMPONENTE CORE: COCKPIT TRILOGÍA */}
          <CockpitTrilogia />

          {/* COMPONENTE VISUAL: MODELOS MENTALES GRÁFICOS */}
          <ModelosVisuales />

          {/* SECCIÓN DE BIBLIOTECA Y DESCARGAS */}
          <div className="card" style={{ marginTop: '1.5rem' }}>
            <h3 style={{ color: '#f8fafc', fontSize: '1.1rem', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
              <Download size={18} color="#38bdf8" /> Biblioteca de Descargas Directas (.docx y .pas)
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '0.82rem', marginBottom: '1rem' }}>
              Archivos compilados, probados con Free Pascal y documentos de Word con formato formal de la docente:
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '0.75rem' }}>
              <a
                href="../Modelos_Examen_Final_Resueltos.docx"
                download
                className="btn btn-secondary"
                style={{ justifyContent: 'flex-start', textAlign: 'left', padding: '0.75rem' }}
              >
                <FileText size={18} color="#3b82f6" />
                <div>
                  <strong style={{ color: '#fff', display: 'block', fontSize: '0.82rem' }}>
                    Modelos_Examen_Final_Resueltos.docx
                  </strong>
                  <span style={{ fontSize: '0.72rem', color: '#64748b' }}>7 Exámenes Finales (28 problemas)</span>
                </div>
              </a>

              <a
                href="../Hoja_De_Atajos_Metodos_Examen.docx"
                download
                className="btn btn-secondary"
                style={{ justifyContent: 'flex-start', textAlign: 'left', padding: '0.75rem' }}
              >
                <FileText size={18} color="#fbbf24" />
                <div>
                  <strong style={{ color: '#fff', display: 'block', fontSize: '0.82rem' }}>
                    Hoja_De_Atajos_Metodos_Examen.docx
                  </strong>
                  <span style={{ fontSize: '0.72rem', color: '#64748b' }}>Series: Divide y Vencerás</span>
                </div>
              </a>

              <a
                href="../Hoja_De_Atajos_Metodos_Numeros.docx"
                download
                className="btn btn-secondary"
                style={{ justifyContent: 'flex-start', textAlign: 'left', padding: '0.75rem' }}
              >
                <FileText size={18} color="#38bdf8" />
                <div>
                  <strong style={{ color: '#fff', display: 'block', fontSize: '0.82rem' }}>
                    Hoja_De_Atajos_Metodos_Numeros.docx
                  </strong>
                  <span style={{ fontSize: '0.72rem', color: '#64748b' }}>Números Naturales & Dígitos</span>
                </div>
              </a>

              <a
                href="../Hoja_De_Atajos_Metodos_Cadenas.docx"
                download
                className="btn btn-secondary"
                style={{ justifyContent: 'flex-start', textAlign: 'left', padding: '0.75rem' }}
              >
                <FileText size={18} color="#c084fc" />
                <div>
                  <strong style={{ color: '#fff', display: 'block', fontSize: '0.82rem' }}>
                    Hoja_De_Atajos_Metodos_Cadenas.docx
                  </strong>
                  <span style={{ fontSize: '0.72rem', color: '#64748b' }}>Cadenas & Subcadenas POO</span>
                </div>
              </a>
            </div>
          </div>

          {/* Pie de página institucional */}
          <footer style={{
            marginTop: '2rem',
            padding: '1.5rem 0',
            borderTop: '1px solid rgba(255,255,255,0.08)',
            textAlign: 'center',
            fontSize: '0.78rem',
            color: '#64748b'
          }}>
            <p>
              🏛️ <strong>UAGRM · Facultad Integral de Ciencias de la Computación y Telecomunicaciones (FICCT)</strong>
            </p>
            <p style={{ marginTop: '0.3rem' }}>
              Materia: <strong>INF-110 (Introducción a la Informática)</strong> · Docente: <strong>M.Sc. Ing. Angélica Garzón Cuéllar</strong>
            </p>
            <p style={{ marginTop: '0.3rem', color: '#475569' }}>
              Migración a React 19 + TypeScript + Vite · Clean Code & Metodología de las 4 Fases
            </p>
          </footer>
        </main>
      </div>
    </div>
  );
};
