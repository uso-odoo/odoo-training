// Search Button Function
        function myFunction() {
            var xhttp = new XMLHttpRequest();
            var search_string = document.getElementById("search_string").value;
            var tr = "";
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var result = JSON.parse(this.responseText);
                    for(i=0;i < result.length;i++) {
                        tr += "<tr><td>"+result[i].id+"</td><td>"+result[i].product+"</td><td>"+result[i].price+"</td><td><input type='number' name'quantity' value='1' min='1' style='width: 70px'></td><td><button type='button' class='btn btn-primary btn-sm' value="+result[i].id+">Add To Cart</button></td></tr>";
                    }
                        document.getElementById("product").innerHTML = tr;
                }
            };
            xhttp.open("POST", "/search?search_string="+search_string, true);
            xhttp.send();
        }
// "Add To Cart" Button Function
        function onclickFuction(id) {
            
            var xhttp = new XMLHttpRequest();
            var li = "";
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200){
                    var result = JSON.parse(this.responseText);
                    console.log(this.responseText);
                    var element = document.getElementById("div");
                    element.classList.remove("d-none");
                    var element = document.getElementById("list");
                    var li = document.createElement('li')
                    li.innerHTML = '<div><h6 class="my-0">'+result[0].product+'</h6></div><span class="text-muted">'+result[0].price+'</span>'
                    att = document.createAttribute("class");
                    att.value = "list-group-item d-flex justify-content-between lh-condensed"
                    li.setAttributeNode(att);

                    element.appendChild(li);
                }
            };
            xhttp.open("POST", "/search?search_string="+id+"&add_to_cart=1", true);
            
            xhttp.send();

                    }


 // "Continue to Check Out" Button Function
      function checkOutFuction() {
            
            alert("Thank You For Your Time ! Your Data Successfully Recorded !");
            var xhttp = new XMLHttpRequest();
            
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200){
                    console.log(this.responseText);
                }
                document.getElementById("check_id")
            };
            xhttp.open("POST", "/check?check_out=0", true);
            xhttp.send();

                    }