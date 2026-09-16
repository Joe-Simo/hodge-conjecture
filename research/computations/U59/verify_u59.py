#!/usr/bin/env python3
"""Exact checker for U59: dense-torus planes on the two degree-7 Delsarte quotients.

Requires SymPy >=1.14. All characteristic-zero Groebner calculations are exact over Q.
Finite-field plane censuses are exact over F_2 and F_3 and are corroboration only.
"""
from __future__ import annotations
import itertools
from collections import Counter, defaultdict
import sympy as sp

EX2=((4,0,0,0,2,1),(1,5,0,0,0,1),(1,2,3,0,1,0),(1,0,1,4,1,0),(0,0,3,1,1,2),(0,0,0,2,2,3))
EX3=((4,0,1,0,0,2),(1,5,0,0,1,0),(1,2,2,0,1,1),(1,0,1,4,0,1),(0,0,2,1,3,1),(0,0,1,2,2,2))

def partitions(seq):
    if not seq:
        yield ()
        return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield ((first,),)+rest
        for i in range(len(rest)):
            yield tuple((tuple(sorted((first,)+rest[j])) if j==i else rest[j]) for j in range(len(rest)))

def canon(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))

PARTS=sorted({canon(p) for p in partitions(tuple(range(6)))})

def valuation_good(ex, part):
    for block in part:
        vals=[sum(row[i] for i in block) for row in ex]
        m=min(vals)
        if vals.count(m)<2:
            return False
    return True

u,v,w=sp.symbols("u v w")
BASIS=(u,v,w)

def _identity_coeffs(ex, forms, scalars):
    expr=0
    for row in ex:
        term=1
        for i,e in enumerate(row):
            term *= (scalars[i]*forms[i])**e
        expr += term
    return sp.Poly(sp.expand(expr),u,v,w).coeffs()

def k3_unit(ex, part):
    forms=[None]*6; scalars=[None]*6; rel=[]
    for bidx,block in enumerate(part):
        form=BASIS[bidx]
        forms[block[0]]=form; scalars[block[0]]=sp.Integer(1)
        for idx in block[1:]:
            z=sp.Symbol(f"c{idx}")
            rel.append(z); forms[idx]=form; scalars[idx]=z
    eqs=_identity_coeffs(ex,forms,scalars)
    t=sp.Symbol("sat")
    G=sp.groebner(eqs+[t*sp.prod(rel)-1],*(rel+[t]),order="grevlex")
    return any(g.as_expr()==1 for g in G.polys)

def k4_unit(ex,part,basis_indices,chart):
    others=[i for i in range(4) if i not in basis_indices]
    other=others[0]
    forms=[None]*6; scalars=[None]*6; rel=[]; unknown=[]
    for form,bi in zip(BASIS,basis_indices):
        block=part[bi]; forms[block[0]]=form; scalars[block[0]]=sp.Integer(1)
        for idx in block[1:]:
            z=sp.Symbol(f"c{idx}"); rel.append(z); unknown.append(z); forms[idx]=form; scalars[idx]=z
    coeff=[]
    for j in range(3):
        if j==chart: coeff.append(sp.Integer(1))
        else:
            z=sp.Symbol(f"a{j}"); coeff.append(z); unknown.append(z)
    L=sum(coeff[j]*BASIS[j] for j in range(3))
    r=sp.Symbol("r"); unknown.append(r)
    block=part[other]; forms[block[0]]=L; scalars[block[0]]=r
    for idx in block[1:]:
        z=sp.Symbol(f"c{idx}"); rel.append(z); unknown.append(z); forms[idx]=L; scalars[idx]=r*z
    eqs=_identity_coeffs(ex,forms,scalars)
    t=sp.Symbol("sat")
    G=sp.groebner(eqs+[t*r*sp.prod(rel)-1],*(unknown+[t]),order="grevlex")
    return any(g.as_expr()==1 for g in G.polys)

