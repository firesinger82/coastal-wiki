---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/wrksize.f
lines: 61
sha256: cc858e514bbc9aa756ff3b1376d4e8569209e4cca64ecaec6727a737ece40c45
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wrksize.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | WRKSIZE는 접촉 의존 관계를 따라 작업 배열 크기를 센다. IP,IP0의 크기는 4096이고 JP는 4이다(4–6). ISLVG를 0으로 채운 뒤 INDC 위치에 ISLV를 복사한다(8–10). NS,NM을 0으로 초기화한다(12–13). 원문: 연속문(1–2): `      SUBROUTINE WRKSIZE(NSIZ1,NSIZ2,NSIZ3,ISLVG,NS,NM,NNOD,NINDC,INDC` (1); `     &                  ,IEDG,IELC,IELQ,IFCQ,IEDQ,IVRQ,ISLV)` (2). 연속문(4–6): `      DIMENSION ISLVG(2,NNOD),ISLV(2,NINDC),INDC(NINDC),IEDG(6,*)` (4); `     &         ,IELC(3,*),IELQ(4,*),IVRQ(*),IEDQ(*),IFCQ(*),JP(4)` (5); `     &         ,IP(4096),IP0(4096),NS(NINDC),NM(NINDC)` (6). `      ISLVG(:,:) = 0` (8). `      ISLVG(:,INDC(:)) = ISLV(:,:)` (10). `      NS(:) = 0` (12). `      NM(:) = 0` (13). |
| 15–42 | 시작 시 1–2행 WRKSIZE 루틴 안. 각 접촉의 INDC를 첫 IP에 넣고 종료 조건 없는 DO를 연다(15–21). 현재 절점 목록 중 IST=0인 항은 건너뛴다(25–32). 나머지는 NS를 증가시키고 MSTNOD로 얻은 주절점(master node) 목록을 IP0에 이어 붙인다(34–41). 원문: `      DO I = 1, NINDC` (15). `        N = 1` (17). `        IP(1) = INDC(I)` (19). `        DO` (21). `          N0 = 0` (23). `          DO J = 1, N` (25). `            JG = IP(J)` (27). `            IST = ISLVG(1,JG)` (29). `            MA = ISLVG(2,JG)` (30). `            IF( IST == 0 ) CYCLE` (32). `            NS(I) = NS(I) + 1` (34). `            CALL MSTNOD(M,JP,IST,MA,IELC,IEDG,IELQ,IFCQ,IEDQ,IVRQ)` (36). `            IP0(N0+1:N0+M) = JP(1:M)` (38). `            N0 = N0 + M` (39). `          ENDDO` (41). |
| 43–61 | 시작 시 1–2행 WRKSIZE 루틴·15행 `DO I = 1, NINDC`와 21행 `DO` 안이며 25행 J 루프 밖. 21행 DO는 53행 `ENDDO`에서 닫힌다. 15행 I 루프는 55행 `ENDDO`에서 닫힌다. N0=0이면 반복을 끝낸다(43). 그 밖에는 다음 목록을 IP에 복사하고 NM을 초기 보정한 뒤 N을 누적한다(45–51). 두 루프 종료 후 SUM(NS),SUM(NM),MAXVAL(NM)으로 NSIZ1,NSIZ2,NSIZ3을 계산한다(53–59). END를 포함한다. 원문: `          IF( N0 == 0 ) EXIT` (43). `          N = N0` (45). `          IP(1:N) = IP0(1:N0)` (47). `          IF( NM(I) == 0 ) NM(I) = 1` (49). `          NM(I) = NM(I) + N` (51). `        ENDDO` (53). `      ENDDO` (55). `      NSIZ1 = SUM(NS) * 9` (57). `      NSIZ2 = SUM(NM) * 9` (58). `      NSIZ3 = MAXVAL(NM) * 3 * 24` (59). `      END` (61). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·38–47: IP,IP0의 크기는 4096이며 N0+M이나 N과 4096의 비교는 없다.
- 21–53: 반복 상한과 방문 절점 중복 검사가 없으며 EXIT 조건은 N0=0이다.
- 57–59: 크기 산식 계수는 9 및 3*24로 고정되어 있다.
