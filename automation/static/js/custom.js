function getAllBranch(){
$('.getAllBranch').click(function(){
var id;
var table = $('#dt-3').DataTable();
var apps = table.column(3).data().toArray();
apps = apps.toString();
var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
	$.ajax( 
	{ 
	    type:"post", 
	    url: "like",
//	    data:{ apps_list: apps, csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(), },
        data:{ apps_list: apps },
        headers:{"X-CSRFToken": $crf_token},
		success: function( data ) 
		{

		console.log(data);
			if(data = 1)
			{
				alert("Branch Data Capture Successfully")
			}
		},
		error : function(xhr,errmsg,err) {
                // Show an error
                console.log("add error to the dom");
            }
	}) 
});
}