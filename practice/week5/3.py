import re

def matcher(txt):
  pattern=r'(\b[a-z]+(_[a-z]+)+\b)*'
  x=re.search(pattern, txt)
  print(x)


txt=input()
matcher(txt)


#a_b_c_d_r_g_h...