import sqlite3
import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'documents.db')

def init_db():
    """Initialize database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            owner TEXT,
            seller TEXT,
            buyer TEXT,
            property TEXT,
            property_address TEXT,
            amount TEXT,
            date_created TIMESTAMP,
            file_path TEXT,
            metadata TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def save_document(doc_data):
    """Save document record to database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO documents (type, owner, seller, buyer, property, property_address, amount, date_created, file_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        doc_data.get('type'),
        doc_data.get('owner'),
        doc_data.get('seller'),
        doc_data.get('buyer'),
        doc_data.get('property'),
        doc_data.get('property_address'),
        doc_data.get('amount'),
        doc_data.get('date_created'),
        doc_data.get('file_path')
    ))
    
    doc_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return doc_id

def get_document(doc_id):
    """Retrieve document from database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM documents WHERE id = ?', (doc_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return dict(row)
    return None

def get_all_documents():
    """Get all documents"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM documents ORDER BY date_created DESC')
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def delete_document(doc_id):
    """Delete document and its file"""
    doc = get_document(doc_id)
    if doc:
        # Delete file
        if os.path.exists(doc['file_path']):
            os.remove(doc['file_path'])
        
        # Delete from database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM documents WHERE id = ?', (doc_id,))
        conn.commit()
        conn.close()
        
        return True
    return False
