% rebase('base.tpl')
sled od matrike 
<table>
% for vrstica in matrika1.polja:
<tr>
% for element in vrstica:
<td>{{str(element)}}</td>
% end
</tr>
% end 
</table>
= 
{{rezultat}}
<br/>
<br/>
<br/>
<form action="/" method="get">
    <button type="submit">Uvodna stran</button>
</form>
