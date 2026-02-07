from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

def get_final_url_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Crucial: Spoof a real browser to bypass bot protection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        time.sleep(3) # Wait for JS redirect
        return driver.current_url
    except:
        return "Error"
    finally:
        driver.quit()

@app.route('/expand', methods=['GET'])
def expand():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "No url provided"}), 400
    
    final_url = get_final_url_selenium(target_url)
    return jsonify({"original": target_url, "final": final_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
