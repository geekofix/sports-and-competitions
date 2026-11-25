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

// Share menu (detail pages)
const shareBtn = document.getElementById('shareBtn');
const shareMenu = document.getElementById('shareMenu');
if (shareBtn && shareMenu) {
  const closeShare = () => {
    shareMenu.hidden = true;
    shareBtn.setAttribute('aria-expanded', 'false');
  };
  shareBtn.addEventListener('click', () => {
    shareMenu.hidden = !shareMenu.hidden;
    shareBtn.setAttribute('aria-expanded', String(!shareMenu.hidden));
  });
  document.addEventListener('click', e => {
    if (!shareMenu.hidden && !shareMenu.contains(e.target) && e.target !== shareBtn) closeShare();
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && !shareMenu.hidden) {
      closeShare();
      shareBtn.focus();
    }
  });
  const shareCopy = shareMenu.querySelector('.share-copy');
  shareCopy.addEventListener('click', () => {
    if (!navigator.clipboard) return;
    navigator.clipboard.writeText(location.href).then(() => {
      shareCopy.textContent = 'Copied!';
      setTimeout(() => { shareCopy.textContent = 'Copy link'; }, 1500);
    }).catch(() => {});
  });
}

// In-page search on detail pages: highlights matches in the article text,
// Enter/arrow buttons jump between matches, Escape clears.
const pageSearchInput = document.getElementById('pageSearchInput');
if (pageSearchInput) {
  const sections = Array.from(document.querySelectorAll('.page section'));
  const countLabel = document.getElementById('pageSearchCount');
  let matches = [];
  let matchIndex = -1;
  let debounceTimer = null;

  const wrapTextNodes = (root, term) => {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: node =>
        node.parentElement.closest('.copy-anchor, .share-menu, script, style, input')
          ? NodeFilter.FILTER_REJECT
          : (node.nodeValue.toLowerCase().includes(term.toLowerCase())
            ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP),
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    const re = new RegExp('(' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    nodes.forEach(node => {
      const frag = document.createDocumentFragment();
      node.nodeValue.split(re).forEach(part => {
        if (!part) return;
        if (part.toLowerCase() === term.toLowerCase()) {
          const mark = document.createElement('mark');
          mark.className = 'ps-match';
          mark.textContent = part;
          frag.appendChild(mark);
          matches.push(mark);
        } else {
          frag.appendChild(document.createTextNode(part));
        }
      });
      node.parentNode.replaceChild(frag, node);
    });
  };

  const unwrap = () => {
    document.querySelectorAll('.ps-match').forEach(mark => {
      const parent = mark.parentNode;
      mark.replaceWith(document.createTextNode(mark.textContent));
      parent.normalize();
    });
    matches = [];
  };

  const showMatch = i => {
    document.querySelectorAll('.ps-match.current').forEach(m => m.classList.remove('current'));
    if (!matches.length) return;
    matchIndex = ((i % matches.length) + matches.length) % matches.length;
    const current = matches[matchIndex];
    current.classList.add('current');
    current.scrollIntoView({ block: 'center', behavior: 'smooth' });
    countLabel.textContent = (matchIndex + 1) + ' / ' + matches.length;
  };

  const run = () => {
    unwrap();
    matchIndex = -1;
    const q = pageSearchInput.value.trim();
    if (q.length < 2) {
      countLabel.textContent = '';
      return;
    }
    sections.forEach(s => wrapTextNodes(s, q));
    if (!matches.length) {
      countLabel.textContent = 'no matches';
      return;
    }
    showMatch(0);
  };

  const step = dir => {
    if (matches.length) showMatch(matchIndex + dir);
  };

  pageSearchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(run, 150);
  });
  pageSearchInput.addEventListener('keydown', e => {
    if (e.key === 'Enter') { e.preventDefault(); step(e.shiftKey ? -1 : 1); }
    if (e.key === 'Escape') { pageSearchInput.value = ''; run(); }
  });
  document.getElementById('pageSearchNext').addEventListener('click', () => step(1));
  document.getElementById('pageSearchPrev').addEventListener('click', () => step(-1));
  document.getElementById('pageSearchClear').addEventListener('click', () => {
    pageSearchInput.value = '';
    run();
    pageSearchInput.focus();
  });
}

// Pair images with their "Figure:" captions and grid them (detail pages).
// Progressive enhancement: wraps <img> + following caption <p><em>Figure:
// ...</em></p> into <figure class="img-pair">, then consecutive figures into
// a grid so multi-photo pages sit side by side.
document.querySelectorAll('.page section').forEach(section => {
  const pairs = [];
  let pendingImg = null;
  let pendingP = null;
  Array.from(section.children).forEach(el => {
    if (el.matches('p') && el.querySelectorAll('img').length === 1 && el.children.length === 1) {
      pendingImg = el.firstElementChild;
      pendingP = el;
      return;
    }
    if (pendingImg && el.matches('p') && el.children.length === 1
        && el.firstElementChild.tagName === 'EM' && /^Figure:/i.test(el.textContent)) {
      const fig = document.createElement('figure');
      fig.className = 'img-pair';
      fig.appendChild(pendingImg);
      fig.appendChild(el.firstElementChild);
      pendingP.remove();
      el.remove();
      pairs.push(fig);
      pendingImg = null;
      pendingP = null;
      return;
    }
    pendingImg = null;
    pendingP = null;
  });
  if (!pairs.length) return;
  let group = [];
  const flushGroup = () => {
    if (group.length === 1) {
      group[0].classList.add('solo');
      group = [];
      return;
    }
    if (group.length > 1) {
      const grid = document.createElement('div');
      grid.className = 'img-grid';
      group[0].parentNode.insertBefore(grid, group[0]);
      group.forEach(f => grid.appendChild(f));
      group = [];
    }
  };
  Array.from(section.children).forEach(el => {
    if (el.classList && el.classList.contains('img-pair')) group.push(el);
    else flushGroup();
  });
  flushGroup();
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

  const resetBtn = document.getElementById('resetFilters');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      searchInput.value = '';
      activeLetter = null;
      activeTags.clear();
      document.querySelectorAll('#alphaBar button.active').forEach(b => b.classList.remove('active'));
      tagChips.forEach(c => c.classList.remove('active'));
      filterRows();
    });
  }

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
