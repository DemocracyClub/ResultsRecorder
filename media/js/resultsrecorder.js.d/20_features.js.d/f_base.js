$.feature('f_base', function () {
  $('body').on('click', 'button[data-loading-text]', function () {
    $(this).button('loading');

    return true;
  });
});
