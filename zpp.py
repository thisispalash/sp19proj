''' Main entry point to the app/service '''

import sys
import os
import getpass
import json


def be_vain(inp=''):
  from zeronet.Vanity import VanityGenerator
  pub,priv,ct = VanityGenerator.generate_address(contains=inp)
  return pub.decode(),priv.decode()

def gen_addr():
  return be_vain()

def sign_site():
  pass

def deploy():
  pass

def extract_files():
  # Unizip uploaded: https://stackoverflow.com/questions/3451111/unzipping-files-in-python
  # check compatibility
  pass

if __name__ == '__main__':
      
  print(__file__)

  if not os.path.isfile('gen.json'):
    json.dump({},open('gen.json','w'))

  if len(sys.argv) == 1:
    while True:
      print('1. Start zeronet\n2. Create zite\n3. Update zite\n4. Sign zite\n5. Exit')
      c = int(input('?: '))
      if c==1: pass
      elif c==2:
        print('1. Random\n2. Vanity')
        c2 = int(input('?: '))
        if c2==1:
          sys.argv.append('siteCreate')
          # TODO open site
        elif c2==2:
          arg = input("Enter choice of substring(use quotes): ")
          # van_bit = call("python3 Vanity/VanityGenerator.py -c " + arg, shell=True)
          VanityGenerator.generate_address(contains=arg)
          continue
      elif c==3:
        addr = raw_input('Site Address: ')
        dir = os.path.join(os.path.join(os.path.dirname(__file__),'data'),addr)
        print('goto %s to edit the contents of your zero site' % dir)
        continue
      elif c==4:
        addr = raw_input('Site Address: ')
        print('1. Enter private key\n2. Get from data')
        c2 = int(input('?: '))
        if c2==1:
          priv = getpass.getpass('private key: [input hidden]')
        elif c2==2:
          d = dict()
          with open('gen.json') as f: d = json.load(f)
          priv = d[addr]['key']
          if not priv:
            print('private key not found. Enter key below')
            priv = getpass.getpass('private key: [input hidden]')
        sys.argv.append('siteSign')
        sys.argv.append(addr)
        sys.argv.append(priv)
      elif c==5:
        print('bye.')
        exit(1)
      print(sys.argv)
      from zeronet.zeronet import main
      main()
  else:
    if sys.argv[1] == 'help':
      print('call `python2 zpp.py` and follow onscreen instructions')
      exit(1)
    else:
      print('invalid call. Try again!')
      exit(1)