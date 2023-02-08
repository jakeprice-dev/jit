# Azure JIT (Just-in-Time) CLI Utility

In lieu of a way to do it using the Azure CLI, and frustrated by the constant need to login to the Azure GUI console to enable Just-in-Time, this is a little Python CLI I've made to enable Just-in-Time on a Virtual Machine from my terminal, using the Azure API.

## Install CLI

```sh
pip3 install -r requirements.txt
pip3 install .
```

## Bash Completion

### Generate Completion File

```sh
_JIT_COMPLETE=bash_source jit > ./.jit-complete.bash
```

### Enable Completion

Source the above file in your `.bashrc` file.

```sh
. <path-to-repo>/.jit-complete.bash
```

## Retrieve an Azure API Token

The API request needs an authorisation token to successfully authenticate. 

For now I just run the below when my current token has expired, and the script will grab the token from the `AZURE_TOKEN` environment variable. The CLI will error if `AZURE_TOKEN` doesn't exist.

```sh
export AZURE_TOKEN=$(az account get-access-token | jq -r '.accessToken')
```

## Enable JIT

The utility will prompt you for the required parameters, but they can also be provided as below.

```sh
python3 main.py activate \
    --justification "" \
    --location <region> \
    --jit_policy_name <policy-name>
    --subscription_id <subscription-id> \
    --resource_group <resource-group> \
    --ip_address <your-public-ip>
```

