
form = document.querySelector("#registration_form");
console.log(form)


// this will run when click on button
if(form!=null){
    form.addEventListener("submit", function(e){
        e.preventDefault();

        // validation starts here
        firstName = document.querySelector("#first_name").value;
        lastName = document.querySelector("#last_name").value;
        email = document.querySelector("#email").value;
        mobile = document.querySelector("#mobile").value;
        password = document.querySelector("#password").value;
        confirmPassword = document.querySelector("#confirm_password").value;
        
        is_form_data_valid = true;
        //print all the values
        console.log("fname:"+firstName+" lastName:"+lastName+" email:"+email+" mobile:"+mobile+" password:"+password+" confirm_password:"+confirmPassword)
        
        // validate for empty first name text field
        if(firstName==""){
            document.querySelector("#firstNameHelp").textContent = "Name can't be blank";
            is_form_data_valid = false;
        }else if(firstName.length < 3 || firstName.length > 25){
            document.querySelector("#firstNameHelp").textContent = "First name must be between 3 and 25 characters.";
            is_form_data_valid = false;
        }else{
            document.querySelector("#firstNameHelp").textContent = "";
        }

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

        // validate for empty mobile text field
        if(mobile==""){
            document.querySelector("#mobileHelp").textContent = "Mobile can't be blank";
            is_form_data_valid = false;
        }else if(isMobileValid(mobile) == false){
            document.querySelector("#mobileHelp").textContent = "Enter 10 digit mobile number";
            is_form_data_valid = false;
        }else{
            document.querySelector("#mobileHelp").textContent = "";
        }

        

        // validate for empty password text field
        if(password==""){
            document.querySelector("#passwordHelp").textContent = "Password can't be blank";
            is_form_data_valid = false;
        }else if(isPasswordSecure(password) == false){
            document.querySelector("#passwordHelp").textContent = "Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)";
            is_form_data_valid = false;
        }else{
            document.querySelector("#passwordHelp").textContent = "";
        }

        

        // validate for empty confirm password text field
        if(confirmPassword==""){
            is_form_data_valid = false;
            document.querySelector("#confirmPasswordHelp").textContent = "Confirm password can't be blank";
        }else if(password !== confirmPassword){
            is_form_data_valid = false;
            document.querySelector("#confirmPasswordHelp").textContent = "The password does not match";
        }else{
            document.querySelector("#confirmPasswordHelp").textContent = "";
        }

        if(is_form_data_valid == true){
            form.submit();
        }

    });
}



//this function will return true if email valid otherwise it return false
const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

// this function validate mobile no. should have 10 digit
const isMobileValid = (mobile) => {
    const re = /^\d{10}$/;
    return re.test(mobile);
};

//this function validate for secure password
const isPasswordSecure = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return re.test(password);
};