# SWAN Phase 1 semantic review

## Summary

Compared pinned `5544152` with `43e9bbba393f2cf9eaff78bc92eaed118a3a5c8e` in the supplied snapshot. Read the task contract first, the complete changed-file diff (with an additional whitespace-insensitive comparison for the heavily reindented computation file), the three affected notes in context, and the relevant new source. No wiki text revisions are proposed.

| Verdict | Count |
|---|---:|
| UPDATE_REQUIRED | 0 |
| REVIEW_ONLY | 16 |
| NO_ACTION | 0 |
| UNRESOLVED | 0 |

These are claim-level verdicts, not a finding that the source changes are behaviorally neutral. The deleted thread partitioner is replaced by wavefront scheduling with a different internal contract. The 16 cited statements do not promise preservation of that partitioner, exact thread assignment or flat traversal order. In particular, the direction-aligned list construction and the abstract sweep/ordered-vertex description remain true.

All new coordinates refer to the checked-in `.ftn`/`.ftn90` files at `43e9bbb`, not generated Fortran. Old coordinates refer to `5544152`. Broad citations were interpreted using the note's specific supported claims; the task file's stricter threshold of span > 60 was used. CSV `wiki_claim` contains the complete original note line read from disk, including the untruncated line 68. `proposed_classification` and `verdict` deliberately contain the same value to satisfy both requested schemas. Empty `reason_type` means no UPDATE_REQUIRED reason applies.

A direct comparison of `src/SwanCompUnstruc.ftn90` old lines 854-1329 against new lines 851-1326 found identical text after normalizing whitespace. This covers the active-vertex body, physical calls, obstacle mapping and solver dispatch; it does not cover the changed enclosing scheduler. Individual failed mappings for S1-1, S1-3 through S1-8, and S1-10 were also verified against matching old/new text. S1-12 is REVIEW_ONLY because its broad span overlaps a changed diagnostic guard; its coordinates already remain correct.

## Candidate verdicts

### S1-1 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:64`. Supported claim: SwanPropvelX is called from the unstructured computation loop.

The same SwanPropvelX call and arguments remain inside the active-vertex/cell calculation. The old line 918 reanchors to 915; adding the surrounding front loop does not remove or redirect this call. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:918-918`. New evidence: `src/SwanCompUnstruc.ftn90:915`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:915 — call SwanPropvelX ( cax, cay, compda(1,JVX2), compda(1,JVY2), cgo, spcdir(1,2), spcdir(1,3) )`

### S1-2 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:68`. Supported claim: Direction-ordered unstructured sweeps and per-cell intersection checks, rather than a hard-coded structured four-quadrant traversal.

The supported claim is the direction-based ordering and cell/sweep intersection test. Both remain: sweeps consume direction-derived flist or vlist and retain the same angular rejection test. The new intermediate wavefront loop changes scheduling, but the note does not specify the removed per-thread bounds algorithm. The existing nsweep-or-one selection is also retained; no new four-quadrant restriction appears. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:829-979`. New evidence: `src/SwanCompUnstruc.ftn90:825-851; src/SwanCompUnstruc.ftn90:877-893; src/SwanCompUnstruc.ftn90:947-975; src/SwanVertlist.ftn90:180-217; src/SwanVertlist.ftn90:235-295; src/SwanVertlist.ftn90:363-373`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:826 — n = nsweep`
- `src/SwanCompUnstruc.ftn90:830 — n = 1`
- `src/SwanCompUnstruc.ftn90:835 — sweeploop: do swpdir = 1, n`
- `src/SwanCompUnstruc.ftn90:839 — !GRAPH          frontloop: do ifront = 1, nfront(swpdir)`
- `src/SwanCompUnstruc.ftn90:844 — !$omp do schedule(static)`
- `src/SwanCompUnstruc.ftn90:848 — !GRAPH                ivert = flist(kvert,swpdir)`
- `src/SwanCompUnstruc.ftn90:849 — !FXFRO                ivert = vlist(kvert,swpdir)`
- `src/SwanCompUnstruc.ftn90:974 — if ( ( thmin < th1 .and. thmax < th1 ) .or. &`
- `src/SwanCompUnstruc.ftn90:975 — ( thmin > th2 .and. thmax > th2 )      ) cycle celloop`
- `src/SwanVertlist.ftn90:185 — dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)`
- `src/SwanVertlist.ftn90:365 — !GRAPH          k = vlist(j,swpdir)`
- `src/SwanVertlist.ftn90:371 — !GRAPH          flist(l,swpdir) = k`

