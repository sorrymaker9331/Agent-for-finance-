
---

# Financial Analysis Agent (LangGraph + LangChain + MCP)

## 项目概述 / Project Overview

这是一个面向 A 股市场的金融分析智能体工程，核心基于 **LangGraph + LangChain**，结合 **MCP 工具服务**。项目提供多智能体框架，支持新闻、股票市场、财务报表、宏观数据等分析，同时可训练与测试 Qwen 系列模型进行风险和情感分析。

This is a financial analysis agent project for A-share markets, built on **LangGraph + LangChain** with **MCP tool services**. The system provides multiple agents to analyze news, stock market, financial reports, macro data, and supports training/testing Qwen-based models for sentiment and risk analysis.

---

## 项目结构 / Project Structure

```
download_qwen.py           # Qwen 模型下载脚本 / model download
models/                    # 本地模型权重（体积大，建议不上传） / local model weights
Finance/                   
requirements.txt           # 主要依赖 / dependencies
train_qwen_sentiment.py    # Qwen 情感模型 LoRA 微调 / sentiment LoRA training
train_qwen_risk.py         # Qwen 风险模型 LoRA 微调 / risk LoRA training
test_qwen_sentiment.py     # 情感模型测试 / sentiment model testing
test_risk_model.py         # 风险模型测试 / risk model testing
a-share-mcp-is-just-i-need/  # MCP 服务及工具 / MCP server & tools
Financial-MCP-Agent/       # 多智能体应用 / multi-agent app
main.py                    # CLI 与 LangGraph 工作流入口 / workflow entry
src/agents/*.py            # 各分析智能体 / analysis agents
src/utils/                 # 日志、执行跟踪、状态定义 / logging & utils
mcp_client.py              # MCP 客户端 / MCP client
```

---

## 快速开始 / Quick Start

### 环境 / Environment

```bash
# 建议创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 配置 / Configuration

在项目根目录或 Finance/ 下创建 `.env`：

```
OPENAI_COMPATIBLE_API_KEY=<your_api_key>
OPENAI_COMPATIBLE_BASE_URL=<your_base_url>
OPENAI_COMPATIBLE_MODEL=<your_model>
```

### 启动 MCP 服务 / Start MCP Server

```bash
python a-share-mcp-is-just-i-need/mcp_server.py
```

### 启动多智能体 / Run Multi-Agent Analysis

```bash
cd src
python main.py --command "分析XXX"
```

### 模型训练与测试 / Train & Test Models

```bash
# LoRA 微调 Qwen 情感 / 风险模型
python train_qwen_sentiment.py
python train_qwen_risk.py

# 测试模型
python test_qwen_sentiment.py
python test_risk_model.py
```

---

## 技术亮点 / Highlights

* **多智能体框架**：结合 ReAct + MCP 工具，实现数据抓取、分析、总结。
* **Qwen LoRA 微调**：针对金融新闻和风险事件进行情感与风险分析。
* **MCP 工具服务**：提供股票市场、财务报表、指数、宏观经济等数据接口。
* **灵活扩展**：可快速添加新的 Agent 或工具函数，支持 LangGraph 工作流。
* **支持 A 股 / 财务分析场景**：覆盖基本面、技术面、估值、新闻与信息面等。

---

## 注意事项 / Notes

* **模型权重**（models/）体积大，请通过云端下载链接管理，不建议上传到 GitHub。
* **训练 LoRA 模型**需大显存或使用 8-bit/4-bit 策略。
* 推荐在虚拟环境中运行，确保依赖版本兼容。

---

