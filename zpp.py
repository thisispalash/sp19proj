''' Main entry point to the app/service '''

import sys
import os
import getpass
import json


def be_vain(inp=''):
  from zeronet.Vanity import VanityGenerator
  pub,priv,ct = VanityGenerator.generate_address(contains=inp)
  return 'Public = ' + pub.decode(),'\nPrivate = '+ priv.decode()

def sign_site():
  pass

def deploy():
  pass

def extract_files(addr,dir):
  import zipfile
  zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')#TODO: how to get the path of uploaded zip
  return zip_ref.extractall(dir) #haven't tested


if __name__ == '__main__':
      
  print(__file__)

  if not os.path.isfile('gen.json'):
    json.dump({},open('gen.json','w'))
  i=1
  if len(sys.argv) == 1:
    while (i==1):
      print('1. Start zeronet --py2\n2. Create zite rand --py2 vanity --py3\n3. Update zite --py2\n4. Sign zite\n5. Exit')
      c = int(input('?: '))
      if c==1: pass
      elif c==2:
        print('1. Random --py2\n2. Vanity --py3')
        c2 = int(input('?: '))
        if c2==1:
          sys.argv.append('siteCreate')
          # TODO open site
        elif c2==2:
          arg = input("Enter choice of substring(use quotes): ")
          print(be_vain(arg))
          continue
      elif c==3:
        addr = raw_input('Site Address: ')
        if len(addr)==0:
          print('\nEnter site address...please!\n')
        else:
          dir = os.path.join(os.path.join(os.path.dirname(__file__),'zeronet/data'),addr)
          extract_files(addr,dir)
          print('goto %s to edit the contents of your zero site' % dir)
        continue
      elif c==4:
        addr = raw_input('Site Address: ')
        if len(addr)==0:
          print('\nEnter site address...please!\n')
        else:
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
      i+=1
  else:
    if sys.argv[1] == 'help':
      print('call `python2 zpp.py` and follow onscreen instructions')
      exit(1)
    else:
      print('invalid call. Try again!')
      exit(1)