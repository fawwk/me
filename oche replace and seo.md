# Task: replace my portfolio code with the new Oche site, then do proper SEO

You are working inside my existing portfolio project. I have a new design, delivered as one finished file, `oche-site-ink.html`, plus a share image, `og.png`. Your job:

1. **Replace** the site's current pages, styles and scripts with the new site, with identical visual and behavioural output.
2. **Do proper SEO**, including adding `og.png` as the social share image.
3. Keep my project's tooling, deployment and settings intact.

Do not redesign anything. The design is finished; your job is to port it faithfully and make it findable.

If the files are not attached, the HTML source is pasted below this prompt. If `og.png` is not attached, ask me for it before finishing; do not generate a substitute.

---

## 1. Inspect first, then tell me the plan (do not edit yet)

1. Look at the project: what stack it uses (plain HTML, Vite, Next.js, Astro, other), how it builds and deploys (Cloudflare Pages, Vercel, GitHub Pages, other), and what the current domain or site URL is.
2. List the files you intend to replace and the files you intend to keep.
3. Reply with a short plan and any questions (see section 7). Then continue unless I tell you to stop.

**Before changing anything, make a restore point:** create a git branch named `backup-before-oche` from the current state (or commit the current state if the tree is dirty). Never delete my old code without that branch in place.

## 2. Replace the code

**Keep untouched:** git history, `package.json` and lockfiles (except for adding a dependency you truly need), build and deploy config, environment files, CI files, domain files such as `CNAME`, redirect and header rules that already exist (extend them, do not overwrite them), and any analytics I already have.

**Replace:** the current pages, components, styles and scripts that make up the visible site.

- **Plain static project:** the new `index.html` becomes the site's `index.html`.
- **Framework project (Vite, Next.js, Astro, etc.):** port the markup, CSS and JavaScript into the framework's page or component **verbatim**. Do not rewrite the CSS in another system, do not add a UI library, do not turn it into "components" in a way that changes output. The rendered HTML, styling and behaviour must match the original file. Use the framework's own mechanism for `<head>` tags.
- Do not add any runtime framework, CSS framework, animation library or icon library. The site is deliberately plain HTML, CSS and a little vanilla JS.

### What the new site contains (do not break any of it)

- One page with a sticky translucent nav bar, a hero (name, one-line pitch, Download CV and Email me buttons, a drawn scribble under the name, a welcoming ink figure on the right), a "Selected work" heading with a pointing figure, a black ProofLeads chapter (a black silhouette with glowing eyes, the tag, title, tagline, copy, and an animated sample lead card), two tiles (Termcard with an animated sample report card, and Houseplug), a Background section (an ink figure, experience, education, skills), a contact section (email, WhatsApp, GitHub, X and a hand-drawn "call me" phone that links to `tel:`), and a footer with a large logo.
- The **logo** is an inline SVG inside a `<template id="logo-t">` that a script clones into every `[data-logo]` element. Its pupils follow the cursor and the scroll direction, it blinks, it wakes up on load, and it wobbles on hover. Keep the template, the script and the markup exactly as they are.
- Animations: hero fade, scribble draw, lead card row sequence, report card count-up, "call me" pop and ring, logo behaviour. Every animation must stay disabled under `prefers-reduced-motion: reduce`. Do not add scroll-triggered effects or new motion.
- A `CONFIG` object near the bottom of the file holds the email, GitHub URL and CV path. Keep it. The email is `ekelephlipemoche@gmail.com`, GitHub is `https://github.com/fawwk`, the CV path is `cv/Philip-Emoche-Ekele-CV-Developer.pdf`.
- **Palette:** only Paper `#FAFAFA`, Fog `#F0F0F0`, Hairline `#D6D6D6`, Graphite `#6B6B6B`, Ink `#1A1A1A`, Black `#000000`, Ash `#A1A1A1`. The artwork is the only colour on the page. Do not add colours, shadows, gradients or dark mode.
- **Content rules (keep exactly):** ProofLeads is tagged "Live, not yet launched"; Termcard and Houseplug are tagged "In development". No invented numbers, users, clients, testimonials or logos. No LinkedIn link. No Journal page. All sample content (the lead card and report card) stays labelled as a sample.

