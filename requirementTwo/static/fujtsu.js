
function myFunction() {
    
    var select = document.getElementById("sel1").value;
    
    if(select != "none"){
    
        var element = document.getElementById("hide");
        element.classList.remove("hide");
   
    }else{
     
        var element = document.getElementById("hide");
        element.classList.add("hide");

    }
  }