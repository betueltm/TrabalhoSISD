$( document ).ready(function() {
    
    $("#iptProduto").on("click",function()
    {
        var valor = $("#iptProduto").val();
        $.ajax({
            type: "POST",
            url: url,
            data: valor           
        });
        
    });
});