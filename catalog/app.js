/* ══════════════════════════════════════════════════════════════════════
   Calwood Flooring Supply — Premium Online Catalog
   app.js — Complete application logic
   ══════════════════════════════════════════════════════════════════════ */

'use strict';

// ── State ──────────────────────────────────────────────────────────────
const state = {
  allProducts: [],
  allStairTreads: [],
  allRisers: [],
  allTrimAccessories: [],
  categories: [],
  filters: { search: '', collection: 'all', species: 'all' },
  modalProductId: null
};

// ── Color family CSS class map ──────────────────────────────────────────
const COLOR_BG = {
  white:   'bg-wood-white',
  beige:   'bg-wood-beige',
  gray:    'bg-wood-gray',
  brown:   'bg-wood-brown',
  natural: 'bg-wood-natural'
};

// ── Category icon map ───────────────────────────────────────────────────
const CATEGORY_ICONS = {
  'engineered-hardwood': '🪵',
  'stair-treads':        '🪜',
  'risers':              '▭',
  'stair-nose':          '⌐',
  'reducer':             '↘',
  't-molding':           '⊤',
  'end-cap':             '⊣',
  'baby-threshold':      '⊥',
  'wood-vent':           '⊞',
  'custom-profile':      '✦'
};

// ── Trim type icon map ──────────────────────────────────────────────────
const TRIM_ICONS = {
  'stair_nose':       '⌐',
  'reducer':          '↘',
  't_molding':        '⊤',
  'end_cap':          '⊣',
  'baby_threshold':   '⊥',
  'flush_vent':       '⊟',
  'surface_mount_vent': '⊞',
  'custom_profile':   '✦'
};

// ── Data loading ────────────────────────────────────────────────────────
async function loadData() {
  const [productsRes, categoriesRes] = await Promise.all([
    fetch('data/products.json'),
    fetch('data/categories.json')
  ]);

  if (!productsRes.ok) throw new Error(`Failed to load products.json: ${productsRes.status}`);
  if (!categoriesRes.ok) throw new Error(`Failed to load categories.json: ${categoriesRes.status}`);

  const products = await productsRes.json();
  const categories = await categoriesRes.json();

  return { products, categories };
}

// ── Helpers ─────────────────────────────────────────────────────────────
function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function formatPrice(value) {
  if (!value || value === 'TBD') return null;
  const n = parseFloat(value);
  if (isNaN(n)) return null;
  return n.toFixed(2);
}

function getDataDotClass(dataSource) {
  if (!dataSource) return 'data-dot-tbd';
  const s = dataSource.toLowerCase();
  if (s.startsWith('confirmed')) return 'data-dot-confirmed';
  if (s.startsWith('estimated')) return 'data-dot-estimated';
  return 'data-dot-tbd';
}

// ── Render category cards ───────────────────────────────────────────────
function renderCategoryCards() {
  const grid = document.getElementById('category-grid');
  if (!grid) return;

  if (!state.categories.length) {
    grid.innerHTML = '<p style="padding:20px;color:var(--text-light)">No categories loaded.</p>';
    return;
  }

  grid.innerHTML = state.categories.map(cat => {
    const icon = CATEGORY_ICONS[cat.id] || '▪';
    const badges = [];
    if (cat.badge_quotecenter) badges.push('<span class="badge badge-qc">QuoteCenter</span>');
    if (cat.badge_matching)    badges.push('<span class="badge badge-match">Matching</span>');

    return `
      <a href="#flooring" class="category-card" data-category="${escapeHtml(cat.id)}">
        <div class="category-icon">${icon}</div>
        <div class="category-name">${escapeHtml(cat.name)}</div>
        ${badges.length ? `<div class="category-badges">${badges.join('')}</div>` : ''}
      </a>
    `;
  }).join('');
}

// ── Render flooring grid ────────────────────────────────────────────────
function renderFlooringGrid() {
  const grid = document.getElementById('flooring-grid');
  if (!grid) return;

  const filtered = applyFlooringFiltersToData();

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="flooring-empty">
        <h3>No products match your filters</h3>
        <p>Try adjusting your search or clearing the filters.</p>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(p => makeProductCard(p)).join('');

  // Attach click handlers to newly rendered cards
  grid.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('click', function(e) {
      // Don't open modal when clicking the "View Details" button directly — it also triggers this
      openModal(this.dataset.productId);
    });
  });
}

