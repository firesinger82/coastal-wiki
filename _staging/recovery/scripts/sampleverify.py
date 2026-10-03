# Sonnet sample-verification prompt for a Codex re-read segment (usage: python3 sampleverify.py N IMGDIR [k])
import json, os, random, sys
j = json.load(open('_staging/recovery/scripts/pdfjobs.json'))[int(sys.argv[1]) - 1]
imgdir = sys.argv[2]; k = int(sys.argv[3]) if len(sys.argv) > 3 else 3
base = os.path.splitext(os.path.basename(j['path']))[0]
key = {'XBeach_manual_kingsday': ('kingsday', 3), 'XBeach_manual_master': ('master', 3), 'Parallellization_report': ('parallel', 2),
       'curvilinear grid properties': ('curvilinear', 2), 'adapted_front_0': ('adapted', 1)}[base]
random.seed(f"{j['out']}-10-03")
pages = sorted(random.sample(range(j['a'], j['b'] + 1), min(k, j['b'] - j['a'] + 1)))
imgs = '\n'.join(f'- {p}쪽: {imgdir}/{key[0]}-{p:0{key[1]}d}.png' for p in pages)
print(f"""너는 판독 기록 검증자다(작업 디렉터리 /home/firesinger/coastal-wiki). 읽기 전용: 어떤 파일도 만들거나 고치지 않고 git을 쓰지 않는다.

기록: {j['out']} (Codex가 쪽 이미지를 보고 재판독한 기록)
검증할 쪽과 300 dpi 쪽 이미지(Read 도구로 연다):
{imgs}

각 쪽의 기록 행(`| p.N ... |`)을 이미지와 대조한다: 수식 LaTeX(첨자·분자/분모·부호·식 번호)가 인쇄와 같은지, 매개변수 이름·기본값·범위, 적용 조건, 한국어 설명이 원문과 반대·과장·누락이 없는지, 원문 오기를 임의로 고치지 않았는지. 작은 글자는 이미지를 확대해 본다.

보고(한국어, 한 문장에 한 사실, 250단어 이내): 쪽마다 판정(맞음 / 틀림 + 무엇이 어떻게 다른지, 원문 인쇄 그대로 인용), 마지막에 틀린 곳 수.""")
