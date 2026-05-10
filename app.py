import os
import sys

# ── Force the current directory into sys.path ────────────────────────────────
# This ensures that 'dashboard' can be found regardless of how Gunicorn is started.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ── Debugging Info (will appear in Render logs) ──────────────────────────────
print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not Set')}")
print(f"sys.path: {sys.path}")
print(f"Current Directory: {os.getcwd()}")
try:
    print(f"Contents of {BASE_DIR}: {os.listdir(BASE_DIR)}")
except Exception as e:
    print(f"Could not list directory: {e}")

# ── Import the server ────────────────────────────────────────────────────────
try:
    from dashboard.app import server
except ModuleNotFoundError as e:
    print(f"ERROR: Could not import dashboard.app. {e}")
    # Fallback attempt: if we are inside a subdirectory, try to find dashboard
    raise e

# Expose 'app' as an alias for 'server' for Gunicorn (web: gunicorn app:app)
app = server

if __name__ == "__main__":
    from dashboard.app import app as dash_app
    port = int(os.environ.get("PORT", 8050))
    dash_app.run(debug=True, host="0.0.0.0", port=port)
