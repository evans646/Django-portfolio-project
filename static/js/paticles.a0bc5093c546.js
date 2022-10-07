particlesJS("particles-js", {
  particles: {
    number: { value: 6, density: { enable: true, value_area: 800 } },
    color: { value: "#34d7cd" },
    shape: {
      type: "polygon",
      stroke: { width: 0, color: "#000" },
      polygon: { nb_sides: 6 },
      image: { src: "img/github.svg", width: 100, height: 100 },
    },
    opacity: {
      value: 0.43292125643369117,
      random: true,
      anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false },
    },
    size: {
      value: 116.2473744127504,
      random: true,
      anim: { enable: true, speed: 10, size_min: 40, sync: false },
    },
    line_linked: {
      enable: false,
      distance: 200,
      color: "#ffffff",
      opacity: 1,
      width: 2,
    },
    move: {
      enable: true,
      speed: 8,
      direction: "none",
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
      attract: { enable: false, rotateX: 600, rotateY: 1200 },
    },
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: { enable: true, mode: "repulse" },
      onclick: { enable: false, mode: "push" },
      resize: true,
    },
    modes: {
      grab: { distance: 852.6326046708033, line_linked: { opacity: 0.9 } },
      bubble: {
        distance: 947.0529470529472,
        size: 63.93606393606394,
        duration: 2,
        opacity: 8,
        speed: 3,
      },
      repulse: { distance: 200, duration: 0.4 },
      push: { particles_nb: 4 },
      remove: { particles_nb: 2 },
    },
  },
  retina_detect: true,
});
var count_particles, stats, update;
stats = new Stats();
stats.setMode(0);
stats.domElement.style.position = "absolute";
stats.domElement.style.left = "0px";
stats.domElement.style.top = "0px";
document.body.appendChild(stats.domElement);
count_particles = document.querySelector(".js-count-particles");
update = function () {
  stats.begin();
  stats.end();
  if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) {
    count_particles.innerText = window.pJSDom[0].pJS.particles.array.length;
  }
  requestAnimationFrame(update);
};
requestAnimationFrame(update);
