from deepeval.dataset import EvaluationDataset
import os
import sys
# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from pathlib import Path
from deepeval.test_case import LLMTestCase
from deepeval import evaluate
import deepeval

from src.chatbot import FinancialAdvisorChatbot
from src.metrics import get_all_metrics

load_dotenv()
confident_api_key = os.getenv("CONFIDENT_API_KEY")
if confident_api_key:
    try:
        deepeval.login(confident_api_key)
        print("✅ Logged in to Confident AI (DeepEval Cloud)")
    except Exception as e:
        print(f"⚠️  Could not login to Confident AI: {e}")
        print("Results will not be logged to dashboard.")
else:
    print("⚠️  CONFIDENT_API_KEY not found - results won't be logged")

def load_golden_test_cases(file_path="test_cases/golden-test-cases.json"):
    dataset = EvaluationDataset()
    dataset.add_goldens_from_json_file(
        file_path=file_path,
        input_key_name="query",
        expected_output_key_name="expected_output",
        context_key_name="context"
    ) 
    return dataset

def generate_actual_output(dataset,chatbot):
    for golden in dataset.goldens:
        actual_output = chatbot.get_response(golden.input)
        test_case = LLMTestCase(
            input=golden.input,
            actual_output=actual_output,
            expected_output=golden.expected_output,
            context=golden.context if hasattr(golden,'context') else None
        )
        dataset.add_test_case(test_case)
    return dataset    

def run_evaluation(chatbot_model="llama-3.1-8b-instant",evaluation_model="llama-3.1-8b-instant"):
    """
    Orchestrate the full evaluation pipeline.
    """
    print("="*70)
    print(f"Financial Advisor - Batch Evaluation")
    print("="*70)

    # Step 1: Initialize chatbot
    chatbot = FinancialAdvisorChatbot(model=chatbot_model)

    # Step 2: Load goldens
    dataset = load_golden_test_cases()
    print(f"Loaded {len(dataset.goldens)} golden test cases")

    # Step 3: Generate actual outputs
    dataset = generate_actual_output(dataset, chatbot)
    print(f"Generated {len(dataset.test_cases)} actual outputs")

    # Step 4 : Create metrics
    metrics = get_all_metrics(evaluation_model=evaluation_model)
    print(f"Initialized {len(metrics)} evaluation metrics")

    # Step 5 : Run Batch Evaluation
    evaluate(
        test_cases=dataset.test_cases,
        metrics=metrics
    )
    print("="*70)
    print("Evaluation complete!")
    print("="*70)

def main():
    """
    CLI entry point.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Batch Evaluation for Financial Advisor Chatbot")
    parser.add_argument("--chatbot-model", default="llama-3.1-8b-instant", help="Model for chatbot")
    parser.add_argument("--eval-model", default="llama-3.1-8b-instant", help="Model for evaluator")
    args = parser.parse_args()
    run_evaluation(chatbot_model=args.chatbot_model, evaluation_model=args.eval_model)

if __name__ == "__main__":
    main()

