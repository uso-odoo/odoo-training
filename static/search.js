(function(){

    function loadDoc() {
      var xhttp = new XMLHttpRequest();
      var search_string = document.getElementById("search_string").values
      console.log(search_string, "aaaaaaaaaaaaaaa");
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("demo").innerHTML =
          this.responseText;
        }
      };
      xhttp.open("POST", "ajax_info.txt", true);
      xhttp.send();
    }


});
