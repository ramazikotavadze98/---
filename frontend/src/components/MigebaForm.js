import React, { useState } from 'react';
import axios from 'axios';
import './MigebaForm.css';

function MigebaForm() {
  const [formData, setFormData] = useState({
    seller_name: '',
    seller_id: '',
    buyer_name: '',
    buyer_id: '',
    property_description: '',
    price: '',
    receipt_method: 'ნაღდი ფული / cash',
    terms: ''
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
      const result = await axios.post('http://localhost:5000/api/generate/migeba-act', formData);
      setResponse(result.data);
      setFormData({
        seller_name: '',
        seller_id: '',
        buyer_name: '',
        buyer_id: '',
        property_description: '',
        price: '',
        receipt_method: 'ნაღდი ფული / cash',
        terms: ''
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
      <h2>მიღება ჩაბარების აქტი (Transfer Act)</h2>
      
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label>გამყიდველის სახელი * / Seller Name *</label>
          <input
            type="text"
            name="seller_name"
            value={formData.seller_name}
            onChange={handleChange}
            required
            placeholder="გამყიდველის სახელი და გვარი"
          />
        </div>

        <div className="form-group">
          <label>გამყიდველის ID რ. / Seller ID Number</label>
          <input
            type="text"
            name="seller_id"
            value={formData.seller_id}
            onChange={handleChange}
            placeholder="ID ნომერი"
          />
        </div>

        <div className="form-group">
          <label>მყიდველის სახელი * / Buyer Name *</label>
          <input
            type="text"
            name="buyer_name"
            value={formData.buyer_name}
            onChange={handleChange}
            required
            placeholder="მყიდველის სახელი და გვარი"
          />
        </div>

        <div className="form-group">
          <label>მყიდველის ID რ. / Buyer ID Number</label>
          <input
            type="text"
            name="buyer_id"
            value={formData.buyer_id}
            onChange={handleChange}
            placeholder="ID ნომერი"
          />
        </div>

        <div className="form-group">
          <label>ქონების აღწერა * / Property Description *</label>
          <textarea
            name="property_description"
            value={formData.property_description}
            onChange={handleChange}
            required
            placeholder="მოწვევილი აღწერა ქონების (მდებარეობა, ტიპი, მახასიათებლები)"
            rows="4"
          ></textarea>
        </div>

        <div className="form-group">
          <label>ფასი * / Price * (₾)</label>
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
            required
            placeholder="მოთხოვნილი თანხა"
          />
        </div>

        <div className="form-group">
          <label>გადახდის მეთოდი / Payment Method</label>
          <select name="receipt_method" value={formData.receipt_method} onChange={handleChange}>
            <option value="ნაღდი ფული / cash">ნაღდი ფული / Cash</option>
            <option value="ბანკი / bank">ბანკი / Bank Transfer</option>
            <option value="სხვა / other">სხვა / Other</option>
          </select>
        </div>

        <div className="form-group">
          <label>დამატებითი პირობები / Additional Terms</label>
          <textarea
            name="terms"
            value={formData.terms}
            onChange={handleChange}
            placeholder="მხარეთა შორის შეთანხმებული დამატებითი პირობები"
            rows="3"
          ></textarea>
        </div>

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

export default MigebaForm;
