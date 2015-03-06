// When a theme-change item is selected, update theme
var supports_storage = supports_html5_storage();
/* On load, set theme from local storage */
if (supports_storage) {
  var theme = localStorage.theme;
  if (theme) {
    set_theme(theme);
  }
} else {
  /* Don't annoy user with options that don't persist */
  $('#theme-dropdown').hide();
}

function supports_html5_storage() {
  try {
    return 'localStorage' in window && window['localStorage'] !== null;
  } catch (e) {
    return false;
  }
}
function set_theme(theme) {
  $('link[title="main"]').attr('href', theme);
  if (supports_storage) {
    localStorage.theme = theme;
  }
}
jQuery(function($) {
    $('body').on('click', '.change-style-menu-item', function() {
      var theme_name = $(this).attr('rel');
      var theme = "//netdna.bootstrapcdn.com/bootswatch/3.0.0/" + theme_name + "/bootstrap.min.css";
      set_theme(theme);
    });
});
