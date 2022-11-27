$('.form').submit(function () {
    if ($('#test-button').val() == 'submit') {
        
        if ($('#name').val() !== '' && $('#email').val() !== '')  {
            
            $('.form__group').toggle();
            $('.fourth-div').css('display', 'none');
            $('.second-div').css('display', 'block');
            $('.third-div').css('display', 'block');
            $('#test-button').text('שלח טופס');
            $('#test-button').val('end');
            $('.form__header').text('ניתן להעלות כאן קובץ דוגמא:')
            return false;
        } else {

            alert('נא למלא את כל השדות');
        }
        } else {
        if ($('#phone').val() == '' || /^[\+]?[(]?[0-9]{2,3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test($('#phone').val()) == false) {
            alert('נא לוודא מספר טלפון תקין');
            return false;

        }

        if ($('#file')[0].files.length === 0) {
            alert('טופס נשלח ברגע זה');
        }

        if ($('#file')[0].files[0].size /1024 /1024 > 5) {
            alert('ניתן להעלות עד 5mb');
            return false;
        } else {
            alert('טופס נשלח ברגע זה');
        }

        
    }})

