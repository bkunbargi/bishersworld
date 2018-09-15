$(document).ready(function(){

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
  }



$(document.body).click(function(){

  var random = getRandomColor();
  var random2 = getRandomColor();
  var deg = '180deg';
  var linear = `linear-gradient(${deg},${random},${random2})`;
  console.log(linear)
  $('body').css('background',linear);

});



//$(".tablinks").bind('click',function(){

  //var class_name = '#'+$(this).attr('class').split(' ')[1];
  //console.log(class_name)
  //$(`${class_name}`).css('display',"active")
  //$('.tabcontent').css('border','5px solid green')

  //var class_finder = `div[class*="${class_name}"]`
  //var other_class_name = $(class_finder).attr('class').split(' ')[0];
  //console.log($(class_finder))
  //console.log(other_class_name,class_name)
  //$(`div.${other_class_name}.${class_name}`).css("display","active");
  //console.log($(`div.${other_class_name}.${class_name}`).innertext)
  //var new_name = other_class_name+'.'+class_name
  //console.log(new_name)
  //$(other_class_name,class_name).css('display',"active")

//})




})
