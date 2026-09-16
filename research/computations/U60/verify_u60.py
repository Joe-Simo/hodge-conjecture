from __future__ import annotations
from itertools import product, combinations
from fractions import Fraction
from math import gcd, lcm
from collections import Counter

ALPHA=(1,20,24,42,61,62)
A_STAR=(
    (3,1,0,2,0,0),
    (3,0,2,1,0,0),
    (0,1,2,2,1,0),
    (1,0,0,0,0,5),
    (3,1,2,0,0,0),
    (1,2,0,0,3,0),
)

def det_int(M):
    A=[list(map(Fraction,row)) for row in M]
    n=len(A); d=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None:return 0
        if p!=c:A[c],A[p]=A[p],A[c];d=-d
        q=A[c][c];d*=q
        for j in range(c,n):A[c][j]/=q
        for r in range(c+1,n):
            q=A[r][c]
            if q:
                for j in range(c,n):A[r][j]-=q*A[c][j]
    assert d.denominator==1
    return d.numerator

def inv_and_cover(M):
    n=len(M); A=[[Fraction(M[i][j]) for j in range(n)]+[Fraction(i==j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if A[r][c])
        if p!=c:A[c],A[p]=A[p],A[c]
        q=A[c][c]
        for j in range(2*n):A[c][j]/=q
        for r in range(n):
            if r!=c and A[r][c]:
                q=A[r][c]
                for j in range(2*n):A[r][j]-=q*A[c][j]
    inv=[row[n:] for row in A]
    m=1
    for row in inv:
        for x in row:m=lcm(m,x.denominator)
    return inv,m

def candidates(d):
    return [v for v in product(range(d+1),repeat=6)
            if any(v) and sum(a*b for a,b in zip(ALPHA,v))%70==0]

def find_matrix(d):
    C=candidates(d); tgt=(d,)*6; nodes=0
    def rec(start,chosen,s):
        nonlocal nodes;nodes+=1
        if len(chosen)==6:
            if s==tgt:
                cols=[C[i] for i in chosen]
                M=tuple(tuple(cols[j][r] for j in range(6)) for r in range(6))
                if det_int(M):return chosen,M
            return None
        need=6-len(chosen)
        for i in range(start,len(C)-need+1):
            ns=tuple(s[r]+C[i][r] for r in range(6))
            if any(x>d for x in ns):continue
            out=rec(i+1,chosen+(i,),ns)
            if out:return out
        return None
    return C,rec(0,(),(0,)*6),nodes

def subgroup_from_rows(rows,m):
    S={(0,)*6}
    for g in rows:
        S={tuple((s[j]+k*g[j])%m for j in range(6)) for s in S for k in range(m)}
    return S

def lpr(x,m):
    r=x%m;return m if r==0 else r

def hodge_audit():
    inv,m=inv_and_cover(A_STAR); assert m==210
    B=tuple(tuple(int(m*x) for x in row) for row in inv)
    S=subgroup_from_rows(B,m)
    units=[u for u in range(1,m) if gcd(u,m)==1]
    prim=[a for a in S if all(a) and sum(a)%m==0]
    dist=Counter(sum(lpr(x,m) for x in a) for a in prim)
    def rat(a):return all(sum(lpr(u*x,m) for x in a)==3*m for u in units)
    rats=[a for a in prim if rat(a)]
    rem=set(rats);orbits=[]
    while rem:
        a=next(iter(rem));o={tuple((u*x)%m for x in a) for u in units};orbits.append(o);rem-=o
    target=tuple((3*x)%m for x in ALPHA)
    return m,B,len(S),len(prim),dist,len(rats),list(map(len,orbits)),target in S,rat(target),any(target in o for o in orbits)

def esser_block_hit():
    C=candidates(6)
    small=[(i,v) for i,v in enumerate(C) if max(v)<=2]
    examples=[]
    for k in range(1,6):
        for comb in combinations(small,k):
            ids=tuple(x[0] for x in comb)
            q=tuple(sum(x[1][r] for x in comb) for r in range(6))
            if all(x in (1,2) for x in q) and 1 in q:
                examples.append((ids,q))
    assert examples==[((C.index((1,1,1,1,1,1)),),(1,1,1,1,1,1))]
    selected=set(examples[0][0]); target=(5,)*6; ids0=examples[0][0]
    def rec(start,chosen,s):
        if len(chosen)==5:
            if s==target:
                ids=ids0+tuple(chosen);cols=[C[i] for i in ids]
                M=tuple(tuple(cols[j][r] for j in range(6)) for r in range(6))
                return bool(det_int(M))
            return False
        need=5-len(chosen)
        for i in range(start,len(C)-need+1):
            if i in selected:continue
            ns=tuple(s[r]+C[i][r] for r in range(6))
            if any(x>5 for x in ns):continue
            if rec(i+1,chosen+[i],ns):return True
        return False
    return len(C),len(small),examples,rec(0,[],(0,)*6)

def main():
    counts={}; witnesses={};nodes={}
    for d in range(2,7):
        C,w,n=find_matrix(d);counts[d]=len(C);nodes[d]=n;witnesses[d]=w
    assert counts=={2:12,3:59,4:230,5:663,6:1716}
    assert all(witnesses[d] is None for d in range(2,6)) and witnesses[6] is not None
    assert all(sum(row)==6 for row in A_STAR)
    assert det_int(A_STAR)==420
    atalpha=tuple(sum(A_STAR[r][c]*ALPHA[r] for r in range(6)) for c in range(6))
    assert atalpha==(350,210,210,70,210,210)
    assert all(x%70==0 for x in atalpha)
    m,B,sub,prim,dist,nrat,osizes,tin,trat,torb=hodge_audit()
    assert (m,sub,prim,nrat,osizes,tin,trat,torb)==(210,420,48,24,[24],True,True,True)
    assert dist==Counter({630:40,420:4,840:4})
    _,small,_,hit=esser_block_hit();assert not hit
    assert any(a%5 for a in ALPHA) and any(a%7 for a in ALPHA)
    print({"candidate_counts":counts,"search_nodes":nodes,"degree6_exists":True,
           "A_star_det":420,"A_star_cover":m,"A_star_ATalpha":atalpha,
           "invariant_subgroup":sub,"primitive":prim,
           "hodge_sum_distribution":dict(dist),"rational_hodge_characters":nrat,
           "rational_orbit_sizes":osizes,"target_orbit":torb,
           "esser_small_columns":small,"esser_block_hit":hit})

if __name__=='__main__':main()
