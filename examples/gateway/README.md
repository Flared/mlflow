# MLflow AI Gateway

The examples provided within this directory show how to get started with individual providers and at least
one of the supported route types. When configuring an instance of the MLflow AI Gateway, multiple providers,
instances of route types, and model versions can be specified for each query route on the Gateway.

## Example configuration files

Within this directory are example config files for each of the supported providers. If using these as a guide
for configuring a large number of routes, ensure that the placeholder names (i.e., "completions", "chat", "embeddings")
are modified to prevent collisions. These names are provided for clarity only for the examples and real-world
use cases should define a relevant and meaningful route name to eliminate ambiguity and minimize the chances of name collisions.

# Getting Started with MLflow AI Gateway for OpenAI

This guide will walk you through the installation and basic setup of MLflow AI Gateway.
Within sub directories of this examples section, you can find specific executable examples
that can be used to validate a given provider's configuration through the AI Gateway.
Let's get started.

## Step 1: Installing the MLflow AI Gateway

MLflow AI Gateway is best installed from PyPI. Open your terminal and use the following pip command:

```sh
# Installation from PyPI
pip install 'mlflow[gateway]'
```

For those interested in development or in using the most recent build of MLflow AI Gateway, you may choose to install from the fork of the repository:

```sh
# Installation from the repository
pip install -e '.[gateway]'
```

## Step 2: Configuring Endpoints

Each provider has a distinct set of allowable route types (i.e., chat, completions, etc) and
specific requirements for the initialization of the routes to interface with their services.
For full examples of configurations and supported route types, see:

- [OpenAI](openai/config.yaml)
- [MosaicML](mosaicml/config.yaml)
- [Anthropic](anthropic/config.yaml)
- [Cohere](cohere/config.yaml)
- [PaLM](palm/config.yaml)
- [AzureOpenAI](azure_openai/config.yaml)

## Step 3: Setting Access Keys

See information on specific methods of obtaining and setting the access keys within the provider-specific documentation within this directory.

## Step 4: Starting the MLflow Gateway Service

With the MLflow configuration file in place and access key(s) set, you can now start the MLflow Gateway service.
Replace `<provider>` with the actual path to the MLflow configuration file for the provider of your choice:

```sh
mlflow gateway start --config-path examples/gateway/<provider>/config.yaml
```

## Step 5: Accessing the Interactive API Documentation

With the MLflow Gateway Service up and running, access its interactive API documentation by navigating to the following URL:

http://127.0.0.1:5000/docs

## Step 6: Sending Test Requests

After successfully setting up the MLflow Gateway Service, you can send a test request using the provided Python script.
Replace <provider> with the name of the provider example test script that you'd like to use:

```sh
python examples/gateway/<provider>/example.py
```
