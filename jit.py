"""
Azure JIT CLI Utility
"""

import os
import click
import requests

auth_token = os.environ["AZURE_TOKEN"]


@click.group()
def cli():

    """
    Azure JIT CLI Utility
    """


@click.command(name="activate")
@click.option(
    "--subscription_id",
    "-s",
    help="Enter your Azure Subscription ID",
    prompt="Azure Subscription ID",
    required=True,
)
@click.option(
    "--resource_group",
    "-r",
    help="Enter the name of your Resource Group",
    prompt="Resource Group Name",
    required=True,
)
@click.option(
    "--ip_address",
    "-i",
    help="Enter your public IP address",
    prompt="Your Public IP Address",
    required=True,
)
@click.option(
    "--location",
    "-l",
    help="Enter the Azure Location/Region Code",
    prompt="Azure Location/Region",
    required=True,
)
@click.option(
    "--justification",
    "-j",
    help="Enter your justification for enabling JIT",
    prompt="Justification Text",
    required=True,
)
@click.option(
    "--jit_policy_name",
    "-p",
    help="Enter the JIT Policy Name",
    prompt="JIT Policy Name",
    required=True,
)
def activate(
    subscription_id,
    resource_group,
    ip_address,
    location,
    justification,
    jit_policy_name,
):
    """
    Activate Just-in-Time
    """

    # TODO: Parameterise port number and duration
    payload = """
    {
      "virtualMachines": [
        {
          "id": "/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines/%s-jumphost",
          "ports": [
            {
              "number": 22,
              "duration": "PT1H",
              "allowedSourceAddressPrefix": "%s"
            }
          ]
        }
      ],
      "justification": "%s"
    }
""" % (
        subscription_id,
        resource_group,
        resource_group,
        ip_address,
        justification,
    )

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    params = {
        "api-version": "2020-01-01",
    }

    data = payload

    response = requests.post(
        f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Security/locations/{location}/jitNetworkAccessPolicies/{jit_policy_name}/initiate",
        params=params,
        headers=headers,
        data=data,
        timeout=300,
    )

    # TODO: Make this prettier
    print(response.text)


# TODO: Bring this into the CLI interface
def get_jit_policies():

    """
    Retrieve Just-in-Time Policies
    """

    headers = {
        "Authorization": f"Bearer {auth_token}",
    }

    params = {
        "api-version": "2020-01-01",
    }

    response = requests.get(
        f"https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.Security/jitNetworkAccessPolicies",
        params=params,
        headers=headers,
        timeout=300,
    )

    print(response.json())


# Commands:
cli.add_command(activate)

# Call the CLI:
cli()
