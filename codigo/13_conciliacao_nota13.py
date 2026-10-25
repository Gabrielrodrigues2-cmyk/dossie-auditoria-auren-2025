import json
from pathlib import Path
O=Path(__file__).resolve().parents[1]/'resultados';O.mkdir(exist_ok=True)
# Valores transcritos da DFP 2025, Nota 13(a), página impressa 95 de 157, em R$ mil.
movimentos=[('Saldo inicial',26183375),('Adições',1015698),('Substituição itens garantia',1011),('Remensuração desmobilização',-26894),('Baixas',-49448),('Depreciação',-1354365),('Amortização ajuste valor justo',-52204),('Empresa incorporada',699),('Transferência ativos indenização',-11245),('Transferência contas a receber',-6082),('Transferências',-270298)]
final=sum(v for _,v in movimentos)
assert final==25430247,(final,25430247)
componentes={'Custo bruto':42273221,'Depreciação acumulada':-17822049,'Ajuste valor justo PPA':1230019,'Amortização acumulada do ajuste valor justo':-250944}
assert sum(componentes.values())==25430247
assert final+140111==25570358
report={'fonte':'DFP Auren Energia S.A. 31/12/2025, Nota 13(a), pagina impressa 95 de 157; balanço consolidado, conferir página física e impressa no PDF local', 'unidade':'R$ mil','movimentacao':dict(movimentos),'saldo_final_imobilizado_operacao':final,'componentes_publicados':componentes,'soma_componentes':sum(componentes.values()),'direito_uso_balanco':140111,'saldo_total_balanco':final+140111,'comparacao_base_sintetica':{'saldo_liquido_calibrado_rs_mil':25570358,'observacao':'A base V2 concilia SOMENTE saldo líquido, com custos e depreciações hipotéticos diferentes dos componentes da Nota 13(a). Não representa cadastro real.'},'alerta':'Conciliação RP dos saldos publicados não constitui validação independente de ativos individuais.'}
(O/'conciliacao_nota13_2025.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print('Saldo nota 13(a):',final,'R$ mil; + direito de uso:',final+140111,'R$ mil; diferença:',final+140111-25570358)
