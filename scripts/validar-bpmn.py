"""Conferência estrutural BPMN usando apenas a biblioteca padrão do Python."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

NS={'b':'http://www.omg.org/spec/BPMN/20100524/MODEL'}
def check(path):
    root=ET.parse(path).getroot()
    ids=[e.get('id') for e in root.iter() if e.get('id')]
    assert len(ids)==len(set(ids)), 'IDs duplicados'
    known=set(ids);owner={}
    for process in root.findall('b:process',NS):
        assert process.get('isExecutable')=='false', 'Modelo acadêmico deve ser não executável'
        for e in process.iter():
            if e.get('id'):owner[e.get('id')]=process.get('id')
    for e in root.iter():
        for attr in ('sourceRef','targetRef','processRef','messageRef','bpmnElement','attachedToRef','dataObjectRef'):
            ref=e.get(attr)
            if ref:assert ref in known, f'Referência ausente: {attr}={ref}'
        if e.tag.rsplit('}',1)[-1] in ('incoming','outgoing','flowNodeRef'):
            assert e.text in known, f'Referência ausente: {e.text}'
    for p in root.findall('.//b:participant',NS):owner[p.get('id')]=p.get('processRef')
    for f in root.findall('.//b:sequenceFlow',NS):
        assert owner[f.get('sourceRef')]==owner[f.get('targetRef')], 'Sequência cruza processos'
    for f in root.findall('.//b:messageFlow',NS):
        assert owner.get(f.get('sourceRef'))!=owner.get(f.get('targetRef')), 'Mensagem na mesma pool'

target=Path(sys.argv[1]) if len(sys.argv)>1 else Path('trabalho/fontes')
files=[target] if target.is_file() else sorted(target.rglob('*.bpmn'))
if not files:
    print('Nenhum BPMN encontrado. Gere os arquivos primeiro.');sys.exit(0)
errors=0
for p in files:
    try:check(p);print(f'OK: {p}')
    except Exception as exc:errors+=1;print(f'ERRO: {p}: {exc}')
print('Esta conferência não substitui a validação semântica nem a revisão no Camunda.')
sys.exit(1 if errors else 0)
