Module[{be={1,42,62,35},ga={20,24,61,35},un,bv,gv,f5,f7,a,b,c,t,x,y,z,gr,tab,pairs,q5,q7,k5,k7},
 un=Select[Range[69],CoprimeQ[#,70]&];
 gr[v_]:=Total[v]/70-1;
 tab[v_]:=Sort[Tally[Table[If[MemberQ[Mod[k v,70],0],Nothing,{70/GCD[k,70],gr[Mod[k v,70]]}],{k,69}]]];
 bv=Select[Range[69],!MemberQ[Mod[# be,70],0]&];
 gv=Select[Range[69],!MemberQ[Mod[# ga,70],0]&];
 pairs[v_,w_,ks_,ls_]:=Select[Tuples[{ks,ls}],Function[p,AllTrue[un,Function[u,gr[Mod[u p[[1]] v,70]]+gr[Mod[u p[[2]] w,70]]==2]]]];
 f5=z^2+y^5+x^9 t+x^2 t^8; f7=z^2+y^5+x^7 y t+t^10;
 q5=Join[{{1,0,0,0,0}},Table[Join[{0},Table[Which[i==j,-2,Abs[i-j]==1,1,True,0],{j,4}]],{i,4}]];
 q7={{1,0,1},{0,-2,1},{1,1,-3}};
 k5=Select[Tuples[{Range[0,4],Range[0,34],Range[0,1]}],Mod[{42,62,35}.#,70]==0&];
 k7=Select[Tuples[{Range[0,6],Range[0,34],Range[0,1]}],Mod[{20,24,35}.#,70]==0&];
 <|"Version"->$Version,"Surface5Orbits"->tab[be],"Surface7Orbits"->tab[ga],
 "MixedBalancedPairs"->pairs[be,ga,bv,gv],"SelfBalancedCounts"->{Length[pairs[be,be,bv,bv]],Length[pairs[ga,ga,gv,gv]]},
 "FirstSubstitutionResidual"->Expand[(f5/.{t->1,x->b^5,y->a b^2,z->c b^5})-b^10(1+a^5+b^35+c^2)],
 "SecondSubstitutionResidual"->Expand[(f7/.{t->1,x->a/b,y->b^7,z->c})-(1+a^7+b^35+c^2)],
 "KernelSizes"->{Length[k5],Length[k7]},
 "SingularBases_T1_X1"->{GroebnerBasis[Join[{f5/.t->1},D[f5/.t->1,#]&/@{x,y,z}],{x,y,z}],GroebnerBasis[Join[{f5/.x->1},D[f5/.x->1,#]&/@{t,y,z}],{t,y,z}],GroebnerBasis[Join[{f7/.t->1},D[f7/.t->1,#]&/@{x,y,z}],{x,y,z}],GroebnerBasis[Join[{f7/.x->1},D[f7/.x->1,#]&/@{t,y,z}],{t,y,z}]},
 "IntersectionDeterminants"->{Det[q5],Det[q7]},
 "QuinticDiscriminant"->Factor[Discriminant[y^5+x^7 y+1,y]]|>]
