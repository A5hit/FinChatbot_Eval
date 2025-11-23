from groq import Groq
import os

class FinancialAdvisorChatbot:
    """
    Financial advisor chatbot using GROQ
    This generates responses that will be evaluated
    """
    def __init__(self, model : str = "llama-3.1-8b-instant"):    
        """Initialize chatbot with GROQ"""
        self.model = model
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment.")
        self.client = Groq(api_key=api_key)

        self.system_prompt = """
        You are a financial advisor chatbot. 
        """"""You are a professional financial advisor chatbot.
Your role is to provide helpful, accurate, and compliant financial advice to users.

Guidelines:
- Provide clear and understandable financial advice
- Always emphasize that you are not a substitute for professional financial advice
- Be compliant with financial regulations
- Avoid giving specific investment recommendations without proper disclaimers
- Be helpful, respectful, and professional
- If asked about topics outside your expertise, politely redirect or suggest consulting a professional"""

        print(f"✅ FinancialAdvisorChatbot initialized with model: {model}")

    def get_response(self, query: str, context: List[str] = None) -> str:
        """
        Generate response to user query
        This is what gets evaluated by metrics
        """
        # Build messages
        message = [
            {"role":"system", "content": self.system_prompt}
        ]

        # Add context if provided
        if context:
            context_str = "\n".join(context)
            messages.append({
                "role": "system",
                "content": f"Additional context: {context_str}"
            })

        # Add user query
        messages.append({"role": "user", "content": query})

        # Generate response
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message,
                max_tokens=2000,
                temperature=0.0,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return 