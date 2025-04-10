<header>

<!--
  <<< Author notes: Course header >>>
  Include a 1280×640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Add your open source license, GitHub uses MIT license.
-->
<div align="center">
<h1>Awesome Test-time-Scaling in LLMs</h1>
</div>


<p align="center">
  <img src="https://img.shields.io/badge/Contributors-10-red?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/testtimescaling/testtimescaling.github.io?style=for-the-badge&color=blue"/>
  <img src="https://img.shields.io/endpoint?url=https://testtimescaling.github.io/arxiv_citations.json&style=for-the-badge&color=green"/>
</p>

Our repository, **Awesome Test-time-Scaling in LLMs**, gathers available papers on test-time scaling, to our current knowledge. Unlike other repositories that categorize papers, we decompose each paper's contributions based on the taxonomy provided by ["What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models"](https://arxiv.org/abs/2503.24235) facilitating easier understand and comparison for readers.


<div align="center">
  <img src="figs/TTS-how.png" width="900"/>
  <p><b>Figure 1:</b> A Visual Map and Comparison: From <i>What to Scale</i> to <i>How to Scale</i>.</p>
</div>

## 📢 News and Updates
- **[9/Apr/2025]** 📌 Our repository is created.
- **[31/Mar/2025]** 📌 Our initial survey is on [**Arxiv**](https://arxiv.org/abs/2503.24235)!

## 📘 Introduction
As enthusiasm for scaling computation (data and parameters) in the pertaining era gradually diminished, test-time scaling (TTS)—also referred to as “test-time computing”—has emerged as a prominent research focus. Recent studies demonstrate that TTS can further elicit the problem-solving capabilities of large language models (LLMs), enabling significant breakthroughs not only in reasoning-intensive tasks, such as mathematics and coding, but also in general tasks like open-ended Q&A. However, despite the explosion of recent efforts in this area, there remains an urgent need for a comprehensive survey offering systemic understanding. To fill this gap, we propose a unified, hierarchical framework structured along four orthogonal dimensions of TTS research: **what to scale**, **how to scale**, **where to scale**, and **how well to scale**. Building upon this taxonomy, we conduct a holistic review of methods, application scenarios, and assessment aspects, and present an organized decomposition that highlights the unique contributions of individual methods within the broader TTS landscape.

## 🧬 Taxonomy

### 1. **What to Scale**
``What to scale'' refers to the specific form of TTS that is expanded or adjusted to enhance an LLM’s performance during inference.
- **Parallel Scaling** improves test-time performance by generating multiple outputs in parallel and then aggregating them into a final answer.
- **Sequential Scaling** involves explicitly directing later computations based on intermediate steps.
- **Hybrid Scaling** exploits the complementary benefits of parallel and sequential scaling.
- **Internal Scaling** elicits a model to autonomously determine how much computation to allocate for reasoning during testing within the model’s internal parameters, instead of external human-guided strategies.

### 2. **How to Scale**
- **Tuning**
  - Supervised Fine-Tuning (_SFT_): by training on synthetic or distilled long CoT examples, SFT allows a model to imitate extended reasoning patterns.
  - Reinforcement Learning (_RL_): RL can guide a model’s policy to generate longer or more accurate solutions.
- **Inference**
  - Stimulation (_STI_): It basically stimulates the LLM to generate more and longer samples instead of generating individual samples directly.
  - Verification (_VER_): The verification process plays an important role in the TTS, and it can be adapted to: i) directly selects the output sample among various ones, under the Parallel Scaling paradigm; ii) guides the stimulation process and determines when to stop, under the Sequential Scaling paradigm; iii) serves as the criteria in the search process; iv) determines what sample to aggregate and how to aggregate them, e.g., weights.
  - Search (_SEA_): Search is a time-tested technique for retrieving relevant information from large databases, and it can also systematically explore the potential outputs of LLMs to improve complex reasoning tasks.
  - Aggregation (_AGG_): Aggregation techniques consolidate multiple solutions into a final decision to enhance the reliability and robustness of model predictions at test time.

