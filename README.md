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
 * Unmasks a shortened URL using your custom Link Unmasker API.
 *
 * @param {string} url The shortened URL (e.g., "bit.ly/xyz").
 * @return {string} The unmasked, final destination URL.
 * @customfunction
 */
function UNMASK(url) {
  // 1. Validation: If cell is empty, do nothing
  if (!url) return "";

  // 2. Define your API Endpoint
  const apiEndpoint = "https://<domain>/expand?url=" + encodeURIComponent(url);

  try {
    // 3. Call the API
    const response = UrlFetchApp.fetch(apiEndpoint, {
      'muteHttpExceptions': true // Prevents the script from crashing if the API returns 404/500
    });

    const json = JSON.parse(response.getContentText());

    // 4. Return the 'final' URL from your JSON response
    return json.final || "Error: No final link found";

  } catch (e) {
    return "Error: " + e.message;
  }
}
```
