# Development and Production Setup Guide

## Environment Variables

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000
```

### Backend (.env)
```
FLASK_ENV=development
DEBUG=True
DATABASE_URL=sqlite:///documents.db
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216
```

## Production Deployment

### Backend with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app
```

### Frontend Build
```bash
cd frontend
npm run build
```

Deploy the contents of `frontend/build/` to your static host or use Flask to serve:

```python
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_url_path='', static_folder='../frontend/build')

@app.route('/')
def serve():
    return send_from_directory('../frontend/build', 'index.html')
```

## Database Backup and Restore

### Backup Documents
```bash
# Copy the database file
cp documents.db documents.db.backup
```

### Restore Documents
```bash
# Restore from backup
cp documents.db.backup documents.db
```

## Performance Optimization

1. **Image Optimization**: Compress PDF output in WeasyPrint
2. **Database Indexing**: Add indexes to frequently queried columns
3. **Caching**: Implement Redis for form templates
4. **CDN**: Serve static assets from CDN in production

## Security Considerations

1. **Input Validation**: All form inputs are validated
2. **File Upload**: Restrict file types and sizes
3. **CORS**: Configure CORS properly for production domain
4. **Environment Variables**: Never commit sensitive data
5. **HTTPS**: Use SSL/TLS in production
