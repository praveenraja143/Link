# IPG - LinkedIn Auto Poster

## Quick Start

### 1. Install Dependencies
```bash
cd IPG
npm install
```

### 2. Run on Web (Development)
```bash
npm run web
```

### 3. Export for Web (Production)
```bash
npm run export:web
```
Output will be in `dist/` folder

### 4. Deploy to Render (Free Hosting)

**Option A: Connect GitHub to Render**
1. Push code to GitHub (already done)
2. Go to https://render.com
3. Sign up/Login
4. Click "New Static Site"
5. Connect your GitHub repo: `praveenraja143/Link`
6. Configure:
   - **Build Command**: `cd IPG && npm install && npm run export:web`
   - **Publish Directory**: `IPG/dist`
7. Click "Create Static Site"
8. Your app will be live at: `https://ipg-xxxx.onrender.com`

**Option B: Manual Upload**
1. Run `npm run export:web`
2. Go to https://render.com
3. Create Static Site
4. Upload `dist/` folder

### 5. Deploy to Vercel (Alternative - Free)
```bash
npm install -g vercel
vercel
```

### 6. Build APK using Android Studio

**Step 1: Create Android WebView Project**
1. Open Android Studio
2. New Project > Empty Activity
3. App Name: **IPG**
4. Package: `com.ipg.app`
5. Language: **Java**
6. Min SDK: **API 24**

**Step 2: Add Internet Permission**
In `AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.INTERNET" />
```

**Step 3: MainActivity.java**
```java
package com.ipg.app;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private WebView webView;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        webView = findViewById(R.id.webview);
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setLoadWithOverviewMode(true);
        webSettings.setUseWideViewPort(true);
        webView.setWebViewClient(new WebViewClient());
        
        // Replace with your Render URL
        webView.loadUrl("https://your-app.onrender.com");
    }
    
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
```

**Step 4: activity_main.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<WebView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/webview"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

**Step 5: Build APK**
1. Build > Build Bundle(s) / APK(s) > Build APK(s)
2. APK location: `app/build/outputs/apk/debug/app-debug.apk`
3. Install on phone or share

### 7. Build APK using EAS (Easier Method)
```bash
npm install -g eas-cli
eas login
eas build --platform android --profile preview
```
Download APK from expo.dev dashboard

## App Features
- Resume upload and skill extraction
- Certificate upload with AI content generation
- Auto-post to LinkedIn (3x daily)
- Auto-update resume with new skills
- Job search with skill matching
- Post history tracking
- WhatsApp notifications

## App Name: IPG
## GitHub: https://github.com/praveenraja143/Link
