% rebase('base.tpl')
<br/>
<br/>
<br/>

<table>
% for vrstica in matrika1.polja:
<tr>
% for element in vrstica:
<td>{{str(element)}}</td>
% end
</tr>
% end 
</table>
TRANSPONIRANKA => <br/>
<table>
% for vrstica in rezultat.polja:
<tr>
% for element in vrstica:
<td>{{str(element)}}</td>
% end
</tr>
% end 
</table>

<br/>
<br/>
<br/>
<form action="/" method="get">
    <button type="submit">Uvodna stran</button>
</form>
