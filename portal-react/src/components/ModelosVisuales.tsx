import React, { useState } from 'react';
import { Cog, Train, Layers, Sparkles, Binary } from 'lucide-react';

export const ModelosVisuales: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'numeros' | 'series' | 'cadenas' | 'fases'>('numeros');

  return (
    <div className="card" style={{ marginTop: '1.5rem', border: '1px solid rgba(139, 92, 246, 0.3)' }}>
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '0.75rem', marginBottom: '1.25rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
          <span style={{ fontSize: '1.5rem' }}>🎨</span>
          <div>
            <h2 style={{ fontSize: '1.25rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.02em' }}>
              Modelos Mentales Gráficos · «Aprende con Diagramas»
            </h2>
            <p style={{ color: '#94a3b8', fontSize: '0.82rem', marginTop: '0.2rem' }}>
              Mecanismos visuales de los 3 temas y la metodología de 4 fases para programadores visuales
            </p>
          </div>
        </div>
        <span style={{
          background: 'rgba(139, 92, 246, 0.15)',
          border: '1px solid #8b5cf6',
          color: '#c084fc',
          padding: '0.25rem 0.65rem',
          borderRadius: '20px',
          fontSize: '0.75rem',
          fontWeight: 800,
          display: 'inline-flex',
          alignItems: 'center',
          gap: '0.35rem'
        }}>
          <Sparkles size={14} /> Modo Visual Activo
        </span>
      </div>

      {/* Tabs accesibles de Modelos Visuales */}
      <div
        role="tablist"
        aria-label="Modelos Mentales Gráficos"
        className="tablist-container"
      >
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'numeros'}
          className="tab-btn"
          onClick={() => setActiveTab('numeros')}
        >
          <span>🔢</span> 1. Máquina Números (mod/div)
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'series'}
          className="tab-btn"
          onClick={() => setActiveTab('series')}
        >
          <span>⚡</span> 2. Sistema 3 Engranajes (Series)
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'cadenas'}
          className="tab-btn"
          onClick={() => setActiveTab('cadenas')}
        >
          <span>🔤</span> 3. Tren de Vagones (Cadenas)
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'fases'}
          className="tab-btn"
          onClick={() => setActiveTab('fases')}
        >
          <span>🏛️</span> 4. Las 4 Fases de Cátedra
        </button>
      </div>

      {/* CONTENIDO DEL MODELO VISUAL */}
      <div style={{ paddingTop: '1.25rem' }}>

        {/* 1. MÁQUINA DE NÚMEROS */}
        {activeTab === 'numeros' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ background: '#050a16', border: '1px solid rgba(56, 189, 248, 0.2)', borderRadius: '10px', padding: '1.25rem' }}>
              <h3 style={{ color: '#38bdf8', fontSize: '1rem', fontWeight: 800, marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                <Binary size={18} /> La Máquina Extractora: Pinza (mod 10) y Sierra (div 10)
              </h3>
              <p style={{ color: '#cbd5e1', fontSize: '0.85rem', marginBottom: '1rem' }}>
                Cualquier número natural se procesa como un bloque físico. En cada vuelta del bucle <code style={{ color: '#38bdf8' }}>while n &gt; 0 do</code>, se extrae el último dígito y se recorta la cola.
              </p>

              {/* Diagrama Gráfico */}
              <div style={{
                background: '#020610',
                padding: '1rem',
                borderRadius: '8px',
                border: '1px solid rgba(255,255,255,0.06)',
                textAlign: 'center',
                fontFamily: 'var(--font-mono)',
                fontSize: '0.85rem'
              }}>
                <div style={{ color: '#fbbf24', fontWeight: 800, fontSize: '1.1rem', marginBottom: '0.6rem' }}>
                  NÚMERO ORIGINAL: [ 4 5 2 1 ]
                </div>
                <div style={{ color: '#64748b' }}>⬇️ entra a la máquina ⬇️</div>
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: '1fr 1fr',
                  gap: '1rem',
                  marginTop: '0.75rem'
                }}>
                  <div style={{ background: 'rgba(56, 189, 248, 0.1)', border: '1px solid #0284c7', borderRadius: '8px', padding: '0.75rem' }}>
                    <div style={{ color: '#38bdf8', fontWeight: 800 }}>📌 d := n MOD 10;</div>
                    <div style={{ color: '#94a3b8', fontSize: '0.75rem', marginTop: '0.2rem' }}>La PINZA saca el último dígito</div>
                    <div style={{ color: '#34d399', fontSize: '1.2rem', fontWeight: 900, marginTop: '0.4rem' }}>d = [ 1 ]</div>
                  </div>

                  <div style={{ background: 'rgba(239, 68, 68, 0.1)', border: '1px solid #ef4444', borderRadius: '8px', padding: '0.75rem' }}>
                    <div style={{ color: '#f87171', fontWeight: 800 }}>✂️ n := n DIV 10;</div>
                    <div style={{ color: '#94a3b8', fontSize: '0.75rem', marginTop: '0.2rem' }}>La SIERRA recorta el número</div>
                    <div style={{ color: '#fbbf24', fontSize: '1.2rem', fontWeight: 900, marginTop: '0.4rem' }}>Queda = [ 452 ]</div>
                  </div>
                </div>
              </div>
            </div>

            {/* Dos formas de reconstrucción */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '0.75rem' }}>
              <div style={{ background: '#0a1020', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '1rem' }}>
                <h4 style={{ color: '#34d399', fontWeight: 800, fontSize: '0.85rem', marginBottom: '0.4rem' }}>
                  A) Ponderación Decimal (Mantiene Orden)
                </h4>
                <code style={{ display: 'block', color: '#38bdf8', fontSize: '0.78rem', background: '#040814', padding: '0.4rem', borderRadius: '6px' }}>
                  res := res + (d * mult);<br />
                  mult := mult * 10;
                </code>
                <p style={{ color: '#94a3b8', fontSize: '0.75rem', marginTop: '0.4rem' }}>
                  Uso: Eliminar repetidos, filtrar pares/impares manteniendo la posición original.
                </p>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '1rem' }}>
                <h4 style={{ color: '#c084fc', fontWeight: 800, fontSize: '0.85rem', marginBottom: '0.4rem' }}>
                  B) Empuje Decimal (Invierte el Número)
                </h4>
                <code style={{ display: 'block', color: '#c084fc', fontSize: '0.78rem', background: '#040814', padding: '0.4rem', borderRadius: '6px' }}>
                  res := (res * 10) + d;
                </code>
                <p style={{ color: '#94a3b8', fontSize: '0.75rem', marginTop: '0.4rem' }}>
                  Uso: Invertir número, verificar si es capicúa (<code style={{ color: '#fff' }}>res = valor</code>).
                </p>
              </div>
            </div>
          </div>
        )}

        {/* 2. SISTEMA DE 3 ENGRANAJES */}
        {activeTab === 'series' && (
          <div style={{ background: '#050a16', border: '1px solid rgba(245, 158, 11, 0.2)', borderRadius: '10px', padding: '1.25rem' }}>
            <h3 style={{ color: '#fbbf24', fontSize: '1rem', fontWeight: 800, marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
              <Cog size={18} /> El Sistema de Tres Engranajes «Divide y Vencerás»
            </h3>
            <p style={{ color: '#cbd5e1', fontSize: '0.85rem', marginBottom: '1rem' }}>
              Cualquier serie fraccionaria se resuelve dividiéndola en 3 componentes independientes sincronizados por el contador <code style={{ color: '#fbbf24' }}>i</code>:
            </p>

            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '0.75rem',
              marginBottom: '1rem'
            }}>
              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem', textAlign: 'center' }}>
                <div style={{ color: '#f87171', fontWeight: 800, fontSize: '0.85rem' }}>⚙️ Engranaje 1: Signo</div>
                <div style={{ color: '#fff', fontSize: '1.1rem', fontWeight: 900, margin: '0.4rem 0' }}>+ / - / + / -</div>
                <code style={{ color: '#94a3b8', fontSize: '0.75rem' }}>signo := -signo</code>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem', textAlign: 'center' }}>
                <div style={{ color: '#38bdf8', fontWeight: 800, fontSize: '0.85rem' }}>⚙️ Engranaje 2: Numerador</div>
                <div style={{ color: '#fff', fontSize: '1.1rem', fontWeight: 900, margin: '0.4rem 0' }}>1, 3, 5, 7, 9...</div>
                <code style={{ color: '#94a3b8', fontSize: '0.75rem' }}>num := 2*i - 1</code>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem', textAlign: 'center' }}>
                <div style={{ color: '#34d399', fontWeight: 800, fontSize: '0.85rem' }}>⚙️ Engranaje 3: Denominador</div>
                <div style={{ color: '#fff', fontSize: '1.1rem', fontWeight: 900, margin: '0.4rem 0' }}>2, 4, 8, 16, 32...</div>
                <code style={{ color: '#94a3b8', fontSize: '0.75rem' }}>den := den * 2</code>
              </div>
            </div>

            <div style={{ background: 'rgba(16, 185, 129, 0.1)', border: '1px solid #10b981', borderRadius: '8px', padding: '0.75rem', textAlign: 'center' }}>
              <div style={{ color: '#34d399', fontWeight: 800, fontSize: '0.85rem' }}>
                🎯 Fracción resultante del término en cada ciclo:
              </div>
              <div style={{ color: '#fff', fontSize: '1rem', fontWeight: 900, fontFamily: 'var(--font-mono)', marginTop: '0.2rem' }}>
                Suma := Suma + (Signo * (Numerador / Denominador));
              </div>
            </div>
          </div>
        )}

        {/* 3. TREN DE VAGONES */}
        {activeTab === 'cadenas' && (
          <div style={{ background: '#050a16', border: '1px solid rgba(168, 85, 247, 0.2)', borderRadius: '10px', padding: '1.25rem' }}>
            <h3 style={{ color: '#c084fc', fontSize: '1rem', fontWeight: 800, marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
              <Train size={18} /> El Tren de Vagones: Cadena = Array de Caracteres 1..L
            </h3>
            <p style={{ color: '#cbd5e1', fontSize: '0.85rem', marginBottom: '1rem' }}>
              Visualiza 'DELPHI' (longitud 6) dividida a la mitad exacta por una guillotina virtual:
            </p>

            <div style={{
              background: '#040814',
              padding: '1rem',
              borderRadius: '8px',
              border: '1px solid rgba(255,255,255,0.06)',
              overflowX: 'auto'
            }}>
              <div style={{ display: 'flex', justifyContent: 'center', gap: '0.4rem', marginBottom: '0.6rem' }}>
                {['D', 'E', 'L', 'P', 'H', 'I'].map((char, i) => (
                  <div key={i} style={{
                    width: '45px',
                    height: '55px',
                    background: i < 3 ? 'rgba(56, 189, 248, 0.15)' : 'rgba(168, 85, 247, 0.15)',
                    border: i < 3 ? '1px solid #0284c7' : '1px solid #a855f7',
                    borderRadius: '6px',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    <span style={{ fontSize: '0.65rem', color: '#64748b' }}>[{i + 1}]</span>
                    <strong style={{ fontSize: '1.1rem', color: '#fff' }}>{char}</strong>
                  </div>
                ))}
              </div>

              <div style={{ textAlign: 'center', fontSize: '0.8rem', color: '#94a3b8' }}>
                <span style={{ color: '#38bdf8', fontWeight: 800 }}>Mitad 1: Copy(s, 1, 3) = "DEL"</span>
                <span style={{ margin: '0 0.5rem' }}>|</span>
                <span style={{ color: '#c084fc', fontWeight: 800 }}>Mitad 2: Copy(s, 4, 3) = "PHI"</span>
              </div>

              <div style={{
                marginTop: '1rem',
                padding: '0.6rem',
                background: '#080e1e',
                borderRadius: '6px',
                textAlign: 'center',
                color: '#34d399',
                fontWeight: 800,
                fontSize: '0.85rem'
              }}>
                🔄 Inversión independiente: "LED" + "IHP" = "LEDIHP"
              </div>
            </div>
          </div>
        )}

        {/* 4. LAS 4 FASES */}
        {activeTab === 'fases' && (
          <div style={{ background: '#050a16', border: '1px solid rgba(16, 185, 129, 0.2)', borderRadius: '10px', padding: '1.25rem' }}>
            <h3 style={{ color: '#34d399', fontSize: '1rem', fontWeight: 800, marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
              <Layers size={18} /> El Mapa de las 4 Fases Académicas (Metodología Garzón)
            </h3>
            <p style={{ color: '#cbd5e1', fontSize: '0.85rem', marginBottom: '1rem' }}>
              Para obtener los 100 puntos, cada problema debe desarrollarse en estas 4 etapas obligatorias:
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(230px, 1fr))', gap: '0.75rem' }}>
              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem' }}>
                <div style={{ color: '#38bdf8', fontWeight: 800, fontSize: '0.82rem' }}>📦 FASE 1: Análisis</div>
                <ul style={{ fontSize: '0.75rem', color: '#94a3b8', paddingLeft: '1rem', marginTop: '0.4rem', lineHeight: 1.6 }}>
                  <li>Caja Negra: Entradas y Salidas</li>
                  <li>Ley de Formación matemática</li>
                  <li>Encabezado del módulo (Función/Proc)</li>
                </ul>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem' }}>
                <div style={{ color: '#fbbf24', fontWeight: 800, fontSize: '0.82rem' }}>📝 FASE 2: Pseudocódigo</div>
                <ul style={{ fontSize: '0.75rem', color: '#94a3b8', paddingLeft: '1rem', marginTop: '0.4rem', lineHeight: 1.6 }}>
                  <li>Algoritmo formal estructurado</li>
                  <li>Variables locales tipadas</li>
                  <li>Inicio, Mientras/Para, Fin</li>
                </ul>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem' }}>
                <div style={{ color: '#c084fc', fontWeight: 800, fontSize: '0.82rem' }}>💻 FASE 3: Delphi Clean Code</div>
                <ul style={{ fontSize: '0.75rem', color: '#94a3b8', paddingLeft: '1rem', marginTop: '0.4rem', lineHeight: 1.6 }}>
                  <li>Tipos fuertes: Cardinal, Byte, Double</li>
                  <li>Variables autodescriptivas</li>
                  <li>0 variables globales innecesarias</li>
                </ul>
              </div>

              <div style={{ background: '#0a1020', border: '1px solid #334155', borderRadius: '8px', padding: '0.85rem' }}>
                <div style={{ color: '#34d399', fontWeight: 800, fontSize: '0.82rem' }}>📊 FASE 4: Traza Tabular</div>
                <ul style={{ fontSize: '0.75rem', color: '#94a3b8', paddingLeft: '1rem', marginTop: '0.4rem', lineHeight: 1.6 }}>
                  <li>Prueba de escritorio en cámara lenta</li>
                  <li>Columnas con cada variable</li>
                  <li>Fila por cada vuelta del ciclo</li>
                </ul>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
};
