ID=01

USER=0j02050
PASS=2pMv4pid
RUN=watch

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
	    $(USER)@$(HOST) 'bash -xc "cd park && source $$HOME/venv/bin/activate; python3  $(RUN).py"'
	    
repl: sync
	@SSH_AUTH_SOCK= \
	sshpass -p $(PASS) \
	ssh -o UserKnownHostsFile=/dev/null \
            -o StrictHostKeyChecking=no \
	    -i ssh/taiken -t \
	    $(USER)@$(HOST) 'bash -c "cd park && source $$HOME/venv/bin/activate; python3 -i init.py"'
	    
setup:
	@SSH_AUTH_SOCK= \
	sshpass -p $(PASS) \
	ssh -o UserKnownHostsFile=/dev/null \
            -o StrictHostKeyChecking=no \
	    -i ssh/taiken -t \
	$(USER)@$(HOST)	bash -c '! test -d $$HOME/venv  && python3 -m venv $$HOME/venv; source ~/venv/bin/activate; cd park; pip3 install -r requirements.txt'

venv:
	-[ ! -d $$HOME/venv ] && python3 -m venv $$HOME/venv

install:
	cd setup; ansible-playbook site.yml

server: 
	bash ./run-server

led-1: 
	make run RUN=led-1

led-2: 
	make run RUN=led-2

