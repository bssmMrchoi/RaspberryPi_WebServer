var oScript = document.createElement("script");
oScript.type = "text/javascript";
oScript.src = "//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(oScript);

var clickLedOn = document.querySelector("#ledOn");
var clickLedOff = document.querySelector("#ledOff");

clickLedOn.addEventListener("click", function() {
	var result = document.querySelector(".result");
	var data = "<img src='https://media.istockphoto.com/vectors/light-bulb-icon-vector-light-bulb-ideas-symbol-illustration-vector-id1166905208?k=20&m=1166905208&s=170667a&w=0&h=r9hpWdCkRsVFQKD5hgmqW8UgZChF2-FvJMWmc-BGbkE=' width: 300px; height: 300px;>";
        result.innerHTML = data;
        $.ajax({
		type: 'GET',
                url:'/led/on',
                success: function(res) {
			alert(res);
		}
	});
});
	
clickLedOff.addEventListener("click", function() {
	var result = document.querySelector(".result")
        var data = "<img style='width: 416px; height: 416px;' src='https://media.istockphoto.com/vectors/the-light-bulb-is-full-of-ideas-and-creative-thinking-analytical-for-vector-id1269586507?k=20&m=1269586507&s=612x612&w=0&h=Al28wgp5uO8ovTLjOv4wBE4HSl2sLpksZso7kW82qkc='>";
        result.innerHTML = data;
	$.ajax({
		type: 'GET',
		url: '/led/off',
		success: function(res) {
			alert(res);
		}
	});
});

