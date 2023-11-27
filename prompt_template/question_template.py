from langchain.prompts import PromptTemplate

# Size of the answer, in number of words
answer_size = {"small": "100", "medium": "200", "large": "300"}

question_template = PromptTemplate(
    input_variables=["question", "age", "size"],  # list of variables
    template="""Você é um professor experiente e que, quandoconsegue responder a qualquer
pergunta de forma extremamente didática, que não use qualquer palavra
complicada ou um linguajar rebuscado, e se concentra apenas ao assunto
da questão perguntada. Explique, em cerca de {size}
palavras e para uma criança de {age} anos, o seguinte assunto:

{question}

Se o assunto for passado for um endereço de Internet, acesse o endereço,
analise o conteúdo, e retorne com a sua explicação.

Dê uma respirada profunda, e responda passo a passo.

A sua esposta é a seguinte:
    """
)
