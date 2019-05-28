$( document ).ready(function() {
    
    $("#iptProduto").on("click",function()
    {
        enviarProdutoPost();               
    });
});

function enviarProdutoPost()
{
    var produtoPost = $("#iptProduto").val();

    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: success
    });
}