function makeProductCard(product) {
  const bgClass = COLOR_BG[product.color_family] || 'bg-wood-natural';
  const price = formatPrice(product.price_per_sqft);
  const isTBD = product.data_source && product.data_source.startsWith('TBD');
  const isEstimated = product.data_source && product.data_source.startsWith('Estimated');
  const dotClass = getDataDotClass(product.data_source);

  const badges = [];
  if (isTBD) {
    badges.push('<span class="badge badge-placeholder">Placeholder</span>');
  } else if (product.data_source && product.data_source.startsWith('Confirmed')) {
    badges.push('<span class="badge badge-confirmed">Confirmed</span>');
  } else if (isEstimated) {
    badges.push('<span class="badge badge-new">Est. Price</span>');
  }
  if (product.matching_accessories) {
    badges.push('<span class="badge badge-match">Matching Avail.</span>');
  }
  if (product.quote_available) {
    badges.push('<span class="badge badge-qc">QuoteCenter</span>');
  }

  const priceHtml = price
    ? `<div class="product-price-row">
        <span class="product-price">$${price}</span>
        <span class="product-price-unit">/ sq.ft.</span>
       </div>`
    : `<div class="product-price-row">
        <span class="product-price-tbd">Quote Required</span>
       </div>`;

  const specLine = [product.species, product.thickness && product.width ? `${product.thickness} × ${product.width}` : null]
    .filter(Boolean)
    .join(' · ');

  return `
    <div class="product-card" data-product-id="${escapeHtml(product.id)}">
      <div class="product-card-img ${bgClass}">
        <div class="product-card-img-label">${escapeHtml(product.product_name)}</div>
      </div>
      <div class="product-card-body">
        <div class="product-collection-tag">${escapeHtml(product.collection)} Collection</div>
        <div class="product-name">${escapeHtml(product.product_name)}</div>
        <div class="product-spec-row">${escapeHtml(specLine)}</div>
        ${priceHtml}
        <div class="product-badges">${badges.join('')}</div>
        <div class="product-sku">
          <span class="data-dot ${dotClass}"></span>SKU: ${escapeHtml(product.vendor_sku)}
        </div>
      </div>
      <div class="product-card-footer">
        <button class="btn btn-primary btn-full" onclick="event.stopPropagation(); openModal('${escapeHtml(product.id)}')">
          View Details
        </button>
      </div>
    </div>
  `;
}

// ── Filter logic ────────────────────────────────────────────────────────
function applyFlooringFiltersToData() {
  return state.allProducts.filter(p => {
    const search = state.filters.search.toLowerCase();
    const collection = state.filters.collection;
    const species = state.filters.species;

    if (search) {
      const haystack = [
        p.product_name, p.collection, p.species,
        p.vendor_sku, p.color_family, p.finish
      ].join(' ').toLowerCase();
      if (!haystack.includes(search)) return false;
    }

    if (collection !== 'all') {
      if (collection === 'TBD') {
        if (!p.collection || p.collection !== 'TBD') return false;
      } else {
        if (p.collection !== collection) return false;
      }
    }

    if (species !== 'all') {
      if (p.species !== species) return false;
    }

    return true;
  });
}

function initFilters() {
  const searchInput = document.getElementById('search-input');
  const clearBtn = document.getElementById('clear-filters');

  if (searchInput) {
    searchInput.addEventListener('input', function() {
      state.filters.search = this.value.trim();
      updateClearVisibility();
      renderFlooringGrid();
    });
  }

  // Collection filter buttons
  document.querySelectorAll('.collection-filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.collection-filter-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      state.filters.collection = this.dataset.collection;
      updateClearVisibility();
      renderFlooringGrid();
    });
  });

  // Species filter buttons
  document.querySelectorAll('.species-filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.species-filter-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      state.filters.species = this.dataset.species;
      updateClearVisibility();
      renderFlooringGrid();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', function(e) {
      e.preventDefault();
      clearAllFilters();
    });
  }
}

function updateClearVisibility() {
  const clearBtn = document.getElementById('clear-filters');
  if (!clearBtn) return;
  const isActive = state.filters.search || state.filters.collection !== 'all' || state.filters.species !== 'all';
  clearBtn.classList.toggle('hidden', !isActive);
}

function clearAllFilters() {
  state.filters = { search: '', collection: 'all', species: 'all' };

  const searchInput = document.getElementById('search-input');
  if (searchInput) searchInput.value = '';

  document.querySelectorAll('.collection-filter-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.collection === 'all');
  });
  document.querySelectorAll('.species-filter-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.species === 'all');
  });

  updateClearVisibility();
  renderFlooringGrid();
}

