from typing import Optional

from ..models.base.model import BaseModel
from .generators.base import BaseDataGenerator


def generate_test_dataset(
    model: BaseModel, num_samples: int = 10, prompt: Optional[str] = None, temperature=0.5, column_types=None
):
    """Generates a synthetic test dataset using an LLM.

    Parameters
    ----------
    model : BaseModel
        The model to generate a test dataset for.
    num_samples : int
        The number of samples to generate, by default 10.
    prompt : Optional[str]
        The prompt to use for the generation, if not specified a default will be used.
    temperature : Optional[float]
        The temperature to use for the generation, by default 0.5.
    column_types :
        (Default value = None)

    Returns
    -------
    Dataset
        The generated dataset.

    Raises
    ------
    LLMGenerationError
        If the generation fails.

    See also
    --------
    :class:`giskard.llm.generators.BaseDataGenerator`
    """
    generator = BaseDataGenerator(prompt=prompt, llm_temperature=temperature)
    return generator.generate_dataset(model, num_samples, column_types)
