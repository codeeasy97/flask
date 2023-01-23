

login_form = document.querySelector("#login_form");
console.log(login_form)

if(login_form!=null){
    login_form.addEventListener("submit", function(e){
        e.preventDefault();
        email = document.querySelector("#email").value;
        password = document.querySelector("#password").value;
        let is_form_data_valid = true;

        // validate for empty email text field
        if(email==""){
            document.querySelector("#emailHelp").textContent = "Email can't be blank";
            is_form_data_valid = false;
        }else if(isEmailValid(email) == false){
            document.querySelector("#emailHelp").textContent = "Email is not valid";
            is_form_data_valid = false;
        }else{
            document.querySelector("#emailHelp").textContent = "";
        }

        // validate for empty confirm password text field
        if(password==""){
            document.querySelector("#passwordHelp").textContent = "Password can't be blank";
            is_form_data_valid = false;
        }else{
            document.querySelector("#passwordHelp").textContent = "";
        }

        // submit to the server if the form is valid
        if (is_form_data_valid == true) {
            login_form.submit();
        }
    });
}

//this function will return true if email valid otherwise it return false
const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};