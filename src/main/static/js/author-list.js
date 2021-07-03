;(function () {
    $(function () {
        const $el = $('#container-author-list');
        $el.append('<div> <button class="btn btn-success">Показать авторов</button></div>');
        const $btn = $el.find('.btn-success');
        const AutorURL = "http://0.0.0.0:8001/api/v1/authors/list/";
        const $pageContainer = $('.container-payload2');

        $btn.click(function () {
            $.get(AutorURL, function (data, status) {
                $pageContainer.hide('slow');
                $pageContainer.empty();
                $.each(data, function (index, value) {
                    $pageContainer.append(`<p>${index} - ${value.name} ${value.email} ${value.age}</p>`);

                })
                $pageContainer.fadeIn(5000);
            })
        })
    })
})()