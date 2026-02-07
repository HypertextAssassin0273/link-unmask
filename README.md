# 🕵️ Link Unmasker

**Because sometimes `HTTP 200 OK` is a lie.**

A high-performance, lightweight API to unmask shortened links (bit.ly, tinyurl, etc.) and reveal their true destination. Built with Python Flask.

## 🚀 Features
- **Lightweight:** Uses `requests` instead of heavy browsers like Selenium.
- **Smart Handling:** Auto-fixes missing protocols (`http/s`) and mimics real browser headers.
- **Fast:** Optimizes connection handling to resolve redirects in milliseconds.
- **JSON API:** Simple endpoint integration for any application.

## ⚡ Usage

**Endpoint:**
`GET https://<domain>/expand`

**Parameters:**
- `url`: The shortened link you want to unmask.

**Example Request:**
```bash
curl "[https://<domain>/expand?url=bit.ly/3gDq9q5](https://<domain>/expand?url=bit.ly/3gDq9q5)"
```

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
  // REPLACE with your actual Render/Cloudfare URL
  const apiEndpoint = "[https://<domain>/expand](https://<domain>/expand)";
  try {
    const response = UrlFetchApp.fetch(apiEndpoint + "?url=" + encodeURIComponent(url));
    const json = JSON.parse(response.getContentText());
    return json.final;
  } catch (e) {
    return "Error: " + e.message;
  }
}
```
