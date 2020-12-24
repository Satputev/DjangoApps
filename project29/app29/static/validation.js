function validate() {
    var name = document.getElementById("a").value;
    var password = document.getElementById('b').value;
    x = name.length;

    for (var i = 0; i < x; i++) {
        if ((name.charCodeAt(i) < 65 || name.charCodeAt(i) > 90) && (name.charCodeAt(i) < 97 || name.charCodeAt(i) > 120)) {


                document.getElementById('s1').innerText = '****Name contaion only alphabets..';
                return false
            }
        }

 if (password.length < 8) {
                document.getElementById('s2').innerText = '****min password length is 8 or more';
        return false


    }
            return true

}