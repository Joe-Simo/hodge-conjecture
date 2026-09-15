Module[{u,t,r,w,v,e,k,f,disc,h,nn,id,om,raw5,raw7,res5,res7,stab,genus,rr,rootChecks},
 f=u^5+t^7 u+1; disc=Factor[Discriminant[f,u]];
 h=u^3+2 r u^2+3 r^2 u+4 r^3;
 nn=Normal[SparseArray[{{1,2}->1},{4,4}]]; id=IdentityMatrix[4];
 om={{0,1,0,0},{-1,0,0,0},{0,0,0,1},{0,0,-1,0}};
 raw5=-w^10 v^2+w^10 u^5+t^9+t^2;
 raw7=-w^14 v^2+t^6(t^5+1)+w^14 u^7;
 res5=PolynomialRemainder[PolynomialRemainder[raw5,v^2-u^5-1,v],w^10-t^2(1+t^7),w];
 res7=PolynomialRemainder[PolynomialRemainder[raw7,v^2-u^7-1,v],w^14-t^6(1+t^5),w];
 stab[m_,phi_]:=Select[Range[m-1],Sort[Mod[# phi,m]]===Sort[phi]&];
 genus[n_,vals_]:=1+(-2 n+Total[(n-GCD[n,#])&/@vals])/2;
 rr=-5/(4 t^7);
 rootChecks=(PolynomialRemainder[Numerator[Together[#]],disc,t]===0)&/@{rr^5-1/4,t^7+5 rr^4};
 <|"Version"->$Version,"Discriminant"->disc,
   "DiscriminantSquarefree"->(PolynomialGCD[disc,D[disc,t]]===1),
   "NodeFactorIdentity"->(Expand[u^5-5 r^4 u+4 r^5-(u-r)^2 h]===0),
   "CubicDiscriminant"->Factor[Discriminant[h,u]],"CubicAtNode"->(h/.u->r),
   "UniqueRootChecks"->rootChecks,"SmoothingDerivative"->(D[f,t]/.u->r),
   "NilpotentRank"->MatrixRank[nn],"NilpotentSquareZero"->(nn.nn===ConstantArray[0,{4,4}]),
   "AllIndexCompositionIdentity"->(Expand[(id+e nn).(id+k nn)-id-(e+k) nn]===ConstantArray[0,{4,4}]),
   "SymplecticIdentity"->(Expand[Transpose[id+e nn].om.(id+e nn)-om]===ConstantArray[0,{4,4}]),
   "CMStabilizers"->{stab[5,{1,2}],stab[7,{1,2,3}]},
   "ImprimitiveControl"->stab[7,{1,2,4}],"ProductMapResiduals"->{res5,res7},
   "CoverGenera"->{genus[10,Join[{2},ConstantArray[1,7],{-9}]],genus[14,Join[{6},ConstantArray[1,5],{-11}]]},
   "ConstantFibreGenera"->{genus[2,Join[ConstantArray[1,5],{-5}]],genus[2,Join[ConstantArray[1,7],{-7}]]}|>]
