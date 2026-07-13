import streamlit as st
import re
from crewai import Agent, LLM


# LLM Configuration
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API"]
)


class FinAgents:

    def __init__(self):
        self.llm = llm


    def financial_researcher(self):
        return Agent(
            role="Financial Research Analyst",
            goal="Collect and analyze financial market information",
            backstory=(
                "You are an expert financial analyst who gathers "
                "stock market data, news, and financial insights."
            ),
            llm=self.llm,
            verbose=True
        )


    def financial_analyst(self):
        return Agent(
            role="Financial Analyst",
            goal="Analyze financial data and provide investment insights",
            backstory=(
                "You specialize in analyzing company performance, "
                "financial statements, and market trends."
            ),
            llm=self.llm,
            verbose=True
        )


    def investment_advisor(self):
        return Agent(
            role="Investment Advisor",
            goal="Provide investment recommendations based on analysis",
            backstory=(
                "You provide clear financial advice using research "
                "and market analysis."
            ),
            llm=self.llm,
            verbose=True
        )


class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander

    def write(self, text):
        self.expander.write(text)

    def flush(self):
        pass
