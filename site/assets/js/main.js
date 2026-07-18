/* Capital Sawmill — interactions */
(function () {
  // ---------- Parallax ----------
  var els = [].slice.call(document.querySelectorAll('[data-parallax]'));
  if (els.length && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    var ticking = false;
    var update = function () {
      var vh = window.innerHeight;
      els.forEach(function (el) {
        var speed = parseFloat(el.getAttribute('data-parallax')) || 0.15;
        var r = el.getBoundingClientRect();
        var mid = r.top + r.height / 2 - vh / 2;
        el.style.transform = 'translateY(' + (-mid * speed).toFixed(1) + 'px)';
      });
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  // ---------- Service-area map (Leaflet) ----------
  var mapEl = document.getElementById('service-map');
  if (mapEl && window.L) {
    var hq = [42.537712, -73.662602]; // 4119 US Highway 20, Nassau NY
    var map = L.map('service-map', { scrollWheelZoom: false }).setView(hq, 9);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap &copy; CARTO',
      maxZoom: 18
    }).addTo(map);

    // service radius: the Capital Region
    var area = L.circle(hq, {
      radius: 42000,
      color: '#0e6b17',
      weight: 2,
      fillColor: '#0e6b17',
      fillOpacity: 0.14
    }).addTo(map);

    var logoIcon = L.divIcon({
      className: 'hq-pin',
      html: '<div style="background:#780027;border:3px solid #fff;width:22px;height:22px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);box-shadow:0 3px 8px rgba(0,0,0,.5)"></div>',
      iconSize: [22, 22],
      iconAnchor: [11, 22]
    });
    L.marker(hq, { icon: logoIcon }).addTo(map)
      .bindPopup('<b>Capital Sawmill Service, LLC</b><br>4119 US Highway 20, Nassau, NY<br><a href="tel:5184790729">(518) 479-0729</a>');

    map.fitBounds(area.getBounds().pad(0.12));
  }

  // ---------- Contact form ----------
  var form = document.getElementById('estimate-form');
  if (form) {
    form.addEventListener('submit', function () {
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
    });
  }
})();
