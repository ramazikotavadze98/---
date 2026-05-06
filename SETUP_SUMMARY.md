
```
baumer-act/
│
├── 📄 README.md                         
├── 📄 GETTING_STARTED.md                 
├── 📄 DEPLOYMENT.md                      
├── 📄 requirements.txt                    
├── 📄 start.bat                           
├── 📄 start.sh                         
├── 📄 .gitignore                      
│
├── 📂 backend/                           
│   ├── 📄 app.py                        
│   │   └─ same:
│   │      • POST /api/generate/migeba-act    
│   │      • GET /api/download/{id}          
│   │      • GET /api/documents/{id}         
│   │
│   ├── 📄 documents.py                   
│   │   └─ contains:
│   │      • generate_migeba_act()      
│   │
│   └── 📄 database.py                    
│       └─ contains:
│          • init_db()                 
│          • save_document()          
│          • get_document()             
│          • delete_document()          
│
└── 📂 frontend/                         
    ├── 📄 package.json                 
    │
    ├── 📂 public/
    │   └── 📄 index.html             
    │
    └── 📂 src/
        ├── 📄 App.js                   
        ├── 📄 App.css                 
        ├── 📄 index.js                 
        ├── 📄 index.css               
        │
        └── 📂 components/
            ├── 📄 MigebaForm.js       
          └── 📄 MigebaForm.css      
```

