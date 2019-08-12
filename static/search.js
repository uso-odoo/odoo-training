/*var myFunction;
var onclickFuction;
*/
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

        function onclickFuction(id) {
            
            var xhttp = new XMLHttpRequest();
            //var search_string = document.getElementById("search_string").value;
            var li = "";
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200){
                    var result = JSON.parse(this.responseText);
                    console.log(this.responseText);
                    /*li = '<li class="list-group-item d-flex justify-content-between lh-condensed"><div><h6 class="my-0">'+result[0].product+'</h6></div><span class="text-muted">'+result[0].price+'</span></li>';*/

                    var element = document.getElementById("div");
                    element.classList.remove("d-none");
                    var element = document.getElementById("list");
                    var li = document.createElement('li')
                    li.innerHTML = '<div><h6 class="my-0">'+result[0].product+'</h6></div><span class="text-muted">'+result[0].price+'</span>'
                    att = document.createAttribute("class");
                    att.value = "list-group-item d-flex justify-content-between lh-condensed"
                    li.setAttributeNode(att);
                    
                   /* element.innerHTML = `

                        <div class="col-6">
                          <h4>
                            <span class="text-muted"> Your cart </span>
                            <!--<span class="badge badge-secondary badge-pill"> 3 </span>-->
                          </h4>  
                          <ul class="list-group mb-3" id="list">
                          <!--{% for row in data %}-->
                        <li class="list-group-item d-flex justify-content-between lh-condensed">
                              <div>
                                <h6 class="my-0">{{ product }}</h6> <!-- row.1 -->
                              </div>
                              <span class="text-muted"> <!-- row.2 -->
                                {{ price }}
                              </span>
                            </li>
                            <!--{% endfor %}-->
                            </div>
                        `
*/

                    element.appendChild(li);
                    //document.body.appendChild(li);
                }
            };
            xhttp.open("POST", "/search?search_string="+id+"&add_to_cart=1", true);
            //xhttp.open("POST", "/add?search_string="+id+"&add_to_cart=1", true);
            //xhttp.open("POST", "/search?search_string="+id, true);
            xhttp.send();

                    }