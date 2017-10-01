var month = [
    'มกราคม' ,
    'กุมภาพันธ์' ,
    'มีนาคม' ,
    'เมษายน' ,
    'พฤษภาคม' ,
    'มิถุนายน' ,
    'กรกฎาคม' ,
    'สิงหาคม' ,
    'กันยายน' ,
    'ตุลาคม' ,
    'พฤศจิกายน' ,
    'ธันวาคม' ,
]
var day = [
    'วันจันทร์',
    'วันอังคาร',
    'วันพุธ',
    'วันพฤหัสบดี',
    'วันศุกร์',
    'วันเสาร์',
    'วันอาทิตย์',
]

var timestamp = new Date().getTime()
while(new Date(timestamp).getUTCDay() > 1) {
    timestamp -= (1000 * 60 * 60 * 24)
}
var start_thisWeek = new Date(timestamp);
var start_nextWeek = new Date(timestamp + (1000 * 60 * 60 * 24 * 7));
var isThisWeek = true;
var isInit = false;

function getDateForDay() {
    $('.schedule .panel-title').each(function() {
        var old_text = $(this).text().replace(/[\ \n]/g, '');
        old_text = old_text.substring(0, old_text.match(/[1234567890]/) ? old_text.match(/[1234567890]/).index : old_text.length);
        var date = isThisWeek ? start_thisWeek : start_nextWeek;
        date = new Date(date.getTime() + (1000 * 60 * 60 * 24 * day.indexOf(old_text)))
        $(this).text(old_text + ' ' + new Date(date).getDate() + ' ' + month[new Date(date).getMonth()] + ' ' + new Date(date).getFullYear());
    });
}

getDateForDay();

$('ul.time li').click(function() {
    $('ul.time li').removeClass('selected');
    $(this).addClass('selected');
    $('p.appointment-time').text($(this).closest('.panel').find('.panel-title').text() + ', เวลา ' + $(this).text());
    $('div.appointment-detail').removeClass('hide');
});

$('.schedule-container .pager li').click(function() {
    $(this).addClass('disabled');
    if($(this).hasClass('previous')) {
        if(!isThisWeek) {
            $('ul.time li').removeClass('selected')
            $('div.appointment-detail').addClass('hide');
            $('.schedule-container .pager li.next').removeClass('disabled');
            isThisWeek = true;
            getDateForDay();
        }
    } else if($(this).hasClass('next')) {
        if(isThisWeek) {
            $('ul.time li').removeClass('selected')
            $('div.appointment-detail').addClass('hide');
            $('.schedule-container .pager li.previous').removeClass('disabled');
            isThisWeek = false;
            getDateForDay();
        }
    }
})