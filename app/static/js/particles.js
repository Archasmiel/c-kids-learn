window.addEventListener("DOMContentLoaded", () => {
    particlesJS("particles-js", {
        /* -------------------------------
           Background Settings
        -------------------------------- */
        background: {
            color: {
                value: "#000000"
            }
        },

        /* -------------------------------
           Particles Settings
        -------------------------------- */
        particles: {
            number: {
                value: 100,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: "#1d6ac9"
            },
            shape: {
                type: "circle",
                stroke: {
                    width: 0,
                    color: "#1d6ac9"
                },
                polygon: {
                    nb_sides: 3
                }
            },
            opacity: {
                value: 0.5,
                random: true,
                anim: {
                    enable: false,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                }
            },
            size: {
                value: 3,
                random: true,
                anim: {
                    enable: false,
                    speed: 40,
                    size_min: 0.1,
                    sync: false
                }
            },
            line_linked: {
                enable: true,
                distance: 125,
                color: "#000000",
                opacity: 0.5,
                width: 0.5
            },
            move: {
                enable: true,
                speed: 2,
                direction: "none",
                random: false,
                straight: false,
                out_mode: "out",
                bounce: false,
                attract: {
                    enable: false,
                    rotateX: 600,
                    rotateY: 1200
                }
            }
        },

        /* -------------------------------
           Interactivity Settings
        -------------------------------- */
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: {
                    enable: false,
                    mode: "repulse"
                },
                onclick: {
                    enable: true,
                    mode: "push"
                },
                resize: true
            },
            modes: {
                grab: {
                    distance: 140,
                    line_linked: {
                        opacity: 1
                    }
                },
                bubble: {
                    distance: 400,
                    size: 40,
                    duration: 2,
                    opacity: 8,
                    speed: 3
                },
                repulse: {
                    distance: 50,
                    duration: 0.4
                },
                push: {
                    particles_nb: 4
                },
                remove: {
                    particles_nb: 2
                }
            }
        },

        /* -------------------------------
           Retina
        -------------------------------- */
        retina_detect: true
    });
});
