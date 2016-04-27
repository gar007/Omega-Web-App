<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
    <title>Omega Web App</title>
    <link rel="stylesheet" href="static/style.css">
    <link rel="shortcut icon" href="static/favicon.ico"> 
</head>
<body>

<div class="topbanner">
    <img src="static/omegatop.png" id = "topbanner" alt="Top banner">
    <audio autoplay>
        <source src="static/lite.mp3" type="audio/mpeg">
    </audio>
</div>

<div class="buttonsLites">

<div class="buttons">       
    <form action="/<pinStates>" enctype="text/plain" method = "POST">
        <input type = "hidden"  id="btnId" name = "btnId" value="0"> 
        <input type="image" id="btn0" src="static/btn15.png" onclick = "toggle('0')"> 
        <input type="image" id="btn1" src="static/btn16.png" onclick = "toggle('1')"> 
        <input type="image" id="btn2" src="static/btn17.png" onclick = "toggle('2')"> 
        <input type="image" id="btn3" src="static/fan_button.png" onclick = "toggle('3')"> 
    </form>
</div> 

<div class="lites">
    <img  id="lite0"  src = "static/blue_lite_off.png" alt="lite0">
    <img  id="lite1"  src = "static/green_lite_off.png" alt="lite1">
    <img  id="lite2"  src = "static/red_lite_off.png" alt="lite2">
    <img  id="fan"  src = "static/fan_off.png" alt="fan">
</div>

</div> 

<script type="text/javascript">

// pinStates is a string list(comma delimited) that determines the state of 
// Omega board pins. Each entry is a number followed by a pinState
// corresponding to this table
// 0on = button 0 lite on
// 0off = button 0 lite off
// 1on = button 1 lite on
// 1off = button 1 lite off
// R0on = relay 0 on
// R0off = relay 0 off

// The following javascript code assigns to the img tags a source for the 
// image based on what pinStates assigns. pinStates is the variable that 
// assigns whether a light/pin/relay is on or off. pinStates is defined on the
// server side(bottle).

// pinObj is an array that lists the objects(by id) being controlled by
// pinStates
var pinObj = [
'lite0',
'lite1',
'lite2',
'fan'
]
var pinStates = '{{pinStates}}';
var pinStatesArr = pinStates.split(",");
var pins = pinStatesArr.length;
for (i = 0; i < pins; i++) {
    switch (pinStatesArr[i]) {
        case '0on':
            document.getElementById(pinObj[i]).src = "static/blue_lite_on.png"; 
            break;  
        case '0off':
            document.getElementById(pinObj[i]).src = "static/blue_lite_off.png"; 
            break; 
        case '1on':
            document.getElementById(pinObj[i]).src = "static/green_lite_on.png"; 
            break; 
        case '1off':
            document.getElementById(pinObj[i]).src = "static/green_lite_off.png"; 
            break; 
        case '2on':
            document.getElementById(pinObj[i]).src = "static/red_lite_on.png"; 
            break; 
        case '2off':
            document.getElementById(pinObj[i]).src = "static/red_lite_off.png"; 
            break;
        case '3on':
            document.getElementById(pinObj[i]).src = "static/fan_on.png"; 
            break; 
        case '3off':
            document.getElementById(pinObj[i]).src = "static/fan_off.png"; 
            break;        
        default :
            alert('Unable to find a matching case for pinStates')
            alert(pinStates)
    }
}
</script>   

<script>
function toggle(btnNum)  {  
     document.getElementById('btnId').value = btnNum;
}
</script> 



</body>
</html>