$(document).ready(function(){
  $('.btn').click(function(){
    $.post( "#", { id: this.getAttribute('id') } );
  });
});
