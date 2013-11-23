from azure.storage import BlobService
import sys, argparse

# There is point of the argparse except for the help
parser = argparse.ArgumentParser(description='Azure Storage command-line client.')

parser.add_argument('-pwd')
parser.add_argument('-ls')
parser.add_argument('-cd', metavar=('destination'), nargs=1, type=str)
parser.add_argument('-rm', metavar=('pathToRemove'), nargs=1, type=str)
parser.add_argument('-cp', metavar=('sourcePath', 'destinationPath'), nargs=2, type=str)
parser.add_argument('-mv', metavar=('sourcePath', 'destinationPath'), nargs=2, type=str)
parser.add_argument('-copyFromLocal', metavar=('localPath', 'azurePath'), nargs=2, type=str)
parser.add_argument('-copyToLocal', metavar=('azurePath', 'localPath'), nargs=2, type=str)

arguments = parser.parse_args()

def pwd(args):
  print("todo")

def ls(args):
  print("todo")

def cd(args):
  print("todo")

def rm(args):
  print("todo")

def cp(args):
  print("todo")

def mv(args):
  print("todo")

def copyFromLocal(args):
  print("todo")

def copyToLocal(args):
  print("todo")

options = {
  '-pwd': pwd,
  '-ls': ls,
  '-cd': cd,
  '-rm': rm,
  '-cp': cp,
  '-mv': mv,
  '-copyFromLocal': copyFromLocal,
  '-copyToLocal': copyToLocal
}

def main(argv):
  options[argv[0]](argv[1:])

if __name__ == "__main__":
  main(sys.argv[1:])
