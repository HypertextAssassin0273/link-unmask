from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def unmask_link(url):
    # 1. AUTO-FIX: Add https:// if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        # 2. MIMIC BROWSER: Use a real User-Agent to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        # 3. USE GET (STREAM): HEAD requests are often blocked. GET with stream=True is safer. 
        response = requests.get(
            url, 
            allow_redirects=True, 
            timeout=10,  # set a reasonable timeout to avoid hanging
            headers=headers, 
            stream=True 
        )
        
        # Close the connection immediately so we don't download the website body
        response.close()
        
        return response.url
        
    except requests.exceptions.Timeout:
        return "Error: Timeout - The website took too long to respond."
    except requests.exceptions.ConnectionError:
        return "Error: Connection Refused - The website might be down or blocking us."
    except requests.exceptions.TooManyRedirects:
        return "Error: Redirect Loop - The link redirects to itself infinitely."
    except Exception as e:
        return "Error: Request Failed - Unable to process the link."

@app.route('/expand', methods=['GET'])
def expand():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing url parameter"}), 400
    
    # Run the unmasker
    final_url = unmask_link(url)
    
    return jsonify({
        "original": url,
        "final": final_url
    })

if __name__ == '__main__':
    # Use a production-ready server argument if needed, but default is fine for Render's Gunicorn
    app.run(host='0.0.0.0', port=10000)
