var currentOption;
var returnOption = $.Event("option");

function getOptionObject(ticker, expiryDay, expiryMonth, expiryYear){
    var url = "http://www.google.com/finance/option_chain?q="
    + ticker 
    + "&expd=" 
    + expiryDay
    + "&expm="
    + expiryMonth
    + "&expy="
    + expiryYear
    + "&ei=&output=json";
    $.get(url,function(data){
        $("body").trigger(returnOptions);
        currentOption = data; 
        console.log(data);
    });
}


