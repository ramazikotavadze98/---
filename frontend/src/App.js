import React, { useState } from 'react';
import MigebaForm from './components/MigebaForm';
import './App.css';

function App() {
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
          <p>Document Generator - მიღება ჩაბარების აქტი</p>
        </div>
      </header>

      <nav className="nav-tabs">
        <button className="nav-tab active">მიღება-ჩაბარების აქტი</button>
      </nav>

      <main className="main-content">
        <MigebaForm />
      </main>

      <footer className="app-footer">
        <p>© 2024 Document Generator | მიღება-ჩაბარების აქტი</p>
      </footer>
    </div>
  );
}

export default App;
