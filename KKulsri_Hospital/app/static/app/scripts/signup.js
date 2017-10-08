$('form').submit(function(e) {
    if($('#id_password1').val() !== $('#id_password2').val()) {
        e.preventDefault();
        alert('รหัสผ่านไม่ตรงกัน')
    }
});