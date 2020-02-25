function saveSelectedBook(btn) {

    let book_card = $(btn).parent().parent();
    let title = $(book_card).find('#book_title').html();
    let publisher = $(book_card).find('#book_publisher').html();
    let authors = $(book_card).find('#book_authors').html();
    let published_date = $(book_card).find('#book_published_date').html();
    let ISBN = $(book_card).find('#book_ISBN').html();
    let thumb = $(book_card).parent().find('.notebook-img-thumb').attr('src');

    $.ajax({
        url: $(btn).attr('submit_url'),
        type: 'post',
        data: { title:title, publisher:publisher,
            authors: authors, published_date: published_date, ISBN: ISBN,
            thumb: thumb,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()},
        success: function (data) {
            location.href= $(btn).attr('redirect_to_page');
        }
    });
}
