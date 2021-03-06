let id = 0;

let apptable = $('#datatables').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": {
        "url": "/api/apps/",
        "type": "GET"
    },
    "columns": [
        {"data": "id"},
        {"data": "name"},
        {"data": "ip"},
        {"data": "port"},
        { defaultContent: '<div class="badge badge-danger">Not Active</div>'},
        {
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-info btn-primary"><i class="far fa-edit"></i></button>' + '&nbsp;&nbsp' +
            '<button type="button" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>'
        }
    ]


});


$('#datatables tbody').on('click', 'button', function () {
    let data = nodetable.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info btn-primary') {
        window.location.href = '../edit/'+data['id'];
    } else {
        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['id'];

});

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    apitable = $('#apitable').val();
    let url = '/api/'+apitable+'/';
    if (type == 'new') {
        method = 'POST';
    } else {
        id = $('#dataid').val();
        url = url + id + '/';
        method = 'PUT';
    }
    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        console.log(data);
        //alert(data);
        //location.reload();
        //if(data.status == 1){
        window.location.href = '/'+apitable+'/';
        //}else{

        //}
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

//$('#confirm').on('click', '#delete', function (e) {
$('#delete').click(function(e){
var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: '/api/apps/' + id + '/',
        headers:{"X-CSRFToken": $crf_token},
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});