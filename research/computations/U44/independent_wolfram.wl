(* Successful independent full reflection/DH/quadruple check. *)
ClearAll[ff,eps,unitList,parityList,dc,allD,quadCheck];
eps[a_Integer]:=Boole[MemberQ[{7,21},420/GCD[420,Mod[a,420]]]];
unitList=Select[Range[1,209],CoprimeQ[#,420]&];
parityList=eps/@Range[1,419];
allD=Flatten[Table[Table[If[Mod[n*a,420]==0,Nothing,{n,a}],{a,1,419}],{n,Rest[Divisors[420]]}],1];
dc[{n_,a_}]:=Mod[Sum[eps[Mod[a+j*(420/n),420]],{j,0,n-1}]-eps[Mod[n*a,420]]-Sum[eps[j*(420/n)],{j,1,n-1}],2];
ff=Compile[{{mm,_Integer},{uu,_Integer,1},{vv,_Integer,1}},Module[{aa=0,bb=0,cc=0,dd=0,jj=0,count=0,bad=0,ok=True,lo=0,hi=0},For[aa=1,aa<=Quotient[mm,2],aa++,For[bb=aa,bb<=Min[mm-1,Quotient[2*mm-aa,3]],bb++,lo=Max[bb,2*mm-aa-bb-(mm-1)];hi=Min[mm-1,Quotient[2*mm-aa-bb,2]];For[cc=lo,cc<=hi,cc++,dd=2*mm-aa-bb-cc;ok=True;For[jj=1,jj<=Length[uu],jj++,If[Mod[uu[[jj]]*aa,mm]+Mod[uu[[jj]]*bb,mm]+Mod[uu[[jj]]*cc,mm]+Mod[uu[[jj]]*dd,mm]!=2*mm,ok=False;Break[]]];If[ok,count++;If[Mod[vv[[aa]]+vv[[bb]]+vv[[cc]]+vv[[dd]],2]!=0,bad++]]]]];{count,bad}],CompilationTarget->"WVM"];
quadCheck=ff[420,unitList,parityList];
<|"Version"->$Version,"AllAdmissibleDHCount"->Length[allD],"AllDHEven"->AllTrue[dc/@allD,#==0&],"AllReflectionsEven"->AllTrue[Range[419],Mod[eps[#]+eps[420-#],2]==0&],"TargetOrders"->(420/GCD[420,#]&/@(6*{1,20,24,42,61,62})),"TargetParity"->Mod[Total[eps/@(6*{1,20,24,42,61,62})],2],"IndependentDirectQuadrupleCensusCountAndOddCount"->quadCheck,"ExtraDivisorSeedCountercheck"->Mod[Total[Boole[MemberQ[{7},420/GCD[420,#]]]&/@(20*{1,4,18,19})],2]|>
