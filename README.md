# DiTool Chat(GPT)bot

DiTool is an innovative chatbot designed to streamline the process of quiz taking and provide instantaneous evaluation, leveraging the capabilities of the ChatGPT API. This advanced tool has been developed with the support of TLIC (Technology and Learning Innovation Center) at Chiang Mai University (CMU), specifically for the course "888212 Digital Tools for Entrepreneurs" offered at the International College of Digital Innovation.

The primary aim of DiTool is to facilitate an interactive learning environment where students can engage in quizzes and receive immediate feedback on their answers. This instant evaluation process not only enhances learning efficiency but also allows students to quickly identify areas where they need improvement, fostering a more personalized learning experience.

By integrating the ChatGPT API, DiTool taps into state-of-the-art natural language processing and machine learning technologies. This enables the chatbot to understand and evaluate complex student responses, making it a highly effective tool for assessing a wide range of subject matters and question types. Whether it's a straightforward factual question or one that requires critical thinking and analysis, DiTool is equipped to provide accurate and insightful evaluations.

The support from TLIC, CMU underscores the institution's commitment to embracing digital innovation in education. This project serves as a testament to the potential of AI and chatbot technology in transforming traditional educational practices, making learning more accessible, engaging, and effective.

For those interested in exploring DiTool and its features, more information can be found by visiting the provided link: [https://cmu.to/DiToolQuiz	](https://cmu.to/DiToolQuiz	). This link offers direct access to the chatbot, allowing educators, students, and digital innovation enthusiasts to experience firsthand the benefits of integrating AI-driven tools into the educational process.

In summary, DiTool represents a significant advancement in educational technology, offering a powerful tool for immediate quiz evaluation. Supported by TLIC, CMU, and designed for the course "888212 Digital Tools for Entrepreneurs," it exemplifies how digital innovations can enhance learning outcomes and prepare students for success in the digital age.


## Understanding the ChatGPT Prompt

A prompt in ChatGPT is essentially a string of text that serves as an instruction for the model. This string can range from a single character to a full-length article. The clarity and specificity of a prompt are crucial, as they directly influence the effectiveness of ChatGPT's responses. A well-crafted prompt can yield precise and relevant answers, while a vague or poorly formulated prompt may lead to unsatisfactory responses.


## Understanding ChatGPT Integration for Developers

### Prerequisites
- Python installed on your machine.
- An OpenAI API key.

### Setup and Installation

1. **Install the OpenAI Python package:**
   ```bash
   pip install openai
   ```

2. **Setup your API key:**
   Replace `sk-xxxxx` with your actual OpenAI API key.
   ```python
   OPENAI_API_KEY = "sk-xxxxx"
   ```

### Example Code

Here is a sample Python script that demonstrates how to use the OpenAI API to make a request to ChatGPT:

```python
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

# Create a completion request to the ChatGPT model
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Model identifier
    messages=[
        {"role": "system", "content": "You are a nurse taking care of kids"},
        {"role": "user", "content": "What food one year old can eat?"}
    ],
)
```

### Explanation of Code Components

- **OpenAI Client**: This is used to interact with the OpenAI API, requiring the API key for authentication.
- **OPENAI_API_KEY**: Your unique API key for accessing OpenAI services; ensure this key remains confidential.
- **Client Instance**: Establishes a session with the OpenAI API using your API key.
- **Response**: Holds the data returned from the ChatGPT model based on the input provided.
- **Model**: Specifies the version of the ChatGPT model to use (e.g., `gpt-3.5-turbo`).
- **Messages**: A list of message dictionaries that set the context and user query:
  - **Role**: Defines the role of each message (`system` for context setting, `user` for query).
  - **Content**: The actual text of each message.

### ChatGPT API Response Structure

For the repsonse, its structure will be as follow:

```plaintext
response = ChatCompletion(
    id='chatcmpl-9HOB3QHg8wb2AWaMeHpYJnWzMLd1F',
    model='gpt-3.5-turbo-0125',
    object='chat.completion',
    created=1713931541,
    system_fingerprint='fp_c2295e73ad',
    usage=CompletionUsage(
        completion_tokens=193,
        prompt_tokens=28,
        total_tokens=221
    ),
    choices=[
        Choice(
            index=0,
            finish_reason='stop',
            logprobs=None,
            message=ChatCompletionMessage(
                content="For a one-year-old child, it is important to provide a variety of nutritious foods to support their growth and development. Some good food options for a one-year-old child include:\n\n1. Soft fruits such as mashed bananas, avocado, or cooked apples\n2. Soft cooked vegetables like sweet potatoes, carrots, and peas\n3. Whole grain cereals and bread\n4. Protein sources like soft-cooked eggs, tofu, or finely minced meat or poultry\n5. Dairy products such as whole milk, yogurt, or cheese\n6. Iron-rich foods like fortified cereals, beans, and lentils\n7. Small pieces of soft fruit or vegetables for self-feeding practice\n\nIt is important to introduce a variety of textures and flavors to help your child develop healthy eating habits. Additionally, always make sure the food is cut into small, manageable pieces to prevent choking hazards. Be sure to consult with your child's pediatrician for more personalized dietary recommendations.",
                role='assistant'
            )
        )
    ]
)
```

This breakdown helps in understanding the various components of the response from the ChatGPT API:

- **ID**: Unique identifier for the completion.
- **Model**: Specifies the ChatGPT model version used for generating the response.
- **Object**: Type of the API object.
- **Created**: Timestamp when the response was generated.
- **System Fingerprint**: System-specific identifier.
- **Usage**: Tokens usage details including completion, prompt, and total tokens.
- **Choices**: Contains the response messages. Each choice includes:
  - **Index**: Position of the choice.
  - **Finish Reason**: Reason why the generation of the completion was stopped.
  - **Logprobs**: Log probabilities of the outputs (not used in this instance).
  - **Message**: The content returned by the assistant, including the role which specifies it as an 'assistant' response.

### What need for users

As you can see, the structure of ChatGPT response is quit complex. However, what user really need is th Message which can only use the line

```python
message_response_to_user = completion.choices[0].message.content
```

which the return as 

```plaintext
For a one-year-old child, it is important to provide a variety of nutritious foods to support their growth and development. Some good food options for a one-year-old child include:\n\n1. Soft fruits such as mashed bananas, avocado, or cooked apples\n2. Soft cooked vegetables like sweet potatoes, carrots, and peas\n3. Whole grain cereals and bread\n4. Protein sources like soft-cooked eggs, tofu, or finely minced meat or poultry\n5. Dairy products such as whole milk, yogurt, or cheese\n6. Iron-rich foods like fortified cereals, beans, and lentils\n7. Small pieces of soft fruit or vegetables for self-feeding practice\n\nIt is important to introduce a variety of textures and flavors to help your child develop healthy eating habits. Additionally, always make sure the food is cut into small, manageable pieces to prevent choking hazards. Be sure to consult with your child's pediatrician for more personalized dietary recommendations.
```


<!-- If you use this code or our findings in your research, please cite our paper as follows: -->

<!-- ```bibtex
@article{Tepsan_Comparative_Analysis_of_2024,
  author = {Tepsan, Worawit and Watcharapinchai, Sitapa and Lueangwitchajaroen, Pitiwat and Sooksatra, Sorn},
  doi = {10.0000/00000},
  journal = {Journal Title},
  month = sep,
  number = {1},
  pages = {1--6},
  title = {{Comparative Analysis of Adaptive ROI Approaches in Human Action Recognition}},
  volume = {1},
  year = {2024}
} -->
