

import os
import sys

# Assuming we run from the ostentatious-ai git repo, put that path
# on python's search path so "import ostentatious_ai" reads the copy of
# ostentatious_ai/__init__.py in the git repo, not another installed version.
sys.path.insert(
  0, os.path.dirname( os.path.dirname(__file__) )
)

import ostentatious_ai

# yeah yeah I'm being pedantic.
if __name__ == '__main__':

  print(f'ostentatious_ai={ostentatious_ai}')


