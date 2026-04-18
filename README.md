# Flask Azure App 🚀

This is a basic Flask application deployed using Azure App Service with GitHub integration.

## 📌 Features

* Health check endpoint
* User management APIs (GET, POST, DELETE)
* Environment variables endpoint
* Ready for Azure deployment

## 🔗 API Endpoints

### Home

GET `/`

```
{"message": "Flask App Running Successfully"}
```

### Health

GET `/health`

### Users

* GET `/users`
* POST `/users`
* DELETE `/users/<index>`

### Environment Variables

GET `/env`

## ⚙️ Setup (Local)

```bash
pip install -r requirements.txt
python app.py
```

## 🌐 Deployment

This app is deployed using Azure App Service via GitHub Actions.

## ⚠️ Notes

* `.env` is not pushed to GitHub
* Environment variables are configured in Azure App Service
