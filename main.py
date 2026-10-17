import io, re
from io import BytesIO
import streamlit as st
from huggingface_hub import InferenceClient
import config

from hf import generate_response

MATH_SYSTEM = """
- You are a math mastermind. 
- Solve with clear and concise steps-by-step reasoning. 
- Verify your answers whenever possible.
"""

CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.card{border:1px solid #e6e6e6; background:#fff;border-radius: 8px; padding: 10px; margin: 10px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.1);}
.meta{display:inline-block; font-size: 12px; color: #999; margin-bottom: 5px;}
.a{whitespace: pre-wrap; word-wrap: break-word;}
</style>
"""

def export_txt(chat_history):
    txt = "".join([f"{role}: {content}\n" for role, content in chat_history])
    bio = BytesIO()
    bio.write(txt.encode())
    bio.seek(0)
    return bio