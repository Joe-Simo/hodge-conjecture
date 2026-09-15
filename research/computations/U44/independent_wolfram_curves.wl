(* Successful separate curve-product census check. Stateless input. *)
ClearAll[uu,rr,tt,gg,pp,ev];
uu=Select[Range[209],CoprimeQ[#,420]&];
rr=Table[Mod[u*a,420],{a,1,419},{u,uu}];
ev[a_]:=Boole[MemberQ[{7,21},420/GCD[420,a]]];
tt=Flatten[Table[With[{c=Mod[-a-b,420]},If[c>=b,{a,b,c},Nothing]],{a,1,419},{b,a,419}],1];
pp[t_]:=Total[rr[[t]]]/420;
gg=GatherBy[tt,pp];
<|"Version"->$Version,"CurveTripleCount"->Length[tt],"ProfileCount"->Length[gg],"OrderedDualHodgePairs"->Total[(Length[#]^2)&/@gg],"AllProfileParitiesConstant"->AllTrue[gg,Length[Union[(Mod[Total[ev/@#],2]&/@#)]]==1&]|>
