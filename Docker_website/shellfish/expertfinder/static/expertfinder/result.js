var countChecked = function() {
  if ($(this).prop('checked')==false && $(this).prop('className')!="read-more-state"){
     console.log("Doc Filter: ", $(this).prop('id'), $(this).prop('checked')==false);
     $('.card:contains("'+ $(this).attr('id') +'")').hide();
  } else {
     console.log("Doc Filter: ", $(this).prop('id'), $(this).prop('checked')==false);
     $('.card:contains("'+ $(this).attr('id') +'")').show();
  }

};
countChecked();
$( "input[type=checkbox]" ).on( "click", countChecked );

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function() {
  if (this.value == 365) {
     output.innerHTML = 'All'
     var x = document.getElementsByName("myDate");
     for (var i=0; i < x.length; i++) {
       //Only if not filtered out by checkbox
       $('.card:contains("'+ x[i].innerHTML +'")').show();
     }
  }
  else {
     output.innerHTML = this.value;
     var x = document.getElementsByName("myDate");
     var d = new Date(Date.now());
     d.setTime(d - (24*60*60*1000*this.value));
     for (var i=0; i < x.length; i++) {
       var nd = new Date(x[i].innerHTML);
       //Known bug will show() things that should still be unfiltered by file type
       // May be more efficient to use Justins backend filters
       if (nd < d) {
         $('.card:contains("'+ x[i].innerHTML +'")').hide();
       }
       else {
         $('.card:contains("'+ x[i].innerHTML +'")').show();
       }
     }
  }
}


var nlpSlider = document.getElementById("NLPcheck");
var nlpMimic = document.getElementById("NLPmirror");
$("#NLPcheck").change(function() {
  console.log('I AM HERE LOOK AT ME NOW');
   if($(this).is(':checked')) {
    console.log(nlpMimic.value);
    nlpMimic.value = "NLP";
  }
  else {
    nlpMimic.value = "_";
  }
});
