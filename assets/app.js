const rows = Array.from(document.querySelectorAll('#tableBody tr'));
const searchInput = document.getElementById('searchInput');
const noResults = document.getElementById('noResults');
const resultCount = document.getElementById('resultCount');
const visibleCount = document.getElementById('visibleCount');
const TOTAL = rows.length;

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
    if (activeLetter) show = name.trim()[0].toUpperCase() === activeLetter;
    else if (q) show = name.toLowerCase().includes(q) || desc.toLowerCase().includes(q);
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
  resultCount.textContent = (q || activeLetter) ? visible + ' result' + (visible !== 1 ? 's' : '') : '';
}

searchInput.addEventListener('input', () => {
  document.querySelectorAll('#alphaBar button.active').forEach(b => b.classList.remove('active'));
  activeLetter = null;
  filterRows();
});
