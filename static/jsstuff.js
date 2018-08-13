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
  $("body").css("background",linear);
});

$('#hnav').click(function(){
  var random = getRandomColor();
  var random2 = getRandomColor();
  var deg = '180deg';
  console.log(random)
  console.log(random2)
  var linear = `linear-gradient(${deg},${random},${random2})`;
  $("hnav").css("background",linear);
});

$(window).resize(function() {
  $("body").css("background-color","white")
  });


//var element = document.getElementById('bigone').textContent
//console.log(element)

//$.get('/num_projects',function(data){
//  for(i = 0; i<data.value; i++){
//      $( "#projectx" ).append("<div class = 'projbox'>Place Holder</div>" );
//    }
//  })


})
