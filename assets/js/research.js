(() => {
  'use strict';
  const videos = [...document.querySelectorAll('video[data-preview]')];
  const toggles = [...document.querySelectorAll('.motion-toggle')];
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const connection = navigator.connection;
  let enabled = !preference.matches && !(connection && connection.saveData);
  const visible = new Set();
  const manuallyPaused = new Set();
  const programmaticPauses = new WeakSet();
  function pause(video) {
    if (!video.paused) {
      programmaticPauses.add(video);
      video.pause();
    }
  }
  function update() {
    videos.forEach(video => {
      if (enabled && visible.has(video) && !document.hidden && !manuallyPaused.has(video)) {
        video.play().catch(() => {});
      } else {
        pause(video);
      }
    });
    toggles.forEach(toggle => {
      toggle.hidden = videos.length === 0;
      toggle.textContent = enabled ? 'Pause videos' : 'Play videos';
      toggle.setAttribute('aria-pressed', String(!enabled));
    });
  }
  videos.forEach(video => {
    video.addEventListener('pause', () => {
      if (programmaticPauses.has(video)) programmaticPauses.delete(video);
      else manuallyPaused.add(video);
    });
    video.addEventListener('play', () => manuallyPaused.delete(video));
  });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) visible.add(entry.target);
        else visible.delete(entry.target);
      });
      update();
    }, {threshold: 0.25});
    videos.forEach(video => observer.observe(video));
  } else {
    enabled = false;
  }
  toggles.forEach(toggle => toggle.addEventListener('click', () => {
    enabled = !enabled;
    manuallyPaused.clear();
    update();
  }));
  preference.addEventListener('change', event => {
    enabled = !event.matches && !(connection && connection.saveData);
    update();
  });
  document.addEventListener('visibilitychange', update);
  update();
})();