## 3. Assets

The HTML contains artwork embedded as `data:` URIs. For a maintainable project:

1. **Extract** each embedded image into an `assets/` (or the project's equivalent public) folder with a clear name: `art-welcome`, `art-pointing`, `art-ink-figure`, `art-silhouette`, `callme-bubble`, `callme-phone`. Keep the same pixel dimensions and update the `src` attributes. Keep the `width` and `height` attributes on every `<img>` (they prevent layout shift).
2. **Keep the formats that matter:**
   - The three coloured artworks are JPEGs with their white backgrounds clamped to pure white, because the CSS uses `mix-blend-mode: multiply` to drop the white. Do not convert them to anything with a transparent or off-white background, and do not apply colour management that shifts the white. WebP is fine if the white stays pure.
   - The silhouette and the two "call me" pieces are PNGs with transparency. Keep alpha. WebP with alpha is fine.
   - If you convert any image, compare before and after at 1x and 2x and confirm nothing changed visually.
3. **Loading:** the hero image gets `fetchpriority="high"` and no lazy loading. Every image below the first screen gets `loading="lazy"` and `decoding="async"`.
4. **Fonts:** the file currently loads Inter from Google Fonts. If you can fetch the Inter variable font (`woff2`, SIL Open Font License), self-host it in `assets/fonts/`, add a `@font-face` with `font-display: swap`, preload it, and remove the Google Fonts links. Keep the font stack unchanged: `"SF Pro Display","SF Pro Text",-apple-system,BlinkMacSystemFont,"Inter",system-ui,"Segoe UI",Roboto,sans-serif`. If you cannot fetch it, keep the Google Fonts link as it is and tell me.
5. Add `og.png` (1200×630) to the site root (or the public folder so it is served at `/og.png`).

## 4. SEO (do all of this)

Everything below needs the site's **real absolute URL**. Take it from the project's existing config or deploy settings. If you cannot find it, ask me, and until I answer use the single placeholder `https://YOUR-DOMAIN` in one place only (a constant or a single find-and-replace target) and tell me where it is.

### 4.1 Head tags (exact copy)

- `<html lang="en">`, `<meta charset="utf-8">`, the existing viewport tag.
- **Title (max 60 characters):** `Oche: Philip Emoche Ekele, automation and software builder`
- **Meta description (max 155 characters):** `Philip Emoche Ekele builds lead pipelines, Telegram and WhatsApp bots and school systems. See ProofLeads, Termcard and Houseplug, and get in touch.`
- `<link rel="canonical" href="{SITE}/">`
- `<meta name="robots" content="index,follow,max-image-preview:large">`
- `<meta name="theme-color" content="#FAFAFA">`
- `<meta name="author" content="Philip Emoche Ekele">`
- Keep `<meta name="color-scheme" content="light">`.

### 4.2 Open Graph and Twitter

```
og:type        website
og:site_name   Oche
og:title       Oche: Philip Emoche Ekele
og:description I build software that automates business work: lead pipelines, bots and school systems.
og:url         {SITE}/
og:image       {SITE}/og.png            (absolute, https)
og:image:type  image/png
og:image:width 1200
og:image:height 630
og:image:alt   Oche logo, a black round character with two eyes, beside the name Philip Emoche Ekele
twitter:card   summary_large_image
twitter:site   @_iamoche
twitter:creator @_iamoche
twitter:title / twitter:description / twitter:image / twitter:image:alt   same values as the Open Graph ones
```

Remove the earlier placeholder Open Graph tags so nothing is duplicated.

### 4.3 Structured data (JSON-LD, one script tag)

Use a `@graph` with a `WebSite` and a `Person`, linked by `@id`. Put in only facts I have stated; never add a job title, rating, employer, phone number or email.

- `WebSite`: `url` = `{SITE}/`, `name` = `Oche`, `inLanguage` = `en`, `publisher` = the Person.
- `Person`: `name` = `Philip Emoche Ekele`, `alternateName` = `Oche`, `url` = `{SITE}/`, `image` = `{SITE}/og.png`, `description` = `Builds software that automates business work: lead pipelines, bots and school systems.`, `sameAs` = `["https://github.com/fawwk","https://x.com/_iamoche"]`, `knowsAbout` = `["Python","JavaScript","Supabase","Telegram bots","Workflow automation"]`.

### 4.4 Icons and manifest

- Create `favicon.svg` from the logo: the same path and eyes as the inline SVG, but with concrete colours (body `#1A1A1A`, eyes `#FAFAFA`, pupils `#000000`) and no CSS variables. Link it with `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`.
- Generate `favicon.ico` (32×32), `apple-touch-icon.png` (180×180, logo centred on `#FAFAFA` with padding), and `icon-192.png` and `icon-512.png`.
- Add `site.webmanifest` with `name` "Oche", `short_name` "Oche", `theme_color` and `background_color` `#FAFAFA`, `display` "browser", and the two icons.

### 4.5 Crawl files

- `robots.txt`: `User-agent: *`, `Allow: /`, and `Sitemap: {SITE}/sitemap.xml`.
- `sitemap.xml` with the single URL `{SITE}/` and today's `lastmod`.
- A `404.html` in the same visual style (Paper background, logo, one line, a link home), if the host supports a custom 404. Keep it minimal and static.

### 4.6 On-page SEO

- Exactly one `<h1>` (the name). Keep the heading order logical. Do not change the visible copy to stuff keywords.
- Keep every `alt` text; confirm each image has a meaningful alt.
- External links to my profiles (`github.com/fawwk`, `x.com/_iamoche`) get `rel="me noopener noreferrer"`. The `tel:`, `mailto:` and WhatsApp links stay as they are.
- Do not add any visible footer link farm, keyword block or hidden text.

### 4.7 Performance and delivery

- Inline critical CSS is already in the file; do not split it unless the framework forces it.
- If the host is Cloudflare Pages, add or extend a `_headers` file: `/assets/*` with `Cache-Control: public, max-age=31536000, immutable`; for all routes `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`. Do not add a Content-Security-Policy unless you can do it without breaking the inline styles and scripts. If the host is something else, do the equivalent in its own config.
- No new third-party scripts, no tracking, no cookie banner. Keep any analytics I already had.

## 5. Verify (do these, then report the results)

1. Build and run locally. Compare the new site against `oche-site-ink.html` opened directly: they must look and behave the same at 390px and 1280px wide.
2. Check: nav, hero image, scribble draw, lead card sequence, report card count-up, call-me pop and ring, logo eyes and blink, `tel:` and `mailto:` links, keyboard focus, and reduced-motion behaviour.
3. Run Lighthouse (CLI or equivalent) on mobile. Target at least 95 for SEO, Accessibility and Best Practices, and 90 or higher for Performance. If a score is lower, say why and what would fix it.
4. Validate the structured data (schema.org validator or Google's Rich Results test, or an offline JSON-LD check if you cannot browse) and the HTML (the W3C validator or an offline equivalent).
5. Confirm `/og.png` returns 200 at 1200×630, and that `og:image` is an absolute `https` URL.
6. Check that the sitemap and robots.txt are served from the site root.

## 6. Report at the end

In a few lines: the files you changed, added and kept; the build and deploy steps; the results of section 5; and what I still have to do. That list will include: add my CV PDF at `cv/Philip-Emoche-Ekele-CV-Developer.pdf` (the button points there), check the share preview in WhatsApp, and submit the sitemap in Google Search Console and Bing Webmaster Tools. Tell me that the WhatsApp preview can take a while to update because WhatsApp caches earlier previews.

## 7. Ask me only if you cannot find it yourself

- The site's final URL, if it is not in the project's config.
- Whether there is existing analytics, a custom domain, or redirects I need to keep.
- `og.png`, if it is not attached.

## 8. Hard rules

- Faithful port: same markup, same CSS, same behaviour, same copy.
- No new libraries, no tracking, no extra colours, no extra motion.
- No invented facts anywhere, including in JSON-LD, meta tags and alt text.
- Make a backup branch before you change anything.
- If something in the existing project blocks the port, stop and ask me; do not improvise a redesign.