// ── Modal ───────────────────────────────────────────────────────────────
function openModal(productId) {
  const product = state.allProducts.find(p => p.id === productId);
  if (!product) return;

  state.modalProductId = productId;

  const overlay = document.getElementById('modal-overlay');
  const tagEl = document.getElementById('modal-tag');
  const nameEl = document.getElementById('modal-name');
  const imgWrap = document.getElementById('modal-img-wrap');
  const specsGrid = document.getElementById('modal-specs-grid');
  const matchingEl = document.getElementById('modal-matching');
  const quoteBtn = document.getElementById('modal-quote-btn');
  const hdBtn = document.getElementById('modal-hd-btn');

  if (!overlay) return;

  // Tag
  if (tagEl) tagEl.textContent = `${product.collection} Collection`;

  // Name
  if (nameEl) nameEl.textContent = product.product_name;

  // Image area
  if (imgWrap) {
    const bgClass = COLOR_BG[product.color_family] || 'bg-wood-natural';
    imgWrap.className = `modal-img-wrap ${bgClass}`;
    imgWrap.innerHTML = '';
  }

  // Specs grid
  if (specsGrid) {
    const specs = [
      { label: 'Species',       value: product.species },
      { label: 'Thickness',     value: product.thickness },
      { label: 'Width',         value: product.width },
      { label: 'Veneer',        value: product.veneer },
      { label: 'Construction',  value: product.construction },
      { label: 'Finish',        value: product.finish },
      { label: 'Sq.Ft./Case',   value: product.sq_ft_per_case !== 'TBD' ? `${product.sq_ft_per_case} sq.ft.` : 'TBD' },
      { label: 'Case Price',    value: product.case_price && product.case_price !== 'TBD' ? `$${product.case_price}` : 'TBD' },
      { label: 'Price/Sq.Ft.',  value: product.price_per_sqft && product.price_per_sqft !== 'TBD' ? `$${product.price_per_sqft}` : 'Quote Required' },
      { label: 'Installation',  value: product.installation },
      { label: 'Warranty',      value: product.warranty },
      { label: 'SKU',           value: product.vendor_sku }
    ].filter(s => s.value && s.value !== 'TBD');

    specsGrid.innerHTML = specs.map(s => `
      <div class="modal-spec-item">
        <div class="modal-spec-label">${escapeHtml(s.label)}</div>
        <div class="modal-spec-value">${escapeHtml(String(s.value))}</div>
      </div>
    `).join('');
  }

  // Matching accessories
  if (matchingEl) {
    if (product.matching_accessories) {
      const trimNames = [
        'Stair Nose', 'Reducer', 'T-Molding', 'End Cap',
        'Baby Threshold', 'Wood Vents', 'Custom Profiles'
      ];
      matchingEl.innerHTML = `
        <div class="modal-matching-title">Matching Accessories Available</div>
        <div class="modal-matching-list">
          ${trimNames.map(t => `<span class="modal-matching-chip">${escapeHtml(t)}</span>`).join('')}
        </div>
      `;
    } else {
      matchingEl.innerHTML = '';
    }
  }

  // Quote button
  if (quoteBtn) {
    quoteBtn.href = `#quote`;
    quoteBtn.addEventListener('click', closeModal, { once: true });
  }

  // HD button
  if (hdBtn) {
    const hdUrl = product.home_depot_url;
    if (hdUrl && hdUrl !== 'Home Depot URL TBD') {
      hdBtn.href = hdUrl;
      hdBtn.target = '_blank';
      hdBtn.rel = 'noopener';
      hdBtn.textContent = 'View on HomeDepot.com';
      hdBtn.style.display = '';
    } else {
      hdBtn.href = 'https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u';
      hdBtn.target = '_blank';
      hdBtn.rel = 'noopener';
      hdBtn.textContent = 'View Calwood on HomeDepot.com';
      hdBtn.style.display = '';
    }
  }

  // Show modal
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';

  // Scroll modal card to top
  const card = overlay.querySelector('.modal-card');
  if (card) card.scrollTop = 0;
}

function closeModal() {
  const overlay = document.getElementById('modal-overlay');
  if (overlay) {
    overlay.classList.remove('open');
  }
  document.body.style.overflow = '';
  state.modalProductId = null;
}

