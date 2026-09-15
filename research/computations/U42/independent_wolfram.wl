Module[{m=70,alpha={1,20,24,42,61,62},ev,refl,dh,np,hp,target,certificate,selected={14,28,42,56},eps,units,admissible,orbit,beta,gamma},
 ev[a_Integer]:=If[Mod[a,m]==0,Throw["zero argument"],UnitVector[70,Mod[a,m]]];
 refl[a_]:=ev[a]+ev[-a]-UnitVector[70,70];
 dh[n_,a_]:=Total[Table[ev[a+j m/n],{j,0,n-1}]]-ev[n a]-Total[Table[ev[j m/n],{j,1,n-1}]];
 np={{1,1},{4,1},{9,1},{16,1},{22,-1},{24,2},{26,1},{28,-1},{30,1}};
 hp={{2,1,1},{2,9,-1},{2,26,1},{2,34,-1},{5,4,-1},{5,6,1},{5,12,-1},{7,2,1},{7,6,-1}};
 target=Total[ev/@alpha]-3 UnitVector[70,70];
 certificate=Total[(#[[2]]refl[#[[1]]])&/@np]+Total[(#[[3]]dh[#[[1]],#[[2]]])&/@hp];
 eps[v_]:=Mod[Total[v[[selected]]],2];
 units=Select[Range[69],CoprimeQ[#,70]&];
 admissible=Select[Tuples[{Rest[Divisors[70]],Range[69]}],Mod[Times@@#,70]!=0&];
 orbit=Mod[# alpha,70]&/@units; beta={1,42,61,36}; gamma={25,23,4,18};
 <|"Version"->$Version,"CertificateResidual"->certificate-2target,
 "ReflectionCoefficientSum"->Total[np[[All,2]]],
 "AllAdmissibleDHCount"->Length[admissible],"DHCountsByDivisor"->Tally[admissible[[All,1]]],
 "AllDHParityZero"->AllTrue[admissible,eps[dh@@#]==0&],
 "AllReflectionParityZero"->AllTrue[Range[69],eps[refl[#]]==0&],
 "TargetParity"->eps[target],"TwiceTargetParity"->eps[2target],
 "UnitOrbitSize"->Length[DeleteDuplicates[orbit]],"UnitResidueSums"->Union[Total/@orbit],
 "AllConjugatesParityOne"->AllTrue[orbit,OddQ[Count[#,a_/;MemberQ[selected,a]]]&],
 "AllSourcePartialMultiplesNonzero"->AllTrue[hp,AllTrue[Range[#[[1]]] #[[2]],Mod[#,70]!=0&]&],
 "TargetPartialSums"->Mod[Accumulate[Most[alpha]],70],
 "SecondaryHodgeProfileEquality"->((Total[Mod[# beta,70]]/70&/@units)==(Total[Mod[# gamma,35]]/35&/@units))|>
]
