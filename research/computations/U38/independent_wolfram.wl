(* The following two expressions were evaluated in separate stateless
   WolframLanguageEvaluator calls on 2026-09-15. The recorded fields are in
   independent_wolfram.json. Inputs do not depend on the Python output. *)
Clear[x];
Module[{alpha={1,20,24,42,61,62},ph=Cyclotomic[70,x],ps={71,211,281,421,491},rows},
 rows=Table[Module[{g,logs,j2,fac,prod,norm,ks,ord},
  g=First[Select[Range[2,p-1],MultiplicativeOrder[#,p]==p-1&]];
  logs=Association[Table[PowerMod[g,k,p]->Mod[k,70],{k,0,p-2}]];
  j2[a_,b_]:=PolynomialRemainder[
    Total[Table[x^Mod[a logs[t]+b logs[Mod[1-t,p]],70],{t,2,p-1}]],ph,x];
  fac=j2@@@{{1,20},{21,24},{45,42},{17,61}};
  prod=Fold[PolynomialRemainder[Expand[#1 #2],ph,x]&,x^Mod[62 logs[p-1],70],fac];
  norm=Expand[prod/p^2];
  ks=Select[Range[0,69],PolynomialRemainder[x^#-norm,ph,x]===0&];
  ord=Select[Divisors[70],PolynomialRemainder[norm^#-1,ph,x]===0&];
  <|"p"->p,"g"->g,"binaryFactors"->fac,"normalized"->norm,
    "rootExponents"->ks,"order"->First[ord],
    "allUnitConjugateOrders"->Union[(70/GCD[70,First[ks] #])&/@
                                      Select[Range[69],CoprimeQ[#,70]&]]|>
 ],{p,ps}];
 <|"version"->$Version,"rows"->rows|>
]

Clear[x];
Module[{m=70,p=491,g=2,lg,phi,factors,j},
 lg=Association[Table[PowerMod[g,k,p]->Mod[k,m],{k,0,p-2}]];
 phi=Cyclotomic[m,x];
 factors=Table[PolynomialRemainder[
   Total[Table[x^Mod[r[[1]]lg[t]+r[[2]]lg[Mod[1-t,p]],m],{t,2,p-1}]],phi,x],
   {r,{{1,20},{21,24},{45,42},{17,61}}}];
 j=Fold[PolynomialRemainder[Expand[#1 #2],phi,x]&,1,factors];
 <|"binaryCoefficientListsAscending"->(PadRight[CoefficientList[#,x],24]&/@factors),
   "jEqualsMinus491SquaredTimesX22"->(Expand[j+491^2*x^22]===0),
   "order70"->(PolynomialRemainder[x^(57*70)-1,phi,x]===0),
   "properDivisorNonidentity"->Table[{d,PolynomialRemainder[x^(57*d)-1,phi,x]=!=0},
                                      {d,Most[Divisors[70]]}]|>
]
