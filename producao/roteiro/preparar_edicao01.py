from pathlib import Path
import json,re
from pypdf import PdfReader
root=Path(__file__).resolve().parents[2]
out=root/'edicoes/Edicao_01'
reader=PdfReader(root/'producao/referencias/A_Farinha_Esquecida_V17_Celular.pdf')
paras=[]
for page in reader.pages[4:9]:
    for line in page.extract_text().splitlines():
        if not line.strip() or line.strip().isdigit() or line.startswith('Capítulo I'): continue
        if line.startswith(' ') or line.startswith('—') or not paras: paras.append(line.strip())
        else: paras[-1]+=' '+line.strip()
text='\n\n'.join(paras)
starts={2:'Quando Miguel era menino',3:'A casa ficava levantada',4:'— Já acordado, menino?',5:'Quando ajudava na farinha',6:'Uma vez perguntou',7:'Mas os adultos falavam',8:'Miguel não sabia o que queria',9:'— Cidade grande tem muita luz',10:'Nos dias que antecederam',11:'Miguel encontrou Jesuína',12:'Miguel se acalmou imediatamente',16:'Na manhã da partida',18:'Miguel olhou para trás.',19:'Jesuína estava no pequeno',20:'Ao lado dela, Dona Luzia',21:'Jesuína não acenava',23:'Miguel não sabia ainda'}
positions=[(page,text.index(marker)) for page,marker in starts.items()]
assert [p for _,p in positions]==sorted(p for _,p in positions)
pages={i:'' for i in range(1,25)}
for idx,(page,pos) in enumerate(positions):
    end=positions[idx+1][1] if idx+1<len(positions) else len(text)
    pages[page]=text[pos:end].strip()
assert re.sub(r'\s+',' ',' '.join(pages.values())).strip()==re.sub(r'\s+',' ',text).strip()
for page,txt in pages.items(): (out/f'Pagina_{page:02}/texto.txt').write_text(txt,encoding='utf-8')
(root/'producao/roteiro/capitulo_01_integral.txt').write_text(text,encoding='utf-8')
(out/'texto_paginado.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((out/'manifesto_producao.json').read_text(encoding='utf-8'))
for asset in manifest['assets']:
    p,a=asset['page'],asset['asset']
    brief=f"# E01-P{p:02}-A{a:02}\n\nFonte: V17, capítulo I; MAPA_EDITORIAL.md e memoria.md.\n\n"
    brief+=f"Proporção: {asset.get('ratio','2:3')}.\nPersonagens/fases: {asset.get('characters','M')} conforme referências do manifesto.\n\n## Prompt final\n\n{asset['prompt']}\n\n## Auditoria\n\nConferir rosto/fase, anatomia, cenário, ação, ausência de texto e margem de reenquadramento.\n"
    (out/f'Pagina_{p:02}'/f'ficha_A{a:02}.md').write_text(brief,encoding='utf-8')
print('24 páginas de texto; capítulo integral conferido; 27 fichas de assets.')
