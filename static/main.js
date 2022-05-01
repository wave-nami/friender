document.querySelector('#loginform').onsubmit = function(event){
    // username
    if ( document.querySelector('#floatingUsername').value.trim().length == 0 ) {
        event.preventDefault();
        document.querySelector('#floatingUsername').classList.add('is-invalid');
    } else {
        document.querySelector('#floatingUsername').classList.remove('is-invalid');
    }
    // password
    if ( document.querySelector('#floatingPassword').value.trim().length == 0 ) {
        event.preventDefault();
        document.querySelector('#floatingPassword').classList.add('is-invalid');
    } else {
        document.querySelector('#floatingPassword').classList.remove('is-invalid');
    }
}