### S1-3 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:68`. Supported claim: SwanSweepSel selects active spectral bins for the sweep.

The SwanSweepSel call, its bin-bound arguments and the following idtot > 0 gate are unchanged apart from indentation and coordinates. Old 983-987 maps to 980-984. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:983-987`. New evidence: `src/SwanCompUnstruc.ftn90:980-986`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:980 — call SwanSweepSel ( idcmin, idcmax, anybin, iscmin, iscmax, &`
- `src/SwanCompUnstruc.ftn90:981 — iddlow, iddtop, idtot , isslow, isstop, &`
- `src/SwanCompUnstruc.ftn90:982 — istot , cax   , cay   , rdx   , rdy   , &`
- `src/SwanCompUnstruc.ftn90:983 — spcsig)`
- `src/SwanCompUnstruc.ftn90:986 — if ( idtot > 0 ) then`

### S1-4 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:68`. Supported claim: SwanPropvelS supplies spectral propagation velocities for the considered sweep.

The same SwanPropvelS call remains under idtot > 0 with the same cad/cas outputs, directional bounds and gradient arguments. Old 994-1000 maps to 991-997. The separate change to OpenMP-private current gradients does not falsify this call/role claim. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:994-1000`. New evidence: `src/SwanCompUnstruc.ftn90:986-997`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:988 — ! compute propagation velocities in spectral space for the considered sweep in present vertex`
- `src/SwanCompUnstruc.ftn90:991 — call SwanPropvelS ( cad             , cas           , compda(1,JVX2), compda(1,JVY2), &`
- `src/SwanCompUnstruc.ftn90:993 — kwave           , cgo           , spcsig        , iddlow        , &`
- `src/SwanCompUnstruc.ftn90:994 — iddtop          , spcdir(1,2)   , spcdir(1,3)   , spcdir(1,4)   , &`
- `src/SwanCompUnstruc.ftn90:996 — dhdx            , dhdy          , dkdx          , dkdy          , &`
- `src/SwanCompUnstruc.ftn90:997 — duxdx           , duxdy         , duydx         , duydy         )`

### S1-5 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:72`. Supported claim: The solver directly divides when refraction and frequency shift are both disabled.

The IREFR == 0 and ITFRE == 0 branch, protected denominator and rhs/rval2 update are unchanged. Old 1206-1228 maps exactly to 1203-1225 after whitespace normalization. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:1206-1228`. New evidence: `src/SwanCompUnstruc.ftn90:1203-1225`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:1203 — if ( IREFR == 0 .and. ITFRE == 0 ) then`
- `src/SwanCompUnstruc.ftn90:1213 — if ( abs(rval1) > 1.e-20 ) then`
- `src/SwanCompUnstruc.ftn90:1216 — rval2 = sign(1.e-20,rval1)`
- `src/SwanCompUnstruc.ftn90:1218 — ac2(id,is,ivert) = rhs(id,is) / rval2`

### S1-6 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:73`. Supported claim: SOLMAT is the Thomas tridiagonal solver call.

The branch still explicitly describes Thomas' algorithm for a tridiagonal system and invokes SOLMAT with the same arguments. Old call 1237-1238 maps to 1234-1235. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:1237-1238`. New evidence: `src/SwanCompUnstruc.ftn90:1228-1235`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:1228 — elseif ( .not.DYNDEP .and. ICUR == 0 .or. int(PNUMS(8)) == 0 ) then`
- `src/SwanCompUnstruc.ftn90:1231 — ! solve tridiagonal system of equations using Thomas' algorithm`
- `src/SwanCompUnstruc.ftn90:1234 — call SOLMAT ( idcmin     , idcmax     , ac2        , rhs, &`
- `src/SwanCompUnstruc.ftn90:1235 — amat(1,1,1), amat(1,1,5), amat(1,1,4)     )`

### S1-7 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:74`. Supported claim: SWSIP handles the pentadiagonal system for implicit sigma propagation.

