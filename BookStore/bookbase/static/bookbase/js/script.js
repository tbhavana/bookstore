$(document).ready(function(){
$('#Addtocart').click(function(){
	
	var bookid;
	bookid = $(this).attr("data-bookId");

	console.log(bookid);
	$.post('books/Addingtocart/',{book_id:bookid},function(data){
			$("#Addtocart").hide();
	});
});
});

/*
$document).ready(function(){
	$('#Addtocart').click(function(){
		console.log('Im called');
		$.ajax({
			type:"POST",
			url: "books/Addingtocart",
			dataType:"json",
			data:{"book_id":$(this).attr('data-bookId')}
		})
	})
})

*/
