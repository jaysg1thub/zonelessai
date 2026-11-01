import os
from flask import Flask, jsonify, request, send_from_directory
import oracledb
from dotenv import load_dotenv

# Load environmental configurations targeting ordsoel88
load_dotenv()

app = Flask(__name__)

def get_oracle_connection():
    """Establishes an isolated network transaction connection to the Oracle 26ai core."""
    return oracledb.connect(
        user=os.getenv("ORACLE_DB_USER"),
        password=os.getenv("ORACLE_DB_PASS"),
        host=os.getenv("ORACLE_DB_HOST"),
        port=os.getenv("ORACLE_DB_PORT"),
        service_name=os.getenv("ORACLE_DB_SERVICE")
    )

@app.route('/manifest.json')
def serve_manifest():
    """Serves the PWA configuration parameters to allow phone installations."""
    return send_from_directory('static', 'manifest.json')

@app.route('/', methods=['GET'])
def serve_dashboard():
    """Renders the mobile-optimized PWA application console shell."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ZonelessAI Engine</title>
        <link rel="manifest" href="/manifest.json">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <style>
            body { background-color: #000000; color: #e5e5e5; font-family: monospace; margin: 0; padding: 0; }
            .main-container { max-width: 440px; margin: 0 auto; min-height: 100vh; display: flex; flex-direction: column; justify-content: space-between; padding: 20px; background-color: #0a0a0a; border-left: 1px solid #1a1a1a; border-right: 1px solid #1a1a1a; box-sizing: border-box; }
            header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 16px; border-bottom: 1px solid #1a1a1a; }
            .header-title { color: #ffffff; font-weight: bold; text-transform: uppercase; font-size: 15px; letter-spacing: 2px; margin: 0; }
            .badge { background-color: #064e3b; color: #34d399; border: 1px solid #047857; padding: 4px 10px; font-size: 11px; border-radius: 4px; font-weight: bold; }
            .stream-area { flex-grow: 1; margin: 20px 0; overflow-y: auto; }
            .node-box { border: 1px solid #1a1a1a; background-color: #121212; padding: 14px; border-radius: 6px; margin-bottom: 20px; }
            .node-label { font-size: 10px; color: #737373; text-transform: uppercase; display: block; margin-bottom: 6px; font-weight: bold; }
            .node-text { font-size: 14px; color: #d4d4d4; }
            .node-highlight { color: #10b981; font-weight: bold; }
            .section-title { font-size: 13px; color: #10b981; text-transform: uppercase; font-weight: bold; letter-spacing: 1px; display: block; margin-bottom: 16px; }
            .merchant-card { border: 1px solid #1a1a1a; background-color: #121212; padding: 16px; border-radius: 6px; margin-bottom: 16px; }
            .card-header { display: flex; justify-content: space-between; align-items: center; }
            .merchant-name { font-size: 15px; font-weight: bold; color: #ffffff; }
            .match-badge { font-size: 11px; background-color: #064e3b; color: #34d399; border: 1px solid #047857; padding: 3px 8px; border-radius: 4px; font-weight: bold; }
            .merchant-perk { font-size: 13px; color: #cbd5e1; margin: 12px 0 8px 0; line-height: 1.5; }
            .merchant-module { font-size: 10px; color: #737373; font-weight: bold; text-transform: uppercase; }
            footer { padding-top: 16px; border-top: 1px solid #1a1a1a; background-color: #0a0a0a; }
            .scan-btn { width: 100%; shortcut: 100%; background-color: #10b981; border: none; color: #000000; font-weight: bold; padding: 14px; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; border-radius: 4px; cursor: pointer; font-family: monospace; transition: all 0.2s; }
            .scan-btn:active { transform: scale(0.99); opacity: 0.9; }
            .nav-grid { display: grid; grid-template-columns: repeat(3, 1fr); text-align: center; font-size: 12px; color: #737373; padding-top: 16px; font-weight: bold; }
            .nav-active { color: #10b981; }
            .placeholder-text { font-size: 13px; color: #737373; font-style: italic; }
            .pulse-text { font-size: 13px; color: #10b981; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="main-container">
            
            <!-- App Header -->
            <header>
                <h1 class="header-title">ZonelessAI Console</h1>
                <span class="badge">AGENT_ACTIVE</span>
            </header>

            <!-- Main Live Stream Node Area -->
            <div class="stream-area">
                <div class="node-box">
                    <span class="node-label">SYSTEM COUPLING</span>
                    <div class="node-text">Connected to Node: <span class="node-highlight">ordsoel88</span></div>
                </div>

                <div>
                    <span class="section-title">🎯 Native Proactive Matches</span>
                    <div id="results-box">
                        <p class="placeholder-text">Initialize location scanning to engage vector space metrics...</p>
                    </div>
                </div>
            </div>

            <!-- Navigation Controls -->
            <footer>
                <button onclick="triggerLocationScan()" class="scan-btn">
                    Scan Local Environment
                </button>
                <div class="nav-grid">
                    <div class="nav-active">Scout</div>
                    <div>Luggage</div>
                    <div>Rentals</div>
                </div>
            </footer>

        </div>

        <script>
        function triggerLocationScan() {
            const resultsBox = document.getElementById('results-box');
            resultsBox.innerHTML = '<p class="pulse-text">Querying Oracle 26ai vector space maps...</p>';
            
            fetch('/api/scout/location', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    latitude: 14.5492,
                    longitude: 121.0478,
                    vibe_preference: "[0.90, 0.80, 0.15]"
                })
            })
            .then(res => res.json())
            .then(data => {
                resultsBox.innerHTML = '';
                data.scout_results.forEach(item => {
                    resultsBox.innerHTML += `
                        <div class="merchant-card">
                            <div class="card-header">
                                <div class="merchant-name">${item.name}</div>
                                <span class="match-badge">MATCH: ${Math.round((1 - item.match_distance_score) * 100)}%</span>
                            </div>
                            <p class="merchant-perk">${item.perk}</p>
                            <div class="merchant-module">${item.category} Module</div>
                        </div>
                    `;
                });
            })
            .catch(err => {
                resultsBox.innerHTML = `<p style="color: #ef4444; font-size: 13px;">Pipeline error: ${err}</p>`;
            });
        }
        </script>
    </body>
    </html>
    """

