<p align="center">
  <img src="assets/banner.svg" alt="Awesome AI Resources" width="100%">
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/resources-100%2B-1a4d3e?style=flat-square" alt="100+ resources">
  <img src="https://img.shields.io/badge/links-verified%20weekly-3dd6c6?style=flat-square" alt="Links verified weekly">
  <img src="https://img.shields.io/badge/license-MIT-f0c75e?style=flat-square" alt="MIT License">
  <img src="https://img.shields.io/github/last-commit/mohabdelkarim/awesome-ai-resources?style=flat-square&label=last%20update" alt="Last update">
</p>

# Awesome AI Resources

A **roadmap-driven collection of free and legal AI resources**: courses, books, papers, tools, APIs, labs, and communities, ordered so you learn in the right sequence.

Built for:
- Beginners entering machine learning
- Engineers leveling up into LLMs and agents
- Builders shipping AI products
- Self-learners preparing for internships and jobs

> Goal: cut noise, keep depth, and point only to resources you can actually open.

---

## How to use this repository

1. Follow the path: **Foundations > ML > Deep Learning > NLP/LLMs > Agents and RAG > Build**
2. Pick one track at a time; you do **not** need every link
3. Prefer official / open content (no paywalled dumps, no shady mirrors)
4. Links are auto-checked **every Thursday**; broken ones are repaired or flagged

<p align="center">
  <img src="assets/roadmap.svg" alt="Learning roadmap" width="100%">
</p>

---

## Table of contents

