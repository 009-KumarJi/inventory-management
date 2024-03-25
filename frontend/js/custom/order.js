var productPrices = {};

$(function () {
    //Json data by api call for order table
    $.get(productListApiUrl, function (response) {
        productPrices = {}
        if(response) {
            console.log(response);
            var options = '<option value="">--Select--</option>';
            $.each(response, function(index, product) {
                console.log(product);
                options += '<option value="'+ product[0] +'">'+ product[1] +'</option>';
                productPrices[product[0]] = product[3];
            });
            $(".product-box").find("select").empty().html(options);
        }
    });
});

$("#addMoreButton").click(function () {
    var row = $(".product-box").html();
    $(".product-box-extra").append(row);
    $(".product-box-extra .remove-row").last().removeClass('hideit');
    $(".product-box-extra .product-price").last().text('0.0');
    $(".product-box-extra .product-qty").last().val('1');
    $(".product-box-extra .product-total").last().text('0.0');
});

$(document).on("click", ".remove-row", function (){
    $(this).closest('.row').remove();
    calculateValue();
});

$(document).on("change", ".cart-product", function (){
    var product_id = $(this).val();
    var price = productPrices[product_id];

    $(this).closest('.row').find('.product-price').text(price);
    calculateValue();
});

$(document).on("change", ".product-qty", function (e){
    calculateValue();
});

$("#saveOrder").on("click", function(){
    var customerName = $("#customerName").val();
    if (!customerName) {
        alert("Customer Name is required");
        return;
    }
    if (!grandTotal) {
        alert("Please add some products");
        return;
    }
    var formData = $("form").serializeArray();
    var requestPayload = {
        customer_name: customerName,
        total: grandTotal,
        order_details: []
    };
    for(var i=0;i<formData.length;++i) {
        var element = formData[i];
        var lastElement = null;

        switch(element.name) {
            case 'product':
                var price = productPrices[element.value];
                requestPayload.order_details.push({
                    product_id: element.value,
                    quantity: null,
                    total_price: price
                });                
                break;
            case 'qty':
                lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                lastElement.quantity = element.value;
                lastElement.total_price *= element.value;
                break;
        }

    }
    callApi("POST", orderSaveApiUrl, {
        'data': JSON.stringify(requestPayload)
    });
});