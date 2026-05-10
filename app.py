import sys
import os

# Add the dashboard directory to sys.path so it can find layout, callbacks, etc.
dashboard_dir = os.path.join(os.path.dirname(__file__), "dashboard")
sys.path.insert(0, dashboard_dir)

from dashboard.app import server

# Expose 'app' as an alias for 'server' because the user is running 'gunicorn app:app'
app = server

if __name__ == "__main__":
    from dashboard.app import app as dash_app
    port = int(os.environ.get("PORT", 8050))
    dash_app.run(debug=True, host="0.0.0.0", port=port)
