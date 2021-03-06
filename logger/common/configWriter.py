import ConfigParser
import sys

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

assert len(sys.argv) == 5 

filepath = sys.argv[1]
section = sys.argv[2]
key = sys.argv[3]
value = sys.argv[4]

config.add_section(section)
config.set(section, key, value)

# check if this config already exsits in file
#try:
#  configRead = ConfigParser.SafeConfigParser()
#  configRead.read(filepath)
#  configRead.get(section, key)
#except:
  # Writing our configuration file to input filename
#  with open(filepath, 'a') as configfile:
#    config.write(configfile)
#    sys.exit(0)

#configRead.remove_option(section, key)
# Writing our configuration file to input filename
with open(filepath, 'a') as configfile:
  config.write(configfile)




