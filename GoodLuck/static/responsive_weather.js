$.getJSON('http://api.openweathermap.org/data/2.5/group?id=1835848,5815135,2643743&APPID=8da41a26ad86b639aad96ecff8e613f9&units=metric  ', function(data){
       
    function getWorldTime(tzOffset) { // 24시간제
  var now = new Date();
  var tz = now.getTime() + (now.getTimezoneOffset() * 60000) + (tzOffset * 3600000);
  now.setTime(tz);
 
 
  var s =
    leadingZeros(now.getFullYear(), 4) + '-' +
    leadingZeros(now.getMonth() + 1, 2) + '-' +
    leadingZeros(now.getDate(), 2) + ' ' +
 
    leadingZeros(now.getHours(), 2) + ':' +
    leadingZeros(now.getMinutes(), 2) 
 
  return s;
}

function leadingZeros(n, digits) {
  var zero = '';
  n = n.toString();
 
  if (n.length < digits) {
    for (i = 0; i < digits - n.length; i++)
      zero += '0';
  }
  return zero + n;
}

 //현재 날짜 뽑아서 출력
   var $sDate = getWorldTime(+9); //서울 시간
   var $wDate = getWorldTime(-4); 
   var $lDate = getWorldTime(+1); 

   //서울 
   var $sminTemp = data.list[0].main.temp_min;
   var $smaxTemp = data.list[0].main.temp_max;
   var $sTemp = data.list[0].main.temp;
   var $sIcon = data.list[0].weather[0].icon;
    

    //alert($.now());//현재 시간을 출력하는 방법
    //alert(new Date(Date.now())); 형식[Wed Jul 15 2020 14:11:30 GMT+0900 (대한민국 표준시)]
    

  

   

   

   //A.appendTo(B) B뒤어 A를 붙이기
   //A.append(B) A뒤어 B를 붙이기
   //A.prependTo(B) B앞에 A를 붙이기
   //A.prepend(B) A앞에 B를 붙이기

    //날짜 출력
   $('.sdate').prepend($sDate);
   $('.wdate').prepend($wDate);
   $('.ldate').prepend($lDate);
   //서울 출력
    $('.stemp').append($sTemp);
    $('.slowtemp').append($sminTemp);
    $('.shightemp').append($smaxTemp);
     //<img src =" http://openweathermap.org/img/wn/10d@2x.png"/>
     $('.sicon').append('<img src =" http://openweathermap.org/img/wn/'+$sIcon+'.png"/>');


});