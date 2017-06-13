import 'bootstrap/dist/css/bootstrap.css';
import '../css/style.css';
import toastr from 'toastr';
import 'toastr/build/toastr.css';

toastr.options.timeout = 2000;

$(document).ready(() => {
    $('#save').click((event) => {
        event.preventDefault();

        let $name = $('input[type=text][name=name]').val();
        $.ajax({
            url: '/api/add_person',
            type: 'POST',
            data: {
                name: $name
            },
            success: (response, status, xhr) => {
                if (xhr.status === 201) {
                    toastr.success(response.person + ' is successfully saved');
                }
            },
            error: (response) => {
                if (response.status === 409) {
                    toastr.warning(response.responseJSON.person + ' is already existed!');
                }
            }
        });
        let $winners = $('.winners');
        $winners.html("");
        $winners.hide();
    });

    $('#delete').click((event) => {
        event.preventDefault();

        let $name = $('input[type=text][name=name]').val();
        $.ajax({
            url: '/api/delete_person',
            type: 'POST',
            data: {
                name: $name
            },
            success: (response, status, xhr) => {
                if (xhr.status === 200){
                    toastr.success(response.person + ' is successfully deleted');
                }
            },
            error: (response) => {
                if (response.status === 400) {
                    toastr.warning(response.responseJSON.person + ' not existed!');
                }
            }
        });
        let $winners = $('.winners');
        $winners.html("");
        $winners.hide();
    });

    $('#random_three').click(event => {
        event.preventDefault();

        $.ajax({
            url: '/api/random_persons',
            type: 'GET',
            success: (response, status, xhr) => {
                if (xhr.status === 200){
                    let $winners = $('.winners');
                    $winners.html('');
                    for (let person of response.persons) {
                        $winners.append('<p>' + person.name + '</p>');
                    }
                    if (response.persons.length > 0) {
                        $winners.show();
                    }
                    else {
                        toastr.info('there is no such name');
                    }
                }
            },
            error: (response) => {}
        });

    });
});