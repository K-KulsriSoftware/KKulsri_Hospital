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
});

$('.btn-summit').click(function() {
  $('#result').empty();
  var data = {};
  data.days = '';
  $('.input-days input[type="checkbox"]').each(function() {
    if($(this).prop('checked')) {
      data.days += $(this).attr('id').substring(0, 3) + ','
    }
  });
  if(data.days === '') {
    delete data.days;
  }
  data.time = '';
  $('.input-time input[type="checkbox"]').each(function() {
    if($(this).prop('checked')) {
      data.time += $(this).closest('label').text().replace(/ /g, '').replace(/\n/g, '') + ',';
    }
  });
  if(data.time === '') {
    delete data.time;
  }
  data.doctor_firstname = $('.input-name input#in-firstname').val();
  if(data.doctor_firstname === '') {
    delete data.doctor_firstname;
  }
  data.doctor_surname = $('.input-name input#in-surname').val();
  if(data.doctor_surname === '') {
    delete data.doctor_surname;
  }
  data.gender = '';
  $('.input-gender input[type="checkbox"]').each(function() {
    if($(this).prop('checked')) {
      data.gender += $(this).closest('label').text().replace(/ /g, '').replace(/\n/g, '') + ',';
    }
  });
  if(data.gender === '') {
    delete data.gender;
  }
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
      });
    }
  });
})
