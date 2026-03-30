#!/usr/bin/env python
"""
Quick test script for the Document Generator API
"""
import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test backend health"""
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print("✓ Backend Health:", response.json())
        return True
    except Exception as e:
        print("✗ Backend Error:", e)
        return False

def test_migeba_act():
    """Test Transfer Act generation"""
    data = {
        "seller_name": "გიორგი ტოგონიძე",
        "seller_id": "12345678",
        "buyer_name": "თეა ხერხეულიძე",
        "buyer_id": "87654321",
        "property_description": "ვაკე, 3 ოთახიანი ბინა",
        "price": "50000",
        "receipt_method": "ნაღდი ფული",
        "terms": "მხარეები ხელი მოიწერენ აქტს"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/generate/migeba-act", json=data)
        result = response.json()
        if response.status_code == 201:
            print("✓ Migeba Act Generated:")
            print(f"  Document ID: {result['document_id']}")
            print(f"  File: {result['file_path']}")
            return result['document_id']
        else:
            print("✗ Error:", result.get('error', 'Unknown error'))
            return None
    except Exception as e:
        print("✗ Request failed:", e)
        return None

def test_forma2():
    """Test Form 2 generation"""
    data = {
        "owner_name": "გიორგი ტოგონიძე",
        "owner_id": "12345678",
        "phone": "+995 599 123456",
        "email": "giorgi@example.com",
        "owner_address": "თბილისი, ვაკე",
        "property_address": "თბილისი, ვაკე, 1-ელი სახ.",
        "property_type": "ბინა",
        "area": "75",
        "legal_basis": "მიგების აქტი",
        "registration_number": "REG123456"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/generate/forma2", json=data)
        result = response.json()
        if response.status_code == 201:
            print("✓ Forma 2 Generated:")
            print(f"  Document ID: {result['document_id']}")
            print(f"  File: {result['file_path']}")
            return result['document_id']
        else:
            print("✗ Error:", result.get('error', 'Unknown error'))
            return None
    except Exception as e:
        print("✗ Request failed:", e)
        return None

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  დოკუმენტაციის გენერატორი - API Test")
    print("="*50 + "\n")
    
    # Test health
    if not test_health():
        print("\n⚠️  Backend is not running!")
        print("Start it with: python backend/app.py")
        exit(1)
    
    print("\n--- Testing Migeba Act ---")
    migeba_id = test_migeba_act()
    
    print("\n--- Testing Forma 2 ---")
    forma2_id = test_forma2()
    
    print("\n" + "="*50)
    if migeba_id and forma2_id:
        print("✅ All tests passed!")
    print("="*50 + "\n")
