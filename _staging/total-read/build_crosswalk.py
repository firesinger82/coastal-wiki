#!/usr/bin/env python3
"""Pilot crosswalk builder — EFDC-000 (6 files). MERGE-PLAN-20260827 §1-4.
Reads the two frozen record layers (1차 fable5 base, 감사 codexaudit) and emits
one crosswalk JSON per file into OUT. Disposition mapping is hand-adjudicated
(pilot = unblinded mechanics validation; production shards use blinded agent, §2).
Pure stdlib. Does NOT touch the locked tree."""
import json, os, hashlib, sys

ROOT = "/home/firesinger/coastal-wiki/_staging/total-read/pending/reread-20260728"
BASE = os.path.join(ROOT, "reread20260728-code-EFDC-000-fable5-20260813T012841Z-5799640f")
AUD  = os.path.join(ROOT, "reread20260728-code-EFDC-000-codexaudit-20260826T022956Z-6d4b819d")
OUT  = os.path.dirname(os.path.abspath(__file__)) + "/records-crosswalk/reread-20260728"
DECIDED_AT = "2026-08-27"
DECIDED_BY = "llm:claude-opus-4-8 (pilot; self-adjudicated, UNBLINDED — mechanics validation only)"

# sha(short) -> short source basename, for readability in outputs
SHA = {
 "5d5841f6191b214880eb061c88a8e31f83574f8ae762e4eb9343331eab057cd8": "mod_scaninp.f90",
 "6de5c1b50366260e1d20e4ab66a609693ac841ea015aba7ac7d1fc6fce195441": "aaefdc.f90",
 "7d0c698c648e94b495a64d9a81a716ca58741b7ab6d4cb1b0a42a931cfb70687": "mod_netcdf.f90",
 "83cfe59f04eabf4457b7e0cc3434bffc9d66323afe7c69e4a1f89584832d644a": "input.f90",
 "9c6058d12a8d3c5afebb807e4c4d04acbd537cc4e4b92163dce07331290fca20": "mod_var_global.f90",
 "e84bbcb331c42f22afcb11d49016c3c52e941eceab26d5df07e9981adbe376a1": "mod_restart.f90",
}

