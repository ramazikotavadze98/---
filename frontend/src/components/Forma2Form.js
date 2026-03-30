import React, { useState } from 'react';
import axios from 'axios';
import './Forma2Form.css';

function Forma2Form() {
  const [formData, setFormData] = useState({
    owner_name: '',
    owner_id: '',
    phone: '',
    email: '',
    owner_address: '',
    property_address: '',
    property_type: '',
    area: '',
    legal_basis: 'მიგების აქტი / Transfer Act',
    registration_number: ''
  });

  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const result = await axios.post('http://localhost:5000/api/generate/forma2', formData);
      setResponse(result.data);
      setFormData({
        owner_name: '',
        owner_id: '',
        phone: '',
        email: '',
        owner_address: '',
        property_address: '',
        property_type: '',
        area: '',
        legal_basis: 'მიგების აქტი / Transfer Act',
        registration_number: ''
      });
    } catch (err) {
      setError(err.response?.data?.error || 'Error generating document');
    } finally {
      setLoading(false);
    }
  };

  const downloadDocument = async (docId) => {
    try {
      const response = await axios.get(`http://localhost:5000/api/download/${docId}`, {
        responseType: 'blob'
      });

      const disposition = response.headers['content-disposition'] || '';
      const filenameMatch = disposition.match(/filename=\"?([^\";]+)\"?/i);
      const filename = filenameMatch?.[1] || `document_${docId}.pdf`;

      const blobUrl = window.URL.createObjectURL(new Blob([response.data], { type: 'application/pdf' }));
      const link = document.createElement('a');
      link.href = blobUrl;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(blobUrl);
    } catch (downloadError) {
      setError('PDF ჩამოტვირთვა ვერ მოხერხდა. სცადეთ თავიდან.');
    }
  };

  return (
    <div className="form-container">
      <h2>ფორმა ორი</h2>
      
      <form onSubmit={handleSubmit} className="form">
        <fieldset>
          <legend>საკუთრის ინფორმაცია / Owner Information</legend>
          
          <div className="form-group">
            <label>მესაკუთრის სახელი * / Owner Name *</label>
            <input
              type="text"
              name="owner_name"
              value={formData.owner_name}
              onChange={handleChange}
              required
              placeholder="სახელი და გვარი"
            />
          </div>

          <div className="form-group">
            <label>პირადი ნომერი / ID Number</label>
            <input
              type="text"
              name="owner_id"
              value={formData.owner_id}
              onChange={handleChange}
              placeholder="პირადი ნომერი ან იურიდიული პირის რეგ. ნომერი"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>ტელეფონი / Phone</label>
              <input
                type="tel"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                placeholder="+995 599 123 456"
              />
            </div>
            <div className="form-group">
              <label>ელ-ფოსტა / Email</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="example@gmail.com"
              />
            </div>
          </div>

          <div className="form-group">
            <label>საცხოვრებელი მისამართი / Residential Address</label>
            <input
              type="text"
              name="owner_address"
              value={formData.owner_address}
              onChange={handleChange}
              placeholder="ქ. თბილისი, პროსპექტი..."
            />
          </div>
        </fieldset>

        <fieldset>
          <legend>ქონების დეტალები / Property Details</legend>
          
          <div className="form-group">
            <label>ქონების მისამართი * / Property Address *</label>
            <input
              type="text"
              name="property_address"
              value={formData.property_address}
              onChange={handleChange}
              required
              placeholder="ქ. თბილისი, გ. ვაკე, სახ. თ. შ."
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>ქონების ტიპი / Property Type</label>
              <select name="property_type" value={formData.property_type} onChange={handleChange}>
                <option value="">არჩეთ ტიპი</option>
                <option value="ბინა / Apartment">ბინა / Apartment</option>
                <option value="სახლი / House">სახლი / House</option>
                <option value="მიწა / Land">მიწა / Land</option>
                <option value="კომერციული / Commercial">კომერციული / Commercial</option>
              </select>
            </div>
            <div className="form-group">
              <label>ფართი * / Area * (m²)</label>
              <input
                type="number"
                name="area"
                value={formData.area}
                onChange={handleChange}
                required
                placeholder="მ²"
              />
            </div>
          </div>

          <div className="form-group">
            <label>რეგ. ნომერი / Registration Number</label>
            <input
              type="text"
              name="registration_number"
              value={formData.registration_number}
              onChange={handleChange}
              placeholder="უძრავი ქონების რეგ. ნომერი"
            />
          </div>

          <div className="form-group">
            <label>სამართლებრივი საფუძველი / Legal Basis</label>
            <select name="legal_basis" value={formData.legal_basis} onChange={handleChange}>
              <option value="მიგების აქტი / Transfer Act">მიგების აქტი / Transfer Act</option>
              <option value="ნასყიდობა / Purchase">ნასყიდობა / Purchase</option>
              <option value="კანონით მემკვიდრეობა / Inheritance">კანონით მემკვიდრეობა / Inheritance</option>
              <option value="ანდერძი / Will">ანდერძი / Will</option>
              <option value="საჩუქარი / Donation">საჩუქარი / Donation</option>
              <option value="გაცვლა / Exchange">გაცვლა / Exchange</option>
              <option value="სამისდღეშიო რჩენა / Lifetime Maintenance">სამისდღეშიო რჩენა / Lifetime Maintenance</option>
              <option value="სასამართლო გადაწყვეტილება / Court Decision">სასამართლო გადაწყვეტილება / Court Decision</option>
              <option value="პრივატიზება / Privatization">პრივატიზება / Privatization</option>
              <option value="საქორწინო ხელშეკრულება / Marital Agreement">საქორწინო ხელშეკრულება / Marital Agreement</option>
              <option value="სხვა / Other">სხვა / Other</option>
            </select>
          </div>
        </fieldset>

        <button type="submit" disabled={loading} className="submit-btn">
          {loading ? 'დოკუმენტი იქმნება...' : 'დოკუმენტის გენერირება'}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}

      {response && (
        <div className="success-message">
          <p>✓ {response.message}</p>
          <button
            onClick={() => downloadDocument(response.document_id)}
            className="download-btn"
          >
            📥 PDF ჩამოტვირთვა
          </button>
        </div>
      )}
    </div>
  );
}

export default Forma2Form;
