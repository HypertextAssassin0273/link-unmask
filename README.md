# 🕵️ link-unmask

**Because sometimes `HTTP 200 OK` is a lie.**

A lightweight Python API that uses a headless Chrome browser (Selenium) to follow links that use JavaScript redirects, meta-refreshes, or client-side logic to cloak their final destination.

Built to be deployed on **Render** (or any Docker-compatible host) and consumed directly by **Google Sheets**.

## ⚡ The Problem
Standard HTTP libraries (like Python's `requests` or Google Apps Script's `UrlFetchApp`) only fetch the initial HTML. They cannot execute JavaScript.
If a link returns a "Loading..." page and then uses `window.location.replace(...)` to redirect you, standard tools will report a success (Status 200) but fail to give you the actual destination URL.

## 🛠️ The Solution
`link-unmask` spins up a headless Chrome instance, visits the URL, waits for the dust to settle (JS execution), and returns the *actual* final URL in the browser address bar.

### Tech Stack
* **Python 3.9+**
* **Flask** (API Server)
* **Selenium** (Browser Automation)
* **Docker** (Containerization)
* **Gunicorn** (Production Server)

## 🚀 Deployment (Render.com)

This project is Dockerized and ready for [Render](https://render.com).

1.  **Fork/Clone** this repo.
2.  Create a new **Web Service** on Render.
3.  Connect your repository.
4.  Select **Docker** as the Runtime.
5.  Deploy! 

*Note: The free tier of Render spins down after inactivity, so the first request might take 50s. Subsequent requests will be fast.*

## 💻 Local Development

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/yourusername/link-unmask.git](https://github.com/yourusername/link-unmask.git)
    cd link-unmask
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the server:**
    ```bash
    python app.py
    ```

4.  **Test it:**
    Visit `http://localhost:10000/expand?url=https://outskill.link/wisprflow`

## 📊 Google Sheets Integration

Want to use this directly in your spreadsheet?

1.  Open your Google Sheet.
2.  Go to **Extensions > Apps Script**.
3.  Paste the following code:

```javascript
/**
 * Calls your custom Link Unmask API to resolve redirects.
 * @param {string} url The short link to resolve.
 * @return The final destination URL.
 * @customfunction
 */
function UNMASK_LINK(url) {
  if (!url) return "";
  
  // REPLACE with your actual Render URL
  var apiEndpoint = "[https://link-unmask.com/expand](https://your-app-name.onrender.com/expand)"; 
  
  try {
    var response = UrlFetchApp.fetch(apiEndpoint + "?url=" + encodeURIComponent(url));
    var json = JSON.parse(response.getContentText());
    return json.final;
  } catch (e) {
    return "Error: " + e.message;
  }
}
```
