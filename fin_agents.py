import streamlit as st
from crewai import Agent, LLM


llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API"],
)


class FinAgents:

    def researcher(self):
        return Agent(
            role="Financial Researcher",
            goal="Research financial markets and companies",
            backstory="Expert financial researcher who collects market data.",
            llm=llm,
            verbose=True
        )


    def analyst(self):
        return Agent(
            role="Financial Analyst",
            goal="Analyze financial data and generate insights",
            backstory="Expert in financial analysis and investment research.",
            llm=llm,
            verbose=True
        )


    def advisor(self):
        return Agent(
            role="Investment Advisor",
            goal="Provide investment recommendations",
            backstory="Experienced investment advisor.",
            llm=llm,
            verbose=True
        )


class StreamToExpander:

    def __init__(self, expander):
        self.expander = expander

    def write(self, text):
        self.expander.write(text)

    def flush(self):
        pass
