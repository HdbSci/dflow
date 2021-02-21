#=====================#
#        dflow        #
#   Installer script  #
#=====================#

# Made by HdbSci
# Visit https://github.com/HdbSci/dflow


#==== main ====#
echo "Getting source code from GitHub..."
git clone https://github.com/HdbSci/dflow.git > /dev/null

echo "Installing dflow..."
cd dflow && python3 setup.py install > /dev/null

echo "Deleting source files..."
rm -r dflow > /dev/null

echo "Done!"
