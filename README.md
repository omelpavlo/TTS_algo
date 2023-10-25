# tts_algo
Reproduces the algorithm presented in section IV of https://arxiv.org/abs/1806.08815 for benchmarking probabilistic algorithms

The tts_algo_code.py script operates on synthetically generated instances. To utilize this code with real-world or other custom datasets, the following modifications are necessary:

Data Input: Replace the synthetic_data function or modify its internals to import or generate your specific dataset. Ensure that the format of the dataset matches the expected input of subsequent functions.

Algorithm Parameters: Depending on your dataset, you might need to adjust parameters such as num_instances, num_runs, and success_prob to better suit your specific requirements.

Histogram generation: comment out histogram-generating pieces of code, the last two lines before the return in the main()
