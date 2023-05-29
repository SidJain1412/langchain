# flake8: noqa
PREFIX = """Assistant is a large language model trained by OpenAI.
It is able to process and understand large amounts of text, and can use this knowledge to provide the accurate and correct source that can be used to best answer a given question."""

FORMAT_INSTRUCTIONS = """RESPONSE FORMAT INSTRUCTIONS
----------------------------

When responding to me, please output a response in this format:
Markdown code snippet formatted in the following schema:

```json
{{{{
    "source": string \\ The source to use. Must be one of {tool_names}
}}}}
```
"""

SUFFIX = """SOURCES
------
Assistant can refer to these sources to look up information that may be helpful in answering the users original question. The sources it can use are:

{{tools}}

{format_instructions}

USER'S INPUT
--------------------
Here is the user's input (remember to respond with a markdown code snippet of a json blob with a single source, and NOTHING else):

{{{{input}}}}"""

TEMPLATE_TOOL_RESPONSE = " "
