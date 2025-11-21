"""
Test CustomGROQLLM - Skeleton

YOUR TASK: Test each method of CustomGROQLLM as you implement it
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()

# TODO: Import after you implement it
# from src.metrics import CustomGROQLLM


def test_initialization():
    """
    Test 1: Can you create CustomGROQLLM instance?
    
    TODO: Implement this test (Day 2)
    """
    print("Test 1: Initializing CustomGROQLLM...")
    # TODO: Your test implementation
    # try:
    #     llm = CustomGROQLLM()
    #     print("✅ PASS: Instance created")
    # except Exception as e:
    #     print(f"❌ FAIL: {e}")
    pass


def test_get_model_name():
    """
    Test 2: Does get_model_name() work?
    
    TODO: Implement this test (Day 2)
    """
    print("\nTest 2: Testing get_model_name()...")
    # TODO: Your test implementation
    pass


def test_load_model():
    """
    Test 3: Does load_model() return client?
    
    TODO: Implement this test (Day 2)
    """
    print("\nTest 3: Testing load_model()...")
    # TODO: Your test implementation
    pass


def test_generate():
    """
    Test 4: Does generate() work and return valid response?
    
    TODO: Implement this test (Day 2)
    """
    print("\nTest 4: Testing generate()...")
    # TODO: Your test implementation
    # Test with: "Say hello in 3 words"
    pass


def test_json_mode():
    """
    Test 5: Does JSON mode work? Is output valid JSON?
    
    TODO: Implement this test (Day 2 Afternoon)
    """
    print("\nTest 5: Testing JSON mode...")
    # TODO: Your test implementation
    # Prompt: Ask for JSON output with score and reason
    # Then: Try to parse with json.loads()
    pass


def run_all_tests():
    """Run all tests"""
    print("="*60)
    print("CustomGROQLLM Test Suite")
    print("="*60)
    
    test_initialization()
    test_get_model_name()
    test_load_model()
    test_generate()
    test_json_mode()
    
    print("\n" + "="*60)
    print("All tests completed!")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()