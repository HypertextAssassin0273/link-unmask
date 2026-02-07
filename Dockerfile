# Use a lightweight Python image
FROM python:3.9-slim

# 1. Install basic utilities first
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    ca-certificates \
    --no-install-recommends

# 2. Add Google's signing key safely (The modern way, replacing apt-key)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg

# 3. Add the Chrome repository using the new key
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# 4. Install Chrome
RUN apt-get update && apt-get install -y google-chrome-stable && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Run the app
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