def k5_unit(ex,part,basis_indices,chart):
    others=[i for i in range(5) if i not in basis_indices]
    forms=[None]*6; scalars=[None]*6; unknown=[]; sat=[]
    for form,bi in zip(BASIS,basis_indices):
        block=part[bi]; forms[block[0]]=form; scalars[block[0]]=sp.Integer(1)
        for idx in block[1:]:
            z=sp.Symbol(f"c{idx}"); unknown.append(z); sat.append(z); forms[idx]=form; scalars[idx]=z
    for oi in others:
        coeff=[]
        for j in range(3):
            if j==chart: coeff.append(sp.Integer(1))
            else:
                z=sp.Symbol(f"a{oi}_{j}"); unknown.append(z); coeff.append(z)
        L=sum(coeff[j]*BASIS[j] for j in range(3))
        r=sp.Symbol(f"r{oi}"); unknown.append(r); sat.append(r)
        block=part[oi]; forms[block[0]]=L; scalars[block[0]]=r
        for idx in block[1:]:
            z=sp.Symbol(f"c{idx}"); unknown.append(z); sat.append(z); forms[idx]=L; scalars[idx]=r*z
    eqs=_identity_coeffs(ex,forms,scalars)
    t=sp.Symbol("sat")
    G=sp.groebner(eqs+[t*sp.prod(sat)-1],*(unknown+[t]),order="grevlex")
    return any(g.as_expr()==1 for g in G.polys)

def rref_matrices(p):
    for piv in itertools.combinations(range(6),3):
        nonp=[j for j in range(6) if j not in piv]
        slots=[(r,j) for r,pc in enumerate(piv) for j in nonp if j>pc]
        for vals in itertools.product(range(p),repeat=len(slots)):
            M=[[0]*6 for _ in range(3)]
            for r,pc in enumerate(piv): M[r][pc]=1
            for (r,j),val in zip(slots,vals): M[r][j]=val
            yield M

def mul(A,B,p):
    out=defaultdict(int)
    for e,a in A.items():
        for f,b in B.items():
            g=(e[0]+f[0],e[1]+f[1],e[2]+f[2])
            out[g]=(out[g]+a*b)%p
    return {e:c for e,c in out.items() if c}

def linpow(vec,n,p):
    out={(0,0,0):1}
    L={(1,0,0):vec[0]%p,(0,1,0):vec[1]%p,(0,0,1):vec[2]%p}
    L={e:c for e,c in L.items() if c}
    for _ in range(n): out=mul(out,L,p)
    return out

def finite_census(ex,p):
    pre={(vec,n):linpow(vec,n,p) for vec in itertools.product(range(p),repeat=3) for n in range(8)}
    total=dense=0
    for M in rref_matrices(p):
        coord=[tuple(M[r][j] for r in range(3)) for j in range(6)]
        P=defaultdict(int)
        for row in ex:
            A={(0,0,0):1}
            for j,n in enumerate(row):
                if n: A=mul(A,pre[(coord[j],n)],p)
            for e,c in A.items(): P[e]=(P[e]+c)%p
        if any(P.values()): continue
        total += 1
        if not any(all(M[r][j]==0 for r in range(3)) for j in range(6)):
            dense += 1
    return total,dense

def main():
    summary={}
    for name,ex in (("A2",EX2),("A3",EX3)):
        good=[p for p in PARTS if len(p)>=3 and valuation_good(ex,p)]
        counts=Counter(map(len,good))
        assert all(len(p)<=5 for p in good)
        k3=[p for p in good if len(p)==3]
        assert all(k3_unit(ex,p) for p in k3)
        k4=[p for p in good if len(p)==4]
        k4cases=0
        for p in k4:
            for bas in itertools.combinations(range(4),3):
                for chart in range(3):
                    assert k4_unit(ex,p,bas,chart)
                    k4cases += 1
        k5=[p for p in good if len(p)==5]
        k5cases=0
        for p in k5:
            for bas in itertools.combinations(range(5),3):
                for chart in range(3):
                    assert k5_unit(ex,p,bas,chart)
                    k5cases += 1
        f2=finite_census(ex,2)
        f3=finite_census(ex,3)
        assert f2[1]==0 and f3[1]==0
        summary[name]={
            "valuation_patterns":dict(sorted(counts.items())),
            "k3_systems":len(k3),
            "k4_charts":k4cases,
            "k5_charts":k5cases,
            "F2_planes_total_dense":f2,
            "F3_planes_total_dense":f3,
        }
    assert summary["A2"]["valuation_patterns"]=={3:18,4:15,5:3}
    assert summary["A3"]["valuation_patterns"]=={3:10,4:6}
    assert summary["A2"]["k4_charts"]==180 and summary["A3"]["k4_charts"]==72
    assert summary["A2"]["k5_charts"]==90 and summary["A3"]["k5_charts"]==0
    assert summary["A2"]["F2_planes_total_dense"]==(84,0)
    assert summary["A3"]["F2_planes_total_dense"]==(109,0)
    assert summary["A2"]["F3_planes_total_dense"]==(233,0)
    assert summary["A3"]["F3_planes_total_dense"]==(312,0)
    print(summary)

if __name__=="__main__":
    main()
