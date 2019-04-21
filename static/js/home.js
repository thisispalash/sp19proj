$('a[data-o').click(function(e) {
  e.preventDefault()

  if (!$(this).attr('data-r')) { $(this).contents().unwrap(); }

  let ob = $(this).attr('data-o');
  if (ob)
    $('[data-ob="' + ob + '"]').removeClass('off').addClass('on');
  
  let cb = $(this).attr('data-c');
  if (cb)
    $('[data-cb="' + cb + '"]').removeClass('on').addClass('off');

  count_clicks(ob,cb);
})

function count_clicks(o,c) {
  // TODO store in db
  console.log('Opened: ' + o);
  console.log('Closed: ' + c);
}

function link_setup() {
  $('a').attr('target','_blank');
}

$(document).ready(function() {
  link_setup();
})