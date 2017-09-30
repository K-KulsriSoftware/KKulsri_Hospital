$('li#auto').click(function(){
  $(this).addClass('active');
  $('li#manual').removeClass('active');
  $('div#manual-page').addClass('hide')
  $('div#auto-page').removeClass('hide')
})

$('li#manual').click(function(){
  $(this).addClass('active');
  $('li#auto').removeClass('active');
  $('div#auto-page').addClass('hide')
  $('div#manual-page').removeClass('hide')
})

$('.btn-summit').click(function() {
  alert('hello')
})
