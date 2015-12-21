$( document ).ready(function() {
    $('.addservicebutton').click(function(){
    	
   		var item = $('.newitem').val();
    	
    	$('#itemlist').append('<li><input type="checkbox" value='+item+'><label>'+item+'</label></li>');

    	//$('<li input type="checkbox"/>', {value:item}).appendTo('.checkboxgroup ul');
    		
    });

    $('.addtobutton').click(function(){

    	//loop through the  ul of available items

    	var listItems = $('#itemlist li');
    	listItems.each(function(idx,listelement){

    		var child = $(this).children('input'); 
			if (($(child).prop('checked'))) {

				var  temp = $('#cartitems');
				var purchaseditem = $(child).next('label').text(); 
				$('.content ul').append('<li><input type="checkbox" value='+purchaseditem+'/><label>'+purchaseditem+'</label></li>');	

			}
    		
    	});   	

    });

    $('.removebutton').click(function(){

    	//loop through the  ul of available items

    	var itemsincart = $('#cartitems li');
    	itemsincart.each(function(idx,listelement){

    		var child = $(this).children('input'); 
			if (($(child).prop('checked'))) {

				//var  temp = $('#cartitems');
				//var purchaseditem = $(child).next('label').text(); 
				//$('.content ul').append('<li><input type="checkbox" value='+purchaseditem+'/><label>'+purchaseditem+'</label></li>');	

				$(this).remove();

			}
    		
    	});   	

    });

});