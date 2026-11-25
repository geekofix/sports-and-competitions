// Section nav on detail pages: pins only after the user scrolls past it,
// so full-page screenshots and print output render it in place, unpinned.
const toc = document.querySelector('.toc');
if (toc) {
  const sentinel = document.createElement('div');
  toc.parentNode.insertBefore(sentinel, toc);
  new IntersectionObserver(entries => {
    toc.classList.toggle('pin', !entries[0].isIntersecting);
  }).observe(sentinel);
}

// Reading progress bar + back-to-top button (all pages); both are
// invisible at scroll position 0, so full-page screenshots stay clean.
const progressBar = document.createElement('div');
progressBar.className = 'progress-bar';
document.body.appendChild(progressBar);

const toTop = document.createElement('button');
toTop.type = 'button';
toTop.className = 'to-top';
toTop.setAttribute('aria-label', 'Back to top');
toTop.textContent = '\u2191';
toTop.hidden = true;
document.body.appendChild(toTop);
toTop.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));

let scrollTicking = false;
const onScroll = () => {
  if (scrollTicking) return;
  scrollTicking = true;
  requestAnimationFrame(() => {
    const max = document.documentElement.scrollHeight - innerHeight;
    progressBar.style.transform = 'scaleX(' + (max > 0 ? scrollY / max : 0) + ')';
    toTop.hidden = scrollY < 600;
    scrollTicking = false;
  });
};
addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Copy section anchor links (detail pages)
document.querySelectorAll('.copy-anchor').forEach(btn => {
  btn.addEventListener('click', () => {
    const url = location.origin + location.pathname + btn.dataset.anchor;
    if (!navigator.clipboard) return;
    navigator.clipboard.writeText(url).then(() => {
      btn.classList.add('copied');
      btn.textContent = '\u2713';
      setTimeout(() => {
        btn.classList.remove('copied');
        btn.textContent = '\u{1F517}';
      }, 1500);
    }).catch(() => {});
  });
});

// Theme toggle (all pages)
const themeBtn = document.getElementById('theme-toggle');
if (themeBtn) {
  const icon = themeBtn.querySelector('.icon');
  const syncIcon = () => {
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    icon.textContent = dark ? '\u2600\uFE0F' : '\uD83C\uDF19';
    themeBtn.setAttribute('aria-pressed', String(dark));
  };
  syncIcon();
  themeBtn.addEventListener('click', () => {
    const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
    syncIcon();
  });
}

// Index table: search + A-Z filter (only on pages that have the table)
if (document.getElementById('tableBody')) {
  const rows = Array.from(document.querySelectorAll('#tableBody tr'));
  const searchInput = document.getElementById('searchInput');
  const noResults = document.getElementById('noResults');
  const resultCount = document.getElementById('resultCount');
  const visibleCount = document.getElementById('visibleCount');

  const activeTags = new Set();
  const tagBar = document.getElementById('tagBar');
  const tagChips = tagBar ? Array.from(tagBar.querySelectorAll('.tag-chip')) : [];
  tagChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const tag = chip.dataset.tag;
      if (activeTags.has(tag)) {
        activeTags.delete(tag);
        chip.classList.remove('active');
      } else {
        activeTags.add(tag);
        chip.classList.add('active');
      }
      filterRows();
    });
  });

  const letterSet = new Set();
  rows.forEach(r => {
    const c = r.querySelector('.name-text').textContent.trim()[0].toUpperCase();
    if (/[A-Z0-9]/.test(c)) letterSet.add(c);
  });
  const alphaBar = document.getElementById('alphaBar');
  let activeLetter = null;
  'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.split('').forEach(ch => {
    const btn = document.createElement('button');
    btn.textContent = ch;
    btn.disabled = !letterSet.has(ch);
    btn.addEventListener('click', () => {
      if (activeLetter === ch) {
        activeLetter = null;
        btn.classList.remove('active');
      } else {
        document.querySelectorAll('#alphaBar button.active').forEach(b => b.classList.remove('active'));
        activeLetter = ch;
        btn.classList.add('active');
        searchInput.value = '';
      }
      filterRows();
    });
    alphaBar.appendChild(btn);
  });

  function escHtml(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function highlight(text, q) {
    if (!q) return escHtml(text);
    const re = new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return escHtml(text).replace(re, '<mark>$1</mark>');
  }

  function filterRows() {
    const q = searchInput.value.toLowerCase().trim();
    let visible = 0;
    rows.forEach(r => {
      const nameEl = r.querySelector('.name-text');
      const descEl = r.querySelector('.desc');
      const name = nameEl.textContent;
      const desc = descEl.textContent;
      let show = true;
      if (activeTags.size) {
        const rowTags = (r.dataset.tags || '').split(' ').filter(Boolean);
        show = rowTags.some(t => activeTags.has(t));
      }
      if (show) {
        if (activeLetter) show = name.trim()[0].toUpperCase() === activeLetter;
        else if (q) show = name.toLowerCase().includes(q) || desc.toLowerCase().includes(q);
      };
      r.classList.toggle('hidden', !show);
      if (q && show) {
        nameEl.innerHTML = highlight(name, q);
        descEl.innerHTML = highlight(desc, q);
      } else {
        nameEl.textContent = name;
        descEl.textContent = desc;
      }
      if (show) visible++;
    });
    noResults.style.display = visible === 0 ? 'block' : 'none';
    visibleCount.textContent = visible;
    resultCount.textContent = (q || activeLetter || activeTags.size) ? visible + ' result' + (visible !== 1 ? 's' : '') : '';
  }

  searchInput.addEventListener('input', () => {
    document.querySelectorAll('#alphaBar button.active').forEach(b => b.classList.remove('active'));
    activeLetter = null;
    filterRows();
  });

  const randomBtn = document.getElementById('randomBtn');
  if (randomBtn) {
    randomBtn.addEventListener('click', () => {
      const pool = rows.filter(r => !r.classList.contains('hidden'));
      const set = pool.length ? pool : rows;
      const href = set[Math.floor(Math.random() * set.length)].querySelector('.sport-name a').getAttribute('href');
      window.location.href = href;
    });
  }
}
