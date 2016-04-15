$.feature('f_align_middle', function () {
  var elem = $('.align-middle');

  elem.show();

  $(window).resize(function () {
    var top = ($(window).height() - elem.outerHeight()) / 2;

    elem.css({
      position: 'relative',
      top: Math.max(top, 0)
    });
  });

  $(window).resize();
});
