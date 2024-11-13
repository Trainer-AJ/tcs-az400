az group create -n leo -l westus
# be in the directory where you have the app files
az webapp up -g "leo" -l centralindia --html -n gh-action-098967 --sku F1
