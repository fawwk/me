# Oche portfolio and CV kit

This folder contains the Oche portfolio site and the two one-page CV PDFs.

## Files

- `index.html` - the one-page portfolio site
- `styles.css` - the monochrome design system and layout
- `script.js` - nav border on scroll and the lead-card animation
- `config.js` - email, GitHub and site URL placeholders
- `cv/cv-data.json` - the shared source of truth for both CV PDFs
- `cv/Philip-Emoche-Ekele-CV-Developer.pdf` - CV A
- `cv/Philip-Emoche-Ekele-CV-Ops-Leads.pdf` - CV B
- `application-email.md` - application email template

## Fill in the placeholders

Edit `oche/config.js` and replace the sample values with Philip's real email, GitHub URL and site URL when available.

## Rebuild the PDFs on Windows / PowerShell

```powershell
cd .\oche\cv
python .\build_cvs.py
```

## Preview the site locally

```powershell
cd .\oche
python -m http.server 8000
```

Then open `http://localhost:8000` in the browser.

## Deploy

This project is static and can be deployed directly to Cloudflare Pages or Vercel as-is.
