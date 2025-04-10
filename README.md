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
<div align="center">
  <img src="figs/TTS-intro.png" width="900"/>
  <p><b>Figure 1:</b> A Visual Map and Comparison: From <i>What to Scale</i> to <i>How to Scale</i>.</p>
</div>

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
|<i><b>Multi-agent verification: Scaling test-time compute with goal verifiers</b></i><br>Lifshitz et al., <a href="https://arxiv.org/abs/2502.20379" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.20379-red" alt="arXiv Badge"></a></li>| Parallel | ✗ | ✗ | Self-Repetition | ✗ | Multiple-Agent<br>Verifiers | Best-of-N | Math,<br>Code,<br>General | BoN-MAV (Cons@k),<br>Pass@1 |
|<i><b>Evolving Deeper LLM Thinking</b></i><br>Lee et al.,  <a href="https://arxiv.org/abs/2501.09891" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.09891-red" alt="arXiv Badge"></a></li>| Sequential | ✗ | ✗ | Self-Refine | ✗ | Functional | ✗ | Open-Ended | Success Rate,<br>Token Cost |
| <i><b>Meta-reasoner: Dynamic guidance for optimized inference-time reasoning in large language models</b></i><br>Sui et al., <a href="https://arxiv.org/abs/2502.19918" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.19918-red" alt="arXiv Badge"></a></li>| Sequential | ✗ | ✗ | CoT +<br>Self-Repetition | ✗ | Bandit | ✗ | Game,<br>Sci,<br>Math | Accuracy,<br>Token Cost |
| <i><b>START: Self-taught reasoner with tools</b></i><br>Li et al., <a href="https://arxiv.org/abs/2503.04625" target="_blank"><img src="https://img.shields.io/badge/arXiv-2503.04625-red" alt="arXiv Badge"></a></li>| Parallel,<br>Sequential | Rejection Sampling | ✗ | Hint-infer | ✗ | Tool | ✗ | Math,<br>Code | Pass@1 |
| <i><b>" Well, Keep Thinking": Enhancing LLM Reasoning with Adaptive Injection Decoding</b></i><br>Jin et al.,  <a href="https://arxiv.org/abs/2503.10167" target="_blank"><img src="https://img.shields.io/badge/arXiv-2503.10167-red" alt="arXiv Badge"></a></li>| Sequential | ✗ | ✗ | Adaptive Injection<br>Decoding | ✗ | ✗ | ✗ | Math,<br>Logical,<br>Commonsense | Accuracy |
| <i><b>Chain of draft: Thinking faster by writing less</b></i><br>Xu et al., <a href="https://arxiv.org/abs/2502.18600" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.18600-red" alt="arXiv Badge"></a></li> | Sequential | ✗ | ✗ | Chain-of-Draft | ✗ | ✗ | ✗ | Math,<br>Symbolic,<br>Commonsense | Accuracy,<br>Latency,<br>Token Cost |
| <i><b>rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking</b></i><br>Guan et al., <a href="https://arxiv.org/abs/2501.04519" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.04519-red" alt="arXiv Badge"></a></li> | Hybrid | imitation | ✗ | ✗ | MCTS | PRM | ✗ | Math | Pass@1 |
| <i><b>Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling</b></i><br>Liu et al., <a href="https://arxiv.org/abs/2502.06703" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.06703-red" alt="arXiv Badge"></a></li> | Parallel,<br>Hybrid | ✗ | ✗ | ✗ | DVTS,<br>Beam Search | PRM | Best-of-N | Math | Pass@1,<br>Pass@k,<br>Majority,<br>FLOPS |
| <i><b>Tree of thoughts: Deliberate problem solving with large language models</b></i><br>Yao et al., <a href="https://arxiv.org/abs/2305.10601" target="_blank"><img src="https://img.shields.io/badge/arXiv-2305.10601-red" alt="arXiv Badge"></a></li> | Hybrid | ✗ | ✗ | Propose Prompt,<br>Self-Repetition | Tree Search | Self-Evaluate | ✗ | Game,<br>Open-Ended | Success Rate,<br>LLM-as-a-Judge |
| <i><b>Mindstar: Enhancing math reasoning in pre-trained llms at inference time</b></i><br>Kang et al., <a href="https://arxiv.org/abs/2405.16265" target="_blank"><img src="https://img.shields.io/badge/arXiv-2405.16265-red" alt="arXiv Badge"></a></li> | Hybrid | ✗ | ✗ | ✗ | LevinTS | PRM | ✗ | Math | Accuracy,<br>Token Cost |
| <i><b>Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving</b></i><br>Wu et al., <a href="https://arxiv.org/abs/2408.00724" target="_blank"><img src="https://img.shields.io/badge/arXiv-2408.00724-red" alt="arXiv Badge"></a></li> | Hybrid | ✗ | ✗ | ✗ | Reward Balanced<br>Search | RM | ✗ | Math | Test Error Rate,<br>FLOPs |
| <i><b>Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment</b></i><br>Li et al., <a href="https://arxiv.org/abs/2502.07803" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.07803-red" alt="arXiv Badge"></a></li> | Hybrid | ✗ | ✗ | Self-Refine | Control Flow Graph | Self-Evaluate | Prompt Synthesis | Math,<br>Code | Pass@1 |
| <i><b>PlanGEN: A Multi-Agent Framework for Generating Planning and Reasoning Trajectories for Complex Problem Solving</b></i><br>Parmar et al., <a href="https://arxiv.org/abs/2502.16111" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.16111-red" alt="arXiv Badge"></a></li>  | Parallel,<br>Hybrid | ✗ | ✗ | MoA | ✗ | Verification Agent | Selection Agent | Math,<br>General,<br>Finance | Accuracy,<br>F1 Score |
| <i><b>A Probabilistic Inference Approach to Inference-Time Scaling of LLMs using Particle-Based Monte Carlo Methods</b></i><br>Puri et al., <a href="https://arxiv.org/abs/2502.01618" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.01618-red" alt="arXiv Badge"></a></li>  | Hybrid | ✗ | ✗ | ✗ | Particle-based<br>Monte Carlo | PRM + SSM | Particle Filtering | Math | Pass@1,<br>Budget vs. Accuracy |
| <i><b>Archon: An Architecture Search Framework for Inference-Time Techniques</b></i><br>Saad-Falcon et al., <a href="https://arxiv.org/abs/2409.15254" target="_blank"><img src="https://img.shields.io/badge/arXiv-2409.15254-red" alt="arXiv Badge"></a></li> | Hybrid | ✗ | ✗ | MoA,<br>Self-Repetition | ✗ | Verification Agent,<br>Unit Testing (Ensemble) | Fusion | Math,<br>Code,<br>Open-Ended | Pass@1,<br>Win Rate |
| <i><b>Wider or deeper? scaling llm inference-time compute with adaptive branching tree search</b></i><br>Misaki et al., <a href="https://arxiv.org/abs/2503.04412" target="_blank"><img src="https://img.shields.io/badge/arXiv-2503.04412-red" alt="arXiv Badge"></a></li> | Hybrid | ✗ | ✗ | Mixture-of-Model | AB-MCTS-(M,A) | ✗ | ✗ | Code | Pass@1,<br>RMSLE,<br>ROC-AUC |
| <i><b>Thinking llms: General instruction following with thought generation</b></i><br>Wu et al., <a href="https://arxiv.org/abs/2410.10630" target="_blank"><img src="https://img.shields.io/badge/arXiv-2410.10630-red" alt="arXiv Badge"></a></li> | Internal,<br>Parallel | ✗ | DPO | Think | ✗ | Judge Models | ✗ | Open-Ended | Win Rate |
| <i><b>Self-Evolved Preference Optimization for Enhancing Mathematical Reasoning in Small Language Models</b></i><br>Singh et al., <a href="https://arxiv.org/abs/2503.04813" target="_blank"><img src="https://img.shields.io/badge/arXiv-2503.04813-red" alt="arXiv Badge"></a></li> | Internal,<br>Hybrid | ✗ | DPO | Diversity Generation | MCTS | Self-Reflect | ✗ | Math | Pass@1 |
| <i><b>MA-LoT: Multi-Agent Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving</b></i><br>Wang et al., <a href="https://arxiv.org/abs/2503.03205" target="_blank"><img src="https://img.shields.io/badge/arXiv-2503.03205-red" alt="arXiv Badge"></a></li> | Internal,<br>Sequential | imitation | ✗ | MoA | ✗ | Tool | ✗ | Math | Pass@k |
| <i><b>Offline Reinforcement Learning for LLM Multi-Step Reasoning</b></i><br>Wang et al., <a href="https://arxiv.org/abs/2412.16145" target="_blank"><img src="https://img.shields.io/badge/arXiv-2412.16145-red" alt="arXiv Badge"></a></li> | Internal,<br>Sequential | ✗ | OREO | ✗ | Beam Search | Value Function | ✗ | Math,<br>Agent | Pass@1,<br>Success Rate |
| <i><b>DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning</b></i><br>DeepSeek-AI, <a href="https://arxiv.org/abs/2501.12948" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.12948-red" alt="arXiv Badge"></a></li> | Internal | warmup,<br>GRPO,<br>Rule-Based | ✗ | ✗ | ✗ | ✗ | Math,<br>Code,<br>Sci | Pass@1,<br>cons@64,<br>Percentile,<br>Elo Rating,<br>Win Rate |
| <i><b>s1: Simple test-time scaling</b></i><br>Muennighoff et al., <a href="https://arxiv.org/abs/2501.19393" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.19393-red" alt="arXiv Badge"></a></li> | Internal | distillation | ✗ | Budget Forcing | ✗ | ✗ | ✗ | Math,<br>Sci | Pass@1,<br>Control,<br>Scaling |
| <i><b>O1 Replication Journey: A Strategic Progress Report -- Part 1</b></i><br>Qin et al., <a href="https://arxiv.org/abs/2410.18982" target="_blank"><img src="https://img.shields.io/badge/arXiv-2410.18982-red" alt="arXiv Badge"></a></li> | Internal | imitation | ✗ | ✗ | Journey Learning | PRM,<br>Critique | Multi-Agents | Math | Accuracy |
| <i><b>From drafts to answers: Unlocking llm potential via aggregation fine-tuning</b></i><br>Li et al., <a href="https://arxiv.org/abs/2501.11877" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.11877-red" alt="arXiv Badge"></a></li> | Internal,<br>Parallel | imitation | ✗ | ✗ | ✗ | Fusion | ✗ | Math,<br>Open-Ended | Win Rate |
| <i><b>Towards System 2 Reasoning in LLMs: Learning How to Think With Meta Chain-of-Though</b></i><br>Xiang et al.,  <a href="https://arxiv.org/abs/2501.04682" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.04682-red" alt="arXiv Badge"></a></li>| Internal,<br>Hybrid | imitation,<br>meta-RL | Think | MCTS,<br>A* | PRM | ✗ | Math,<br>Open-Ended | Win Rate |
| <i><b>ReasonFlux: Hierarchical LLM Reasoning via Scaling Thought Templates</b></i><br>Yang et al., <a href="https://arxiv.org/abs/2502.06772" target="_blank"><img src="https://img.shields.io/badge/arXiv-2502.06772-red" alt="arXiv Badge"></a></li> | Internal,<br>Sequential | ✗ | PPO,<br>Trajectory | Thought Template Retrieve | ✗ | ✗ | Math | Pass@1 |
| <i><b>L1: Controlling how long a reasoning model thinks with reinforcement learning</b></i><br>Aggarwal and Welleck, <a href="https://arxiv.org/abs/2503.04697" target="_blank"><img src="https://img.shields.io/badge/arXiv-2503.04697-red" alt="arXiv Badge"></a></li> | Internal | ✗ | GRPO,<br>Length-Penalty | ✗ | ✗ | ✗ | ✗ | Math | Pass@1,<br>Length Error |
| <i><b>Marco-o1: Towards Open Reasoning Models for Open-Ended Solutions</b></i><br>Zhao et al., <a href="https://arxiv.org/abs/2411.14405" target="_blank"><img src="https://img.shields.io/badge/arXiv-2411.14405-red" alt="arXiv Badge"></a></li> | Internal,<br>Hybrid | distillation,<br>imitation | ✗ | Reflection Prompt | MCTS | Self-Critic | ✗ | Math | Pass@1,<br>Pass@k |




</footer>
