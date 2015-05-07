stocks = {'GOOG': 500}

// $.get('/volatility', stocks, function(data){
//   console.log("success");
// });

$.ajax({
  url: "/volatility",
  data: {'GOOG': 500},
  contentType: 'text/json',
  success: function(data){
    console.log(JSON.stringify(data));
    console.log(data.vol)
    $('#vol').text(data.vol);
  }
});
