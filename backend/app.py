from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
import os
from documents import generate_migeba_act
from database import init_db, save_document, get_document

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')


def resolve_document_path(file_path):
    """Resolve stored file path safely across different process working directories."""
    if not file_path:
        return None

    # Already absolute and exists
    if os.path.isabs(file_path) and os.path.exists(file_path):
        return file_path

    # Relative to backend directory
    backend_relative = os.path.join(BASE_DIR, file_path)
    if os.path.exists(backend_relative):
        return backend_relative

    # Fallback for old entries: resolve by filename under backend/uploads
    filename = os.path.basename(file_path)
    uploads_fallback = os.path.join(UPLOADS_DIR, filename)
    if os.path.exists(uploads_fallback):
        return uploads_fallback

    return None

# Initialize database
init_db()

# Create uploads directory
os.makedirs(UPLOADS_DIR, exist_ok=True)

@app.route('/api/generate/migeba-act', methods=['POST'])
def generate_migeba():
    """Generate Migeba Chabarebis Act PDF"""
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ['seller_name', 'buyer_name', 'property_description', 'price']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Generate PDF
        pdf_path = generate_migeba_act(data)
        
        # Save to database
        doc_id = save_document({
            'type': 'migeba_act',
            'seller': data.get('seller_name'),
            'buyer': data.get('buyer_name'),
            'property': data.get('property_description'),
            'amount': data.get('price'),
            'date_created': datetime.now(),
            'file_path': pdf_path
        })
        
        return jsonify({
            'success': True,
            'document_id': doc_id,
            'file_path': pdf_path,
            'message': 'Migeba Chabarebis Act generated successfully'
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/documents/<doc_id>', methods=['GET'])
def get_doc(doc_id):
    """Retrieve document by ID"""
    try:
        doc = get_document(doc_id)
        if doc:
            return jsonify(doc), 200
        return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/<doc_id>', methods=['GET'])
def download_doc(doc_id):
    """Download PDF document"""
    try:
        doc = get_document(doc_id)
        resolved_path = resolve_document_path(doc.get('file_path') if doc else None)
        if doc and resolved_path:
            return send_file(
                resolved_path,
                as_attachment=True,
                download_name=os.path.basename(resolved_path),
                mimetype='application/pdf'
            )
        return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'Backend is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
