#!/usr/bin/env python3
"""Visual read of chart, DFP2025 PDF physical p106, printed p105, unit R$ thousand."""
import csv,json,pathlib
root=pathlib.Path(__file__).resolve().parent.parent;o=root/'analises';o.mkdir(exist_ok=True)
vals=[('2026',645762,1292578,1938340),('2027',465833,1247735,1713568),('2028',500916,1284954,1785870),('2029',529754,2123343,2653097),('2030',462833,1755190,2218023),('2031',443724,1862477,2306201),('2032+',3136883,8769271,11906154)]
assert all(a+b==t for _,a,b,t in vals)
with (o/'NOTA15B_PERFIL_VENCIMENTO_DFP_2025.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['ano','agencia_fomento_RSmil','debentures_RSmil','total_RSmil','pagina_fisica_pdf','pagina_impressa','inclui_juros_projetados']);
 for year,a,b,t in vals:w.writerow([year,a,b,t,106,105,'SIM'])
total=sum(t for *_,t in vals)
rep={'fonte':'DFP 2025 Nota 15(b), gráfico no PDF físico p.106, impresso p.105','natureza':'RP transcrição manual verificada aritmeticamente dos rótulos do gráfico','soma_fluxos_RSmil':total,'2032_mais_RSmil':vals[-1][-1],'pct_2032_mais':round(100*vals[-1][-1]/total,2),'2026_RSmil':vals[0][-1],'nota_importante':'O gráfico inclui amortização e PROJEÇÃO DE JUROS; não equivale ao saldo contábil do passivo.','conferencias':{'soma_cada_barra':True,'total_anuais_7':len(vals)}}
(o/'NOTA15B_ANALISE.json').write_text(json.dumps(rep,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');print(rep)