The PNUMS(8) == 1 branch, implicit-sigma/SIP description and SWSIP arguments are preserved. Old call 1251-1255 maps to 1248-1252. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:1251-1255`. New evidence: `src/SwanCompUnstruc.ftn90:1242-1252`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:1242 — if ( int(PNUMS(8)) == 1 ) then`
- `src/SwanCompUnstruc.ftn90:1244 — ! implicit scheme in sigma space`
- `src/SwanCompUnstruc.ftn90:1245 — ! solve pentadiagonal system of equations using SIP solver`
- `src/SwanCompUnstruc.ftn90:1248 — call SWSIP ( ac2        , amat(1,1,1)    , rhs            , amat(1,1,4), &`
- `src/SwanCompUnstruc.ftn90:1249 — amat(1,1,5), amat(1,1,2)    , amat(1,1,3)    , ac2old     , &`

### S1-8 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md:75`. Supported claim: SOLMT1 handles the tridiagonal system for explicit sigma propagation.

The PNUMS(8) == 2 branch still describes explicit sigma and a Thomas tridiagonal solve, with the same SOLMT1 arguments. Old call 1264-1266 maps to 1261-1263. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:1264-1266`. New evidence: `src/SwanCompUnstruc.ftn90:1255-1263`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:1255 — elseif (int(PNUMS(8)) == 2 ) then`
- `src/SwanCompUnstruc.ftn90:1257 — ! explicit scheme in sigma space`
- `src/SwanCompUnstruc.ftn90:1258 — ! solve tridiagonal system of equations using Thomas' algorithm`
- `src/SwanCompUnstruc.ftn90:1261 — call SOLMT1  ( idcmin     , idcmax     , ac2        , rhs    , &`
- `src/SwanCompUnstruc.ftn90:1262 — amat(1,1,1), amat(1,1,5), amat(1,1,4),          &`
- `src/SwanCompUnstruc.ftn90:1263 — isstop     , anyblk     , iddlow     , iddtop )`

### S1-9 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-diffraction-obstacles.md:23`. Supported claim: The broad source-basis entry supports the note's unstructured obstacle-link mapping and diffraction-to-transport path (sections F and G).

Read in note context, the broad entry supports face-crossing obstacle treatment and diffraction-modified transport, not a particular OpenMP partition scheme. The cross-to-link mapping, SWTRCF call, diffraction calculation and velocity-to-SwanTranspAc dataflow all remain. Focused anchors include the complete transport call, which extended beyond the old broad citation's endpoint. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:780-1080`. New evidence: `src/SwanCompUnstruc.ftn90:779; src/SwanCompUnstruc.ftn90:915; src/SwanCompUnstruc.ftn90:991-997; src/SwanCompUnstruc.ftn90:1036-1085; src/SwanPropvelX.ftn90:94-101; src/SwanPropvelS.ftn90:266-271`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:779 — if ( IDIFFR /= 0 ) call SwanDiffPar ( ac2, compda(1,JDP2), spcsig )`
- `src/SwanCompUnstruc.ftn90:1052 — link(1) = cross(iface)`
- `src/SwanCompUnstruc.ftn90:1057 — link(2) = cross(iface)`
- `src/SwanCompUnstruc.ftn90:1067 — call SWTRCF ( compda(1,JDP2), compda(1,JWLV2), compda(1,JHS)  , link, obredf    , ac2, reflso, dummy ,         &`
- `src/SwanCompUnstruc.ftn90:1080 — call SwanTranspAc ( amat  , rhs   , leakcf, ac2   , ac1   , &`
- `src/SwanCompUnstruc.ftn90:1081 — cgo   , cax   , cay   , cad   , cas   , &`
- `src/SwanPropvelX.ftn90:97 — cax(id,is,ic) = cax(id,is,ic)*DIFPARAM(ivert)`
- `src/SwanPropvelS.ftn90:270 — if ( IDIFFR /= 0 ) cad(id,is) = cad(id,is)*DIFPARAM(iv1) - DIFPARDX(iv1)*cgo(is,1)*esin(id) + DIFPARDY(iv1)*cgo(is,1)*ecos(id)`

### S1-10 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-diffraction-obstacles.md:107`. Supported claim: Crossed faces are mapped to two local stencil links and passed to SWTRCF.

