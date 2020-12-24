function elgible(){

   var name=document.getElementById("name").value;
   var contact=document.getElementById("contact").value;

      var disease=document.getElementsByName("diseases").value;
   var antibio=document.getElementsByName("antib").value;
   var alchohol=document.getElementsByName("alchohol").value;


   for (var i=0;i<name.length;i++){
if( name.charCodeAt(i)<65 || name.charCodeAt(i)>90 && name.charCodeAt(i)!=32){

    alert("All letters must be capital only and length is three or more")
    return false
}else{
    continue
}
}
if(contact.length !="10"){
    alert("Contact must be of 10 digit..")
    return false
}
else {
    if (contact[0] != "9" && contact[0] != "8" && contact[0] != "7" && contact[0] != "6"){
        alert("Contect must be start with 9/8/7/6..")
        return false
    }
        }

       if(disease !="no") {
           alert("You are not eligible for blood donation")
           return false
       }
       if(antibio !="no"){
                      alert("You are not eligible for blood donation")

           return false
       }
       if(alchohol!="no"){
                      alert("You are not eligible for blood donation")

           return false
       }
return true;
}