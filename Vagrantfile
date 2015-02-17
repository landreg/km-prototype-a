# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "landregistry/centos-beta"
  config.vm.network "forwarded_port", guest: 5001, host: 5001
  config.vm.provision "shell", path: "provision.sh"

end
