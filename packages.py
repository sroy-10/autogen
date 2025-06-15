import os
from dotenv import find_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential
from autogen_ext.models.azure import AzureAIChatCompletionClient
from autogen_ext.models.anthropic import AnthropicChatCompletionClient
from autogen_ext.auth.azure import AzureTokenProvider
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from azure.identity import DefaultAzureCredential
