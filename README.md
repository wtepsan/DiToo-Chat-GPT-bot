# DiTool Chat(GPT)bot

DiTool is an innovative chatbot designed to streamline the process of quiz taking and provide instantaneous evaluation, leveraging the capabilities of the ChatGPT API. This advanced tool has been developed with the support of TLIC (Technology and Learning Innovation Center) at Chiang Mai University (CMU), specifically for the course "888212 Digital Tools for Entrepreneurs" offered at the International College of Digital Innovation.

The primary aim of DiTool is to facilitate an interactive learning environment where students can engage in quizzes and receive immediate feedback on their answers. This instant evaluation process not only enhances learning efficiency but also allows students to quickly identify areas where they need improvement, fostering a more personalized learning experience.

By integrating the ChatGPT API, DiTool taps into state-of-the-art natural language processing and machine learning technologies. This enables the chatbot to understand and evaluate complex student responses, making it a highly effective tool for assessing a wide range of subject matters and question types. Whether it's a straightforward factual question or one that requires critical thinking and analysis, DiTool is equipped to provide accurate and insightful evaluations.

The support from TLIC, CMU underscores the institution's commitment to embracing digital innovation in education. This project serves as a testament to the potential of AI and chatbot technology in transforming traditional educational practices, making learning more accessible, engaging, and effective.

For those interested in exploring DiTool and its features, more information can be found by visiting the provided link: [DiTool Quiz](https://cmu.to/DiToolQuiz). This link offers direct access to the chatbot, allowing educators, students, and digital innovation enthusiasts to experience firsthand the benefits of integrating AI-driven tools into the educational process.

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

# Print the response from ChatGPT
print(response)
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

For the response, its structure will be as follows:

```plaintext
response = ChatCompletion(
    id='chatcmpl-9HOB3QHg8wb2

AWaMeHpYJnWzMLd1F',
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

### What Users Really Need

As you can see, the structure of a ChatGPT response is quite complex. However, what users really need is the message which can be obtained using the line:

```python
message_response_to_user = response.choices[0].message.content
```

which returns as:

```plaintext
For a one-year-old child, it is important to provide a variety of nutritious foods to support their growth and development. Some good food options for a one-year-old child include:\n\n1. Soft fruits such as mashed bananas, avocado, or cooked apples\n2. Soft cooked vegetables like sweet potatoes, carrots, and peas\n3. Whole grain cereals and bread\n4. Protein sources like soft-cooked eggs, tofu, or finely minced meat or poultry\n5. Dairy products such as whole milk, yogurt, or cheese\n6. Iron-rich foods like fortified cereals, beans, and lentils\n7. Small pieces of soft fruit or vegetables for self-feeding practice\n\nIt is important to introduce a variety of textures and flavors to help your child develop healthy eating habits. Additionally, always make sure the food is cut into small, manageable pieces to prevent choking hazards. Be sure to consult with your child's pediatrician for more personalized dietary recommendations.
```

## ChatGPT API Integration with FastAPI

To tailor ChatGPT for your specific user base, we need to develop a backend platform. For the user interface, users will input prompts which require integration with a frontend. There are several options for web frameworks and platforms to achieve this, but for our application, we will use FastAPI to create the web application.

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. The key features of FastAPI that make it an excellent choice for this project include:

- **Fast Execution**: FastAPI is built on Starlette for the web parts and uses Pydantic for the data parts. It's one of the fastest web frameworks available.
- **Asynchronous Support**: FastAPI supports asynchronous request handling, which is perfect for handling long-running operations such as requests to the ChatGPT API without blocking the server.
- **Type Checking**: Built-in support for data validation and type checking using Python type hints ensures that the data exchanged between the server and clients is correctly typed and structured.
- **Automatic API Documentation**: FastAPI automatically generates interactive API documentation (using Swagger UI and ReDoc) that makes it easy for developers to test and understand the API.

### Implementation Steps

Here’s a brief guide on how to integrate ChatGPT with FastAPI:

1. **Setup FastAPI Project**:
   - Install FastAPI and an ASGI server like Uvicorn:
     ```bash
     pip install fastapi uvicorn
     ```

2. **Create a FastAPI Application**:
   - Write a basic FastAPI app to handle requests:
     ```python
     from fastapi import FastAPI
     app = FastAPI()

     @app.get("/")
     def read_root():
         return {"Hello": "World"}
     ```

3. **Integrate ChatGPT**:
   - Include the OpenAI API to interact with ChatGPT:
     ```python
     from openai import OpenAI
     client = OpenAI(api_key="your_openai_api_key")

     @app.post("/chat/")
     async def chat(prompt: str):
         response = client.chat.completions.create(
             model="gpt-3.5-turbo",
             messages=[{"role": "user", "content": prompt}]
         )
         return {"response": response.choices[0].message.content}
     ```

4. **Run the Server**:
   - Start the Uvicorn server to host the API:
     ```bash
     uvicorn app:app --reload
     ```

5. **Testing and Deployment**:
   - Test the application locally and then deploy it to a production environment.

By integrating FastAPI with the ChatGPT API, we create a powerful and scalable platform that can handle a high volume of requests efficiently. This setup not only serves user inputs and generates responses dynamically but also benefits from FastAPI's modern features such as automatic data validation and API documentation.

## Application 1: Chatbot Answering Student Questions

This application utilizes the ChatGPT API to create a chatbot designed specifically for answering students' questions. By integrating ChatGPT into an educational platform, students can interact with the chatbot to get immediate, informative responses to their queries. This can be particularly useful in scenarios like virtual learning environments, homework help, or as a study aid. The chatbot can handle a range of subjects and complexities, adapting its responses to the level of the question posed by the student.

### Key Features:
- **Instant Response**: Students receive answers immediately, which is crucial for maintaining engagement and fostering a dynamic learning experience.
- **Wide Range of Subjects**: Capable of handling inquiries across various subjects, making it a versatile tool for students of all educational levels.
- **Natural Language Understanding**: Utilizes advanced NLP to understand and process student inquiries, ensuring that the responses are relevant and accurately address the questions.

### Implementation:
The chatbot would be accessible through an educational platform or a dedicated app, where students can type their questions and receive answers directly from ChatGPT.

## Application 2: Immediate Evaluating Students' Answers

In this application, the ChatGPT API is integrated to immediately evaluate students' answers to quiz or test questions. This tool can be especially beneficial during examinations or practice tests, providing students with instant feedback on their performance and explanations on topics they may have misunderstood.

### Key Features:
- **Immediate Feedback**: Offers real-time grading of answers, which helps students understand their mistakes right away.
- **Adaptive Learning**: Provides personalized feedback, suggesting areas for improvement and additional resources for study.
- **Support for Various Question Types**: Capable of evaluating different types of answers, from multiple choice to more complex, open-ended responses.

### Implementation:
This tool could be part of a larger educational platform or a standalone testing application. It would involve students submitting their answers through the platform, with the system using ChatGPT to analyze and grade these responses based on set criteria.

### Benefits of Both Applications:
- **Enhanced Learning**: Both tools facilitate a more engaging and interactive learning experience, encouraging students to actively participate and improve their knowledge.
- **Efficiency in Education**: Automating responses and evaluations saves time for educators and provides students with immediate assistance and feedback.
- **Accessibility**: Increases educational accessibility, allowing students to learn and receive assistance outside of traditional classroom settings and hours.

By harnessing the capabilities of ChatGPT, these applications aim to transform traditional educational practices, making learning more accessible, engaging, and effective for students and educators alike.


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
