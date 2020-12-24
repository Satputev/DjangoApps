function check(){
   var name=document.getElementById("name").value;
   var contact=document.getElementById("cno").value;
   var age=document.getElementById("age").value;
   var uname=document.getElementById("uname").value;
   var passwd=document.getElementById("p1").value;
   var conf_pass=document.getElementById("p2").value;

   for(var x=0;x<=name.length;x++){
       if((name.charCodeAt(x)>=65 && name.charCodeAt(x)<=92)||(name.charCodeAt(x)>=97 && name.charCodeAt(x)<=122)|| name.charCodeAt(x==28)){
       continue
       }
       else{
           return false
       }
   }


if(contact.length !=10){
alert("Contact length should be 10 digits")
    return false;
}else{
    if(contact[0]!="9" && contact[0] !="8" && contact[0] !="7" &&contact[0] !="6"){
alert("Invalid contact no")

        return false;
    }
}
if(passwd != conf_pass){
alert("Password not matching")
    return false;
}

return true
}