# ---- Disposition mapping. Each entry: (disp, [base_idx], [audit_idx], note) ----
# Every base finding index must appear exactly once across its file's base_ids;
# same for audit indices. Verifier enforces this.
DISPO = {
 "mod_scaninp.f90": [
   ("equivalent",[3],[3],"SCANASER prints unassigned NS not loop var NA; B adds NDASER post-read broadcast gap"),
   ("equivalent",[5],[9],"SCANSEDZLJ read errors gated on ERROR==1; other IOSTAT/EOF bypass handlers"),
   ("equivalent",[6],[8],"FNWQSR fixed dim 40 filled to 19+NALGAE+NZOOPL with no bound check"),
   ("base_only",[0],[],"assumed-length char with length spec, no parameter attr — nonstandard"),
   ("base_only",[1],[],"SCANGWSR groundwater record count 'DELME - WQ'"),
   ("base_only",[2],[],"SCANWRSER label-20 error falls through to label-40 message before STOPP"),
   ("base_only",[4],[],"WQPSL.INP opened but ERRSTR reads 'WPQSL.INP' (transposed)"),
   ("base_only",[7],[],"NWSER re-broadcast — defensive vs vestigial unresolved"),
   ("distinct_unconfirmed",[],[0],"C45E TOXDEP TXDRY/TXWET read but only ITXDRY/ITXWET flags broadcast (MPI)"),
   ("distinct_unconfirmed",[],[1],"C46 VOL_VEL_MAX/VOL_DEP_MIN read, absent from broadcast list (MPI)"),
   ("distinct_unconfirmed",[],[2],"MODCHAN MDCHH/MDCHHD/MDCHHD2 read, only MDCHH broadcast (MPI)"),
   ("distinct_unconfirmed",[],[4],"SCANDSER opens DSER.INP master-only but close(1) on all ranks"),
   ("distinct_unconfirmed",[],[5],"SCANWQ master-only NCSERM increment not propagated (MPI)"),
   ("distinct_unconfirmed",[],[6],"wq_biota master sets MACDRAG/ISVEG but broadcasts only ISMOB/IVARSETL"),
   ("distinct_unconfirmed",[],[7],"FNWQSR uninitialized in ISWQLVL==0 path yet used as filename"),
   ("distinct_unconfirmed",[],[10],"SCANSEDZLJ reads SEDSTEP/.../HPMIN but broadcasts only 4 values (MPI)"),
   ("distinct_unconfirmed",[],[11],"SCNTXSED broadcasts NLOOP even when left unassigned"),
   ("distinct_unconfirmed",[],[12],"SCANEFDC C67 NPDM=max(1,NPD) with NPD not assigned in routine"),
   ("distinct_unconfirmed",[],[13],"C22 Broadcast_Scalar(NDYE) called twice — copy trace"),
 ],
 "aaefdc.f90": [
   ("confirmed_delta",[],[1],"DETTMP=1/det then compared ==0.0: reciprocal of singular det is Inf not 0, so STOPP guard is dead code",
     {"path":"EFDC/raw/source_code/EFDCPlus_Stable/EFDC/aaefdc.f90","lines":"924-928",
      "quote":"DETTMP = 1./( CUE(L)*CVN(L) - CUN(L)*CVE(L) )\n      if( DETTMP == 0.0 )then\n        write(6,6262)\n        write(6,6263) IL(L), JL(L)\n        call STOPP('.', 1)"}),
   ("equivalent",[0],[3],"DZC_Global(LG,:)=DZCK(K) after DO K loop closed — K is post-loop KC+1, scalar broadcast/OOB"),
   ("equivalent",[1],[5],"south toxic boundary tests NCSERS(LL,4) while W/E/N use index 5"),
   ("equivalent",[10],[2],"foodchain read pulls leading integer into real C; B adds diagnostic WRITE of unassigned JDUMY"),
   ("base_only",[2],[],"DYE cold-start uses ISRESTI==1 while SAL/TEM/TOX use >=1"),
   ("base_only",[3],[],"VERSION 41-43 && NTHREADS>2 branch unreachable (VERSION set to 3)"),
   ("base_only",[4],[],"STOPP GNU branch ilen undeclared / assigned-but-unused"),
   ("base_only",[5],[],"FRACK computed but unused in this file"),
   ("base_only",[6],[],"open unit 5000+process_id but close(5000) — mismatch on non-root ranks"),
   ("base_only",[7],[],"declared-but-unused local list"),
   ("base_only",[8],[],"W-face commented block asymmetry vs E/S/N"),
   ("base_only",[9],[],"ISPPH==100->1 loses high-freq snapshot marker"),
   ("distinct_unconfirmed",[],[0],"LXLY ISWGS84 conversion applied to row 1 only; DLON/DLAT from row LG pre-conversion"),
   ("distinct_unconfirmed",[],[4],"IGRIDV==1 leaves R1D_Global zero, stores all-zero DZC_Global row"),
   ("distinct_unconfirmed",[],[6],"SGZV normalization-failure branch prints SGZU per-layer diagnostic"),
   ("distinct_unconfirmed",[],[7],"single-domain reads domain_list_*.txt without OUTDIR vs multi-domain OUTDIR//mpi_list"),
   ("distinct_unconfirmed",[],[8],"MAPHMD.INP uses global L directly as local index without LIJ/Map2Local"),
   ("distinct_unconfirmed",[],[9],"STOPP('.',1) calls vs GNU STOPP(MSG) — argument-count interface mismatch"),
   ("distinct_unconfirmed",[],[10],"timing report columns (TPROPW/DSITIMING) differ between text report and TIME.CSV"),
 ],
 "mod_netcdf.f90": [
   ("equivalent",[0],[11],"wave var 18 'Diss' filled from WV_Global.FREQ — same source as Tp"),
   ("equivalent",[7],[7],"nc_write_bed_2d: 2-element start with 3-element count (KB layer) — start/count rank mismatch"),
   ("base_only",[1],[],"msg 'WQAQ' for all 12 shellfish 2D writes (vars 143-154)"),
   ("base_only",[2],[],"def_time_vars defines 11-12 with no ISWAVE guard; nc_write writes only ISWAVE>=1"),
   ("base_only",[3],[],"timesec used without local declaration (use-associated)"),
   ("base_only",[4],[],"catalog vars 10/45/46 have no write; TODO stubs"),
   ("base_only",[5],[],"set_nc_flags never invoked (both call sites commented)"),
   ("base_only",[6],[],"def_var 9 'non-cohesive' but idx 9 and idx 12 share msg 'SHEAR2'"),
   ("base_only",[8],[],"commented if(r>0) guard leaves nv(c,k)==0 indexing lon(0)/lat(0)"),
   ("distinct_unconfirmed",[],[0],"UGRID face_node_connectivity vs misspelled 'connnectivity' cf_role"),
   ("distinct_unconfirmed",[],[1],"Sigma-Z depth attr 'Bottom' vs 'BELV' across branches"),
   ("distinct_unconfirmed",[],[2],"hf file lacks Mesh2D/crs vars but def_var attaches those coords — dangling refs"),
   ("distinct_unconfirmed",[],[3],"inactive component counts as fixed dim lengths; zero -> unintended unlimited dim"),
   ("distinct_unconfirmed",[],[4],"RSSBC written count LCM_Global-1 vs face dim LA_Global-1"),
   ("distinct_unconfirmed",[],[5],"hf lon/lat stay MISSING when IJHFRE(IS)!=0"),
   ("distinct_unconfirmed",[],[6],"nc_write_wc_2d hf branch leaves Sigma-Z layers below KSZ unassigned"),
   ("distinct_unconfirmed",[],[8],"LAYERACTIVE put_var count (KB,cellcnt,1) reverses first two dims"),
   ("distinct_unconfirmed",[],[9],"TOXB bed-layer var fed a cell-by-NTOX surface via vertical-layer helper"),
   ("distinct_unconfirmed",[],[10],"shellfish class vars use water-column helper (loops KSZ..KC not 1..NSF)"),
   ("distinct_unconfirmed",[],[12],"Sxx/Sxy/Syy labelled W/m2 but from WVHUU/WVHUV/WVHVV without conversion"),
   ("distinct_unconfirmed",[],[13],"nc_close_file never clears isopen — reopen/close state desync"),
   ("distinct_unconfirmed",[],[14],"date rollover writes nc(0) to a closed handle before creating new file"),
   ("distinct_unconfirmed",[],[15],"most direct NetCDF ops omit check_err — inconsistent error contract"),
 ],
 "input.f90": [
   ("equivalent",[5],[0],"NPFORT>=1 ordered before ==2 makes mode-2 PFX2 read/broadcast unreachable (C17/C21)"),
   ("equivalent",[1],[10],"PARTITIONB constant else branch writes TOXPARW, leaving bed TOXPARB unfilled"),
   ("equivalent",[2],[12],"DYE.INP loop do L=LG,LA_Global stores DYE_Global(LG,...) with stale LG, L unused"),
   ("equivalent",[3],[13],"TOXB missing-layer fill outside cell loop — fills only final LG"),
   ("equivalent",[9],[18],"ISICE==1 series read on master but Broadcast sits in elseif(ISICE==2) branch"),
   ("equivalent",[10],[19],"MHK NFLAGPWR nesting pairs elseif 2/3 with master test; flag-1 broadcasts master-only"),
   ("equivalent",[4,8,15],[11],"COMPOSITE many-to-one: B11 bundles STPOCB(L,K)=0.0 outside loop (A8), STDOCB cleared in POCB branch (A15), FPOCB NS implied-do stride (A4)"),
   ("base_only",[0],[],"C37 SEDVRDT vs SEDVDRT letter transposition"),
   ("base_only",[6],[],"Broadcast_Array(HS_COEFF) called 4x — 3 redundant"),
   ("base_only",[7],[],"C14D block headed '!C14C', read lacks ISO>0 error guard"),
   ("base_only",[11],[],"tau_crit_coh.inp hard-coded loop bound do L=2,4393"),
   ("base_only",[12],[],"WINDFA/B/C *4.42674E-10 unconditional — re-run re-scales"),
   ("base_only",[13],[],"TEMB(1)=ABS(TEMBO) with TEMBO uninitialized when NASER==0"),
   ("base_only",[14],[],"dead card slots C66A/B,C68-C83 set NCARD only"),
   ("distinct_unconfirmed",[],[1],"south NPFORT=1 cosine uses PCBS(L,M) while block populates PCBS_GL"),
   ("distinct_unconfirmed",[],[2],"L508 diagnostic labels global_max_width_y as x-direction"),
   ("distinct_unconfirmed",[],[3],"Jet/WQ MMAX+NWQV then reuses completed DO var MS — index can exceed MMAX"),
   ("distinct_unconfirmed",[],[4],"C39 ISEDSCOR/C40 WCLIMIT/TAUCRCOH broadcasts omitted in cohesive path"),
   ("distinct_unconfirmed",[],[5],"DYESTEPW read on master with no following broadcast"),
   ("distinct_unconfirmed",[],[6],"CLTMSR_GL broadcast commented out"),
   ("distinct_unconfirmed",[],[7],"MODDXDY calls LIJ(ITMP,JTMP) not LIJ(I,J)"),
   ("distinct_unconfirmed",[],[8],"MODCHAN syncs selected raw arrays; MDCHH/QCHERR/LMDCH*/QCHAN* unsynced"),
   ("distinct_unconfirmed",[],[9],"AVO=ABS(AVO) precedes if(AVO<0) — AVMAP mode unreachable"),
   ("distinct_unconfirmed",[],[14],"PSERAVG divides by TIM(NREC)-TIM(1) with no NREC>=2 / nonzero check"),
   ("distinct_unconfirmed",[],[15],"SSER reads MCSER(NS,1) but loops TSSAL(NS).NREC (ASER/WSER/ISER repeat)"),
   ("distinct_unconfirmed",[],[16],"TXDRY /86400 applied to class 1 only, omitted for 2..NTOX"),
   ("distinct_unconfirmed",[],[17],"QCTRULES sorts IDX but triggers use RULES(M) not RULES(IDX(M))"),
   ("distinct_unconfirmed",[],[20],"PARSE_LOGICAL/PARSESTRING/READ_SUBSET unassigned-return & missing broadcast paths"),
 ],
 "mod_var_global.f90": [
   ("equivalent",[0],[0],"LWC doc comment reads SOUTH (dup of LSC); by naming should be WEST"),
   ("equivalent",[4],[6],"NSEDS2 comment '2*NSCM' inconsistent with 2*NSEDS naming pattern"),
   ("base_only",[1],[],"DV comment duplicates DU 'Temporary delta U array'"),
   ("base_only",[2],[],"SEDB/SEDB1 current/previous comments appear swapped"),
   ("base_only",[3],[],"NSCM/NSED and NSND/NSNM carry identical comments"),
   ("base_only",[5],[],"delme-flagged but still declared: NDPSER/NFLTMT/RKTOXP/CBEDTOTAL"),
   ("base_only",[6],[],"DAYNEXT declaration commented out while HOUR*NEXT active"),
   ("base_only",[7],[],"IS2TIM/IS2TL identical comments"),
   ("base_only",[8],[],"ZZ/ZZC index-order swap asserted only in comments"),
   ("base_only",[9],[],"LKSZ/LSGZU/LSGZV flag polarity inverted vs names"),
   ("base_only",[10],[],"IWRSP/IWRSPB semantics undefined in this file"),
   ("base_only",[11],[],"SEDZLJ block shapes asserted only in trailing comments"),
   ("base_only",[12],[],"numerous empty '!<' doc comments"),
   ("base_only",[13],[],"NPSERM comment corrupted '<aximum'"),
   ("base_only",[14],[],"NMAXBC/MSVDOX declared without comment"),
   ("distinct_unconfirmed",[],[1],"TOXCLASS BIO_KB and BIO_KW both commented 'sediment bed'"),
   ("distinct_unconfirmed",[],[2],"HQCTLU and HQCTLD both commented 'Offset for upstream head'"),
   ("distinct_unconfirmed",[],[3],"WCVPOINTER initializes ID/VAL0/VAL1 but not WCLIMIT"),
   ("distinct_unconfirmed",[],[4],"COARE_NITS 'Number of iterations' declared REAL"),
   ("distinct_unconfirmed",[],[5],"WCV fixed 100 with no NACTIVEWC<=100 guard"),
   ("distinct_unconfirmed",[],[7],"declaration module lacks self-correction for cross-file broadcast gaps"),
 ],
 "mod_restart.f90": [
   ("equivalent",[0],[5],"freezing-point TF uses SAL(L,KC) while enclosing loop indexes LG/LL — stale L"),
   ("equivalent",[1],[8],"lower-chord/rating-curve restart read on unit 1 not UINP; B adds write/read order mismatch"),
   ("equivalent",[2],[13],"restart overwrites configured NSEDS/NSEDS2 from file at first global cell"),
   ("equivalent",[3],[1],"shellfish (ISTRAN(4)) restart reads local SFL/SFL2 by LG, broadcast/populate are placeholders"),
   ("base_only",[4],[],"ISCOCHK read only Ver>=720 but used on <=710 path unassigned"),
   ("base_only",[5],[],"WQ_WCRST writes VER=8400 but input never parses the version"),
   ("base_only",[6],[],"Gather stores derived total ice; Restart_In reads as plain thickness — round-trip asymmetry"),
   ("base_only",[7],[],"WQSDRST_IN reads target L from file with no bounds check"),
   ("base_only",[8],[],"NSCM0=max(1,NSED) computed but unused"),
   ("base_only",[9],[],"header lists nonexistent subroutines — stale comment"),
   ("distinct_unconfirmed",[],[0],"shellfish Gather TODO + SFLSBOT written twice (output side)"),
   ("distinct_unconfirmed",[],[2],"drying state ISCDRY/NATDRY/IDRY consumed all ranks but omitted from broadcast"),
   ("distinct_unconfirmed",[],[3],"legacy ISDRY==99 path maps drying on all ranks with no broadcast"),
   ("distinct_unconfirmed",[],[4],"Ver>=1200 ISGOTM>0 TKE3D/EPS3D/GL3D read master, used all ranks, no broadcast"),
   ("distinct_unconfirmed",[],[6],"ice permits negative TF but later loop forces TEM/TEM1>=0"),
   ("distinct_unconfirmed",[],[7],"ISBELVC set only when ISRESTIOPT!=0 but correction requires ==0 — unreachable"),
   ("distinct_unconfirmed",[],[9],"bathymetry diag writes IL_GL twice; shallow warning uses local IL/JL by global LG"),
   ("distinct_unconfirmed",[],[10],"debug restart uses local KBT(LG) while iterating global LG"),
   ("distinct_unconfirmed",[],[11],"WQ_WCRST_IN formatted path stores by loop pos not file-read L,M identifiers"),
   ("distinct_unconfirmed",[],[12],"Setup_Continuation_Files builds unquoted shell commands, ignores RESLOG"),
 ],
}

