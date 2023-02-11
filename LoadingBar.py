from tqdm import tqdm
import time

for _ in tqdm(range(100),
              desc="Hacking the system....",
              ascii=False):
    time.sleep(0.05)

print("...Done")
