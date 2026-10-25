import numpy as np
f32=np.float32
print("=== 1. precision cliff: c = p*ln2 (p = mantissa bits incl. implicit) ===")
for name,p in [("bf16",8),("fp32",24),("fp64",53)]:
    print(f"  {name}: p={p} -> c={p*np.log(2):.2f}")
print("=== 2. equilibrium m* = ln(1/eps) ===")
for e in [1e-8,1e-7,1e-12,1e-16]:
    print(f"  eps={e:g} -> m*={np.log(1/e):.2f}")
print("=== 3. rounding of 1 + e^-m in fp32 ===")
for m in [12,16,16.6,17,18,20]:
    d=f32(1.0)+f32(np.exp(-m))
    print(f"  m={m:5.1f} e^-m={np.exp(-m):.3e} -> 1+e^-m = {d!r}  (==1.0? {d==f32(1.0)})")
print("=== 4. example z=[9,-9,-9], t=0 (fp32) ===")
z=np.array([9.,-9.,-9.],dtype=f32); t=0
others=z[np.arange(3)!=t]
m=z[t]-np.log(np.sum(np.exp(others),dtype=f32))
print(f"  margin m = {m:.6f}   e^-m = {np.exp(-m):.6e}")
zm=z.max(); lse=np.log(np.sum(np.exp(z-zm),dtype=f32),dtype=f32)
logq=(z-zm)-lse; q=np.exp(logq)
print(f"  standard log-softmax = {logq}")
print(f"  standard g_t = q_t-1 = {q[t]-1.0}   g_others = {q[1:]}")
print(f"  standard sum(g) = {np.sum(np.where(np.arange(3)==t,q-1,q)):.6e}")
print(f"  fixed g_t = -e^-m/(1+e^-m) = {-np.exp(-m)/(1+np.exp(-m)):.6e}")
print(f"  fixed sum(g) = exactly 0 by construction")
print("=== 5. exercise answers ===")
print("  Q1 softmax [0,0,0] ->", np.exp(0)/3)
print("  Q2 z_t=5, others [0,0]: m = 5 - ln2 =", 5-np.log(2))
print("  Q3 q_t at m=15:", 1/(1+np.exp(-15)), " 1-q_t =", np.exp(-15)/(1+np.exp(-15)))
print("  Q4 normalized adam step |g|/(|g|+eps), eps=1e-8:")
for g in [1e-2,1e-8,3e-8,1e-10,1e-13]:
    print(f"     |g|={g:.0e} -> {g/(g+1e-8):.4f}")
print("  Q5 log(1/1e-7) =", np.log(1e7))
print("  Q6 e^-17 =", np.exp(-17), " half ulp of 1 in fp32 =", 2**-24)
print("  Q7 two non-target grads sum:", 2*1.523e-8)
print("  Q8 m for eps=1e-16 =", np.log(1e16))
