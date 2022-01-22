import os,sys,time

os.system('clear')
time.sleep(2)
print("""
TOOLS LOADING
INI HANYA CONTOH NGAB
MAKASIH DAH NONTON
""")
load = '~'
count = 0
proses = "\rLoading"

for x in range(101):
  time.sleep(0.1)
  print(proses, load, x, "%", end='', flush=True)
  count += 1
  if count == 20:
    count = 0
    load += '~'
time.sleep(2)
print("\nLoading selesai")
