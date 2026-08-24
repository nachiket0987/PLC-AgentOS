# 🏭 AutoPLC-Studio: Multi-Agent Industrial PLC Code Synthesis & Formal Verification System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![IEC 61131-3](https://img.shields.io/badge/Standard-IEC%2061131--3-green?logo=microchip&logoColor=white)
![Multi-Agent](https://img.shields.io/badge/Architecture-Multi--Agent%20RAG-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Author](https://img.shields.io/badge/Author-Nachiket%20Gadilohar-purple)

**AutoPLC-Studio** is an enterprise-grade multi-agent AI environment designed for industrial control engineering. It automates the end-to-end process of retrieving industrial patterns, planning sequential control logic, synthesizing **IEC 61131-3 Structured Text (ST)** code, formally verifying safety properties (LTL/CTL logic), and executing Chain-of-Thought (CoT) debugging for Programmable Logic Controllers (PLCs).

---

## 🌟 Key Features

- **🤖 6-Agent Orchestration Workflow**: Central orchestrator controlling specialized agents (Retrieval, Planning, Coding, Validation, Debugging).
- **📚 Industrial RAG Knowledge Base**: Validated control patterns for wastewater treatment, multi-station manufacturing assembly lines, ASRS material handling, and OSCAT libraries (`PID_3TERM`, `SCALE_X_R`, `PUMP_CTRL_3`).
- **🛡️ Formal Verification & Safety Interlocks**: Automatic property generation (LTL/CTL specs) for model checkers like NuSMV/CBMC and safety interlock enforcement (`E-Stop`, low-flow cutoffs).
- **🐛 Chain-of-Thought (CoT) Error Repair**: Closed-loop debugging cycle that analyzes compiler output and applies minimal logic corrections.
- **⚡ OpenPLC Runtime Compatibility**: Produces standardized Structured Text output ready for OpenPLC, Siemens TIA Portal, Rockwell Studio 5000, and CODESYS environments.

---

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    User([User Requirement]) --> Orchestrator[@orchestrator Workflow Orchestrator]
    Orchestrator --> Retrieval[@retrieval Knowledge Base Search]
    Retrieval --> Planning[@planning Implementation Planner]
    Planning --> Coding[@coding ST Generator]
    Coding --> Validation[@validation Syntax & Formal Verifier]
    Validation -->|Pass| VerifiedCode([Verified ST Program])
    Validation -->|Fail| Debugging[@debugging CoT Error Repair]
    Debugging --> Coding
```

---

## 🛠️ Tech Stack

- **Core AI**: LLM Multi-Agent Orchestration, Retrieval-Augmented Generation (RAG), Chain-of-Thought (CoT) Debugging.
- **Industrial Standards**: IEC 61131-3 Structured Text (ST), OSCAT Industrial Library.
- **Verification & Runtime**: OpenPLC Runtime, LTL/CTL Formal Verification Specifications (SMV/CBMC).

---

## ⚙️ Quick Start & Setup

### 1. Installation
Clone the repository:
```bash
git clone https://github.com/nachiket0987/AutoPLC-Studio.git
cd AutoPLC-Studio
pip install -e .
```

### 2. Configure Agents in Claude Code
Create the core agents:
```bash
/agent create orchestrator "AutoPLC Workflow Orchestrator"
/agent create retrieval "PLC Knowledge Retrieval Agent"
/agent create planning "PLC Implementation Planning Agent"
/agent create coding "ST Code Generation Agent"
/agent create debugging "ST Code Debugging Agent"
/agent create validation "ST Code Validation Agent"
```

Train each agent using prompt files in `./agent_prompts/`:
```bash
/agent train orchestrator   # Paste contents of agent_prompts/orchestrator_agent_prompt.md
/agent train retrieval      # Paste contents of agent_prompts/retrieval_agent_prompt.md
/agent train planning       # Paste contents of agent_prompts/planning_agent_prompt.md
/agent train coding         # Paste contents of agent_prompts/coding_agent_prompt.md
/agent train validation     # Paste contents of agent_prompts/validation_agent_prompt.md
/agent train debugging      # Paste contents of agent_prompts/debugging_agent_prompt.md
```

---

## 🚀 Usage Example

Execute a request via the Orchestrator:
```bash
@orchestrator "Create a 4-bed sand filter backwash control system with differential pressure triggers"
```

The system guides you through:
1. **Retrieval**: Pulls backwash sequencing patterns from `./datasets/industrial_water_treatment.md`.
2. **Planning**: Generates 3 implementation plans (Simple to High Complexity).
3. **Coding**: Produces compilable ST code.
4. **Validation**: Checks syntax and generates LTL timing properties.

---

## 👤 Author & Contact

**Nachiket Gadilohar**
- **Email**: [nachiketlohar0306@gmail.com](mailto:nachiketlohar0306@gmail.com)
- **GitHub**: [github.com/nachiket0987](https://github.com/nachiket0987)
- **LinkedIn**: [linkedin.com/in/nachiket-gadilohar-profile/](https://linkedin.com/in/nachiket-gadilohar-profile/)