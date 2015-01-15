#!/usr/local/bin/python

import shutil
import yaml
import os


import docker_registry.drivers.gitdriver

config_path = os.environ.get('DOCKER_REGISTRY_CONFIG', 'config.yml')
if not os.path.isabs(config_path):
        config_path = os.path.join(os.path.dirname(__file__), 
                                   'config', config_path)
flavor = os.environ.get('SETTINGS_FLAVOR', 'dev')
print config_path


def envVar(var):
	# Parse yaml variable
	# Return value of env.variable or value from var
	if var.find("_env:") >=0:
		parts = var.split(":")
		if parts[1] is not None:
			default = parts[len(parts)-1]
			value = os.environ.get(parts[1],default)
			return value
		else:
			print "Wrong format: "+var
			return var
	else:
		return var

try:
    f = open(config_path)
except Exception:
    print "Heads-up! File is missing: "+ config_path

try:
    conf = yaml.load(f.read())
except Exception as e:
    # Failed yaml loading? Stop here!
    print "Config is not valid yaml" + e + "\nconfig:\n" + conf


if flavor:
    conf = conf[flavor]
    
print flavor 
print conf

storage_path = envVar(conf["storage_path"])
db = envVar(conf["sqlalchemy_index_database"])
print db
try :
	os.remove(db)
	print db
except OSError:
	pass

dirs = [
	docker_registry.drivers.gitdriver.working_dir, 
	docker_registry.drivers.gitdriver.storage_dir,
	docker_registry.drivers.gitdriver.imagetable,
	"images"
]

print storage_path

for dir in dirs:
	print dir
	target = os.path.join(storage_path,dir)	
	try:
		shutil.rmtree(target)
		print target
	except OSError as ex:
		try:
			os.remove(target)
			print target
		except OSError as ex:
			print "Cannot remove "+ str(target)

"""
rm -rf /Users/peterbryzgalov/tmp/gitrepo 
rm -rf /Users/peterbryzgalov/tmp/gitregistry 
rm -rf /private/tmp/docker-registry.db
rm -rf /Users/peterbryzgalov/tmp/git_tmp
rm /Users/peterbryzgalov/tmp/git_imagetable.txt
kill $(ps ax | grep ":5000" | awk '{ print $1 }')
./registry-start

"""
