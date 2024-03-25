function addRow_in() {
  const div = document.createElement('div');

  div.className = 'in_div';

  const inp = `
    <select name="incoming" class="incoming">
      {% for el in count %}
        <option value="{{ el.num }}">{{ el.name }}</option>
      {% endfor %}
    </select>
    <input type="number" placeholder="Вес" class="weight">
  `;

  div.innerHTML = inp;

  document.getElementById('all_in_div_in').appendChild(div);
}

function addRow_out() {
  const div = document.createElement('div');

  div.className = 'in_div';

  div.innerHTML = `
    <select name="outgoing" class="outgoing">
      {% for el in count %}
        <option value="{{ el.num }}">{{ el.name }}</option>
      {% endfor %}
    </select>
    <input type="number" placeholder="Вес" class="weight">
  `;

  document.getElementById('all_in_div_out').appendChild(div);
}
