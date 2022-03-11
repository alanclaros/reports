
function openURL(url) {
    window.open(url, '_self');
}

function addComment(row_id) {
    const dialog = document.getElementById('dialogComment');
    if (!dialog.showModal) {
        dialogPolyfill.registerDialog(dialog);
    }

    $('#commentTxt').val('');
    document.getElementById('row_id').value = row_id;

    $("#td_loading_comment").html('&nbsp;');
    $("#tr_loading_comment").fadeOut('slow');

    dialog.showModal();
}

function closeComment() {
    const dialog = document.getElementById('dialogComment');
    if (!dialog.showModal) {
        dialogPolyfill.registerDialog(dialog);
    }

    dialog.close();
}

function sendComment() {
    const snackbarContainer = document.querySelector('#contact-toast_comment');
    const contactBtn = document.getElementById('contact-btn_comment');
    let dataToast = {};

    const comment = $("#commentTxt").val().trim();
    if (comment === '') {
        $('#commentTxt').val('');
        dataToast = { message: 'Must fill comment', timeout: 2000 };
        snackbarContainer.MaterialSnackbar.showSnackbar(dataToast);
        return false;
    }

    const img_load = document.getElementById('path_img').value;
    const token = document.forms['form_data'].elements['csrfmiddlewaretoken'].value;

    $("#tr_loading_comment").fadeIn('slow');
    $("#td_loading_comment").html('<img src="' + img_load + '">');
    contactBtn.disabled = true;

    const row_select = document.getElementById('row_id').value;

    const data = {
        'comment': comment,
        'row_id': row_select,
        'operation_x': 'save_comment',
        'csrfmiddlewaretoken': token,
    }

    $("#div_comment_" + row_select).load('', data, function () {
        resultSaveComment(row_select);
    });
}

function resultSaveComment(row_select) {
    let comment_response = 'error';
    try {
        comment_response = document.getElementById('comment_response_' + row_select).value;
    }
    catch (e) {

    }
    //console.log('comment response: ', comment_response);

    $("#td_loading").html('&nbsp;');
    $("#tr_loading").fadeOut('slow');
    const contactBtn = document.getElementById('contact-btn_comment');
    contactBtn.disabled = false;

    const dialog = document.getElementById('dialogComment');
    if (!dialog.showModal) {
        dialogPolyfill.registerDialog(dialog);
    }

    dialog.close();

    if (comment_response === 'ok') {
        setTimeout(showToastMessageOk, 100);
    }
    else {
        setTimeout(showToastMessageError, 100);
    }
}

function showToastMessageOk() {
    const snackbarContainer = document.querySelector('#toast_index');
    dataToast = { message: 'Comment save sucessfully', timeout: 3000 };
    snackbarContainer.MaterialSnackbar.showSnackbar(dataToast);
}

function showToastMessageError() {
    const snackbarContainer = document.querySelector('#toast_index');
    dataToast = { message: 'Error saving comment', timeout: 3000 };
    snackbarContainer.MaterialSnackbar.showSnackbar(dataToast);
}
