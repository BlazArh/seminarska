% rebase

<table>
% for vrstica in matrika1.polja:
<tr>
% for element in vrstica:
<td>{{str(element)}}</td>
% end
</tr>
% end 
</table>
* <br/>
<table>
% for vrstica in matrika2.polja:
<tr>
% for element in vrstica:
<td>{{str(element)}}</td>
% end
</tr>
% end 
</table>
= <br/>
<table>
% for vrstica in rezultat.polja:
<tr>
% for element in vrstica:
<td>{{str(element)}}</td>
% end
</tr>
% end 
</table>
