$(document).ready(function(){
  $('.btn').click(function(){
    var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
    $.post("./regular-packages", { id: this.getAttribute('id'), csrfmiddlewaretoken: CSRFtoken },function(data) {
      console.log(data)
    } );
  });
});
