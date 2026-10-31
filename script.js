document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const leadCard = document.querySelector('.lead-card');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const applyConfig = () => {
    const cfg = window.siteConfig || {};
    const email = cfg.email || 'ekelephlipemoche@gmail.com';
    const github = cfg.github || 'https://github.com/fawwk';

    document.querySelectorAll('#emailLink, #footerEmail').forEach((node) => {
      node.href = `mailto:${email}`;
      node.textContent = email;
    });

    const githubLink = document.getElementById('footerGithub');
    if (githubLink) {
      githubLink.href = github;
    }
  };

  const setScrollState = () => {
    if (!header) return;
    if (window.scrollY > 0) {
      header.classList.add('has-scrolled');
    } else {
      header.classList.remove('has-scrolled');
    }
  };

  setScrollState();
  window.addEventListener('scroll', setScrollState, { passive: true });

  applyConfig();

  const year = document.getElementById('year');
  if (year) {
    year.textContent = new Date().getFullYear();
  }

  if (leadCard && !reduceMotion) {
    const rows = [...leadCard.querySelectorAll('.lead-row')];
    rows.forEach((row, index) => {
      row.style.setProperty('--index', index);
    });

    window.setTimeout(() => {
      leadCard.classList.add('ready');
    }, 400);
  }

  if (reduceMotion && leadCard) {
    leadCard.querySelectorAll('.lead-row').forEach((row) => {
      row.style.opacity = '1';
      row.style.transform = 'none';
    });
  }
});