@app.route('/api/agent/status', methods=['GET'])
def agent_status():
    """Tests connection to ordsoel88 dynamically and returns status metrics."""
    try:
        conn = get_oracle_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT banner_full FROM v$version")
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"status": "online", "database_version": db_version if db_version else "Unknown"}), 200
    except Exception as e:
        return jsonify({"status": "offline", "details": str(e)}), 500

@app.route('/api/scout/location', methods=['POST'])
def scout_location():
    """Processes coordinates using native Oracle 26ai VECTOR_DISTANCE metrics."""
    data = request.get_json() or {}
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    user_vibe = data.get("vibe_preference", "[0.90, 0.70, 0.20]")
    
    if not latitude or not longitude:
        return jsonify({"error": "Missing coordinates"}), 400
        
    try:
        conn = get_oracle_connection()
        cursor = conn.cursor()
        query = """
            SELECT name, category, perk_description, is_partner,
                   VECTOR_DISTANCE(vibe_vector, TO_VECTOR(:vibe), COSINE) as distance
            FROM ZONELESS_MERCHANTS
            ORDER BY distance ASC
        """
        cursor.execute(query, vibe=user_vibe)
        rows = cursor.fetchall()
        
        scout_results = []
        for row in rows:
            scout_results.append({
                "name": row, "category": row, "perk": row,
                "is_partner": bool(row), "match_distance_score": round(float(row), 4)
            })
        cursor.close()
        conn.close()
        return jsonify({"scout_results": scout_results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
