$(document).ready(function(){

  function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  console.log(color)
  return color;
  }


//var random = getRandomColor();
//var random2 = getRandomColor();
//var deg = '180deg';
//var linear = `linear-gradient(${deg},${random},${random2})`;
//$("html").css("background",linear);

var sub1 = $('.sub1')
sub1.hide()
var sub2 = $('.sub2')
sub2.hide()
var sub3 = $('.sub3')
sub3.hide()
var sub4 = $('.sub4')
sub4.hide()

var redditinputs = $('input[name=subkey], input[name=redditkeyword],input[name=madecomment],input[name=subid],input[name=uresponse]');
var twitterinputs = $('input[name=keyword1], input[name=statusid], input[name=user_tweet],input[name=responderhandle]');
var instainputs = $('input[name=tpic], input[name=file],input[name=caption]')

$(redditinputs).bind('keypress keydown keyup change',function(){
  sub1.show(); });

$(twitterinputs).bind('keypress keydown keyup change',function(){
  sub2.show(); });

$(instainputs).bind('keypress keydown keyup change',function(){
  sub3.show(); });

$('input[name=craigsbit]').bind('keypress keydown keyup change',function(){
  sub4.show(); });


//$(document.body).click(function(){
//
//  var random = getRandomColor();
//  var random2 = getRandomColor();
//  var deg = '180deg';
//  var linear = `linear-gradient(${deg},${random},${random2})`;
//  $("html").css("background",linear);
//});



//var element = document.getElementById('bigone').textContent
//console.log(element)

//$.get('/num_projects',function(data){
//  for(i = 0; i<data.value; i++){
//      $( "#projectx" ).append("<div class = 'projbox'>Place Holder</div>" );
//    }
//  })


})