The two endpoint tests still assign cross(iface) to link(1) and link(2); a nonzero link still triggers SWTRCF with link as an argument. Old 1039-1080 maps exactly to 1036-1077 after whitespace normalization. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:1039-1080`. New evidence: `src/SwanCompUnstruc.ftn90:1036-1077`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:1047 — if ( vb==ivert .or. ve==ivert ) then`
- `src/SwanCompUnstruc.ftn90:1049 — if ( vb==vu(1) .or. ve==vu(1) ) then`
- `src/SwanCompUnstruc.ftn90:1052 — link(1) = cross(iface)`
- `src/SwanCompUnstruc.ftn90:1054 — elseif ( vb==vu(2) .or. ve==vu(2) ) then`
- `src/SwanCompUnstruc.ftn90:1057 — link(2) = cross(iface)`
- `src/SwanCompUnstruc.ftn90:1065 — if ( link(1)/=0 .or. link(2)/=0 ) then`
- `src/SwanCompUnstruc.ftn90:1067 — call SWTRCF ( compda(1,JDP2), compda(1,JWLV2), compda(1,JHS)  , link, obredf    , ac2, reflso, dummy ,         &`

### S1-11 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-diffraction-obstacles.md:123`. Supported claim: Diffraction-modified propagation velocities are used by SwanTranspAc.

The specific broad-span claim is the velocity dataflow. SwanDiffPar precedes the propagation calls; SwanPropvelX scales cax/cay when its diffraction gate permits, SwanPropvelS adjusts cad, and those arrays are passed to SwanTranspAc. The relevant code is unchanged; the focused new anchor includes the full transport call. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:780-1080`. New evidence: `src/SwanCompUnstruc.ftn90:779; src/SwanCompUnstruc.ftn90:915; src/SwanCompUnstruc.ftn90:991-997; src/SwanCompUnstruc.ftn90:1080-1085; src/SwanPropvelX.ftn90:94-101; src/SwanPropvelS.ftn90:266-271; src/SwanTranspAc.ftn90:80-83`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:779 — if ( IDIFFR /= 0 ) call SwanDiffPar ( ac2, compda(1,JDP2), spcsig )`
- `src/SwanPropvelX.ftn90:94 — if ( IDIFFR /= 0 .and. PDIFFR(3) /= 0. ) then`
- `src/SwanPropvelX.ftn90:97 — cax(id,is,ic) = cax(id,is,ic)*DIFPARAM(ivert)`
- `src/SwanPropvelX.ftn90:98 — cay(id,is,ic) = cay(id,is,ic)*DIFPARAM(ivert)`
- `src/SwanPropvelS.ftn90:270 — if ( IDIFFR /= 0 ) cad(id,is) = cad(id,is)*DIFPARAM(iv1) - DIFPARDX(iv1)*cgo(is,1)*esin(id) + DIFPARDY(iv1)*cgo(is,1)*ecos(id)`
- `src/SwanCompUnstruc.ftn90:1080 — call SwanTranspAc ( amat  , rhs   , leakcf, ac2   , ac1   , &`
- `src/SwanCompUnstruc.ftn90:1081 — cgo   , cax   , cay   , cad   , cas   , &`
- `src/SwanTranspAc.ftn90:80 — real, dimension(MDC,MSC), intent(in)        :: cad    ! wave transport velocity in theta-direction`

### S1-12 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:21`. Supported claim: Structured sweep order, accuracy tests and STRSXY/SACCUR/SWSTPC references.

The only diff in this file adds ITEST >= 10 to the thread-count diagnostic WRITE guard at 1192. The structured sweep, solver dispatch and convergence claims are unaffected. All three citation ranges remain numerically unchanged. REVIEW_ONLY records the reviewed hunk overlap under the task's rule; no coordinate change is needed for this row. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/swancom1.ftn:724-2356; src/swancom1.ftn:5393-5411; src/swancom1.ftn:9618-9928`. New evidence: `src/swancom1.ftn:724-2356; src/swancom1.ftn:5393-5411; src/swancom1.ftn:9618-9928`.

Exact new-source evidence:

