//js file for question voting, click on plus is 1, click on minus is -1,
//takes user, answer, score

$('#plus_vote').click(function(event) {
    event.preventDefault();
    console.log("plus");
    let $info = $("#vote_form :input");
    let $user_id = $info[1];
    //let $q_id = $info[2];
    var $form = {
        "user": 1, //needs to be $user_id,
        "question": 1, //needs tobe $q_id
        "score": 1,
        'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
    }

    $.ajax({
        type: 'POST',
        url: '/api/votequestion/',
        data: $form,
        success: function(result) {
            alert("You Voted");
            window.location.href = '/';
        }
    })
});

$('#minus_vote').click(function(event) {
    console.log("minus");
    let $info = $("#vote_form :input");
    let $user_id = $info[1];
    //let $q_id = $info[2];
    var $form = {
        "user": 1, //needs to be $user_id
        "question": 1, //needs to be $q_id
        "score": -1,
        'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
    }
    console.log($form);

    $.ajax({
        type: 'POST',
        url: '/api/votequestion/',
        data: $form,
        success: function(result) {
            alert("You Voted");
            window.location.href = '/';
        }
    })
});