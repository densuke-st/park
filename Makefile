ID=01

USER=0j02050
PASS=2pMv4pid

HOST=taiken-$(ID).local

#-----

.PHONY: repl setup venv install

sync:
	@echo "ソースコードを同期しています..."
	@sshpass -p $(PASS) rsync -auze ssh ~/park $(HOST):

run: sync
	@SSH_AUTH_SOCK= \
	sshpass -p $(PASS) \
	ssh -o UserKnownHostsFile=/dev/null \
            -o StrictHostKeyChecking=no \
	    -i ssh/taiken -t \
	    $(USER)@$(HOST) 'bash -c "cd park && source $$HOME/venv/bin/activate; python3 -i watch.py"'
	    
repl: sync
	@SSH_AUTH_SOCK= \
	sshpass -p $(PASS) \
	ssh -o UserKnownHostsFile=/dev/null \
            -o StrictHostKeyChecking=no \
	    -i ssh/taiken -t \
	    $(USER)@$(HOST) 'bash -c "cd park && source $$HOME/venv/bin/activate; python3 -i init.py"'
	    
setup: venv
	bash -c 'source ~/venv/bin/activate; pip3 install -r requirements.txt'

venv:
	-[ ! -d $$HOME/venv ] && python3 -m venv $$HOME/venv

install:
	cd setup; ansible-playbook site.yml
