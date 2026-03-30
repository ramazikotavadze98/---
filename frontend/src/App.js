import React, { useState } from 'react';
import MigebaForm from './components/MigebaForm';
import Forma2Form from './components/Forma2Form';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('migeba');
  const [logoVisible, setLogoVisible] = useState(true);

  const handleLogoLoad = (e) => {
    const img = e.currentTarget;
    const ratio = img.naturalHeight > 0 ? img.naturalWidth / img.naturalHeight : 0;
    if (ratio < 2.2) {
      setLogoVisible(false);
    }
  };

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          {logoVisible && (
            <img
              src="/Baumer-Logo.png"
              alt="Baumer"
              className="brand-logo"
              onLoad={handleLogoLoad}
              onError={() => setLogoVisible(false)}
            />
          )}
          {!logoVisible && (
            <div className="brand-fallback" aria-label="Baumer">
              <div className="brand-fallback-title">BAUMER</div>
              <div className="brand-fallback-subtitle">ENGINEERING EXCELLENCE</div>
            </div>
          )}
          <h1>დოკუმენტაციის გენერატორი</h1>
          <p>Document Generator - მიღება ჩაბარების აქტი და ფორმა 2</p>
        </div>
      </header>

      <nav className="nav-tabs">
        <button
          className={`nav-tab ${activeTab === 'migeba' ? 'active' : ''}`}
          onClick={() => setActiveTab('migeba')}
        >
          მიგების აქტი
        </button>
        <button
          className={`nav-tab ${activeTab === 'forma2' ? 'active' : ''}`}
          onClick={() => setActiveTab('forma2')}
        >
          ფორმა 2
        </button>
      </nav>

      <main className="main-content">
        {activeTab === 'migeba' && <MigebaForm />}
        {activeTab === 'forma2' && <Forma2Form />}
      </main>

      <footer className="app-footer">
        <p>© 2024 Document Generator | მიგების აქტი და ფორმა 2</p>
      </footer>
    </div>
  );
}

export default App;
