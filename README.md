# Oche portfolio and CV kit

This is a static portfolio site with two downloadable CVs.

## Files

- `index.html` - portfolio markup, styles, scripts and SEO metadata
- `assets/` - extracted original artwork and the self-hosted Inter font
- `og.png` - 1200×630 social preview image
- `cv/Philip-Emoche-Ekele-CV-Developer.pdf` - developer CV
- `cv/Philip-Emoche-Ekele-CV-Ops-Leads.pdf` - operations and leads CV
- `cv/cv-data.json` - shared source for the CV PDFs
- `cv/build_cvs.py` - CV PDF generator
- `application-email.md` - application email template

## Preview locally

From the project root:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Rebuild the CVs

Install ReportLab if needed, then run:

```sh
python3 cv/build_cvs.py
```

## Deploy

The project is static and ready for Cloudflare Pages:

- Connect the repository in Cloudflare Pages.
- Set the build command to blank and the build output directory to `.` (the project root).
- No framework preset or environment variables are required.

The root `404.html`, `robots.txt`, `sitemap.xml`, `site.webmanifest` and `_headers` are included. The same static files can also be deployed to GitHub Pages, Netlify or another static host.
