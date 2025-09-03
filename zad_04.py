"""
 • Stranice trokuta, površinu trokuta (P = 𝑎 ∗𝑣𝑎2 , 𝑣𝑎 je visina na stranicu a) te opseg trokuta.
"""
a = 8.0    # stranica a
v = 5.0    # visina na stranicu a
b = 6.0    # stranica b
c = 7.0    # stranica c

# Površina trokuta
povrsina_trokuta = (a * v) / 2

# Opseg trokuta
opseg_trokuta = a + b + c

print(f"Stranica a: {a} cm")
print(f"Visina na stranicu a (v): {v} cm")
print(f"Stranica b: {b} cm")
print(f"Stranica c: {c} cm")
print(f"Površina trokuta: {povrsina_trokuta} cm²")
print(f"Opseg trokuta: {opseg_trokuta} cm")