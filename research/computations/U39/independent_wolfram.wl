(* Exact independent-engine corroboration of U39; no external resources. *)
ClearAll[x];
Module[{aa={1,20,24,42,61,62}, rc, dc, ev, refl, hd, lhs, target,
 rhs, ph, tau, primes={71,211,281,421,491}, rows},
 rc={{8,2},{9,1},{10,1},{11,1},{12,1},{13,-2},{18,-1},{20,4},
 {21,-1},{22,-2},{24,2},{26,2},{28,1},{29,-2},{30,-1},{32,-1},{34,1}};
 dc={{2,1,-1},{2,3,1},{2,5,2},{2,6,1},{2,7,1},{2,8,-2},{2,9,-1},
 {2,10,1},{2,11,-2},{2,13,2},{2,14,1},{2,15,-3},{2,16,-1},{2,17,1},
 {5,1,2},{5,2,-1},{5,3,-1},{7,1,1}};
 ev[a_]:=UnitVector[70,a];
 refl[a_]:=ev[a]+ev[70-a]-ev[70];
 hd[n_,a_]:=Total[Table[ev[Mod[a+j*70/n,70]],{j,0,n-1}]]
 -ev[Mod[n*a,70]]-Total[Table[ev[j*70/n],{j,1,n-1}]];
 lhs=Total[(#[[2]]*refl[#[[1]]])& /@ rc]
 +Total[(#[[3]]*hd[#[[1]],#[[2]]])& /@ dc];
 target=2*Total[ev /@ aa]-6*ev[70];
 rhs={Total[Times@@#& /@ rc],Sequence@@Table[
 Total[(-#[[1]]*#[[2]]*#[[3]])& /@ Select[dc,#[[1]]==n&]],{n,{2,5,7}}]};
 ph=Cyclotomic[70,x];
 tau=PolynomialRemainder[Sum[JacobiSymbol[a,35]*x^(2a),{a,0,34}],ph,x];
 rows=Table[Module[{g=PrimitiveRoot[p],logs,j,fac,dval,cval,z0,k,h},
 logs=Association[Table[PowerMod[g,i,p]->Mod[i,70],{i,0,p-2}]];
 fac=Table[PolynomialRemainder[Sum[
 x^Mod[ab[[1]]*logs[t]+ab[[2]]*logs[Mod[1-t,p]],70],{t,2,p-1}],ph,x],
 {ab,{{1,20},{21,24},{45,42},{17,61}}}];
 j=PolynomialRemainder[Times@@fac,ph,x]/p^2;
 k=Select[Range[0,69],PolynomialRemainder[x^#-j,ph,x]==0&];
 z0=PowerMod[g,(p-1)/70,p];
 dval=Mod[-PowerMod[2,32,p]*PowerMod[5,15,p]*PowerMod[7,-7,p],p];
 cval=Mod[PowerMod[2,16,p]*PowerMod[5,7,p]*PowerMod[7,-4,p]*(tau/.x->z0),p];
 h=logs[cval];{p,g,First[k],logs[dval],h,Mod[First[k]-h,70]}],{p,primes}];
 <|"version"->$Version,
 "integerCertificateZero"->(lhs-target==ConstantArray[0,70]),
 "RHSExponentsMinusOneTwoFiveSeven"->rhs,
 "tauSquarePlus35Remainder"->PolynomialRemainder[tau^2+35,ph,x],
 "prime_g_jExponent_DExponent_CExponent_residual"->rows|>]
