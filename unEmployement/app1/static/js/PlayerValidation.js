function validate(){

if(ValidateName() && validateContact()){
    return true
}
else {

    return false
}
}

function ValidateName(){
let name=document.getElementById('f11').value;
for (let x=0;x<name.length;x++){
    if((name.charCodeAt(x)<65 || name.charCodeAt(x)>90) && ((name.charCodeAt(x)<97 || name.charCodeAt(x)>122))){
document.getElementById('i1').innerText="Name contain only alphabets";
return false
    }
    else {
        document.getElementById('i1').innerText="ok";
return true
    }
}
}

function validateContact(){

    let cno=document.getElementById('f33').value;


     if ((cno[0] !== '7' && cno[0] !== '8' && cno[0] !=='9' && cno[0] !=='6') || (cno.length !==10)){
        document.getElementById('i2').innerText="contact number must start with 9/8/7/6 and length mst be 10 digit";

        return false
    }else{
                 document.getElementById('i2').innerText="ok";
return true
     }
}