import { useEffect, useState } from 'react';

type Step = 'Business profile' | 'Objectives' | 'Geography' | 'Market scan' | 'Review' | 'Results';

type Assessment = {
  name: string;
  status: string;
  region: string;
  confidence: string;
};

const steps: Step[] = [
  'Business profile',
  'Objectives',
  'Geography',
  'Market scan',
  'Review',
  'Results',
];

const fallbackAssessments: Assessment[] = [
  { name: 'Central Colombo expansion', status: 'Ready for analysis', region: 'Colombo District', confidence: 'Moderate' },
  { name: 'Kandy showroom review', status: 'Draft', region: 'Kandy District', confidence: 'Pending' },
  { name: 'Galle outlet coverage', status: 'Results available', region: 'Galle District', confidence: 'High' },
];

const candidateSites = [
  { name: 'Pelawatta Crossing', score: '72/100', type: 'Prime retail frontage', notes: 'High visibility and close to commuter routes.' },
  { name: 'Kottawa Growth Hub', score: '68/100', type: 'Emerging area', notes: 'Strong demand potential with moderate competition.' },
  { name: 'Battaramulla Town Centre', score: '81/100', type: 'Dense urban catchment', notes: 'High foot traffic and service accessibility.' },
];

export default function App() {
  const [assessments, setAssessments] = useState<Assessment[]>(fallbackAssessments);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAssessments = async () => {
      try {
        const response = await fetch('/api/assessments');
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const data = (await response.json()) as Assessment[];
        if (data.length > 0) {
          setAssessments(data);
        }
      } catch (error) {
        console.warn('Using fallback assessment data because the backend is unavailable.', error);
      } finally {
        setLoading(false);
      }
    };

    void fetchAssessments();
  }, []);

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div>
          <div className="brand">Retail Site Selection</div>
          <nav className="nav">
            <button className="nav-item active">Dashboard</button>
            <button className="nav-item">Assessments</button>
            <button className="nav-item">Map explorer</button>
            <button className="nav-item">Data sources</button>
            <button className="nav-item">Settings</button>
          </nav>
        </div>
        <div className="account-card">
          <div className="eyebrow">Signed in</div>
          <strong>Operations Team</strong>
        </div>
      </aside>

      <main className="main-panel">
        <header className="topbar">
          <div>
            <p className="eyebrow">Location intelligence</p>
            <h1>Assessment dashboard</h1>
          </div>
          <button className="primary-button">New assessment</button>
        </header>

        <section className="overview-grid">
          <article className="metric-card accent">
            <span className="metric-label">Accessible assessments</span>
            <strong>{assessments.length}</strong>
            <small>Across 4 active regions</small>
          </article>
          <article className="metric-card">
            <span className="metric-label">Drafts</span>
            <strong>{assessments.filter((item) => item.status === 'Draft').length}</strong>
            <small>2 awaiting geography input</small>
          </article>
          <article className="metric-card">
            <span className="metric-label">Results this month</span>
            <strong>7</strong>
            <small>Based on synthetic demo data</small>
          </article>
        </section>

        <section className="content-grid">
          <div className="panel">
            <div className="panel-header">
              <h2>Your assessments</h2>
              <button className="link-button">View all</button>
            </div>
            <div className="card-list">
              {assessments.map((item) => (
                <div className="assessment-card" key={item.name}>
                  <div>
                    <h3>{item.name}</h3>
                    <p>{item.region}</p>
                  </div>
                  <div className="status-row">
                    <span className="status-badge">{item.status}</span>
                    <small>{item.confidence} confidence</small>
                  </div>
                </div>
              ))}
            </div>
            {loading ? <p className="loading-text">Loading live assessment data…</p> : null}
          </div>

          <div className="panel">
            <div className="panel-header">
              <h2>Assessment wizard</h2>
              <button className="link-button">Save draft</button>
            </div>
            <div className="wizard-steps">
              {steps.map((step, index) => (
                <div key={step} className={`step ${index === 0 ? 'current' : ''}`}>
                  <span>{index + 1}</span>
                  {step}
                </div>
              ))}
            </div>
            <div className="wizard-form">
              <label>
                Business profile
                <input defaultValue="D. Samson & Sons (Pvt) Ltd." />
              </label>
              <label>
                Primary objective
                <input defaultValue="Evaluate expansion opportunity in Colombo metro" />
              </label>
              <label>
                Geographic scope
                <input defaultValue="Colombo, Sri Jayawardenepura, and surrounding growth corridors" />
              </label>
            </div>
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h2>Candidate site shortlist</h2>
            <button className="link-button">Compare sites</button>
          </div>
          <div className="site-grid">
            {candidateSites.map((site) => (
              <div className="site-card" key={site.name}>
                <div className="site-header">
                  <h3>{site.name}</h3>
                  <span>{site.score}</span>
                </div>
                <small>{site.type}</small>
                <p>{site.notes}</p>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
