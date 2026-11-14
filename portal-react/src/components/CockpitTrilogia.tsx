import React, { useState } from 'react';
import { METODOS_TRILOGIA, MetodoTrilogia } from '../data/trilogiaData';
import { PascalCodeBlock } from './PascalCodeBlock';
import { TrazaViewer } from './TrazaViewer';
import { Play, Sparkles, Award, Layers, BookOpen, Code2 } from 'lucide-react';

export const CockpitTrilogia: React.FC = () => {
  const [activeCategory, setActiveCategory] = useState<'series' | 'numeros' | 'cadenas'>('series');
  const [faseActiva, setFaseActiva] = useState<number>(3); // 1: Análisis, 2: Pseudocódigo, 3: Pascal, 4: Traza

  // Estados interactivos para pruebas en vivo
  const [nSeries, setNSeries] = useState<number>(4);
  const [resultadoSerie, setResultadoSerie] = useState<number | null>(null);

  const [numeroInput, setNumeroInput] = useState<number>(445122);
  const [resultadoNumero, setResultadoNumero] = useState<number | null>(null);

  const [cadenaInput, setCadenaInput] = useState<string>('DELPHI');
  const [resultadoCadena, setResultadoCadena] = useState<string | null>(null);

  const metodoActual: MetodoTrilogia = METODOS_TRILOGIA.find(m => m.categoria === activeCategory) || METODOS_TRILOGIA[0];

  // Ejecutor en vivo para Series
  const ejecutarSerie = () => {
    let sum = 0;
    let fact = 1;
    let pot = 1;
    for (let i = 1; i <= nSeries; i++) {
      fact *= i;
      pot *= 2;
      sum += fact / pot;
    }
    setResultadoSerie(sum);
  };

  // Ejecutor en vivo para Números (Eliminar duplicados)
  const ejecutarNumero = () => {
    let temp = numeroInput;
    let res = 0;
    let mult = 1;
    while (temp > 0) {
      const d = temp % 10;
      // Verificar si d ya está en res
      let c = res;
      let existe = false;
      while (c > 0) {
        if (c % 10 === d) {
          existe = true;
          break;
        }
        c = Math.floor(c / 10);
      }
      if (!existe) {
        res += d * mult;
        mult *= 10;
      }
      temp = Math.floor(temp / 10);
    }
    setResultadoNumero(res);
  };

  // Ejecutor en vivo para Cadenas (Invertir por mitades)
  const ejecutarCadena = () => {
    const s = cadenaInput;
    const len = s.length;
    if (len <= 1) {
      setResultadoCadena(s);
      return;
    }
    const mitad = Math.floor(len / 2);
    const m1 = s.slice(0, mitad).split('').reverse().join('');
    if (len % 2 !== 0) {
      const central = s[mitad];
      const m2 = s.slice(mitad + 1, mitad + 1 + mitad).split('').reverse().join('');
      setResultadoCadena(m1 + central + m2);
    } else {
      const m2 = s.slice(mitad, mitad + mitad).split('').reverse().join('');
      setResultadoCadena(m1 + m2);
    }
  };

  return (
    <div className="card" style={{ marginTop: '1.5rem', border: '1px solid rgba(14, 165, 233, 0.25)' }}>
      {/* Encabezado del Cockpit */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '0.75rem', marginBottom: '1.25rem' }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span style={{ fontSize: '1.4rem' }}>👑</span>
            <h2 style={{ fontSize: '1.25rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.02em' }}>
              Cockpit Trilogía del Examen Final (100 Puntos)
            </h2>
          </div>
          <p style={{ color: '#94a3b8', fontSize: '0.82rem', marginTop: '0.2rem' }}>
            Simulador interactivo del examen: Series (30 pts) + Números (35 pts) + Cadenas (35 pts) en React
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <span style={{
            background: 'rgba(16, 185, 129, 0.15)',
            border: '1px solid #10b981',
            color: '#34d399',
            padding: '0.3rem 0.65rem',
            borderRadius: '20px',
            fontSize: '0.75rem',
            fontWeight: 800,
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.35rem'
          }}>
            <Award size={14} /> Total Cátedra: 100 Pts
          </span>
        </div>
      </div>

      {/* Tabs principales de la Trilogía (Modern Web Guidance Tabs) */}
      <div
        role="tablist"
        aria-label="Temas del Examen Final"
        className="tablist-container"
      >
        <button
          type="button"
          role="tab"
          id="tab-series"
          aria-selected={activeCategory === 'series'}
          className="tab-btn"
          onClick={() => setActiveCategory('series')}
        >
          <span>⚡</span>
          <span>1. Series Numéricas</span>
          <span style={{ fontSize: '0.7rem', padding: '0.1rem 0.4rem', borderRadius: '6px', background: 'rgba(245,158,11,0.2)', color: '#fbbf24', marginLeft: '0.2rem' }}>
            30 pts
          </span>
        </button>

        <button
          type="button"
          role="tab"
          id="tab-numeros"
          aria-selected={activeCategory === 'numeros'}
          className="tab-btn"
          onClick={() => setActiveCategory('numeros')}
        >
          <span>🔢</span>
          <span>2. Números & Dígitos (POO)</span>
          <span style={{ fontSize: '0.7rem', padding: '0.1rem 0.4rem', borderRadius: '6px', background: 'rgba(56,189,248,0.2)', color: '#38bdf8', marginLeft: '0.2rem' }}>
            35 pts
          </span>
        </button>

        <button
          type="button"
          role="tab"
          id="tab-cadenas"
          aria-selected={activeCategory === 'cadenas'}
          className="tab-btn"
          onClick={() => setActiveCategory('cadenas')}
        >
          <span>🔤</span>
          <span>3. Cadenas de Caracteres</span>
          <span style={{ fontSize: '0.7rem', padding: '0.1rem 0.4rem', borderRadius: '6px', background: 'rgba(168,85,247,0.2)', color: '#c084fc', marginLeft: '0.2rem' }}>
            35 pts
          </span>
        </button>
      </div>

      {/* Panel de Contenido del Tab */}
      <div
        role="tabpanel"
        aria-labelledby={`tab-${activeCategory}`}
        style={{ paddingTop: '1.25rem' }}
      >
        {/* Banner del ejercicio seleccionado */}
        <div style={{
          background: 'rgba(255, 255, 255, 0.03)',
          border: '1px solid rgba(255, 255, 255, 0.07)',
          borderRadius: '10px',
          padding: '1rem',
          marginBottom: '1rem'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
            <h3 style={{ color: '#38bdf8', fontSize: '1rem', fontWeight: 800 }}>
              {metodoActual.titulo}
            </h3>
            <span style={{ color: '#34d399', fontWeight: 800, fontSize: '0.8rem' }}>
              Valor: {metodoActual.puntos} Puntos
            </span>
          </div>
          <p style={{ color: '#cbd5e1', fontSize: '0.85rem' }}>{metodoActual.enunciado}</p>

          {/* SIMULADOR EN VIVO ESPECÍFICO DE CADA TEMA */}
          <div style={{
            marginTop: '0.85rem',
            padding: '0.75rem',
            background: '#040813',
            border: '1px solid rgba(255,255,255,0.06)',
            borderRadius: '8px',
            display: 'flex',
            alignItems: 'center',
            gap: '0.75rem',
            flexWrap: 'wrap'
          }}>
            {activeCategory === 'series' && (
              <>
                <label style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 700 }}>
                  Términos (N):
                </label>
                <input
                  type="number"
                  min="1"
                  max="12"
                  value={nSeries}
                  onChange={(e) => setNSeries(Math.max(1, parseInt(e.target.value) || 1))}
                  style={{
                    width: '70px',
                    padding: '0.35rem 0.5rem',
                    background: '#090f1e',
                    border: '1px solid #334155',
                    borderRadius: '6px',
                    color: '#fff',
                    fontWeight: 700,
                    textAlign: 'center'
                  }}
                />
                <button onClick={ejecutarSerie} className="btn btn-primary" style={{ padding: '0.35rem 0.8rem', fontSize: '0.78rem' }}>
                  <Play size={13} /> Calcular Serie
                </button>
                {resultadoSerie !== null && (
                  <div style={{ marginLeft: 'auto', color: '#34d399', fontWeight: 800, fontSize: '0.85rem' }}>
                    S = {resultadoSerie.toFixed(4)}
                  </div>
                )}
              </>
            )}

            {activeCategory === 'numeros' && (
              <>
                <label style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 700 }}>
                  Valor (Cardinal):
                </label>
                <input
                  type="number"
                  value={numeroInput}
                  onChange={(e) => setNumeroInput(parseInt(e.target.value) || 0)}
                  style={{
                    width: '120px',
                    padding: '0.35rem 0.5rem',
                    background: '#090f1e',
                    border: '1px solid #334155',
                    borderRadius: '6px',
                    color: '#fff',
                    fontWeight: 700,
                    textAlign: 'center'
                  }}
                />
                <button onClick={ejecutarNumero} className="btn btn-primary" style={{ padding: '0.35rem 0.8rem', fontSize: '0.78rem' }}>
                  <Play size={13} /> Eliminar Repetidos
                </button>
                {resultadoNumero !== null && (
                  <div style={{ marginLeft: 'auto', color: '#34d399', fontWeight: 800, fontSize: '0.85rem' }}>
                    Resultado = {resultadoNumero}
                  </div>
                )}
              </>
            )}

            {activeCategory === 'cadenas' && (
              <>
                <label style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 700 }}>
                  Texto:
                </label>
                <input
                  type="text"
                  value={cadenaInput}
                  onChange={(e) => setCadenaInput(e.target.value)}
                  style={{
                    width: '140px',
                    padding: '0.35rem 0.5rem',
                    background: '#090f1e',
                    border: '1px solid #334155',
                    borderRadius: '6px',
                    color: '#fff',
                    fontWeight: 700,
                    textAlign: 'center'
                  }}
                />
                <button onClick={ejecutarCadena} className="btn btn-primary" style={{ padding: '0.35rem 0.8rem', fontSize: '0.78rem' }}>
                  <Play size={13} /> Invertir por Mitades
                </button>
                {resultadoCadena !== null && (
                  <div style={{ marginLeft: 'auto', color: '#34d399', fontWeight: 800, fontSize: '0.85rem' }}>
                    Resultado = "{resultadoCadena}"
                  </div>
                )}
              </>
            )}
          </div>
        </div>

        {/* SUB-TABS: LAS 4 FASES OBLIGATORIAS DE LA CÁTEDRA */}
        <div style={{
          display: 'flex',
          gap: '0.4rem',
          flexWrap: 'wrap',
          marginBottom: '0.75rem',
          borderBottom: '1px solid rgba(255,255,255,0.06)',
          paddingBottom: '0.5rem'
        }}>
          {[
            { num: 1, label: 'Fase 1: Análisis', icon: BookOpen },
            { num: 2, label: 'Fase 2: Pseudocódigo', icon: Layers },
            { num: 3, label: 'Fase 3: Código Pascal Clean Code', icon: Code2 },
            { num: 4, label: 'Fase 4: Prueba de Escritorio (Traza)', icon: Sparkles }
          ].map((fase) => {
            const Icon = fase.icon;
            const activo = faseActiva === fase.num;
            return (
              <button
                key={fase.num}
                type="button"
                onClick={() => setFaseActiva(fase.num)}
                className={`btn ${activo ? 'btn-primary' : 'btn-secondary'}`}
                style={{ fontSize: '0.78rem', padding: '0.35rem 0.75rem' }}
              >
                <Icon size={13} /> {fase.label}
              </button>
            );
          })}
        </div>

        {/* CONTENIDO DE LAS 4 FASES */}
        {faseActiva === 1 && (
          <div style={{ background: '#050a16', padding: '1rem', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.06)' }}>
            <h4 style={{ color: '#38bdf8', fontSize: '0.85rem', fontWeight: 800, marginBottom: '0.5rem' }}>
              📋 Análisis Metodológico Formal
            </h4>
            <ul style={{ listStyle: 'none', padding: 0, fontSize: '0.82rem', lineHeight: 1.8, color: '#cbd5e1' }}>
              <li><strong>📥 Entrada(s):</strong> {metodoActual.fase1Analisis.entradas}</li>
              <li><strong>📤 Salida(s):</strong> {metodoActual.fase1Analisis.salidas}</li>
              <li><strong>⚙️ Ley de Formación:</strong> {metodoActual.fase1Analisis.leyFormacion}</li>
              <li><strong>🏛️ Módulo Delphi:</strong> <code style={{ color: '#34d399', fontFamily: 'var(--font-mono)' }}>{metodoActual.fase1Analisis.tipoModulo}</code></li>
            </ul>
          </div>
        )}

        {faseActiva === 2 && (
          <PascalCodeBlock
            codigo={metodoActual.fase2Pseudocodigo}
            titulo="Algoritmo / Pseudocódigo Formal"
          />
        )}

        {faseActiva === 3 && (
          <PascalCodeBlock
            codigo={metodoActual.fase3Pascal}
            titulo="Implementación Delphi / Pascal (Tipado Fuerte & Clean Code)"
          />
        )}

        {faseActiva === 4 && (
          <TrazaViewer
            descripcion={metodoActual.fase4TrazaEjemplo.descripcion}
            columnas={metodoActual.fase4TrazaEjemplo.columnas}
            filas={metodoActual.fase4TrazaEjemplo.filas}
          />
        )}
      </div>
    </div>
  );
};

