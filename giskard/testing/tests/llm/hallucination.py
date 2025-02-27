from typing import Optional

from ....core.test_result import TestResult
from ....datasets.base import Dataset
from ....llm.evaluators.coherency import CoherencyEvaluator
from ....llm.evaluators.plausibility import PlausibilityEvaluator
from ....models.base.model import BaseModel
from ....registry.decorators import test


@test(name="LLM Coherency", tags=["llm", "hallucination"])
def test_llm_output_coherency(
    model: BaseModel, dataset_1: Dataset, dataset_2: Optional[Dataset] = None, eval_prompt: Optional[str] = None
):
    """Tests that the model output is coherent for multiple inputs.

    Parameters
    ----------
    model : BaseModel
        The model to test.
    dataset_1 : Dataset
        Another sample dataset of inputs, with same index as ``dataset_1``. If
        not passed, we will run a again predictions on the first inputs
        ``dataset_1``, and check that the outputs are coherent.
    dataset_2 : Optional[Dataset]
        Another sample dataset of inputs, with same index as ``dataset_1``. If
        not passed, we will rerun the model on ``dataset_1``.
    eval_prompt : Optional[str]
        Optional custom prompt to use for evaluation. If not provided, the
        default prompt of :class:`.CoherencyEvaluator` will be used.

    Returns
    -------
    TestResult
        The test result.
    """
    evaluator = CoherencyEvaluator(eval_prompt=eval_prompt)
    eval_result = evaluator.evaluate(model, dataset_1, dataset_2)

    return TestResult(
        passed=eval_result.passed,
        is_error=eval_result.has_errors,
        metric=len(eval_result.failure_examples),
        metric_name="Failing examples",
    )


@test(name="LLM Plausibility", tags=["llm", "hallucination"])
def test_llm_output_plausibility(model: BaseModel, dataset: Dataset, eval_prompt: Optional[str] = None):
    """Tests that the model output is plausible.

    Parameters
    ----------
    model : BaseModel
        The model to test.
    dataset : Dataset
        A sample dataset of inputs.
    eval_prompt : Optional[str]
        Optional custom prompt to use for evaluation. If not provided, the
        default prompt of `CoherencyEvaluator` will be used.

    Returns
    -------
    TestResult
        The test result.
    """
    evaluator = PlausibilityEvaluator(eval_prompt=eval_prompt)
    eval_result = evaluator.evaluate(model, dataset)

    return TestResult(
        passed=eval_result.passed,
        is_error=eval_result.has_errors,
        metric=len(eval_result.failure_examples),
        metric_name="Failing examples",
    )
