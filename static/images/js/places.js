
(function($) {
  skel.init(
    {
      reset: "full",
      breakpoints: {
        global: {
          range: "*",
          href: "css/places.css",
          containers: 1400,
          grid: { gutters: 50 }
        },
        wide: {
          range: "-1680",
          href: "css/style-wide.css",
          containers: 1200,
          grid: { gutters: 40 }
        },
        normal: {
          range: "-1280",
          href: "css/style-normal.css",
          containers: 960,
          lockViewport: true
        },
        narrow: {
          range: "-980",
          href: "css/style-narrow.css",
          containers: "95%",
          grid: { gutters: 30 }
        },
        narrower: {
          range: "-840",
          href: "css/style-narrower.css",
          grid: { collapse: 1 }
        },
        mobile: {
          range: "-640",
          href: "css/style-mobile.css",
          containers: "90%",
          grid: { gutters: 15, collapse: 2 }
        }
      }
    },
    {
      layers: {
        layers: {
          navPanel: {
            animation: "pushX",
            breakpoints: "narrower",
            clickToClose: true,
            height: "100%",
            hidden: true,
            html: '<div data-action="navList" data-args="nav"></div>',
            orientation: "vertical",
            position: "top-left",
            side: "left",
            width: 275
          },
          titleBar: {
            breakpoints: "narrower",
            height: 44,
            html:
              '<span class="toggle" data-action="toggleLayer" data-args="navPanel"></span><span class="title" data-action="copyHTML" data-args="logo"></span>',
            position: "top-left",
            side: "top",
            width: "100%"
          }
        }
      }
    }
  );
})(jQuery);