- `src/swancom1.ftn:724 — !     The numerical procedure in SWAN is based on the four-direction`
- `src/swancom1.ftn:1192 — !$    IF ( IT.EQ.1.AND.ITEST.GE.10 )                                      43.05 41.10`
- `src/swancom1.ftn:1194 — !$   +      ' Number of threads during execution of parallel region = ',  41.10 40.22`
- `src/swancom1.ftn:2271 — CALL SACCUR (COMPDA(1,JDP2),KGRPNT          ,                  40.30`
- `src/swancom1.ftn:2278 — CALL SWSTPC ( HSAC0         ,HSAC1           ,HSAC2 ,          40.41`
- `src/swancom1.ftn:2352 — IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.                       40.41`
- `src/swancom1.ftn:2353 — &                                      ACCUR.GE.PNUMS(4) ) GOTO 470  40.41`
- `src/swancom1.ftn:5406 — CALL STRSXY(ISSTOP   ,IDCMIN   ,IDCMAX   ,CAX      ,             40.00`
- `src/swancom1.ftn:9620 — !     Check convergence based on the relative, absolute`
- `src/swancom1.ftn:9621 — !     and curvature values of wave height and period`
- `src/swancom1.ftn:9928 — ACCUR  = CEILING(REAL(IACCUR) * 10000. / REAL(WETGRD))/100.`

### S1-13 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:25`. Supported claim: The source-basis entry supports section F's unstructured sweep/ordered-vertex, topology and spectral-sector description.

