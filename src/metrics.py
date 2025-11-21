"""
Metrics Module - Skeleton with TODOs

YOUR TASK: Implement CustomGROQLLM and metrics functions
This is YOUR EVALUATOR - what judges chatbot quality
"""

from deepeval.models import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric, ToxicityMetric, GEval
from deepeval.test_case import LLMTestCaseParams
import os
from typing import Optional


# Default thresholds for metrics
DEFAULT_THRESHOLDS = {
    "relevancy": 0.7,
    "correctness": 0.75,
    "completeness": 0.7,
    "toxicity": 0.10,
    "compliance": 0.8
}


class CustomGROQLLM(DeepEvalBaseLLM):
    """
    Custom GROQ LLM for DeepEval metrics evaluation
    
    This is YOUR JUDGE - evaluates chatbot response quality
    Uses GROQ Llama-3.1 with JSON confinement
    """
    
    def __init__(self, model: str = "llama-3.1-8b-instant"):
        """
        Initialize GROQ LLM for evaluation
        
        TODO: Implement this method (Day 2 Morning)
        Steps:
        1. Import Groq from groq package
        2. Get GROQ_API_KEY from environment using os.getenv()
        3. Check if API key exists, raise ValueError if not
        4. Create Groq client: self.client = Groq(api_key=api_key)
        5. Store model name: self.model = model
        
        Args:
            model: GROQ model name (llama-3.1-8b-instant or llama-3.1-70b-versatile)
        
        Raises:
            ValueError: If GROQ_API_KEY not found in environment
        """
        # TODO: Your implementation here
        pass
    
    def load_model(self):
        """
        Load and return the GROQ client
        
        TODO: Implement this method (Day 2 Morning)
        Simply return self.client
        
        Returns:
            Groq client instance
        """
        # TODO: Your implementation here
        pass
    
    def generate(self, prompt: str) -> str:
        """
        Generate response from GROQ with JSON confinement
        
        TODO: Implement this method (Day 2 Morning) - MOST IMPORTANT!
        
        Steps:
        1. Get client using self.load_model()
        2. Call client.chat.completions.create() with:
           - model=self.model
           - messages=[{"role": "user", "content": prompt}]
           - response_format={"type": "json_object"}  ← KEY FOR JSON CONFINEMENT!
           - temperature=0.0  (deterministic evaluation)
           - max_tokens=2000
        3. Extract and return: response.choices[0].message.content
        
        Args:
            prompt: Evaluation prompt from DeepEval (asks for JSON response)
        
        Returns:
            Valid JSON string with evaluation results
        
        Example flow:
            DeepEval → calls generate(prompt) → 
            You call GROQ → returns JSON → 
            DeepEval parses JSON
        """
        # TODO: Your implementation here
        # Remember: response_format={"type": "json_object"} is CRITICAL!
        pass
    
    async def a_generate(self, prompt: str) -> str:
        """
        Async version of generate
        
        TODO: Implement this method (Day 2 Morning)
        For now, just call self.generate(prompt)
        
        Args:
            prompt: Evaluation prompt
        
        Returns:
            JSON string (same as generate)
        """
        # TODO: Your implementation here
        pass
    
    def get_model_name(self) -> str:
        """
        Return model name for logging
        
        TODO: Implement this method (Day 2 Morning)
        Return f"GROQ {self.model}"
        
        Returns:
            Model name string
        """
        # TODO: Your implementation here
        pass


def get_relevancy_metric(
    threshold: Optional[float] = None,
    evaluation_model: str = "llama-3.1-8b-instant"
):
    """
    Create Answer Relevancy Metric
    
    TODO: Implement this function (Day 3 Morning)
    
    Steps:
    1. Get threshold (use parameter or DEFAULT_THRESHOLDS["relevancy"])
    2. Create CustomGROQLLM instance with evaluation_model
    3. Return AnswerRelevancyMetric configured with:
       - threshold=threshold
       - model=eval_llm_instance
       - include_reason=True
    
    Args:
        threshold: Minimum score to pass (default: 0.7)
        evaluation_model: GROQ model for evaluation
    
    Returns:
        Configured AnswerRelevancyMetric
    """
    # TODO: Your implementation here (Day 3)
    pass


def get_correctness_metric(
    threshold: Optional[float] = None,
    evaluation_model: str = "llama-3.1-8b-instant"
):
    """
    Create Correctness Metric using GEval
    
    TODO: Implement this function (Day 3 Afternoon)
    
    Similar to get_relevancy_metric but uses GEval with:
    - name="Correctness"
    - criteria=(description of what correctness means)
    - evaluation_params=[INPUT, ACTUAL_OUTPUT, EXPECTED_OUTPUT]
    
    Args:
        threshold: Minimum score to pass (default: 0.75)
        evaluation_model: GROQ model for evaluation
    
    Returns:
        Configured GEval metric
    """
    # TODO: Your implementation here (Day 3)
    pass


def get_completeness_metric(
    threshold: Optional[float] = None,
    evaluation_model: str = "llama-3.1-8b-instant"
):
    """
    Create Completeness Metric using GEval
    
    TODO: Implement this function (Day 3 Afternoon)
    
    Args:
        threshold: Minimum score to pass (default: 0.7)
        evaluation_model: GROQ model for evaluation
    
    Returns:
        Configured GEval metric
    """
    # TODO: Your implementation here (Day 3)
    pass


def get_toxicity_metric(
    threshold: Optional[float] = None,
    evaluation_model: str = "llama-3.1-8b-instant"
):
    """
    Create Toxicity Metric
    
    TODO: Implement this function (Day 3 Afternoon)
    
    Note: Lower scores are better! Pass if score < threshold
    
    Args:
        threshold: Maximum toxicity allowed (default: 0.10)
        evaluation_model: GROQ model for evaluation
    
    Returns:
        Configured ToxicityMetric
    """
    # TODO: Your implementation here (Day 3)
    pass


def get_compliance_metric(
    threshold: Optional[float] = None,
    evaluation_model: str = "llama-3.1-8b-instant"
):
    """
    Create Compliance Metric using GEval
    
    TODO: Implement this function (Day 3 Afternoon)
    
    Args:
        threshold: Minimum score to pass (default: 0.8)
        evaluation_model: GROQ model for evaluation
    
    Returns:
        Configured GEval metric
    """
    # TODO: Your implementation here (Day 3)
    pass


def get_all_metrics(
    thresholds: Optional[dict] = None,
    evaluation_model: str = "llama-3.1-8b-instant"
):
    """
    Get all 5 configured metrics
    
    TODO: Implement this function (Day 3 Evening)
    
    Steps:
    1. Handle thresholds parameter (use {} if None)
    2. Call all 5 get_*_metric functions
    3. Return list of all metrics
    
    Args:
        thresholds: Optional dict to override defaults
        evaluation_model: GROQ model for all metrics
    
    Returns:
        List of 5 configured metrics
    
    Example:
        >>> metrics = get_all_metrics()
        >>> len(metrics)
        5
    """
    # TODO: Your implementation here (Day 3)
    pass


# Test your implementation
if __name__ == "__main__":
    # TODO: Test CustomGROQLLM (Day 2)
    # llm = CustomGROQLLM()
    # print(llm.get_model_name())
    # response = llm.generate("Say hello in JSON: {\"message\": \"text\"}")
    # print(response)
    pass