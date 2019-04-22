import os,sys
sys.path.append(os.path.join(os.getcwd(),'zeronet/src')) # TODO: Better solution

def new_pair():
  from src.Crypt import CryptBitcoin
  priv = CryptBitcoin.newPrivatekey()
  pub = CryptBitcoin.privatekeyToAddress(priv)
  return pub,priv


if __name__=='__main__':
  if sys.argv[1] == 'new':
    pub,priv = new_pair()
    print(pub)
    print(priv)