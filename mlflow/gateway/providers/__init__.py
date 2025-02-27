from mlflow.exceptions import MlflowException
from mlflow.gateway.config import Provider
from mlflow.gateway.providers.ai21labs import AI21LabsProvider
from mlflow.gateway.providers.anthropic import AnthropicProvider
from mlflow.gateway.providers.base import BaseProvider
from mlflow.gateway.providers.cohere import CohereProvider
from mlflow.gateway.providers.mlflow import MlflowModelServingProvider
from mlflow.gateway.providers.mosaicml import MosaicMLProvider
from mlflow.gateway.providers.openai import OpenAIProvider
from mlflow.gateway.providers.palm import PaLMProvider


def get_provider(provider: Provider) -> BaseProvider:
    provider_to_class = {
        Provider.OPENAI: OpenAIProvider,
        Provider.ANTHROPIC: AnthropicProvider,
        Provider.COHERE: CohereProvider,
        Provider.AI21LABS: AI21LabsProvider,
        Provider.MOSAICML: MosaicMLProvider,
        Provider.PALM: PaLMProvider,
        Provider.MLFLOW_MODEL_SERVING: MlflowModelServingProvider,
    }
    if prov := provider_to_class.get(provider):
        return prov

    raise MlflowException.invalid_parameter_value(f"Provider {provider} not found")