// ── Stair treads and risers rendering ──────────────────────────────────
function renderStairSection() {
  renderStairGrid('stair-treads-grid', state.allStairTreads);
  renderStairGrid('risers-grid', state.allRisers);
  initStairTabs();
}

function renderStairGrid(gridId, items) {
  const grid = document.getElementById(gridId);
  if (!grid) return;

  if (!items || items.length === 0) {
    grid.innerHTML = '<p style="padding:20px;color:var(--text-light)">No items loaded.</p>';
    return;
  }

  grid.innerHTML = items.map(item => makeStairCard(item)).join('');
}

function makeStairCard(item) {
  const isTBD = !item.price_per_unit || item.price_per_unit === 'TBD';
  const isRiser = !!item.width && parseFloat(item.width) < 12;

  const lengths = Array.isArray(item.lengths_available)
    ? item.lengths_available.filter(l => l !== 'TBD')
    : [];

  const priceHtml = !isTBD
    ? `<div class="stair-price">$${parseFloat(item.price_per_unit).toFixed(2)} <span style="font-size:.8125rem;font-weight:500;color:var(--text-light)">/ unit</span></div>`
    : `<div class="stair-price-tbd">Price TBD — contact Calwood</div>`;

  const lengthChips = lengths.length
    ? `<div class="stair-lengths">${lengths.map(l => `<span class="stair-length-chip">${escapeHtml(l)}</span>`).join('')}</div>`
    : '';

  return `
    <div class="stair-card">
      <div class="stair-card-header">
        <div class="stair-card-species">${escapeHtml(item.species)}</div>
        <div class="stair-card-name">${escapeHtml(item.product_name)}</div>
      </div>
      <div class="stair-specs">
        ${item.thickness && item.thickness !== 'TBD' ? `
          <div class="stair-spec">
            <span class="stair-spec-label">Thickness</span>
            <span class="stair-spec-value">${escapeHtml(item.thickness)}</span>
          </div>` : ''}
        ${item.width && item.width !== 'TBD' ? `
          <div class="stair-spec">
            <span class="stair-spec-label">Width</span>
            <span class="stair-spec-value">${escapeHtml(item.width)}</span>
          </div>` : ''}
        <div class="stair-spec">
          <span class="stair-spec-label">Finish</span>
          <span class="stair-spec-value">${escapeHtml(item.finish || 'Unfinished')}</span>
        </div>
      </div>
      ${lengthChips}
      ${priceHtml}
      ${item.vendor_sku && item.vendor_sku !== 'SKU TBD'
        ? `<div class="stair-sku">SKU: ${escapeHtml(item.vendor_sku)}</div>` : ''}
      ${item.data_source === 'TBD'
        ? '<div style="margin-top:8px"><span class="badge badge-placeholder">Placeholder</span></div>'
        : '<div style="margin-top:8px"><span class="badge badge-confirmed">Confirmed</span></div>'}
    </div>
  `;
}

function initStairTabs() {
  const tabs = document.querySelectorAll('.stair-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');

      const which = this.dataset.tab;
      const treadsGrid = document.getElementById('stair-treads-grid');
      const risersGrid = document.getElementById('risers-grid');

      if (treadsGrid) treadsGrid.classList.toggle('hidden', which !== 'treads');
      if (risersGrid) risersGrid.classList.toggle('hidden', which !== 'risers');
    });
  });
}

// ── Trim accessories rendering ──────────────────────────────────────────
function renderTrimCards() {
  const grid = document.getElementById('trim-grid');
  if (!grid) return;

  if (!state.allTrimAccessories.length) {
    grid.innerHTML = '<p style="padding:20px;color:rgba(250,246,240,0.5)">No trim accessories loaded.</p>';
    return;
  }

  grid.innerHTML = state.allTrimAccessories.map(trim => {
    const icon = TRIM_ICONS[trim.trim_type] || '▪';
    const species = Array.isArray(trim.species_available)
      ? trim.species_available.join(', ')
      : '';

    return `
      <div class="trim-card">
        <span class="trim-card-icon">${icon}</span>
        <div class="trim-card-name">${escapeHtml(trim.product_name)}</div>
        <div class="trim-card-desc">${escapeHtml(trim.use_case)}</div>
        ${species ? `<div class="trim-card-species">Available in: ${escapeHtml(species)}</div>` : ''}
        <div class="trim-card-badges">
          ${trim.matching_available ? '<span class="badge badge-match">Matching Available</span>' : ''}
          ${trim.quote_available ? '<span class="badge badge-qc">Quote Required</span>' : ''}
        </div>
      </div>
    `;
  }).join('');
}

