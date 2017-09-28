$('li#auto').click(function(){
  if($('li#manual').hasClass('active')){
    $('li#manual').removeClass('active');
    $('div#manual-page').hide();
    $('div#auto-page').removeClass('hide');
  }
  $('li#auto').addClass('active');

})

$('li#manual').click(function(){
  if($('li#auto').hasClass('active')){
    $('li#auto').removeClass('active');
    $('div#auto-page').hide();
    $('div#manual-page').removeClass('hide');
  }
  $('li#auto').addClass('active');

})
