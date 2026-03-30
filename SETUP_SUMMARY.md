# პროექტის ღირებული, დაამატა
 
ამჯამად თქვენი სრული ღირებული აპლიკაციის ფოლდერი დაიზღვება:

## 📁 პროექტის სტრუქტურა

```
baumer-act/
│
├── 📄 README.md                          # პროექტის მოკლე აღწერა
├── 📄 GETTING_STARTED.md                 # დაშვების დეტალური გზა
├── 📄 DEPLOYMENT.md                      # შენახვის ინსტრუქციები
├── 📄 requirements.txt                   # Python დამოკიდებულებები
├── 📄 start.bat                          # Windows დაშვების სკრიპტი
├── 📄 start.sh                           # Linux/Mac დაშვების სკრიპტი
├── 📄 .gitignore                        # Git უგულელყოფის ფაილი
│
├── 📂 backend/                           # Flask API სერვერი
│   ├── 📄 app.py                        # მთავარი აპლიკაცია
│   │   └─ შესაბამის:
│   │      • POST /api/generate/migeba-act    (მიგების აქტი)
│   │      • POST /api/generate/forma2        (ფორმა 2)
│   │      • GET /api/download/{id}          (PDF ჩამოტვირთვა)
│   │      • GET /api/documents/{id}         (დოკ. მონაცემი)
│   │
│   ├── 📄 documents.py                  # PDF გენერაციის ფუნქციები
│   │   └─ შეიცავს:
│   │      • generate_migeba_act()      (მიგების აქტი PDF)
│   │      • generate_forma2()          (ფორმა 2 PDF)
│   │
│   └── 📄 database.py                  # ბაზის ოპერაციები SQLite
│       └─ შეიცავს:
│          • init_db()                 (ბაზის შექმნა)
│          • save_document()            (დოკუმენტის შენახვა)
│          • get_document()             (დოკუმენტის მიღება)
│          • delete_document()          (დოკუმენტის წაშლა)
│
└── 📂 frontend/                          # React ვებ აპლიკაცია
    ├── 📄 package.json                  # NPM დამოკიდებულებები
    │
    ├── 📂 public/
    │   └── 📄 index.html               # HTML შაბლონი
    │
    └── 📂 src/
        ├── 📄 App.js                   # მთავარი კომპონენტი
        ├── 📄 App.css                  # მთავარი სტილი
        ├── 📄 index.js                 # React შე
        ├── 📄 index.css                # გლობალური სტილი
        │
        └── 📂 components/
            ├── 📄 MigebaForm.js        # მიგების აქტის ფორმა
            ├── 📄 MigebaForm.css       # მიგების ფორმის სტილი
            ├── 📄 Forma2Form.js        # ფორმა 2
            └── 📄 Forma2Form.css       # ფორმა 2 სტილი
```

---

## 🚀 দ্রুত დაশვება

### Windows-ზე:
```bash
# უბრალო Double-click ან:
start.bat
```

### Mac/Linux-ზე:
```bash
chmod +x start.sh
./start.sh
```

### ხელის მართ დაშვება:

**ტერმინალი 1 - Backend:**
```bash
cd backend
pip install -r ../requirements.txt
python app.py
```

**ტერმინალი 2 - Frontend:**
```bash
cd frontend
npm install
npm start
```

---

## ✨ ძირითადი ფუნქციონალობა

### 1. მიგების აქტი (Transfer Act)
- გამყიდველის და მყიდველის ინფორმაცია
- ქონების დეტალური აღწერა
- ფასი პირობები
- **ავტომატური PDF გენერაცია**

### 2. ფორმა 2 (Registration Form)
- საკუთრის ინფორმაცია
- ქონების დეტალები
- რეგისტრაციის მონაცემი
- **ავტომატური PDF გენერაცია**

### 3. ონლაინ დაფა
- ტაბი ორი დოკუმენტი ტიპისთვის
- მითითების პარალელი (Response)
- PDF ჩამოტვირთვის შესაძლებლობა
- MySQLите ბაზაზე სელის შენახვა

---

## 🔗 API მაგალითი

### მიგების აქტი გენერირება
```bash
curl -X POST http://localhost:5000/api/generate/migeba-act \
  -H "Content-Type: application/json" \
  -d '{
    "seller_name": "გიორგი სმიტი",
    "buyer_name": "თეა ხერხეულიძე",
    "property_description": "ვაკე, 3 ოთახიანი ბინა",
    "price": "50000"
  }'
```

### პასუხი
```json
{
  "success": true,
  "document_id": 1,
  "message": "მიგების აქტი успешно generated"
}
```

---

## 📊 ტექოლოგიის დეტალი

| ღირებული | ტეხნოლოგია | ვერსია | დანიშვულება |
|---------|-----------|--------|----------|
| ფრონტენდი | React | 18.2.0 | UI ინტერფეისი |
| ფრონტენდი | Axios | 1.5.0 | API გამოძახება |
| ბექენდი | Python | 3.x | მენეჯერი |
| ბექენდი | Flask | 2.3.3 | ვებ სერვერი |
| ბექენდი | WeasyPrint | 59.0 | PDF გენერაცია |
| ბაზა | SQLite | განუკითხავი | უძრავი მონაცემი |

---

## 📝 შემდეგი რეკომენდებული ნაშრომები

**დაკომპლექსება:**
- [ ] დაამატოთ ククი/ID ლოგინი
- [ ] დაამატოთ დოკუმენტების ისტორია
- [ ] გაკეთდეთ დოკუმენტის რედაქტირება
- [ ] დაამატოთ ელ-მეილის განცხადება
- [ ] დაამატოთ ბაჟი უტილიტა კოპირებისთვის

**ოპტიმიზაცია:**
- [ ] Redis ის ლიდერობა
- [ ] ფrontend CDN კონფიგურაცია
- [ ] database ინდექსირება
- [ ] PDF შეკუმშვა

---

## ⚠️ მნიშვნელოვანი შენიშვნები

1. **WeasyPrint ჩასატვირთ Windows-ზე:**
   ```bash
   pip install --upgrade pip
   pip install weasyprint
   ```

2. **Port რეკომენდაცია:**
   - Backend: `5000`
   - Frontend: `3000`
   
   თუ კონფლიქტი - შეცვალეთ `app.py`-ში

3. **CORS პრობლემის შემთხვევაში:**
   - შემოწმეთ რომ Backend სწორი port-ზე დღეგ
   - აირჩიეთ CORS აქტიურია `app.py`-ში

---

## 🆘 დახმარება

რიცხვითი ემოციონალური გეხმარება:
1. `GETTING_STARTED.md` - დეტალური დაშვება
2. `DEPLOYMENT.md` - შითავების სახელმძღვანელო
3. Backend logs - თითოეული ზე `localhost:5000`
4. Frontend logs - ბრაუზერი Console (F12)

---

## 📧 კონტაქტი

თქვენი ID დაზღვები გაგახელი... რა აპლიკაციის პროგრძელებასთან!

---

**დაწერილია:** 2024
**მდგომარეობა:** ✅ რეხ