// ── Navigation behavior ─────────────────────────────────────────────────
function initNav() {
  const nav = document.getElementById('site-nav');
  const hamburger = document.getElementById('hamburger');

  if (!nav) return;

  // Scroll class
  function handleScroll() {
    nav.classList.toggle('scrolled', window.scrollY > 50);
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // Hamburger toggle
  if (hamburger) {
    hamburger.addEventListener('click', function() {
      nav.classList.toggle('nav-open');
    });
  }

  // Close hamburger when a nav link is clicked
  nav.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('nav-open');
    });
  });

  // Active link highlighting via IntersectionObserver
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');

  if ('IntersectionObserver' in window && sections.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach(link => {
            const href = link.getAttribute('href');
            link.classList.toggle('active', href === `#${id}`);
          });
        }
      });
    }, {
      rootMargin: '-20% 0px -60% 0px',
      threshold: 0
    });

    sections.forEach(section => io.observe(section));
  }

  // Close mobile nav on outside click
  document.addEventListener('click', function(e) {
    if (nav.classList.contains('nav-open') && !nav.contains(e.target)) {
      nav.classList.remove('nav-open');
    }
  });
}

// ── Smooth scroll ───────────────────────────────────────────────────────
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const href = link.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const navHeight = document.getElementById('site-nav')?.offsetHeight || 68;
        const top = target.getBoundingClientRect().top + window.scrollY - navHeight - 12;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });
}

// ── Quote form ──────────────────────────────────────────────────────────
function initQuoteForm() {
  const form = document.getElementById('quote-form');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    this.style.display = 'none';
    const success = document.getElementById('quote-success');
    if (success) success.style.display = 'block';
  });
}

// ── Reveal animations (IntersectionObserver) ───────────────────────────
function initRevealAnimations() {
  if (!('IntersectionObserver' in window)) return;

  const targets = document.querySelectorAll('.section, .category-card, .package-card');
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  targets.forEach(el => {
    el.classList.add('reveal');
    io.observe(el);
  });
}

// ── Init ────────────────────────────────────────────────────────────────
async function init() {
  try {
    const data = await loadData();
    state.allProducts        = data.products.flooring        || [];
    state.allStairTreads     = data.products.stair_treads    || [];
    state.allRisers          = data.products.risers          || [];
    state.allTrimAccessories = data.products.trim_accessories || [];
    state.categories         = data.categories               || [];

    renderCategoryCards();
    renderFlooringGrid();
    renderTrimCards();
    renderStairSection();
    initFilters();
    initNav();
    initSmoothScroll();
    initQuoteForm();
    initRevealAnimations();

    // Modal: close on overlay background click
    const overlay = document.getElementById('modal-overlay');
    if (overlay) {
      overlay.addEventListener('click', function(e) {
        if (e.target.id === 'modal-overlay') closeModal();
      });
    }

    // Modal: close on Escape
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && state.modalProductId) closeModal();
    });

    // Category card scroll
    document.querySelectorAll('.category-card').forEach(card => {
      card.addEventListener('click', function(e) {
        e.preventDefault();
        const catId = this.dataset.category;
        // For stair categories, scroll to stairs section; trims to trims; else flooring
        let target = '#flooring';
        if (['stair-treads', 'risers'].includes(catId)) target = '#stairs';
        else if (['stair-nose','reducer','t-molding','end-cap','baby-threshold','wood-vent','custom-profile'].includes(catId)) target = '#trims';

        const el = document.querySelector(target);
        if (el) {
          const navHeight = document.getElementById('site-nav')?.offsetHeight || 68;
          const top = el.getBoundingClientRect().top + window.scrollY - navHeight - 12;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      });
    });

  } catch (err) {
    console.error('Catalog failed to load:', err);
    const grid = document.getElementById('flooring-grid');
    if (grid) {
      grid.innerHTML = `
        <div style="grid-column:1/-1;padding:40px;text-align:center;color:#666">
          <p style="margin-bottom:8px;font-size:1rem;font-weight:600">Unable to load catalog data.</p>
          <p style="font-size:.875rem">Please try refreshing the page, or contact
            <a href="mailto:jmaslenko@gmail.com" style="color:#1d3d28;font-weight:700">jmaslenko@gmail.com</a>
            for assistance.
          </p>
        </div>
      `;
    }
  }
}

document.addEventListener('DOMContentLoaded', init);
