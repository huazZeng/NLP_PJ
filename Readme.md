# 大模型数学能力微调实践
https://zhuanlan.zhihu.com/p/673789772 一篇炼丹的简单综述
https://zhuanlan.zhihu.com/p/681299172 数学推理综述
## Baseline SFT
* GSM8K baseline Done


## 数据增强
* https://arxiv.org/pdf/2310.05506  
  * 问题增强的改写方式为根据人类知识设计的五条规则：Change specific numbers; Introduce fractions or percentages; Combine multiple concepts; Include a conditional statement; Increase the complexity of the problem.
  * https://github.com/OFA-Sys/gsm8k-ScRel
* 拿GPT生成一些（？）；问题拆解（？）
  
## LoRA
* 直接用LoRA,Cot
* 学习一个答案验证器 ：
  * 需要训练多个模型 ，麻烦
  * 根据Cobbe等(2021)，OpenAI的研究人员将一个拥有1750亿参数的GPT-3模型微调为一个验证器，为解决候选项赋予概率。在探索MWP解决的复审过程时，Bin等(2023)提出了伪双学习，其中涉及解决和复审模块。对于MWP解决方案，Zhu等(2023)开发了一个合作推理诱导的PLM，其中GPT-J(Wang和Komatsuzaki，2021)生成路径，而DeBERTa-large(He等，2021)进行监督评估。 根据Liu等(2023c)，谷歌研究人员观察到，LLM通过多次尝试可以提高正确性，这表明LLM可能生成正确的解决方案，而在区分准确和不准确方案时遇到困难。他们顺序地将PaLM 2模型(Anil等，2023)先作为解生成器进行了微调，然后作为评估器，最后再次作为生成器进行了微调。


