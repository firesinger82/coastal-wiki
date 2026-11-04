---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Create_Textures.js
lines: 100
sha256: 7e3633573acc4b6d39cd185ae3d699df6f52012e8caaf9eafa41fd32897da728
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Create_Textures.js — 판독 구간 기록

구간은 1행부터 100행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 머리말·빈 줄과 두 생성 루틴을 포함한다. 텍스처(texture)는 각각 `rgba32float`의 단일 층과 `rgba16float`의 지정 층 수를 사용한다. 저장 바인딩·양방향 복사·렌더 부착·샘플링 용도와 추적 집합 등록을 지정한다(2–25). 원문: `export function create_2D_Texture(device, width, height, allTextures) {` (2)<br>`const texture = device.createTexture({` (3)<br>`size: [width, height, 1],` (4)<br>`format: 'rgba32float',` (5)<br>`usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (6)<br>`});` (7)<br>`allTextures.add(texture);` (10)<br>`return texture;` (12)<br>`}` (13)<br>`export function create_2D_F16Texture(device, width, height, depth, allTextures) {` (15)<br>`const texture = device.createTexture({` (16)<br>`size: [width, height, depth],` (17)<br>`format: 'rgba16float',` (18)<br>`usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (19)<br>`});` (20)<br>`allTextures.add(texture);` (23)<br>`return texture;` (25)<br>`}` (26) |
| 28–53 | 2차원 및 이름상 3차원 이미지 텍스처 생성 루틴이다. 둘 다 `bgra8unorm`이고 저장 바인딩 용도는 없다. 크기의 세 번째 성분은 각각 1과 `depth`이다(28–52). 원문: `export function create_2D_Image_Texture(device, width, height, allTextures) {` (28)<br>`const texture = device.createTexture({` (29)<br>`size: [width, height, 1],` (30)<br>`format: 'bgra8unorm',` (31)<br>`usage: GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (32)<br>`});` (33)<br>`allTextures.add(texture);` (36)<br>`return texture;` (38)<br>`}` (39)<br>`export function create_3D_Image_Texture(device, width, height, depth, allTextures) {` (41)<br>`const texture = device.createTexture({` (42)<br>`size: [width, height, depth],` (43)<br>`format: 'bgra8unorm',` (44)<br>`usage: GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (45)<br>`});` (46)<br>`allTextures.add(texture);` (49)<br>`return texture;` (51)<br>`};` (52) |
| 54–80 | 3차원 데이터 텍스처는 `dimension: '3d'`와 `rgba32float`를 지정한다(54–66). 1차원 이름의 생성 루틴은 높이·층 수가 1인 크기를 지정한다(68–79). 각 결과를 추적 집합에 등록한다. 원문: `export function create_3D_Data_Texture(device, width, height, depth, allTextures) {` (54)<br>`const texture = device.createTexture({` (55)<br>`size: [width, height, depth],` (56)<br>`dimension:  '3d',` (57)<br>`format: 'rgba32float',` (58)<br>`usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (59)<br>`});` (60)<br>`allTextures.add(texture);` (63)<br>`return texture;` (65)<br>`}` (66)<br>`export function create_1D_Texture(device, width, allTextures) {` (68)<br>`const texture = device.createTexture({` (69)<br>`size: [width, 1, 1],` (70)<br>`format: 'rgba32float',` (71)<br>`usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (72)<br>`});` (73)<br>`allTextures.add(texture);` (76)<br>`return texture;` (78)<br>`}` (79) |
| 81–100 | 유니폼 버퍼(uniform buffer)는 기본 크기 256바이트와 UNIFORM·COPY_DST·COPY_SRC 용도를 사용한다(81–86). 깊이 텍스처는 `depth24plus`와 렌더 부착 용도만 사용하며 추적 집합에 등록한다(88–99). 마지막 빈 줄을 포함한다. 원문: `export function createUniformBuffer(device, bufferSize = 256) {` (81)<br>`return device.createBuffer({` (82)<br>`size: bufferSize,  // use provided size or default to 256` (83)<br>`usage: GPUBufferUsage.UNIFORM \| GPUBufferUsage.COPY_DST \| GPUBufferUsage.COPY_SRC` (84)<br>`});` (85)<br>`}` (86)<br>`export function create_Depth_Texture(device, width, height, allTextures) {` (88)<br>`const texture = device.createTexture({` (89)<br>`size   : [width, height, 1],` (90)<br>`format : 'depth24plus',` (91)<br>`usage  : GPUTextureUsage.RENDER_ATTACHMENT,` (92)<br>`});` (93)<br>`allTextures.add(texture);` (96)<br>`return texture;` (98)<br>`}` (99) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–46·54–59: `create_3D_Image_Texture`는 `dimension`을 명시하지 않는다. `create_3D_Data_Texture`는 `dimension: '3d'`를 명시한다.
- 68–73: `create_1D_Texture`는 `dimension`을 명시하지 않고 크기를 `[width, 1, 1]`로 지정한다.
