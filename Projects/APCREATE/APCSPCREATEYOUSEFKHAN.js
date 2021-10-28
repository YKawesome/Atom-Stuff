//US dollar, Euro, Japanese Yen, Pound sterling, Australian dollar
//Data used in the program
var data = [
["USD",["EUR",0.82],["JPY",103.64],["GBP",0.74],["AUD",1.32],["USD",1]],
["EUR",["JPY",126.59],["GBP",0.9],["AUD",1.61],["USD",1.22],["EUR",1]],
["JPY",["GBP",0.007],["AUD",0.127],["USD",0.097],["EUR",0.008],["JPY",1]],
["GBP",["AUD",1.78],["USD",1.35],["EUR",1.11],["JPY",139.99],["GBP",1]],
["AUD",["USD",0.76],["EUR",0.62],["JPY",78.69],["GBP",0.56],["AUD",1]]
];


//Algorithm to Convert Currency
function computeCurrency(curr1, curr2) {
  var listy = [];
  for (var element = 0; element <= data.length-1; element++) {
    if (curr1==data[element][0]) {
      listy = data[element];
      break;
    }
  }

  var tup = null;
  for (var thing = 1; thing <= listy.length-1; thing++) {
    if (curr2==listy[thing][0]) {
      tup = listy[thing];
    }
  }

  if (curr1 == "Currency 1" && curr2 == "Currency 2") {
    setText("c2text","You need to select currencies to convert between!");
    return "end";
  }

  if (curr1 == "Currency 1") {
    setText("c2text","You need to select which currency you inputted!");
    return "end";
  }

  if (curr2 == "Currency 2") {
    setText("c2text","You need to select a currency to convert to!");
    return "end";
  }

  var answer = getText("c1text")*tup[1];
  setText("c2text",answer);
}


//Call to Algorithm
onEvent("calculate", "click", function( ) {
	computeCurrency(getText("c1"),getText("c2"));
});
