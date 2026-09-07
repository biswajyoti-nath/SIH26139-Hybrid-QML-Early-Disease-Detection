import { useState, useEffect } from "react";
import axios from 'axios';
import { Database, Activity, Cpu, Microscope, Clock, ShieldCheck, FileWarning, BarChart4 } from 'lucide-react';
import './App.css';

const API_BASE = import.meta.env.BASE_URL + 'api';

function App() {
  const [dataset, setDataset] = useState('wdbc');
  const [profile, setProfile] = useState<any>(null);
  const [results, setResults] = useState<any>(null);
  const [routing, setRouting] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [analyzing, setAnalyzing] = useState(false);

  const loadData = async (name: string) => {
    setLoading(true);
    setRouting(null);
    try {
      const [profRes, resultsRes] = await Promise.all([
        axios.get(`${API_BASE}/dataset/${name}/profile`),
        axios.get(`${API_BASE}/dataset/${name}/results`)
      ]);
      setProfile(profRes.data);
      setResults(resultsRes.data);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  };

  useEffect(() => {
    loadData(dataset);
  }, [dataset]);

  const handleEvaluate = async () => {
    setAnalyzing(true);
    try {
      const res = await axios.post(`${API_BASE}/route`, { dataset_name: dataset });
      setTimeout(() => {
        setRouting(res.data);
        setAnalyzing(false);
      }, 1000);
    } catch (e) {
      console.error(e);
      setAnalyzing(false);
    }
  };

  const getMetric = (modelName: string) => {
    if (!results) return '-';
    try {
      return results.results[modelName].metrics_mean.roc_auc.toFixed(3);
    } catch {
      return '-';
    }
  };

  const getRuntime = (modelName: string) => {
    if (!results) return '-';
    try {
      const s = results.results[modelName].metrics_mean;
      const t = (s.training_time_s || 0) + (s.inference_time_s || 0);
      if (t < 0.25) return '<0.25s';
      return `~${Math.round(t)}s`;
    } catch {
      return '-';
    }
  };

  return (
    <div className="layout">
      {/* Top Navbar */}
      <header className="navbar">
        <div className="navbar-logo">
          <Activity size={28} className="text-blue" />
          <div className="navbar-titles">
            <h1>SIH 26139 | CHAI.EXE</h1>
            <h2>Evidence-Gated Hybrid QML Platform</h2>
          </div>
        </div>
        <div className="navbar-controls">
          <div className="dataset-selector">
            <Database size={18} className="text-gray" />
            <select 
              className="select-box" 
              value={dataset} 
              onChange={(e) => setDataset(e.target.value)}
              disabled={analyzing}
            >
              <option value="wdbc">Dataset: WDBC (Control)</option>
              <option value="parkinsons">Dataset: Parkinson's (High-Dim)</option>
            </select>
          </div>
        </div>
      </header>

      <main className="main-content">
        {!loading && profile && results ? (
          <>
            {/* KPI Cards */}
            <div className="kpi-grid">
              <div className="kpi-card">
                <div className="kpi-icon"><Database size={24} /></div>
                <div className="kpi-info">
                  <div className="kpi-label">Dimensions (Raw → PCA)</div>
                  <div className="kpi-value">{profile.raw_dimensions} → {profile.reduced_dimensions}</div>
                </div>
              </div>
              <div className="kpi-card">
                <div className="kpi-icon highlight"><BarChart4 size={24} /></div>
                <div className="kpi-info">
                  <div className="kpi-label">Variance Retained (PCA)</div>
                  <div className="kpi-value">{(profile.variance_retained * 100).toFixed(1)}%</div>
                </div>
              </div>
              <div className="kpi-card">
                <div className="kpi-icon"><ShieldCheck size={24} /></div>
                <div className="kpi-info">
                  <div className="kpi-label">Separability Proxy</div>
                  <div className="kpi-value">{profile.separability_proxy.toFixed(3)}</div>
                </div>
              </div>
            </div>

            <div className="dashboard-grid">
              {/* Left Column: Evidence & Models */}
              <div className="left-column">
                <div className="card">
                  <h2 className="card-title"><Microscope size={20}/> Empirical Shootout (T-103)</h2>
                  <table className="modern-table">
                    <thead>
                      <tr>
                        <th>Model</th>
                        <th>ROC-AUC</th>
                        <th>Runtime / Fold</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr className="classical-row">
                        <td><div className="model-name">SVM <span>(Classical)</span></div></td>
                        <td className="metric-bold">{getMetric('svm')}</td>
                        <td>{getRuntime('svm')}</td>
                      </tr>
                      <tr className="classical-row">
                        <td><div className="model-name">XGBoost <span>(Classical)</span></div></td>
                        <td className="metric-bold">{getMetric('xgboost')}</td>
                        <td>{getRuntime('xgboost')}</td>
                      </tr>
                      <tr className="quantum-row">
                        <td><div className="model-name">QSVM <span>(8 Qubits)</span></div></td>
                        <td className="metric-bold">{getMetric('qsvm')}</td>
                        <td><span className="runtime-warn">{getRuntime('qsvm')}</span></td>
                      </tr>
                      <tr className="quantum-row">
                        <td><div className="model-name">VQC <span>(8 Qubits)</span></div></td>
                        <td className="metric-bold">{getMetric('vqc')}</td>
                        <td><span className="runtime-warn">{getRuntime('vqc')}</span></td>
                      </tr>
                    </tbody>
                  </table>

                  {!routing && (
                    <button 
                      className={`evaluate-btn ${analyzing ? 'analyzing' : ''}`}
                      onClick={handleEvaluate}
                      disabled={analyzing}
                    >
                      {analyzing ? (
                        <><Cpu size={20} className="spin" /> Analyzing Evidence Map...</>
                      ) : (
                        <><Cpu size={20} /> Execute Pathway Router</>
                      )}
                    </button>
                  )}
                </div>

                {routing && (
                  <div className="card">
                    <h2 className="card-title"><BarChart4 size={20}/> Pathway Comparison</h2>
                    <div className="chart-container">
                      <div className="bar-row">
                        <span className="bar-label">SVM</span>
                        <div className="bar-track">
                          <div className="bar-fill blue" style={{width: `${routing.classical_score * 100}%`}}></div>
                        </div>
                        <span className="bar-value">{routing.classical_score.toFixed(3)}</span>
                      </div>
                      
                      <div className="bar-row">
                        <span className="bar-label">QSVM</span>
                        <div className="bar-track">
                          <div className="bar-fill gray" style={{width: `${getMetric('qsvm') * 100}%`}}></div>
                        </div>
                        <span className="bar-value">{getMetric('qsvm')}</span>
                      </div>

                      <div className="bar-row">
                        <span className="bar-label">VQC</span>
                        <div className="bar-track">
                          <div className="bar-fill gray" style={{width: `${getMetric('vqc') * 100}%`}}></div>
                        </div>
                        <span className="bar-value">{getMetric('vqc')}</span>
                      </div>
                    </div>
                  </div>
                )}
              </div>

              {/* Right Column: Recommendation */}
              <div className="right-column">
                {routing ? (
                  <div className="recommendation-card active">
                    <div className="rec-header">
                      <span>T-062 ROUTER DECISION</span>
                      <div className="pulse-dot"></div>
                    </div>
                    
                    <div className="rec-badge classical">
                      {routing.recommendation}
                    </div>
                    
                    <p className="rec-reason">{routing.reason}</p>
                    
                    <div className="rec-factors">
                      <h3>ROUTING FACTORS</h3>
                      <ul>
                        <li><ShieldCheck size={18} className="text-green"/> Strong classical reference performance</li>
                        <li>
                          <FileWarning size={18} className="text-orange"/> 
                          {routing.delta < 0 ? "Quantum delta is strictly negative" : "Quantum delta insufficient"}
                        </li>
                        <li><Clock size={18} className="text-orange"/> Prohibitive simulator runtime ratio</li>
                        <li><Database size={18} className="text-blue"/> Evidence does not justify quantum allocation</li>
                      </ul>
                    </div>
                  </div>
                ) : (
                  <div className="recommendation-card empty">
                    <Cpu size={48} className="empty-icon" />
                    <h3>Awaiting Router Execution</h3>
                    <p>Select a dataset and click evaluate to generate a purely evidence-driven pathway recommendation.</p>
                  </div>
                )}
              </div>
            </div>
          </>
        ) : (
          <div className="loading-state">Loading dataset evidence...</div>
        )}
      </main>

      <footer className="footer">
        <div className="disclaimer-badge">DEMO MODE</div>
        <p><strong>Research prototype. Not a medical device.</strong> Using validated T-103 cached artifacts. Simulator execution only.</p>
      </footer>
    </div>
  );
}

export default App;
