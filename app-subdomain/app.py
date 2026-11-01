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
        <script src="https://jsdelivr.net"></script>
    </head>
    <body class="bg-black text-neutral-200 font-mono antialiased">
        <main class="max-w-md mx-auto min-h-screen flex flex-col justify-between p-4 bg-neutral-950 border-x border-neutral-900 shadow-2xl">
            
            <!-- App Header -->
            <header class="flex justify-between items-center py-3 border-b border-neutral-900">
                <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <h1 class="text-white font-bold tracking-widest text-xs uppercase">ZonelessAI Console</h1>
                </div>
                <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-900 px-2 py-0.5 rounded font-sans">AGENT_ACTIVE</span>
            </header>

            <!-- Main Live Stream Node Area -->
            <section class="flex-grow my-4 space-y-4 overflow-y-auto max-h-[70vh]">
                <div class="border border-neutral-900 bg-black/40 p-4 rounded-lg space-y-1">
                    <span class="text-[9px] text-neutral-500">SYSTEM COUPLING</span>
                    <div class="text-xs text-neutral-300">Connected to Node: <span class="text-emerald-400">ordsoel88</span></div>
                </div>

                <div class="space-y-2">
                    <span class="text-[10px] text-emerald-500 uppercase tracking-wider font-bold">🎯 Native Proactive Matches</span>
                    <div id="results-box" class="space-y-2">
                        <p class="text-[11px] text-neutral-600 italic">Initialize location scanning to engage vector space metrics...</p>
                    </div>
                </div>
            </section>

            <!-- Navigation Controls -->
            <footer class="space-y-2 pt-2 border-t border-neutral-900">
                <button onclick="triggerLocationScan()" class="w-full bg-emerald-500 hover:bg-emerald-400 active:scale-[0.99] text-black font-bold py-3 text-xs tracking-wider uppercase rounded transition-all cursor-pointer">
                    Scan Local Environment
                </button>
                <div class="grid grid-cols-3 text-center text-[10px] text-neutral-500 pt-2 font-sans font-medium">
                    <div class="text-emerald-400 font-mono font-bold">Scout</div>
                    <div>Luggage</div>
                    <div>Rentals</div>
                </div>
            </footer>

        </main>

        <script>
        function triggerLocationScan() {
            const resultsBox = document.getElementById('results-box');
            resultsBox.innerHTML = '<p class="text-[11px] text-emerald-400 animate-pulse">Querying Oracle 26ai vector space maps...</p>';
            
            // Simulating a mobile GPS hardware polling interaction coordinate drop
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
                        <div class="border border-neutral-900 bg-neutral-900/30 p-3 rounded space-y-2">
                            <div class="flex justify-between items-start">
                                <div class="text-xs font-bold text-white">${item.name}</div>
                                <span class="text-[8px] bg-emerald-950 text-emerald-400 border border-emerald-900/50 px-1.5 py-0.5 rounded font-sans font-bold">MATCH: ${Math.round((1 - item.match_distance_score) * 100)}%</span>
                            </div>
                            <p class="text-[10px] text-neutral-400 leading-normal">${item.perk}</p>
                            <div class="text-[9px] text-neutral-600 font-sans font-semibold">${item.category} Module</div>
                        </div>
                    `;
                });
            })
            .catch(err => {
                resultsBox.innerHTML = `<p class="text-xs text-red-500">Pipeline error: ${err}</p>`;
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
        return jsonify({"status": "online", "database_version": db_version[0] if db_version else "Unknown"}), 200
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
                "name": row[0], "category": row[1], "perk": row[2],
                "is_partner": bool(row[3]), "match_distance_score": round(float(row[4]), 4)
            })
        cursor.close()
        conn.close()
        return jsonify({"scout_results": scout_results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
