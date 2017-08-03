function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}


function right(){

  $(document).ready(function(){
      $("button").click(function(){
          $("#move").animate({left: '550px'});
      });
  });



}



function left(){

  $("#pig").ready(function(){
      $("input").click(function(){
          $("div").animate({right: '250px'});
      });
  });



}



function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#rightpig").click(right);

}



$(document).ready(setup);