def sha_bytes(p):
    return hashlib.sha256(open(p,"rb").read()).hexdigest()

def load(dirp):
    out={}
    for f in os.listdir(dirp):
        if not f.endswith(".json"): continue
        rec=json.load(open(os.path.join(dirp,f)))
        out[f[:-5]]={"rec":rec,"file":f,"path":os.path.join(dirp,f)}  # key by record-file stem
    return out

def main():
    os.makedirs(OUT, exist_ok=True)
    base=load(BASE); aud=load(AUD)
    for stem, name in SHA.items():   # SHA keys are record-file stems
        b=base[stem]; a=aud[stem]
        sha=b["rec"]["source_sha256"]
        bu=b["rec"]["content"]["unresolved"]; au=a["rec"]["content"]["unresolved"]
        assert b["rec"]["source_sha256"]==a["rec"]["source_sha256"]==sha, "source sha mismatch"
        assert b["rec"]["path"]==a["rec"]["path"], "source path mismatch across layers"
        disp=[]
        for entry in DISPO[name]:
            d,bids,aids,note = entry[0],entry[1],entry[2],entry[3]
            span = entry[4] if len(entry)>4 else None
            item={"disposition":d,
                  "base_ids":[f"A{i}" for i in bids],
                  "audit_ids":[f"B{i}" for i in aids],
                  "base_member_text":[bu[i] for i in bids],
                  "audit_member_text":[au[i] for i in aids],
                  "representative":"audit" if aids else "base",
                  "rationale":note,
                  "decided_by":DECIDED_BY,"decided_at":DECIDED_AT}
            if span: item["evidence_span"]=span
            disp.append(item)
        cw={"schema":"crosswalk/v1","model":"EFDC","shard":"EFDC-000",
            "source_path":b["rec"]["path"],"source_sha256":sha,
            "base_run_id":b["rec"]["run_id"],"audit_run_id":a["rec"]["run_id"],
            "base_record_file":b["file"],"audit_record_file":a["file"],
            "base_record_sha256_bytes":sha_bytes(b["path"]),
            "audit_record_sha256_bytes":sha_bytes(a["path"]),
            "base_finding_count":len(bu),"audit_finding_count":len(au),
            "provenance":{"pilot":True,"blinded":False,
              "note":"Pilot mechanics validation. Production shards use blinded A/B-randomized agent (MERGE-PLAN §2). confirmed_delta span verified against read-only source.",
              "decided_by":DECIDED_BY,"decided_at":DECIDED_AT},
            "dispositions":disp}
        json.dump(cw, open(os.path.join(OUT, name+".crosswalk.json"),"w"), ensure_ascii=False, indent=1)
        print(f"wrote {name}: base={len(bu)} audit={len(au)} dispositions={len(disp)}")
    print("OUT:", OUT)

if __name__=="__main__":
    main()