- [Learning roadmap](#learning-roadmap)
  - [Foundations](#foundations-python-math--ml-basics)
  - [Machine learning](#machine-learning)
  - [Deep learning](#deep-learning)
  - [NLP and LLMs](#nlp-and-llms)
  - [Agents and RAG](#agents-and-rag)
  - [Specialize and build](#specialize-and-build)
- [Tools and APIs](#tools-and-apis)
  - [Chat and coding assistants](#chat-and-coding-assistants)
  - [Free / freemium LLM APIs](#free--freemium-llm-apis)
  - [Local AI](#local-ai)
  - [Frameworks and orchestration](#frameworks-and-orchestration)
  - [Embeddings and vector databases](#embeddings-and-vector-databases)
  - [Datasets and model hubs](#datasets-and-model-hubs)
- [Practice and communities](#practice-and-communities)
  - [Hands-on labs and platforms](#hands-on-labs-and-platforms)
  - [Newsletters and reading](#newsletters-and-reading)
  - [Communities and forums](#communities-and-forums)
- [Contributing](#contributing)

**Legend:** `Beginner` · `Intermediate` · `Advanced` · `Editor's pick`

---

# Learning roadmap

## Foundations: Python, math & ML basics

### Python for AI
- [Python.org official tutorial](https://docs.python.org/3/tutorial/): Canonical language tour. `Beginner`
- [Real Python](https://realpython.com/): Practical Python articles and guides. `Beginner`
- [CS50 Introduction to Programming with Python](https://cs50.harvard.edu/python/): Free Harvard course with problem sets. `Beginner` `Editor's pick`

### Math for ML
- [Essence of Linear Algebra (3Blue1Brown)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab): Visual intuition for vectors and matrices. `Beginner` `Editor's pick`
- [Essence of Calculus (3Blue1Brown)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr): Derivatives and integrals the geometric way. `Beginner`
- [Mathematics for Machine Learning (Imperial / Coursera free audit)](https://www.coursera.org/specializations/mathematics-machine-learning): Linear algebra, multivariate calculus, PCA. `Intermediate`
- [Immersive Linear Algebra](https://immersivemath.com/ila/index.html): Interactive free linear algebra book. `Beginner`
- [StatQuest with Josh Starmer](https://www.youtube.com/@statquest): Clear stats/ML explainers. `Beginner` `Editor's pick`

### First ML overview
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course): Free structured ML intro from Google. `Beginner` `Editor's pick`
- [fast.ai Practical Deep Learning for Coders](https://course.fast.ai/): Top-down deep learning for practitioners. `Beginner` `Editor's pick`
- [Elements of AI](https://www.elementsofai.com/): Non-technical AI literacy course. `Beginner`

---

## Machine learning

### Courses
- [Andrew Ng Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction): Classic supervised/unsupervised foundations (audit free). `Beginner` `Editor's pick`
- [MIT 6.036 Introduction to Machine Learning](https://openlearninglibrary.mit.edu/courses/course-v1:MITx+6.036+1T2019/about): Rigorous undergrad ML. `Intermediate`
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html): Definitive classical ML library docs. `Beginner`
- [Kaggle Learn](https://www.kaggle.com/learn): Short free micro-courses with notebooks. `Beginner`

### Free books and notes
- [An Introduction to Statistical Learning (ISLP)](https://www.statlearning.com/): Free PDF + labs; gold-standard intro. `Beginner` `Editor's pick`
- [Hands-On Machine Learning resources (Geron companion)](https://github.com/ageron/handson-ml3): Official notebooks for the popular book. `Intermediate`
- [Pattern Recognition and Machine Learning (Bishop) errata and resources](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/): Classic probabilistic ML reference. `Advanced`
- [Probabilistic Machine Learning (Murphy) book site](https://probml.github.io/pml-book/): Modern free draft / companion materials. `Advanced`

### Practice
- [Kaggle Competitions](https://www.kaggle.com/competitions): Real datasets and public notebooks. `Intermediate`
- [OpenML](https://www.openml.org/): Open datasets and reproducible ML experiments. `Intermediate`

---

## Deep learning

### Courses
- [Neural Networks: Zero to Hero (Andrej Karpathy)](https://karpathy.ai/zero-to-hero.html): Build neural nets and GPT pieces from scratch. `Intermediate` `Editor's pick`
- [DeepLearning.AI Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning): CNNs, RNNs, sequence models (audit free). `Intermediate`
- [Stanford CS231n](http://cs231n.stanford.edu/): Computer vision classic course. `Advanced`
- [MIT 6.S191 Introduction to Deep Learning](http://introtodeeplearning.com/): Short, intense DL intro with labs. `Intermediate` `Editor's pick`
- [NYU Deep Learning (Yann LeCun)](https://atcold.github.io/NYU-DLSP21/): Free course materials and notebooks. `Advanced`

### Frameworks and docs
- [PyTorch Tutorials](https://pytorch.org/tutorials/): Official beginner to advanced tutorials. `Beginner` `Editor's pick`
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials): Official Keras/TF learning path. `Beginner`
- [JAX Documentation](https://docs.jax.dev/en/latest/): Composable NumPy + autodiff. `Advanced`

### Free books
- [Deep Learning Book (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/): Free online deep learning textbook. `Advanced` `Editor's pick`
- [Dive into Deep Learning](https://d2l.ai/): Interactive free book with code (PyTorch/MXNet/JAX). `Intermediate` `Editor's pick`
- [Neural Networks and Deep Learning (Nielsen)](http://neuralnetworksanddeeplearning.com/): Friendly free online book. `Beginner`

---

## NLP and LLMs

### Courses
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course): Transformers, tokenizers, fine-tuning. `Intermediate` `Editor's pick`
- [Stanford CS224n NLP with Deep Learning](https://web.stanford.edu/class/cs224n/): Foundational NLP course. `Advanced`
- [DeepLearning.AI Generative AI courses](https://www.deeplearning.ai/courses/): Short free GenAI / LLM courses. `Beginner` `Editor's pick`
- [LangChain Academy](https://academy.langchain.com/): Free courses on LangChain and LangGraph. `Intermediate`

### Prompting and LLM engineering
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering): Official prompting patterns. `Beginner`
- [Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview): Claude-focused prompting. `Beginner`
- [Prompt Engineering Guide](https://www.promptingguide.ai/): Community-maintained prompting encyclopedia. `Beginner` `Editor's pick`
- [OpenAI Cookbook](https://cookbook.openai.com/): Practical LLM recipes and notebooks. `Intermediate`

### Papers and reading lists
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): The Transformer paper. `Advanced` `Editor's pick`
- [BERT](https://arxiv.org/abs/1810.04805): Bidirectional pretraining breakthrough. `Advanced`
- [GPT-3 / Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165): Scaling and in-context learning. `Advanced`
- [Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/): Best visual explainer. `Beginner` `Editor's pick`
- [Papers With Code NLP](https://paperswithcode.com/area/natural-language-processing): Papers, leaderboards, and code. `Intermediate`

---

## Agents and RAG

### Courses and guides
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course): Build agents end-to-end, free. `Intermediate` `Editor's pick`
- [Anthropic Courses](https://github.com/anthropics/courses): Prompting, tool use, RAG, agents. `Intermediate` `Editor's pick`
- [LangChain RAG Tutorials](https://python.langchain.com/docs/tutorials/rag/): Official RAG walkthrough. `Intermediate`
- [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/): Data framework for LLM apps. `Intermediate`
- [OpenAI Assistants / Responses docs](https://platform.openai.com/docs/overview): Official OpenAI API building blocks. `Intermediate`

### Agent frameworks
- [LangGraph](https://langchain-ai.github.io/langgraph/): Stateful multi-actor agent graphs. `Intermediate`
- [Microsoft AutoGen](https://microsoft.github.io/autogen/): Multi-agent conversation framework. `Intermediate`
- [CrewAI](https://docs.crewai.com/): Role-based multi-agent crews. `Intermediate`
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/): Microsoft orchestration SDK. `Intermediate`

### Evaluation and safety
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/): Security risks for LLM apps. `Intermediate` `Editor's pick`
- [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents): Practical agent design notes. `Intermediate` `Editor's pick`
- [RAGAS](https://docs.ragas.io/): RAG evaluation framework. `Intermediate`

---

## Specialize and build

### Computer vision
- [Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course): Free CV with transformers/diffusers. `Intermediate`
- [PyTorch Vision Docs](https://pytorch.org/vision/stable/index.html): Models, datasets, transforms. `Intermediate`

### Speech and multimodal
- [OpenAI Whisper](https://github.com/openai/whisper): Robust speech recognition. `Intermediate`
- [Hugging Face Audio Course](https://huggingface.co/learn/audio-course): ASR, TTS, audio transformers. `Intermediate`
- [Stable Diffusion web resources (Stability)](https://stability.ai/): Image generation ecosystem hub. `Intermediate`

### MLOps and production
- [Made With ML](https://madewithml.com/): Production ML course (free). `Intermediate` `Editor's pick`
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/): Course on shipping ML systems. `Intermediate`
- [Weights and Biases Docs](https://docs.wandb.ai/): Experiment tracking. `Beginner`
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html): Open-source ML lifecycle. `Intermediate`

### Careers and interviews
- [Hugging Face Jobs](https://huggingface.co/jobs): ML/AI job board. `Beginner`
- [Machine Learning Interview (khangich)](https://github.com/khangich/machine-learning-interview): Curated ML system design and interview notes. `Intermediate`
- [Chip Huyen ML interviews and systems](https://huyenchip.com/): Essays on ML systems and careers. `Intermediate` `Editor's pick`

---

# Tools and APIs

## Chat and coding assistants
| Tool | Link | Notes |
|------|------|-------|
| ChatGPT | https://chatgpt.com/ | Free tier + paid |
| Google Gemini | https://gemini.google.com/ | Strong free multimodal |
| Claude | https://claude.ai/ | Free tier available |
| Microsoft Copilot | https://copilot.microsoft.com/ | Free assistant in Edge/Windows |
| Perplexity | https://www.perplexity.ai/ | Search-grounded answers |
| Cursor | https://cursor.com/ | AI-first code editor |
| GitHub Copilot | https://github.com/features/copilot | Free for eligible students / OSS |
| Continue | https://www.continue.dev/ | Open-source coding assistant |

## Free / freemium LLM APIs
- [GroqCloud](https://console.groq.com/): Very fast OpenAI-compatible inference. `Beginner` `Editor's pick`
- [Google AI Studio (Gemini API)](https://aistudio.google.com/): Free Gemini API key tier. `Beginner` `Editor's pick`
- [OpenRouter](https://openrouter.ai/): Multi-model router with free models. `Beginner`
- [Together AI](https://www.together.ai/): Open-model inference (free credits). `Intermediate`
- [Fireworks AI](https://fireworks.ai/): Fast inference for open models. `Intermediate`
- [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers): Run models via HF. `Intermediate`
- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/): Edge AI inference free tier. `Intermediate`

## Local AI
- [Ollama](https://ollama.com/): Run LLMs locally with a simple CLI. `Beginner` `Editor's pick`
- [LM Studio](https://lmstudio.ai/): Desktop UI for local models. `Beginner`
- [GPT4All](https://www.nomic.ai/gpt4all): Local chat on consumer hardware. `Beginner`
- [llama.cpp](https://github.com/ggerganov/llama.cpp): Efficient C/C++ LLM inference. `Intermediate` `Editor's pick`
- [Open WebUI](https://github.com/open-webui/open-webui): ChatGPT-like UI for Ollama / OpenAI APIs. `Beginner`
- [Jan](https://jan.ai/): Offline-first desktop AI. `Beginner`
- [vLLM](https://github.com/vllm-project/vllm): High-throughput serving engine. `Advanced`
- [Hugging Face Transformers](https://huggingface.co/docs/transformers): The Python model library. `Intermediate` `Editor's pick`

## Frameworks and orchestration
- [LangChain](https://python.langchain.com/): Popular LLM application framework. `Intermediate`
- [LlamaIndex](https://www.llamaindex.ai/): RAG / data agents. `Intermediate`
- [Haystack](https://haystack.deepset.ai/): Production NLP/RAG pipelines. `Intermediate`
- [DSPy](https://dspy.ai/): Programmatic prompting and optimization. `Advanced`
- [Instructor](https://python.useinstructor.com/): Structured LLM outputs. `Intermediate`
- [PydanticAI](https://ai.pydantic.dev/): Type-safe agent framework. `Intermediate`
- [LiteLLM](https://docs.litellm.ai/): Unified API across 100+ providers. `Intermediate`

## Embeddings and vector databases
- [Chroma](https://www.trychroma.com/): Developer-friendly vector DB. `Beginner`
- [Qdrant](https://qdrant.tech/): Vector search engine (open-source + cloud). `Intermediate`
- [Weaviate](https://weaviate.io/): Open-source vector database. `Intermediate`
- [pgvector](https://github.com/pgvector/pgvector): Vector extension for Postgres. `Intermediate` `Editor's pick`
- [FAISS](https://github.com/facebookresearch/faiss): Similarity search library from Meta. `Advanced`
- [Pinecone](https://www.pinecone.io/): Managed vector DB (free tier). `Beginner`
- [sentence-transformers](https://www.sbert.net/): Easy embedding models. `Beginner` `Editor's pick`

## Datasets and model hubs
- [Hugging Face Hub](https://huggingface.co/): Models, datasets, Spaces. `Beginner` `Editor's pick`
- [Hugging Face Datasets](https://huggingface.co/docs/datasets): Dataset loading library. `Beginner`
- [TensorFlow Datasets](https://www.tensorflow.org/datasets): Ready-to-use TF datasets. `Beginner`
- [Papers With Code](https://paperswithcode.com/): SOTA papers with implementations. `Intermediate` `Editor's pick`
- [EleutherAI](https://www.eleuther.ai/): Open research org (GPT-NeoX, evals). `Advanced`
- [LAION](https://laion.ai/): Large open image-text datasets. `Advanced`
- [Common Crawl](https://commoncrawl.org/): Open web crawl corpus. `Advanced`

---

# Practice and communities

## Hands-on labs and platforms
- [Google Colab](https://colab.research.google.com/): Free GPU notebooks in the browser. `Beginner` `Editor's pick`
- [Kaggle Notebooks](https://www.kaggle.com/code): Free notebooks + GPUs + datasets. `Beginner`
- [Hugging Face Spaces](https://huggingface.co/spaces): Host demos for free. `Beginner`
- [Weights and Biases Reports / gallery](https://wandb.ai/fully-connected): Public ML write-ups. `Intermediate`
- [LeetCode](https://leetcode.com/): Algorithms practice (useful for ML interviews). `Beginner`
- [NeetCode](https://neetcode.io/): Curated coding interview paths. `Beginner`
- [Lightning AI Studios](https://lightning.ai/): Cloud studios for PyTorch Lightning. `Intermediate`
- [Modal](https://modal.com/): Serverless GPUs for experiments (free credits). `Intermediate`

## Newsletters and reading
- [The Batch (DeepLearning.AI)](https://www.deeplearning.ai/the-batch/): Weekly AI news from Andrew Ng's team. `Beginner` `Editor's pick`
- [Import AI (Jack Clark)](https://importai.substack.com/): Research and policy oriented AI newsletter. `Intermediate`
- [TLDR AI](https://tldr.tech/ai): Short daily AI digest. `Beginner`
- [AlphaSignal](https://alphasignal.ai/): ML research and tooling highlights. `Intermediate`
- [SemiAnalysis](https://www.semianalysis.com/): AI infra / semiconductor analysis (mixed free). `Advanced`
- [Distill](https://distill.pub/): Visual ML explainers (classic archive). `Intermediate` `Editor's pick`
- [Lil'Log (Lilian Weng)](https://lilianweng.github.io/): Deep dives on RL, agents, LLMs. `Advanced` `Editor's pick`
- [Simon Willison's Weblog](https://simonwillison.net/): Practical LLM engineering notes. `Intermediate` `Editor's pick`

## Communities and forums
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/): Large research/discussion subreddit. `Intermediate`
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/): Local models, quantization, tooling. `Intermediate` `Editor's pick`
- [Hugging Face Discord](https://discord.com/invite/hugging-face): Official HF community. `Beginner`
- [EleutherAI Discord](https://discord.gg/eleutherai): Open ML research community. `Advanced`
- [PyTorch Forums](https://discuss.pytorch.org/): Official PyTorch Q&A. `Beginner`
- [Latent Space community](https://www.latent.space/): AI eng podcast and community hub. `Intermediate`
- [AI Engineer](https://www.aicamp.so/): Events and community for AI builders. `Intermediate`
- [LangChain Discord](https://discord.gg/langchain): LangChain community. `Intermediate`

---

## Contributing

Contributions welcome. Keep the bar high:

1. Resource must be **free or meaningfully freemium** and **legal** to access
2. Prefer official docs, open textbooks, reputable courses, and maintained repos
3. Add a one-line description + difficulty marker (`Beginner` / `Intermediate` / `Advanced`, optional `Editor's pick`)
4. Place it in the correct roadmap / tools / practice section
5. Open a PR; weekly link checks will re-verify URLs every Thursday

Do **not** submit paywalled ebook dumps, cracked PDFs, or dead mirrors.

---

### Found this useful?

Star the repo and share it with someone learning AI.

Maintained by [mohabdelkarim](https://github.com/mohabdelkarim).
