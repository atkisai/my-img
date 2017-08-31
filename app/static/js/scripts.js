
// $(document).ready(function() {
//  var path = "{% static 'img/scroll/back0.jpg' %}",
//       header = $('.header'),
//       i = 0,
//       maxi = 99;
//     $('html').mousewheel(function(event) {
//       var deltaY = event.deltaY;
//       if (deltaY < 0 && i < maxi) {
//          i -= deltaY;
//       	$(header).css('background-image','url(' + path + i + ')');
//         event.preventDefault();
//         $(header).html(i);
//       }
//     });
// });

// var step=100;
// $(window).scroll(function() {
//     var index = $(this).scrollTop();
//     if (index>step) {
//       step+=100;
//       //можно и step=index+100 (нужно смотреть что будет лучше)
//         // (меняем картинку, алгоритм можно любой придумать)
//     }
//   });

 // alert("Welcom to my site!");

// function printTime() {
//     var d=new Date();
//     var hours=d.getHours();
//     var mins=d.getMinutes();
//     var secs=d.getSeconds();
//     document.write(hours+":"+mins+":"+secs+"<br/>")
// }
// setInterval(printTime, 1000);

window.onload = function () {
    var pos=0;
    var box=document.getElementByld('box');
    var t=setInterval(move,10);

    function move() {
    if(pos>=150){clearInterval(t);}
    else{pos+=1;box.style.left=pos+'px';}}
};