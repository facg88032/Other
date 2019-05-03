import argparse

p=argparse.ArgumentParser()
p.add_argument('--subtype',required=False,default='mp4')
p.add_argument('--url',required=False,default='')
args=p.parse_args()
subtype=args.subtype
url=args.url

print(subtype)
print(url)