# Getting Started Guide

## რა არის ეს პროექტი?

ეს არის სრული ღირებული აპლიკაცია Georgian დოკუმენტების (მიგების აქტი და ფორმა 2) ავტომატური გენერირებისთვის. სისტემა დინამიურად აკლებს PDF დოკუმენტებს ფორმებიდან შემოსული მონაცემების საფუძველზე.

## ტექოლოგიის სტეკი

### Frontend
- ⚛️ **React 18** - ინტერფეისი
- 🎨 **CSS3** - სტილიზაცია
- 📡 **Axios** - ბექენდთან კომუნიკაცია

### Backend  
- 🐍 **Python 3.x** - სერვერ ენა
- 🔌 **Flask** - ვებ ჩარჩო
- 🗄️ **SQLite** - ბაზა
- 📄 **WeasyPrint** - PDF გენერაცია

---

## ღირებული დაინსტალაცი球

### 1️⃣ Python დამოკიდებულებები დაინსტალირება

```bash
# გადაადგილება ბექენდ ფოლდერში
cd backend

# დამოკიდებულებების დაინსტალაცია
pip install -r ../requirements.txt
```

**შენიშვნა Windows-ზე WeasyPrint-ის პრობლემის შემთხვევაში:**
```bash
pip install --upgrade pip
pip install weasyprint
```

### 2️⃣ React დამოკიდებულებები დაინსტალირება

```bash
# გადაადგილება ფრონტენდ ფოლდერში  
cd frontend

# ზეპირი მოთხოვნილებები
npm install
```

> **შენიშვნა:** თქვენ უნდა გქონდეთ Node.js დაინსტალირებული. დაიწერეთ: `node --version`

---

## დაშვების გზა

### ვარიანტი 1: ხელის მართ დაშვება

#### ბექენდის დაშვება
```bash
cd backend
python app.py
```
✅ ტერმინალი გამოაჩენს: `Running on http://localhost:5000`

#### ფრონტენდის დაშვება (ახალ ტერმინალში)
```bash
cd frontend
npm start
```
✅ ბრაუზერი გაიხსნება: `http://localhost:3000`

### ვარიანტი 2: PowerShell ტექსტიდან ერთი ნაჭერი

თქვენი Windows აჭენის დირექტორია `baumer-act` ფოლდერში და დაშვება:

```powershell
# ორი პარალელური ზე დაშვება
Start-Process powershell -ArgumentList "cd $PWD\backend; python app.py"
Start-Process powershell -ArgumentList "cd $PWD\frontend; npm start"
```

---

## API Endpoints

### მიგების აქტი გენერირება
```
POST /api/generate/migeba-act
Content-Type: application/json

{
  "seller_name": "გიორგი ტოგონიძე",
  "seller_id": "12345678",
  "buyer_name": "თეა ხერხეულიძე",
  "buyer_id": "87654321",
  "property_description": "ვაკე, 3 ოთახიანი ბინა",
  "price": "50000",
  "receipt_method": "ნაღდი ფული",
  "terms": "მხარეები თანათავსე მოაქვს"
}
```

**პასუხი:**
```json
{
  "success": true,
  "document_id": 1,
  "file_path": "uploads/migeba_act_20240101_120000.pdf",
  "message": "Migeba Chabarebis Act generated successfully"
}
```

### ფორმა 2 გენერირება
```
POST /api/generate/forma2
Content-Type: application/json

{
  "owner_name": "გიორგი სმიტი",
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
```

### დოკუმენტის ჩამოტვირთვა
```
GET /api/download/{document_id}
```

---

## პროექტის სტრუქტურა

```
baumer-act/
├── README.md                    # ეს ფაილი
├── GETTING_STARTED.md          # დაშვების გზა
├── requirements.txt             # Python დამოკიდებულებები
│
├── backend/                     # Flask API
│   ├── app.py                   # მთავარი აპლიკაცია
│   ├── documents.py             # PDF გენერაციის ფუნქციები
│   └── database.py              # ბაზის ოპერაციები
│
└── frontend/                    # React აპლიკაცია
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js               # მთავარი კომპონენტი
        ├── App.css
        ├── index.js
        ├── index.css
        └── components/
            ├── MigebaForm.js    # მიგების აქტის ფორმა
            ├── MigebaForm.css
            ├── Forma2Form.js    # ფორმა 2
            └── Forma2Form.css
```

---

## გამოთეხვა (Troubleshooting)

### ❌ თითსითი / CORS ძალის ცერემონია
**პრობლემა:** Requests დაუშვება ფრონტედიდან

**ხსნა:** 
- strap Backend სწორი port-ზე დღეგ: `:5000`
- შემოწმეთ CORS ჩართული `app.py`-ში

### ❌ WeasyPrint-ს ინსტალაციის პრობლემა Windows-ზე
**ხსნა:**
```bash
pip install --upgrade pip setuptools
pip install weasyprint
```

### ❌ `npm start` დაკრაშირდა
**ხსნა:**
```bash
rm -r node_modules
npm install
npm start
```

### ❌ Port 5000 ან 3000 უკვე გამოიყენება
**ხსნა:**
- შეცვალეთ port `app.py`-ში: `app.run(port=5001)`
- შეცვალეთ REACT_APP_API_URL `.env` ფაილში (Frontend სცენარში)

---

## შემდეგი ნაშრომები

- [ ] ადმინ დაფა დოკუმენტებისთვის
- [ ] ზღვრული შემოწმება ფორმებისთვის
- [ ] ელმეილით PDF გაზიარება
- [ ] მულტიენოვანი ხელმისაწვდომობა
- [ ] დოკუმენტის რედაქტირების ფუნქცია

---

## ავტორი
თქვენი სახელი | 2024

## ლიცენცია
MIT
