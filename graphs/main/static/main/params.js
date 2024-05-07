function addRow_in() {
  const div = document.createElement('div');

  div.className = 'in_div';

  const evt = document.getElementById('costil').innerHTML.split(/\r?\n/);

  var inp = `<select name="incoming" class="incoming">\n`;

  for (var index = 2; index < evt.length; index = index + 2) {
    if (index < evt.length - 1) {
      const inp_t = `<option value="` + index/2 + `">` + evt[index].slice(17, -6) + `</option>\n`;
      inp = inp + inp_t;
    }
  }
  inp = inp + `</select>\n<input type="number" placeholder="Вес" class="weight">`;
  
  div.innerHTML = inp;

  document.getElementById('all_in_div_in').appendChild(div);
}

function addRow_out() {
  const div = document.createElement('div');

  div.className = 'in_div';

  const evt = document.getElementById('costil').innerHTML.split(/\r?\n/);

  var inp = `<select name="outgoing" class="outgoing">\n`;

  for (var index = 2; index < evt.length; index = index + 2) {
    if (index < evt.length - 1) {
      const inp_t = `<option value="` + index/2 + `">` + evt[index].slice(17, -6) + `</option>\n`;
      inp = inp + inp_t;
    }
  }
  inp = inp + `</select>\n<input type="number" placeholder="Вес" class="weight">`;
  
  div.innerHTML = inp;

  document.getElementById('all_in_div_out').appendChild(div);
}