### 3. **Where to Scale**
- **Reasoning**: Math, Code, Science, Game & Strategy, Medical and so on.
- **General-Purpose**: Basics, Agents,  Knowledge, Open-Ended, Multi-Modal and so on.

### 4. **How Well to Scale**
- **Performance**: This dimension measures the correctness and robustness of outputs.
- **Efficiency**: it captures the cost-benefit tradeoffs of TTS methods.
- **Controllability**: This dimension assesses whether TTS methods adhere to resource or output constraints, such as compute budgets or output lengths.
- **Scalability**: Scalability quantifies how well models improve with more test-time compute (e.g., tokens or steps).

## 🔍 Paper Tables
| <div style="width:300px">Method(PapersTitles)</div> | What | How → |        |        |        |        |        | Where | How Well |
|--------|------|-------|--------|--------|--------|--------|--------|-------|-------|
|        |      | SFT   | RL     | STI | SEA | VER | AGG |        |        |
|<i><b>Scaling llm test-time compute optimally can be more effective than scaling model parameters.</b></i>, Snell et al., <a href="https://arxiv.org/abs/2408.03314" target="_blank"><img src="https://img.shields.io/badge/arXiv-2408.03314-red" alt="arXiv Badge"></a></li>|Parallel,<br>Sequential|✗|✗|✗|Beam,<br>LookAhead|Verifier|(Weighted) Best-of-N,<br>Stepwise Aggregation|Math|Pass@1,<br>FLOPsMatched Evaluation|
| <i><b>Meta-Reasoner</b></i><br>Sui et al., 2025 | Sequential | ✗ | ✗ | CoT +<br>Self-Repetition | ✗ | Bandit | ✗ | Game,<br>Sci,<br>Math | Accuracy,<br>Token Cost |
| <i><b>START</b></i><br>Li et al., 2025b | Parallel,<br>Sequential | Rejection Sampling | ✗ | Hint-infer | ✗ | Tool | ✗ | Math,<br>Code | Pass@1 |
| <i><b>AID</b></i><br>Jin et al., 2025 | Sequential | ✗ | ✗ | Adaptive Injection<br>Decoding | ✗ | ✗ | ✗ | Math,<br>Logical,<br>Commonsense | Accuracy |
| <i><b>CoD</b></i><br>Xu et al., 2025b | Sequential | ✗ | ✗ | Chain-of-Draft | ✗ | ✗ | ✗ | Math,<br>Symbolic,<br>Commonsense | Accuracy,<br>Latency,<br>Token Cost |
| <i><b>rStar-Math</b></i><br>Guan et al., 2025b | Hybrid | imitation | ✗ | ✗ | MCTS | PRM | ✗ | Math | Pass@1 |
| <i><b>Liu et al.</b></i><br>2025a | Parallel,<br>Hybrid | ✗ | ✗ | ✗ | DVTS,<br>Beam Search | PRM | Best-of-N | Math | Pass@1,<br>Pass@k,<br>Majority,<br>FLOPS |
| <i><b>Tree of Thoughts</b></i><br>Yao et al., 2023b | Hybrid | ✗ | ✗ | Propose Prompt,<br>Self-Repetition | Tree Search | Self-Evaluate | ✗ | Game,<br>Open-Ended | Success Rate,<br>LLM-as-a-Judge |
| <i><b>MindStar</b></i><br>Kang et al., 2024 | Hybrid | ✗ | ✗ | ✗ | LevinTS | PRM | ✗ | Math | Accuracy,<br>Token Cost |
| <i><b>REBASE</b></i><br>Wu et al., 2025a | Hybrid | ✗ | ✗ | ✗ | Reward Balanced<br>Search | RM | ✗ | Math | Test Error Rate,<br>FLOPs |
| <i><b>RaLU</b></i><br>Li et al., 2025c | Hybrid | ✗ | ✗ | Self-Refine | Control Flow Graph | Self-Evaluate | Prompt Synthesis | Math,<br>Code | Pass@1 |
| <i><b>PlanGen</b></i><br>Parmar et al., 2025 | Parallel,<br>Hybrid | ✗ | ✗ | MoA | ✗ | Verification Agent | Selection Agent | Math,<br>General,<br>Finance | Accuracy,<br>F1 Score |
| <i><b>Puri et al.</b></i><br>2025 | Hybrid | ✗ | ✗ | ✗ | Particle-based<br>Monte Carlo | PRM + SSM | Particle Filtering | Math | Pass@1,<br>Budget vs. Accuracy |
| <i><b>Archon</b></i><br>Saad-Falcon et al., 2024 | Hybrid | ✗ | ✗ | MoA,<br>Self-Repetition | ✗ | Verification Agent,<br>Unit Testing (Ensemble) | Fusion | Math,<br>Code,<br>Open-Ended | Pass@1,<br>Win Rate |
| <i><b>AB-MCTS</b></i><br>Misaki et al., 2025 | Hybrid | ✗ | ✗ | Mixture-of-Model | AB-MCTS-(M,A) | ✗ | ✗ | Code | Pass@1,<br>RMSLE,<br>ROC-AUC |
| <i><b>TPO</b></i><br>Wu et al., 2024a | Internal,<br>Parallel | ✗ | DPO | Think | ✗ | Judge Models | ✗ | Open-Ended | Win Rate |
| <i><b>SPHERE</b></i><br>Singh et al., 2025 | Internal,<br>Hybrid | ✗ | DPO | Diversity Generation | MCTS | Self-Reflect | ✗ | Math | Pass@1 |
| <i><b>MA-LoT</b></i><br>Wang et al., 2025b | Internal,<br>Sequential | imitation | ✗ | MoA | ✗ | Tool | ✗ | Math | Pass@k |
| <i><b>OREO</b></i><br>Wang et al., 2024b | Internal,<br>Sequential | ✗ | OREO | ✗ | Beam Search | Value Function | ✗ | Math,<br>Agent | Pass@1,<br>Success Rate |
| <i><b>DeepSeek-R1</b></i><br>DeepSeek-AI, 2025 | Internal | warmup,<br>GRPO,<br>Rule-Based | ✗ | ✗ | ✗ | ✗ | Math,<br>Code,<br>Sci | Pass@1,<br>cons@64,<br>Percentile,<br>Elo Rating,<br>Win Rate |
| <i><b>s1</b></i><br>Muennighoff et al., 2025 | Internal | distillation | ✗ | Budget Forcing | ✗ | ✗ | ✗ | Math,<br>Sci | Pass@1,<br>Control,<br>Scaling |
| <i><b>o1-Replication</b></i><br>Qin et al., 2024 | Internal | imitation | ✗ | ✗ | Journey Learning | PRM,<br>Critique | Multi-Agents | Math | Accuracy |
| <i><b>AFT</b></i><br>Li et al., 2025g | Internal,<br>Parallel | imitation | ✗ | ✗ | ✗ | Fusion | ✗ | Math,<br>Open-Ended | Win Rate |
| <i><b>Meta-CoT</b></i><br>Xiang et al., 2025 | Internal,<br>Hybrid | imitation,<br>meta-RL | Think | MCTS,<br>A* | PRM | ✗ | Math,<br>Open-Ended | Win Rate |
| <i><b>ReasonFlux</b></i><br>Yang et al., 2025a | Internal,<br>Sequential | ✗ | PPO,<br>Trajectory | Thought Template Retrieve | ✗ | ✗ | Math | Pass@1 |
| <i><b>l1</b></i><br>Aggarwal and Welleck, 2025b | Internal | ✗ | GRPO,<br>Length-Penalty | ✗ | ✗ | ✗ | ✗ | Math | Pass@1,<br>Length Error |
| <i><b>Marco-o1</b></i><br>Zhao et al., 2024 | Internal,<br>Hybrid | distillation,<br>imitation | ✗ | Reflection Prompt | MCTS | Self-Critic | ✗ | Math | Pass@1,<br>Pass@k |




</footer>
