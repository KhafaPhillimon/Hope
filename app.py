import os
from dashboard.app import server

# Expose 'app' as an alias for 'server' for Gunicorn (web: gunicorn app:app)
app = server

if __name__ == "__main__":
    from dashboard.app import app as dash_app
    port = int(os.environ.get("PORT", 8050))
    dash_app.run(debug=True, host="0.0.0.0", port=port)
