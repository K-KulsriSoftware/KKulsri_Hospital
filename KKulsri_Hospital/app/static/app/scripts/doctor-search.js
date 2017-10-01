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
  $.get('/doctor_search_api', {}, function(data) {
    if(data && data.status && data.result.length > 0) {
      $(data.result).each(function() {
        $('#result').append(`<div class="result-block">
          <div class="div-img-circle"><img src="` + this.doctor_img + `" class="img-cir"/></div>
          <div class="div-name"><span class="span-detail">` + this.doctor_name_title + this.doctor_name + ' ' + this.doctor_surname + `</span></div>
          <span class="span-detail">` + this.department_name + `</span><br>
          <button class="btn btn-default btn-res" type="button">นัดหมายแพทย์</button>
          </div>`
        );
      })
    }
  })
})
