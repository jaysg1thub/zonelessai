import os
from flask import Flask, jsonify, request
import oracledb
from dotenv import load_dotenv

# Load environmental variables from your local network .env configuration
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
        
        return jsonify({
            "status": "online",
            "active_agent": "ZonelessAI Scout Core",
            "infrastructure": "Oracle 26ai Linked",
            "database_version": db_version[0] if db_version else "Unknown",
            "target_node": "ordsoel88 (192.168.1.16)"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "offline",
            "infrastructure": "Connection Error",
            "details": str(e)
        }), 500

@app.route('/api/scout/location', methods=['POST'])
def scout_location():
    """Processes coordinates using native Oracle 26ai VECTOR_DISTANCE metrics."""
    data = request.get_json() or {}
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    # Optional vector preference sent by client: [Expat/Tech, Nightlife, Quiet]
    # Defaults to a high Expat/Tech preference vector if none provided
    user_vibe = data.get("vibe_preference", "[0.90, 0.70, 0.20]")
    
    if not latitude or not longitude:
        return jsonify({"error": "Missing precise timeline coordinates"}), 400
        
    try:
        conn = get_oracle_connection()
        cursor = conn.cursor()
        
        # Native Oracle 26ai Vector Distance Query Statement
        # Orders merchants by closest geometric match to user's interest matrix
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
                "name": row[0],
                "category": row[1],
                "perk": row[2],
                "is_partner": bool(row[3]),
                "match_distance_score": round(float(row[4]), 4)
            })
            
        cursor.close()
        conn.close()
        
        return jsonify({
            "message": "Coordinates processed successfully via Oracle 26ai Vector Core",
            "target_coordinates": {"lat": latitude, "lng": longitude},
            "scout_results": scout_results,
            "total_matches_found": len(scout_results)
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Boot the application server on local port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