The broad entry is contextualized by note lines 123-138, not by every behavior in the cited span. Top-level unstructured dispatch, direction-derived traversal, topology-based stencil selection and spectral selection remain. Wavefront scheduling replaces thread bounds, but this source-basis claim does not assert that internal API or a flat traversal. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:780-1080`. New evidence: `src/SwanCompUnstruc.ftn90:825-851; src/SwanCompUnstruc.ftn90:877-901; src/SwanCompUnstruc.ftn90:974-986; src/swanmain.ftn:493-495; src/swanmain.ftn:623-627`.

Exact new-source evidence:

- `src/swanmain.ftn:495 — IF (OPTG.EQ.5) CALL SwanVertlist(COMPDA)`
- `src/swanmain.ftn:625 — CALL SwanCompUnstruc ( AC2   , AC1   , COMPDA,           40.80`
- `src/SwanCompUnstruc.ftn90:835 — sweeploop: do swpdir = 1, n`
- `src/SwanCompUnstruc.ftn90:839 — !GRAPH          frontloop: do ifront = 1, nfront(swpdir)`
- `src/SwanCompUnstruc.ftn90:848 — !GRAPH                ivert = flist(kvert,swpdir)`
- `src/SwanCompUnstruc.ftn90:849 — !FXFRO                ivert = vlist(kvert,swpdir)`
- `src/SwanCompUnstruc.ftn90:889 — vu(1) = v(mod(k  ,3)+1)`
- `src/SwanCompUnstruc.ftn90:890 — vu(2) = v(mod(k+1,3)+1)`
- `src/SwanCompUnstruc.ftn90:980 — call SwanSweepSel ( idcmin, idcmax, anybin, iscmin, iscmax, &`

### S1-14 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:25`. Supported claim: The SwanVertlist source-basis entry supports direction-aligned vertex-list creation in section F.

The original list creation and direction-projection/sort remain at 141 and 149-217; the machine mapping 48-217 is valid. Additional wavefront construction follows at 219-408. The extra investigation finds an algorithm/interface replacement, not a pure move, but that replacement does not make the cited vertex-list purpose false. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanVertlist.ftn90:45-181`. New evidence: `src/SwanVertlist.ftn90:48-57; src/SwanVertlist.ftn90:141; src/SwanVertlist.ftn90:149-217; src/SwanVertlist.ftn90:219-408`.

Exact new-source evidence:

- `src/SwanVertlist.ftn90:50 — !   Creates vertex list in line with sweep direction`
- `src/SwanVertlist.ftn90:51 — !   Note: first sweep direction always equals user-given/wave/wind direction`
- `src/SwanVertlist.ftn90:141 — if(.not.allocated(vlist)) allocate (vlist(nverts,nsweep), stat = istat)`
- `src/SwanVertlist.ftn90:185 — dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)`
- `src/SwanVertlist.ftn90:200 — kd = minloc(dist(j:nverts,swpdir))`
- `src/SwanVertlist.ftn90:210 — vlist(j,swpdir) = vlist(k,swpdir)`
- `src/SwanVertlist.ftn90:219 — !GRAPH    ! create wavefronts based on graph levels`
- `src/SwanVertlist.ftn90:220 — !FXFRO    ! create wavefronts`

### S1-15 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:129`. Supported claim: SwanVertlist creates direction-aligned orderings, allocates vlist(nverts,nsweep), projects coordinates and sorts by distance.

All explicit claims in note lines 129-132 remain supported by the same direction setup, allocation, projection and sorting code. The new front construction is an additional result of SwanVertlist, not a replacement of these operations. Old 45-181 maps to 48-217. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanVertlist.ftn90:45-181`. New evidence: `src/SwanVertlist.ftn90:48-57; src/SwanVertlist.ftn90:141; src/SwanVertlist.ftn90:149-217`.

Exact new-source evidence:

- `src/SwanVertlist.ftn90:51 — !   Note: first sweep direction always equals user-given/wave/wind direction`
- `src/SwanVertlist.ftn90:57 — !   Sorting based on increasing distance along sweep direction`
- `src/SwanVertlist.ftn90:141 — if(.not.allocated(vlist)) allocate (vlist(nverts,nsweep), stat = istat)`
- `src/SwanVertlist.ftn90:182 — sdir = asort + PI/real(nsweep)`
- `src/SwanVertlist.ftn90:183 — do swpdir = 1, nsweep`
- `src/SwanVertlist.ftn90:185 — dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)`
- `src/SwanVertlist.ftn90:200 — kd = minloc(dist(j:nverts,swpdir))`
- `src/SwanVertlist.ftn90:209 — itmp            = vlist(j,swpdir)`
- `src/SwanVertlist.ftn90:210 — vlist(j,swpdir) = vlist(k,swpdir)`
- `src/SwanVertlist.ftn90:211 — vlist(k,swpdir) = itmp`

### S1-16 — REVIEW_ONLY

Note: `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:134`. Supported claim: SwanCompUnstruc iterates over sweeps and ordered vertices, identifies upwave vertices from topology and selects a spectral sector.

The explicit abstraction and its two bullets still hold: sweeps traverse an ordered, direction-derived front list (or fixed ranges of vlist), then retain the same topology and spectral-selection code. The new loop is sweep -> front -> vertex, so the old thread scheduling and exact flat list traversal are not preserved. Neither is asserted by this note. Thus the code has a behavioral change, while this candidate claim remains valid; see the dedicated investigation. Meaning changed: **no**. Confidence: **HIGH**. UPDATE_REQUIRED reason type: not applicable.

Old evidence: `src/SwanCompUnstruc.ftn90:829-987`. New evidence: `src/SwanCompUnstruc.ftn90:825-851; src/SwanCompUnstruc.ftn90:877-901; src/SwanCompUnstruc.ftn90:974-986; src/SwanCompUnstruc.ftn90:1328-1338; src/SwanVertlist.ftn90:235-295; src/SwanVertlist.ftn90:363-373`.

Exact new-source evidence:

- `src/SwanCompUnstruc.ftn90:835 — sweeploop: do swpdir = 1, n`
- `src/SwanCompUnstruc.ftn90:839 — !GRAPH          frontloop: do ifront = 1, nfront(swpdir)`
- `src/SwanCompUnstruc.ftn90:840 — !FXFRO          frontloop: do ifront = 1, nfront`
- `src/SwanCompUnstruc.ftn90:844 — !$omp do schedule(static)`
- `src/SwanCompUnstruc.ftn90:848 — !GRAPH                ivert = flist(kvert,swpdir)`
- `src/SwanCompUnstruc.ftn90:849 — !FXFRO                ivert = vlist(kvert,swpdir)`
- `src/SwanCompUnstruc.ftn90:889 — vu(1) = v(mod(k  ,3)+1)`
- `src/SwanCompUnstruc.ftn90:890 — vu(2) = v(mod(k+1,3)+1)`
- `src/SwanCompUnstruc.ftn90:980 — call SwanSweepSel ( idcmin, idcmax, anybin, iscmin, iscmax, &`
- `src/SwanCompUnstruc.ftn90:1329 — !$omp end do`
- `src/SwanVertlist.ftn90:239 — !GRAPH          pos(k) = j`
- `src/SwanVertlist.ftn90:279 — !GRAPH             if ( pos(m) < pos(k) ) then`
- `src/SwanVertlist.ftn90:289 — !GRAPH          level(k) = lmax + 1`
- `src/SwanVertlist.ftn90:365 — !GRAPH          k = vlist(j,swpdir)`
- `src/SwanVertlist.ftn90:371 — !GRAPH          flist(l,swpdir) = k`

## Required investigation: deleted SwanThreadBounds

### Finding and caller search

**Classification: behavioral and internal-interface replacement, not a pure code move or symbol rename.** Its scheduling responsibility is split between new front construction in `SwanVertlist` and OpenMP worksharing in `SwanCompUnstruc`; the former active-vertex-balanced thread-bound algorithm was not copied intact into either file.

The exact-symbol searches `git grep -n SwanThreadBounds 5544152 -- src/` and `git grep -n SwanThreadBounds 43e9bbb -- src/` found:

- Old executable caller: `5544152:src/SwanCompUnstruc.ftn90:845`, `!$ call SwanThreadBounds( nwetp, ivlow, ivup, tlist, swpdir )`.
- Old definition/end and trace entry: `5544152:src/SwanThreadBounds.ftn90:1,85,160`; old build registrations: `src/srclist.cmake:61` and `src/srclistnc.cmake:64`.
- No new-tree occurrences under `src/`. The complete diff deletes the 160-line routine and those two source-list entries; new `src/SwanCompUnstruc.ftn90:835-851` contains the replacement traversal.

### What the old routine actually did

The deleted routine's declarations at `5544152:src/SwanThreadBounds.ftn90:53-58` define its five arguments. Lines 95-97 get the actual OpenMP team size and calling thread ID. Lines 101-105 compute each thread's active-vertex quota, including `nacvt(i) = (nint(nwetp)*i)/nth - nvcum`. Lines 115-134 scan `vlist(kvert,n)`, count only `vert(ivert)%active`, and derive the calling thread's lower/upper list positions. Lines 136-158 populate that thread's interval in `tlist`, placing active vertices first and inactive vertices after them.

| Old argument / meaning | New disposition |
|---|---|
| `nwetp`: real input, total active-vertex count (old 58, 101-105) | No corresponding input to front construction. New GRAPH construction visits all `nverts` (`SwanVertlist:235-250,307-311,327-333`); FXFRO sizing uses `nverts` and maximum thread count (`382-406`). The active-update test is later at `SwanCompUnstruc:851`. |
| `n`: input sweep index; actual caller passes `swpdir` (old definition 55, use 117, caller 845) | Sweep indexing remains in `vlist(:,swpdir)` / `flist(:,swpdir)` (`SwanVertlist:237,365-371; SwanCompUnstruc:848-849`). There is no replacement positional argument. This old formal `n` must not be confused with `SwanCompUnstruc`'s local `n`, the sweep count at new 825-835. |
| `ivlow,ivup`: output positions bounding the calling thread's interval, not vertex IDs (old 53-54, 121-123) | Removed. GRAPH uses `fptr(ifront,swpdir):fptr(ifront+1,swpdir)-1`; FXFRO uses `fronts(ifront):fronte(ifront)` (new `SwanCompUnstruc:845-846`). These delimit a front shared by the worksharing loop, not a returned per-thread interval. |
| `tlist(nverts)`: output list for the calling thread, populated over its interval (old 56, 139-158) | Removed. GRAPH consumes module `flist`; FXFRO consumes module `vlist` directly (new `SwanCompUnstruc:848-849`). The old active-first thread-list rearrangement is absent from the replacement construction at `SwanVertlist:219-408`. |

### Where the scheduling responsibility went

The new source contains two build-selected paths, not two simultaneously executed loops. `switch.pl:5,24,87-88` initializes `$ffro = "FALSE"`, accepts `-fixfront`, and strips either `!FXFRO` or `!GRAPH`. The supplied CMake default is `option( FFRO "" OFF )` at `CMakeLists.txt:46`; `src/CMakeLists.txt:26-28` adds `-fixfront` when requested, and lines 34-36 invoke the switch script. Thus the supplied default selects GRAPH, while FFRO selects the fixed-front alternative.

**GRAPH preparation:** `src/SwanVertlist.ftn90:235-241` builds each vertex's position in the direction-sorted `vlist`. Lines 248-289 iterate through that list and incident cells, select `m = vu(1)` at 274, use `if ( pos(m) < pos(k) )` at 279 to accumulate `lmax`, then set `level(k) = lmax + 1` at 289. Lines 293-309 derive the number of fronts and front IDs using `nlpf = 1` (78). Lines 317-341 construct front pointers from vertex counts. Lines 363-373 populate `flist` in front order while visiting the original `vlist`. This establishes a direction-derived graph/front order; it does not establish identity with the former flat global distance order.

**FXFRO preparation:** `src/SwanVertlist.ftn90:79` sets `nvth = 10`. Lines 382-391 use `omp_get_max_threads()`, `nvf = nvth * nth`, and `nfront = min(nverts,max(100,ceiling(real(nverts)/real(nvf))))`. Lines 398-406 compute the actual size and start/end indices of each contiguous range of `vlist`. This differs from the deleted routine's use of actual team size and active-point quotas.

**Consumption:** `src/SwanCompUnstruc.ftn90:835-849` now nests sweep -> front -> vertex. The loop has `!$omp do schedule(static)` at 844 and consumes either front pointers/`flist` or fixed ranges/`vlist`. It retains `if ( vert(ivert)%active )` at 851. Lines 1328-1331 close the vertex worksharing loop with `!$omp end do` (no `nowait`) before the next front; the explicit sweep barrier is at 1335-1336. Front-level work distribution and synchronization therefore replace the old whole-sweep per-thread interval.

The added arrays are module state, not new formal arguments: `src/SwanCompdata.ftn90:64,74-79` declares scalar FXFRO `nfront`, GRAPH `flist/fptr/nfront(:)`, FXFRO `fronts/fronte`, and the retained `vlist`.

### Which interfaces and call relationships were preserved

The outer setup/compute relationship remains unchanged in both revisions: `src/swanmain.ftn:493-495` calls `SwanVertlist(COMPDA)` for `OPTG == 5`, and `623-627` dispatches to `SwanCompUnstruc(AC2,AC1,COMPDA,SPCSIG,SPCDIR,XYTST,CROSS,IT)`. New `src/SwanVertlist.ftn90:1,74` retains its single input argument `compda(nverts,MCMVAR)`; the old-to-new diff does not change that signature. It now prepares additional module data consumed during computation.

The inner `SwanCompUnstruc -> SwanThreadBounds` call relationship and its five-argument contract are **not preserved**. There is no equivalent renamed callee. Only the high-level responsibility of arranging traversal survives, using the different construction and worksharing mechanisms above.

Related removal of per-thread bounds is visible in the convergence interfaces: new `src/SwanCompUnstruc.ftn90:1474-1482` calls `SwanConvAccur` / `SwanConvStopc` inside `!$omp single`, without `ivlow,ivup`. Both new definitions at line 1 drop those arguments; `SwanConvAccur:127,151` and `SwanConvStopc:139` loop over `1,nverts`. The complete diff also changes the ACCUR rounding/guard (`SwanConvAccur:236`) and STOPC denominator guard (`SwanConvStopc:267`). These observations further rule out describing the entire change as relocation; they are not additional candidate verdicts.

### Effect on S1-14, S1-15 and S1-16

- **S1-14 / S1-15 remain REVIEW_ONLY:** the explicit supported facts are list creation, first-direction setup, allocation, coordinate projection and distance sorting. Those remain in `SwanVertlist:50-57,141,149-217`; front construction is appended. Neither note claims that this routine produces only `vlist` or preserves the old thread partitioner.
- **S1-16 remains REVIEW_ONLY:** the note asserts sweeps plus ordered vertices, followed by topology-based upwave selection and spectral-sector selection. New `SwanCompUnstruc:835-851,877-901,974-986` and the `vlist`-derived front construction support those exact facts. It does not assert a flat `vlist` walk, unchanged active-vertex balancing, or the deleted call/arguments. A behavior change in those unclaimed details is not enough to make this claim UPDATE_REQUIRED.
- The same distinction applies to the broad source-basis S1-13 and sweep description S1-2.

This is a source-level determination of changed scheduling and interfaces. Numerical-result or bitwise equivalence is not established or asserted.

## UNRESOLVED

None. The supplied new source and old-to-new diff resolve all 16 claim-level verdicts and the required routine investigation. All REANCHOR entries have concrete, claim-focused new evidence above and in the CSV.

No additional candidates are introduced. No files under `models/` were modified.
