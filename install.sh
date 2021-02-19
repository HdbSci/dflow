#=====================#
#        dflow        #
#   Installer script  #
#=====================#

# Made by HdbSci
# Visit https://github.com/HdbSci/dflow


get_repo() {
	git clone https://github.com/HdbSci/dflow
}

build() {
	cd dflow && python3 setup.py sdist bdist_wheel
}

install() {
	pip3 install dflow/dist/dflow-1.0.0-py3-none-any.whl
}



#==== main ====#
echo "Getting source code from GitHub..."
get_repo > /dev/null

echo "Building dflow wheel file..."
build > /dev/null

echo "Installing dflow..."
install > /dev/null

echo "Done!"
