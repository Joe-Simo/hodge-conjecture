Module[{m=420,us,idx,perms,ts,ps,uniq,pkeys,unseen,dims,oc=<||>,p,orb,ks,g,gs,small,epsilon,dual,word,wp,dimDirect,breakers},
 us=Select[Range[419],CoprimeQ[#,420]&];
 idx=AssociationThread[us->Range[Length[us]]];
 perms=Table[Lookup[idx,Mod[u us,m]],{u,us}];
 ts=Select[Flatten[Table[{a,b,Mod[-a-b,m]},{a,1,419},{b,a,419}],1],#[[3]]>=#[[2]]&];
 ps=Table[(Total[Mod[u t,m]]/m)-1,{t,ts},{u,us}];
 uniq=DeleteDuplicates[ps];pkeys=ToString[#,InputForm]&/@ps;
 unseen=AssociationThread[(ToString[#,InputForm]&/@uniq)->ConstantArray[True,Length[uniq]]];dims=<||>;
 While[Length[unseen]>0,p=ToExpression[First[Keys[unseen]]];orb=DeleteDuplicates[p[[#]]&/@perms];
  ks=ToString[#,InputForm]&/@orb;g=Length[orb]/2;AssociateTo[oc,g->(Lookup[oc,g,0]+1)];
  Do[AssociateTo[dims,k->g],{k,ks}];KeyDropFrom[unseen,ks]];
 gs=Lookup[dims,pkeys];small=Flatten[Position[gs,x_/;x<=8]];
 epsilon[t_]:=Mod[Count[m/(GCD[m,#]&/@t),7|21],2];
 dual[q_]:=Mod[Total[q[[Lookup[idx,{11,23,37,59,71}]]]]-5q[[1]],2];
 breakers=Select[small,epsilon[ts[[#]]]!=dual[ps[[#]]]&];
 word=6{{24,61,55},{20,15,35},{35,42,63},{7,62,1}};
 wp=Table[Total[Mod[u t,m]]/m-1,{t,word},{u,us}];
 dimDirect[q_]:=Length[DeleteDuplicates[q[[#]]&/@perms]]/2;
 <|"Version"->$Version,"Triples"->Length[ts],"Profiles"->Length[uniq],
 "OrbitCountsByG"->KeySort[oc],"SmallTriples"->Length[small],"SmallProfiles"->Length[DeleteDuplicates[ps[[small]]]],
 "SmallTripleDimensionCounts"->Counts[gs[[small]]],"FormulaFailureCount"->Length[breakers],
 "Dimension12Control"->{dimDirect[Table[Total[Mod[u{2,140,278},m]]/m-1,{u,us}]],epsilon[{2,140,278}],dual[Table[Total[Mod[u{2,140,278},m]]/m-1,{u,us}]]},
 "BoundaryDimensions"->(dimDirect/@wp),"BoundaryHodgeProfileSum"->Union[Total[wp]],"BoundaryParity"->Mod[Total[epsilon/@word],2]|>]
