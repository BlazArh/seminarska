% rebase('base.tpl', naslov='Kalkulator matrik')


<img src="https://raw.githubusercontent.com/BlazArh/seminarska/main/views/matrika.jpg" alt="Dostava hrane" width=400>
<br> 
<form action="/vsota" method="get">
    <button type="submit">Seštej matriki</button>
</form>
<form action="/razlika" method="get">
    <button type="submit">Odštej matriki</button>
</form>
<form action="/produkt" method="get">
    <button type="submit">Zmnoži matriki</button>
</form>
<form action="/sled" method="get">
    <button type="submit">Izračunaj sled matrike</button>
</form>

