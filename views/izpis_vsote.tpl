% rebase

% for vrstica in matrika1.polja:
{{" ".join([str(x) for x in vrstica])}}<br/>
% end
+ <br/>
% for vrstica in matrika2.polja:
{{" ".join([str(x) for x in vrstica])}}<br/>
% end
= <br/>
% for vrstica in rezultat.polja:
{{" ".join([str(x) for x in vrstica])}}<br/>
% end