---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Create_Textures.js
lines: 100
sha256: a4820fda52518e131241cfc9bcf0cbfb57a989910d4b989fa3f6b44fbeef92b2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Create_Textures.js — 판독 구간 기록

구간은 1행부터 100행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 식별 주석과 `create_2D_Texture`는 폭·높이·1 크기의 rgba32float 텍스처(texture)를 만든다(2–7). 저장 바인딩·양방향 복사·렌더 부착·텍스처 바인딩 용도를 합치고 추적 집합에 추가하여 반환한다(6–12). 원문: `export function create_2D_Texture(device, width, height, allTextures) {` (2); `const texture = device.createTexture({` (3); `size: [width, height, 1],` (4); `format: 'rgba32float',` (5); `usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (6); `});` (7); `allTextures.add(texture);` (10); `return texture;` (12); `}` (13) |
| 15–27 | `create_2D_F16Texture`는 크기 세 번째 인수에 depth를 받고 형식을 rgba16float로 정한다(15–20). 나머지 용도 플래그·추적·반환은 앞 루틴과 같다(19–25). 원문: `export function create_2D_F16Texture(device, width, height, depth, allTextures) {` (15); `const texture = device.createTexture({` (16); `size: [width, height, depth],` (17); `format: 'rgba16float',` (18); `usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (19); `});` (20); `allTextures.add(texture);` (23); `return texture;` (25); `}` (26) |
| 28–40 | `create_2D_Image_Texture`는 폭·높이·1, bgra8unorm 텍스처를 만든다(28–33). 저장 바인딩 플래그 없이 복사·렌더·표본화 용도를 사용하고 추적 후 반환한다(32–38). 원문: `export function create_2D_Image_Texture(device, width, height, allTextures) {` (28); `const texture = device.createTexture({` (29); `size: [width, height, 1],` (30); `format: 'bgra8unorm',` (31); `usage: GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (32); `});` (33); `allTextures.add(texture);` (36); `return texture;` (38); `}` (39) |
| 41–53 | `create_3D_Image_Texture`는 폭·높이·depth 및 bgra8unorm을 사용한다(41–46). 이 생성 객체는 dimension 필드를 명시하지 않는다. 추적 집합에 추가하고 반환한다(49–52). 원문: `export function create_3D_Image_Texture(device, width, height, depth, allTextures) {` (41); `const texture = device.createTexture({` (42); `size: [width, height, depth],` (43); `format: 'bgra8unorm',` (44); `usage: GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (45); `});` (46); `allTextures.add(texture);` (49); `return texture;` (51); `};` (52) |
| 54–67 | `create_3D_Data_Texture`는 폭·높이·depth, `dimension:  '3d'`, rgba32float 및 저장·복사·렌더·표본화 용도를 명시한다(54–60). 추적 후 반환한다(63–65). 원문: `export function create_3D_Data_Texture(device, width, height, depth, allTextures) {` (54); `const texture = device.createTexture({` (55); `size: [width, height, depth],` (56); `dimension:  '3d',` (57); `format: 'rgba32float',` (58); `usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (59); `});` (60); `allTextures.add(texture);` (63); `return texture;` (65); `}` (66) |
| 68–80 | `create_1D_Texture`는 크기 [width,1,1], rgba32float 및 다섯 용도 플래그를 사용한다(68–73). dimension은 명시하지 않는다. 추적 후 반환한다(76–78). 원문: `export function create_1D_Texture(device, width, allTextures) {` (68); `const texture = device.createTexture({` (69); `size: [width, 1, 1],` (70); `format: 'rgba32float',` (71); `usage: GPUTextureUsage.STORAGE_BINDING \| GPUTextureUsage.COPY_SRC \| GPUTextureUsage.COPY_DST \| GPUTextureUsage.RENDER_ATTACHMENT \| GPUTextureUsage.TEXTURE_BINDING` (72); `});` (73); `allTextures.add(texture);` (76); `return texture;` (78); `}` (79) |
| 81–87 | `createUniformBuffer`는 기본 크기 256인 유니폼 버퍼(uniform buffer)를 만든다(81–85). UNIFORM과 양방향 복사 용도를 합친다(84). 원문: `export function createUniformBuffer(device, bufferSize = 256) {` (81); `return device.createBuffer({` (82); `size: bufferSize,  // use provided size or default to 256` (83); `usage: GPUBufferUsage.UNIFORM \| GPUBufferUsage.COPY_DST \| GPUBufferUsage.COPY_SRC` (84); `});` (85); `}` (86) |
| 88–100 | `create_Depth_Texture`는 폭·높이·1의 depth24plus 텍스처를 렌더 부착 용도로 만들고 추적하여 반환한다(88–99). 끝 빈 줄을 포함한다(100). 원문: `export function create_Depth_Texture(device, width, height, allTextures) {` (88); `const texture = device.createTexture({` (89); `size   : [width, height, 1],` (90); `format : 'depth24plus',` (91); `usage  : GPUTextureUsage.RENDER_ATTACHMENT,` (92); `});` (93); `allTextures.add(texture);` (96); `return texture;` (98); `}` (99) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–60: create_3D_Image_Texture는 dimension을 지정하지 않는다. create_3D_Data_Texture는 dimension을 '3d'로 지정한다.
- 68–73: create_1D_Texture는 size를 [width,1,1]로 지정하지만 dimension 필드는 지정하지 않는다.
